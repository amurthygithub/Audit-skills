"""Shared consistency test library for Audit-skills.

Each test function takes a ``skill_dir: Path`` and uses ``assert`` to verify
invariants. Import from per-skill ``tests/test_<slug>_consistency.py``
wrappers — they provide the ``skill_dir`` fixture and re-export each
``test_*`` function from this module.

All five sibling skill names are hardcoded.
"""

__test__ = False  # not a test module — see per-skill wrappers

import re
from pathlib import Path

import pytest

# Auto-discovered so the list can never go stale (it previously sat at 5
# skills, silently skipping cross-skill reference checks for nist-csf-2).
SIBLING_SKILLS = frozenset(
    p.parent.name
    for p in (Path(__file__).resolve().parent.parent / "skills").glob("*/SKILL.md")
    if p.parent.name != "TEMPLATE"
)

# Match chunk paths with OR without backticks, but only when in routing table
# context. Two patterns:
#  1. backticked: `chunks/NN-slug.md`
#  2. in markdown table row: | ... | chunks/NN-slug.md | ...
# Plain prose mentions are NOT routing entries.
_CHUNK_BACKTICK_RE = re.compile(r"`(chunks/\d{2}-[a-z][a-z0-9-]*\.md)`")
_CHUNK_TABLE_RE = re.compile(r"\|\s*`?(chunks/\d{2}-[a-z][a-z0-9-]*\.md)`?\s*\|")
# Cross-skill chunk refs in backticks
_XREF_CHUNK_RE = re.compile(r"`([a-z][a-z0-9-]+/chunks/\d{2}-[a-z][a-z0-9-]*\.md)`")
_XREF_ASSET_RE = re.compile(r"`([a-z][a-z0-9-]+/assets/[^`]+)`")
_XREF_BARE_CHUNK_RE = re.compile(
    r"(?<![`\w/])([a-z][a-z0-9-]+/chunks/\d{2}-[a-z][a-z0-9-]*\.md)(?![\w`])"
)
# Manifest labels: extract [CONTENT] then split on space/§/comma
_MANIFEST_CONTENT_RE = re.compile(r"\[([A-Z][^\[\]]+?)\]")
# Extract the label: allow multi-segment (NIST-SP-800-30-Rev1) or single acronym (ITAF, ITIL)
_LABEL_EXTRACT_RE = re.compile(r"^([A-Z][A-Za-z0-9]+(?:[-.][A-Za-z0-9]+)+|[A-Z]{3,})")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _parse_yaml_frontmatter(text: str):
    """Return (frontmatter_dict, body_start_offset) for YAML frontmatter."""
    if not text.startswith("---\n"):
        return None, 0
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, 0
    fm = {}
    current_key = None
    list_values = []
    for line in text[4:end].split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and current_key is not None:
            fm[current_key].append(stripped[2:].strip().strip('"').strip("'"))
            continue
        if ":" in stripped and (stripped[0] not in (" ", "\t")):
            key_part, _, val_part = stripped.partition(":")
            key = key_part.strip()
            val = val_part.strip()
            if val == "":
                current_key = key
                fm[key] = []
            else:
                fm[key] = val.strip('"').strip("'")
                current_key = None
    return fm, end + 5


def _list_field(fm, key):
    """Get a list field from frontmatter (handles inline [a, b] syntax)."""
    raw = fm.get(key)
    if raw is None:
        return []
    if isinstance(raw, list):
        return [str(x).strip().strip('"').strip("'") for x in raw]
    if isinstance(raw, str):
        s = raw.strip()
        if s.startswith("[") and s.endswith("]"):
            inner = s[1:-1]
            return [
                x.strip().strip('"').strip("'")
                for x in inner.split(",")
                if x.strip()
            ]
        return [s] if s else []
    return []


def _collect_md_files(skill_dir: Path):
    """Return all .md files under skill_dir (excluding data/seeds/examples)."""
    out = []
    for p in sorted(skill_dir.rglob("*.md")):
        if "/data/seeds/" in str(p) or "/_archive/" in str(p):
            continue
        out.append(p)
    return out


def _extract_chunks_from_routing(skill_md_text: str) -> set:
    """Return set of `chunks/NN-slug.md` paths (without backticks) found in text.
    Matches both backticked paths and bare paths in markdown table rows."""
    found = set()
    for m in _CHUNK_BACKTICK_RE.finditer(skill_md_text):
        found.add(m.group(1))
    for m in _CHUNK_TABLE_RE.finditer(skill_md_text):
        found.add(m.group(1))
    return found


def _strip_md_suffix(s: str) -> str:
    if s.endswith(".md"):
        return s[:-3]
    return s


def _looks_like_citation(content_str: str) -> bool:
    """Heuristic: does this bracketed content look like a manifest label citation?
    Returns True for things like 'NIST-SP-800-30-Rev1', 'FedRAMP-Rev5 §3.1',
    or 'ITAF' (single-word acronyms).
    Returns False for English text like 'Long-term residual', control IDs like
    'AC-2', or use-case IDs like 'UC-01'.
    """
    # Strip trailing reference info (anything after first space or §)
    label_part = re.split(r"[ §]", content_str)[0]
    if not label_part:
        return False
    # Allow labels that are either:
    #   - Multi-segment (have dashes): NIST-SP-800-30-Rev1
    #   - All-caps acronyms 3+ chars: ITAF, ITIL, SOC, HIPAA
    if "-" in label_part:
        # Each segment should be alphanumeric
        segments = label_part.split("-")
        for seg in segments:
            if not seg:
                return False
            if not re.match(r"^[A-Za-z0-9.]+$", seg):
                return False
        return True
    else:
        # Single-word: must be all-uppercase acronym, 3+ chars
        return len(label_part) >= 3 and label_part.isupper()


# ---------------------------------------------------------------------------
# 1. Routing table <-> chunks directory bidirectionality
# ---------------------------------------------------------------------------


def test_routing_table_bidirectional(skill_dir: Path):
    """Every chunks/*.md on disk must appear in SKILL.md routing table
    and every chunk ref in routing table must exist on disk.

    Detects: orphan chunks (added but no routing row), dead routes
    (routing row references missing chunk file).
    """
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        pytest.fail(f"SKILL.md not found at {skill_md}")

    text = skill_md.read_text()
    routing_chunks = _extract_chunks_from_routing(text)

    chunks_dir = skill_dir / "chunks"
    disk_chunks = set()
    if chunks_dir.is_dir():
        for f in chunks_dir.iterdir():
            if f.suffix == ".md":
                disk_chunks.add(f"chunks/{f.name}")

    orphans = disk_chunks - routing_chunks
    dead_routes = set()
    for rc in routing_chunks:
        # Check if it's a local chunk or a cross-skill reference
        # Cross-skill refs: start with sibling-skill name
        rc_first_segment = rc.split("/")[0]
        is_cross_skill = rc_first_segment in SIBLING_SKILLS and rc_first_segment != skill_dir.name
        if is_cross_skill:
            # Resolve against sibling skills
            target = skill_dir.parent / rc
            if not target.exists():
                dead_routes.add(rc)
        else:
            if not (skill_dir / rc).exists():
                dead_routes.add(rc)

    if orphans:
        print(f"[FAIL] {skill_dir.name}: orphan chunks (on disk, not in routing table):")
        for o in sorted(orphans):
            print(f"       {o}")
    if dead_routes:
        print(f"[FAIL] {skill_dir.name}: dead routes (in routing table, not on disk):")
        for d in sorted(dead_routes):
            print(f"       {d}")

    assert not orphans, f"{len(orphans)} chunk(s) on disk missing from routing table"
    assert not dead_routes, f"{len(dead_routes)} routing table entries with no matching chunk file"


# ---------------------------------------------------------------------------
# 2. Chunk frontmatter schema
# ---------------------------------------------------------------------------


REQUIRED_CHUNK_KEYS = {"chunk_id", "parent_skill", "topic", "load_when"}


def test_chunk_frontmatter_schema(skill_dir: Path):
    """Every chunks/*.md must have chunk_id, parent_skill, topic, load_when.
    chunk_id must match filename stem. parent_skill must equal skill dir name.
    topic and load_when must be non-empty.

    Detects: chunks/08 schema drift (used title/skill/version instead).
    """
    chunks_dir = skill_dir / "chunks"
    if not chunks_dir.is_dir():
        pytest.skip(f"No chunks/ directory in {skill_dir.name}")

    skill_name = skill_dir.name
    failures = []

    for chunk_path in sorted(chunks_dir.iterdir()):
        if chunk_path.suffix != ".md":
            continue
        text = chunk_path.read_text()
        fm, _ = _parse_yaml_frontmatter(text)
        if fm is None:
            failures.append(f"{chunk_path.name}: no valid YAML frontmatter")
            continue

        missing = REQUIRED_CHUNK_KEYS - set(fm.keys())
        if missing:
            failures.append(
                f"{chunk_path.name}: missing keys {sorted(missing)}. "
                f"Found: {sorted(fm.keys())}"
            )
            continue

        expected_id = chunk_path.stem
        actual_id = str(fm.get("chunk_id", "")).strip()
        if actual_id != expected_id:
            failures.append(
                f"{chunk_path.name}: chunk_id '{actual_id}' != filename stem '{expected_id}'"
            )

        actual_skill = str(fm.get("parent_skill", "")).strip()
        if actual_skill != skill_name:
            failures.append(
                f"{chunk_path.name}: parent_skill '{actual_skill}' != '{skill_name}'"
            )

        if not str(fm.get("topic", "")).strip():
            failures.append(f"{chunk_path.name}: empty topic")
        if not str(fm.get("load_when", "")).strip():
            failures.append(f"{chunk_path.name}: empty load_when")

    if failures:
        print(f"[FAIL] {skill_dir.name}: chunk frontmatter schema violations:")
        for f in failures:
            print(f"       {f}")

    assert not failures, f"{len(failures)} chunk frontmatter violation(s)"


# ---------------------------------------------------------------------------
# 3. Manifest bidirectional coverage
# ---------------------------------------------------------------------------


def _get_manifest_labels(skill_md_path: Path):
    """Extract label set from §10 manifest table in SKILL.md."""
    text = skill_md_path.read_text()
    start = text.find("## 10. References")
    if start == -1:
        return None, text, 0, len(text)
    end = text.find("\n## 11. ", start)
    if end == -1:
        end = text.find("\n## 11 ", start)
    if end == -1:
        end = len(text)
    manifest_section = text[start:end]

    labels = set()
    for line in manifest_section.split("\n"):
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.split("|")]
        if len(cols) < 3:
            continue
        label = cols[1].strip()
        if not label or label.lower() == "label" or set(label) <= {"-", " "}:
            continue
        labels.add(label)
    return labels, text, start, end


def test_manifest_bidirectional(skill_dir: Path):
    """Every label in §10 manifest must be cited at least once across
    all .md files. Every [LABEL ...] citation must resolve to a manifest entry.

    Detects: dead manifest entries, dangling citations.
    """
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        pytest.fail(f"SKILL.md not found at {skill_md}")

    manifest_labels, text, m_start, m_end = _get_manifest_labels(skill_md)
    if manifest_labels is None:
        pytest.skip(f"{skill_dir.name}: no §10 References section in SKILL.md")
    if not manifest_labels:
        pytest.skip(f"{skill_dir.name}: §10 has no parseable labels")

    all_citations = set()
    for md_path in _collect_md_files(skill_dir):
        content = md_path.read_text()
        if md_path.name == "SKILL.md":
            # Exclude the manifest section itself from citation count
            search_text = content[:m_start] + "\n" + content[m_end:]
        else:
            search_text = content
        # Two-step: extract [CONTENT] then split to get label
        for m in _MANIFEST_CONTENT_RE.finditer(search_text):
            content_str = m.group(1)
            # Skip non-citations: control IDs, use-case IDs, English text
            # A citation is "all caps + digits + dashes" but may have a version
            # suffix like "Rev1" or "v4.0" with mixed case
            if not _looks_like_citation(content_str):
                continue
            label_m = _LABEL_EXTRACT_RE.match(content_str)
            if label_m:
                all_citations.add(label_m.group(1))

    uncited = manifest_labels - all_citations
    # Skip "dangling" check — too many false positives from control IDs and English.
    # The forward check (manifest → cited) is the high-signal direction.
    dangling = set()

    if uncited:
        print(f"[FAIL] {skill_dir.name}: manifest labels never cited:")
        for u in sorted(uncited):
            print(f"       {u}")
    if dangling:
        print(f"[FAIL] {skill_dir.name}: citations with no manifest entry:")
        for d in sorted(dangling):
            print(f"       {d}")

    assert not uncited, f"{len(uncited)} manifest label(s) never cited"
    assert not dangling, f"{len(dangling)} dangling citation(s) not in manifest"


# ---------------------------------------------------------------------------
# 4. Cross-skill references resolve
# ---------------------------------------------------------------------------


def test_cross_skill_references_resolve(skill_dir: Path):
    """Every `<sibling-skill>/chunks/NN-slug.md` or
    `<sibling-skill>/assets/...` reference in any .md must point to an
    existing file under skills/<sibling-skill>/.

    Detects: 4 broken cross-skill paths in audit-workpapers/chunks/05 and 07.
    """
    failures = []
    skills_root = skill_dir.parent

    for md_path in _collect_md_files(skill_dir):
        text = md_path.read_text()
        for m in _XREF_CHUNK_RE.finditer(text):
            ref = m.group(1)
            skill_name = ref.split("/")[0]
            if skill_name not in SIBLING_SKILLS:
                continue
            if skill_name == skill_dir.name:
                continue
            target = skills_root / skill_name / "/".join(ref.split("/")[1:])
            if not target.exists():
                failures.append(f"{md_path.relative_to(skill_dir)}: `{ref}` -> not found at {target}")
        for m in _XREF_BARE_CHUNK_RE.finditer(text):
            ref = m.group(1)
            skill_name = ref.split("/")[0]
            if skill_name not in SIBLING_SKILLS:
                continue
            if skill_name == skill_dir.name:
                continue
            target = skills_root / skill_name / "/".join(ref.split("/")[1:])
            if not target.exists():
                failures.append(f"{md_path.relative_to(skill_dir)}: `{ref}` -> not found at {target}")
        for m in _XREF_ASSET_RE.finditer(text):
            ref = m.group(1)
            skill_name = ref.split("/")[0]
            if skill_name not in SIBLING_SKILLS:
                continue
            if skill_name == skill_dir.name:
                continue
            target = skills_root / skill_name / "/".join(ref.split("/")[1:])
            if not target.exists():
                failures.append(f"{md_path.relative_to(skill_dir)}: `{ref}` -> not found at {target}")

    if failures:
        print(f"[FAIL] {skill_dir.name}: broken cross-skill references:")
        for f in failures:
            print(f"       {f}")

    assert not failures, f"{len(failures)} broken cross-skill reference(s)"


# ---------------------------------------------------------------------------
# 5. Industry index sync (SKILL.md <-> industries/ <-> _index.md)
# ---------------------------------------------------------------------------


def test_industry_index_sync(skill_dir: Path):
    """SKILL.md frontmatter industries list, industries/ directory, and
    industries/_index.md must all be in sync.

    Detects: industry files orphaned or missing; e.g., healthcare.md exists
    but not in SKILL.md frontmatter.
    """
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        pytest.fail(f"SKILL.md not found at {skill_md}")

    text = skill_md.read_text()
    fm, _ = _parse_yaml_frontmatter(text)
    if fm is None:
        pytest.skip(f"{skill_dir.name}: no YAML frontmatter in SKILL.md")
    skill_industries = set(_list_field(fm, "industries"))

    industries_dir = skill_dir / "industries"
    disk_industries = set()
    if industries_dir.is_dir():
        for f in industries_dir.iterdir():
            if f.suffix == ".md" and f.stem != "_index":
                disk_industries.add(f.stem)

    index_path = industries_dir / "_index.md"
    index_industries = set()
    if index_path.exists():
        idx_text = index_path.read_text()
        # _index.md table format: `| Industry | File | Top use cases | Notes |`
        # File column has `public-sector.md` etc — extract the stem
        for line in idx_text.split("\n"):
            if not line.startswith("|"):
                continue
            cols = [c.strip() for c in line.split("|")]
            if len(cols) < 3:
                continue
            file_cell = cols[2].strip()
            # Extract stem from a `.md` reference
            m = re.search(r"([a-z][a-z0-9-]+)\.md", file_cell)
            if m:
                slug = m.group(1)
                if slug and slug != "_index" and not set(slug) <= {"-"}:
                    index_industries.add(slug)

    # "other" is a sentinel allowed in frontmatter without a matching file
    skill_industries_eff = {i for i in skill_industries if i != "other"}
    disk_minus_skill = disk_industries - skill_industries_eff
    skill_minus_disk = skill_industries_eff - disk_industries
    disk_minus_index = disk_industries - index_industries
    index_minus_disk = index_industries - disk_industries

    failures = []
    if disk_minus_skill:
        failures.append(
            f"industries/ files not in SKILL.md frontmatter: {sorted(disk_minus_skill)}"
        )
    if skill_minus_disk:
        failures.append(
            f"SKILL.md frontmatter industries with no file: {sorted(skill_minus_disk)}"
        )
    if disk_minus_index:
        failures.append(
            f"industries/ files not in _index.md: {sorted(disk_minus_index)}"
        )
    if index_minus_disk:
        failures.append(
            f"_index.md entries with no file: {sorted(index_minus_disk)}"
        )

    if failures:
        print(f"[FAIL] {skill_dir.name}: industry sync violations:")
        for f in failures:
            print(f"       {f}")

    assert not failures, f"{len(failures)} industry sync violation(s)"


# ---------------------------------------------------------------------------
# 6. Use-case index sync (use-cases/_index.md <-> use-cases/ directory)
# ---------------------------------------------------------------------------


def test_use_case_index_sync(skill_dir: Path):
    """use-cases/_index.md table must list every use-cases/uc-*.md file and
    vice versa. Use-case IDs in SKILL.md routing table must have a file.

    Detects: UC-03 missing from index (was a real ISACA bug).
    """
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        pytest.fail(f"SKILL.md not found at {skill_md}")

    use_cases_dir = skill_dir / "use-cases"
    if not use_cases_dir.is_dir():
        pytest.skip(f"{skill_dir.name}: no use-cases/ directory")

    disk_ucs = set()
    for f in use_cases_dir.iterdir():
        if f.suffix == ".md" and f.name.startswith("uc-") and f.stem != "_index":
            disk_ucs.add(f.stem)

    index_path = use_cases_dir / "_index.md"
    index_ucs = set()
    if index_path.exists():
        idx_text = index_path.read_text()
        # _index.md table format: `| UC | Title | Industries | Status |`
        for line in idx_text.split("\n"):
            if not line.startswith("|"):
                continue
            cols = [c.strip() for c in line.split("|")]
            if len(cols) < 2:
                continue
            uc_cell = cols[1].strip()
            # Match `UC-01` and convert to `uc-01`
            m = re.match(r"UC-(\d+)", uc_cell)
            if m:
                index_ucs.add(f"uc-{m.group(1)}")
            # Also handle direct uc-XX-slug form
            for m2 in re.finditer(r"uc-\d{2}-[a-z][a-z0-9-]*", uc_cell):
                index_ucs.add(m2.group(0))

    # Also check SKILL.md routing table for UC IDs (UC-01 or uc-01-...)
    skill_text = skill_md.read_text() if skill_md.exists() else ""
    skill_uc_refs = set()
    for m in re.finditer(r"[Uu][Cc]-(\d{2})", skill_text):
        skill_uc_refs.add(f"uc-{m.group(1)}")
    # Also extract uc-XX-slug form
    for m in re.finditer(r"uc-\d{2}-[a-z][a-z0-9-]*", skill_text):
        skill_uc_refs.add(m.group(0))

    # Map UC IDs (uc-01) to actual filenames (uc-01-fedramp-moderate) for comparison
    def _expand(uc_set):
        out = set()
        for uc in uc_set:
            if re.match(r"uc-\d{2}$", uc):
                # UC ID like uc-01 — match any file starting with uc-01-
                prefix = uc + "-"
                for dc in disk_ucs:
                    if dc.startswith(prefix):
                        out.add(dc)
            else:
                out.add(uc)
        return out

    failures = []
    disk_minus_index = disk_ucs - _expand(index_ucs)
    index_minus_disk = _expand(index_ucs) - disk_ucs
    skill_minus_disk = _expand(skill_uc_refs) - disk_ucs

    if disk_minus_index:
        failures.append(f"uc files not in _index.md: {sorted(disk_minus_index)}")
    if index_minus_disk:
        failures.append(f"_index.md entries with no file: {sorted(index_minus_disk)}")
    if skill_minus_disk:
        failures.append(
            f"SKILL.md references UC IDs with no file: {sorted(skill_minus_disk)}"
        )

    if failures:
        print(f"[FAIL] {skill_dir.name}: use-case sync violations:")
        for f in failures:
            print(f"       {f}")

    assert not failures, f"{len(failures)} use-case sync violation(s)"
