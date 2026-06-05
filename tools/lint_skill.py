#!/usr/bin/env python3
"""Tier 0a skill linter (SOX-616).

Validates a skill directory against the contracts in skills/TEMPLATE/SKILL.md.
Exits non-zero on any failure; prints a human-readable report.

Usage:
    python tools/lint_skill.py skills/nist-800-53-rmf
    python tools/lint_skill.py skills/TEMPLATE
    python tools/lint_skill.py skills/*            # lint all
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable, List, Tuple

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


REQUIRED_FRONTMATTER = {
    "name", "description", "category", "risk", "source",
    "date_added", "version", "status", "industries", "frameworks",
    "telemetry_contract", "context_budget", "tags",
}
OPTIONAL_FRONTMATTER = {"token_baseline_target"}

REQUIRED_TOP_SECTIONS = [
    "When to Use",
    "Framework Overview",
    "Core Concepts",
    "Decision Logic",
    "Procedure Templates",
    "Output Templates",
    "Cross-References",
    "Worked Examples",
    "Anti-Hallucination",
    "References & Citation Manifest",
]

# SKILL.md line-count threshold. Above this, the chunks/ folder is required
# and SKILL.md must contain a routing table (§11).
SKILL_MD_LINE_LIMIT = 300
# Per-chunk line-count limit.
CHUNK_LINE_LIMIT = 200

REQUIRED_FOLDERS = [
    "industries",
    "use-cases",
    "data",
    "tests",
    "telemetry",
    "docs",
]

REQUIRED_DOCS = [
    "docs/architecture.md",
    "docs/limits-and-disclaimers.md",
    "docs/changelog.md",
    "docs/acceptance-gate.md",
]

REQUIRED_TELEMETRY = [
    "telemetry/schema.json",
    "telemetry/instrument.py",
    "telemetry/redaction.md",
    "telemetry/baseline.md",
]

INDUSTRY_KEYS = {
    "financial-services", "healthcare", "saas-technology", "public-sector",
    "manufacturing", "retail-ecommerce", "energy-utilities", "other",
}

CITE_PATTERN = re.compile(r"\[([A-Z][A-Z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-]+)\]")


def split_frontmatter(text: str) -> Tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    fm = yaml.safe_load(text[4:end])
    body = text[end + 5:]
    return fm or {}, body


def find_top_sections(body: str) -> List[str]:
    return [line[3:].strip() for line in body.splitlines() if line.startswith("## ")]


def find_todo_outside_changelog(skill_dir: Path, body: str) -> List[str]:
    offenders: List[str] = []
    # scan SKILL.md body
    for i, line in enumerate(body.splitlines(), 1):
        if re.search(r"\b(TODO|FIXME|XXX|HACK)\b", line):
            offenders.append(f"SKILL.md:{i}: {line.strip()}")
    # scan all files except changelog
    for p in skill_dir.rglob("*"):
        if not p.is_file():
            continue
        if p.name == "changelog.md":
            continue
        if p.suffix in {".pyc"}:
            continue
        try:
            for i, line in enumerate(p.read_text(errors="ignore").splitlines(), 1):
                if re.search(r"\b(TODO|FIXME|XXX|HACK)\b", line):
                    rel = p.relative_to(skill_dir)
                    offenders.append(f"{rel}:{i}: {line.strip()}")
        except Exception:
            pass
    return offenders


def lint_skill(skill_dir: Path) -> Tuple[int, List[str]]:
    errors: List[str] = []
    warnings: List[str] = []

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return 1, [f"SKILL.md missing in {skill_dir}"]
    text = skill_md.read_text()
    fm, body = split_frontmatter(text)

    is_template = fm.get("status") == "template"

    # Frontmatter
    if is_template:
        # TEMPLATE folder is the scaffold; only the bare-minimum frontmatter is required.
        template_min = {"name", "description", "category", "risk", "source", "date_added", "status"}
        missing = template_min - set(fm.keys())
    else:
        missing = REQUIRED_FRONTMATTER - set(fm.keys())
    if missing:
        errors.append(f"frontmatter missing fields: {sorted(missing)}")
    if "name" in fm and fm["name"] != skill_dir.name:
        errors.append(f"frontmatter name '{fm['name']}' != folder '{skill_dir.name}'")
    if "version" in fm and not re.match(r"^\d+\.\d+\.\d+", str(fm["version"])):
        errors.append(f"version '{fm['version']}' not semver")
    if "industries" in fm:
        for ind in fm["industries"]:
            if ind not in INDUSTRY_KEYS:
                errors.append(f"unknown industry key '{ind}' in frontmatter")
            if len(fm["industries"]) < 3:
                warnings.append("frontmatter lists <3 industries")
    if "tags" in fm and len(fm["tags"]) < 5:
        warnings.append("frontmatter lists <5 tags")

    # Sections
    if not is_template:
        sections = find_top_sections(body)
        for required in REQUIRED_TOP_SECTIONS:
            if not any(required in s for s in sections):
                errors.append(f"missing required section containing '{required}'")

    # Folders
    if not is_template:
        for f in REQUIRED_FOLDERS:
            if not (skill_dir / f).is_dir():
                errors.append(f"missing required folder '{f}/'")

    # SKILL.md size rule + chunks/ pattern
    if not is_template:
        line_count = len(text.splitlines())
        has_chunks = (skill_dir / "chunks").is_dir()
        if line_count > SKILL_MD_LINE_LIMIT and not has_chunks:
            errors.append(
                f"SKILL.md is {line_count} lines (> {SKILL_MD_LINE_LIMIT}). "
                f"Split into chunks/ subfolder per TEMPLATE §11. "
                f"SKILL.md becomes a router; chunks/ holds the deep-dive."
            )
        if has_chunks:
            # Chunks folder: each file must be ≤ CHUNK_LINE_LIMIT, named NN-slug.md
            chunk_files = sorted((skill_dir / "chunks").glob("*.md"))
            if not chunk_files:
                warnings.append("chunks/ exists but is empty")
            for cf in chunk_files:
                cf_lines = len(cf.read_text().splitlines())
                if cf_lines > CHUNK_LINE_LIMIT:
                    errors.append(
                        f"chunks/{cf.name} is {cf_lines} lines (> {CHUNK_LINE_LIMIT}). "
                        f"Split further or extract a sub-chunk."
                    )
                if not re.match(r"^\d{2}-[a-z0-9-]+\.md$", cf.name):
                    errors.append(
                        f"chunks/{cf.name} must match 'NN-slug.md' (e.g., 01-categorize.md)"
                    )
        # context_budget field check
        if "context_budget" not in fm:
            errors.append("frontmatter missing 'context_budget' (see TEMPLATE §11)")
        else:
            cb = fm["context_budget"] or {}
            for k in ("always_loaded_tokens", "per_call_typical_tokens",
                      "per_call_max_tokens", "per_call_p90_tokens"):
                if k not in cb:
                    errors.append(f"context_budget missing field '{k}'")
                elif not isinstance(cb[k], int):
                    errors.append(f"context_budget.{k} must be an integer")
        # If using chunks, require a routing table in §11
        if has_chunks:
            if "Routing" not in body and "routing" not in body.lower():
                errors.append(
                    "chunks/ exists but SKILL.md has no routing table. "
                    "Add §11 Routing per TEMPLATE §11."
                )

    # Docs
    for d in REQUIRED_DOCS:
        if not (skill_dir / d).is_file():
            errors.append(f"missing required doc '{d}'")
        else:
            content = (skill_dir / d).read_text()
            if "TEMPLATE" in content and "Replace placeholders" not in content and d == "docs/architecture.md":
                warnings.append(f"{d} still has TEMPLATE placeholder text")

    # Telemetry
    for t in REQUIRED_TELEMETRY:
        if not (skill_dir / t).exists():
            errors.append(f"missing telemetry file '{t}'")
    schema_path = skill_dir / "telemetry" / "schema.json"
    if schema_path.exists():
        try:
            json.loads(schema_path.read_text())
        except json.JSONDecodeError as e:
            errors.append(f"telemetry/schema.json invalid JSON: {e}")

    # Industries count
    if not is_template:
        ind_dir = skill_dir / "industries"
        if ind_dir.is_dir():
            ind_files = [p for p in ind_dir.iterdir() if p.suffix == ".md" and p.name != "_index.md"]
            if len(ind_files) < 3:
                errors.append(f"industries/ has {len(ind_files)} files, require ≥3")
            if not (ind_dir / "_index.md").exists():
                warnings.append("industries/_index.md missing")

    # Use cases count
    if not is_template:
        uc_dir = skill_dir / "use-cases"
        if uc_dir.is_dir():
            uc_files = [p for p in uc_dir.iterdir() if p.suffix == ".md" and p.name != "_index.md"]
            if len(uc_files) < 3:
                errors.append(f"use-cases/ has {len(uc_files)} files, require ≥3")
            if not (uc_dir / "_index.md").exists():
                warnings.append("use-cases/_index.md missing")
            # Per-UC frontmatter checks
            for uc in uc_files:
                uc_text = uc.read_text()
                uc_fm, _ = split_frontmatter(uc_text)
                for k in ("uc_id", "title", "industries", "procedure", "expected_outputs", "oracle", "data_refs", "tests", "status"):
                    if k not in uc_fm:
                        errors.append(f"use-case {uc.name} missing frontmatter field '{k}'")

    # Data
    data_dir = skill_dir / "data"
    if data_dir.is_dir():
        if not (data_dir / "README.md").exists():
            warnings.append("data/README.md missing")
        gens = data_dir / "generators"
        if not gens.exists() or not any(gens.glob("*.py")):
            warnings.append("data/generators/ missing or empty")
        seeds = data_dir / "seeds"
        if not seeds.exists() or not any(seeds.glob("*.json")):
            warnings.append("data/seeds/ missing or empty")

    # Tests
    tests_dir = skill_dir / "tests"
    if tests_dir.is_dir():
        slug = skill_dir.name
        required_tests = {
            f"test_{slug.replace('-', '_')}_lint.py",
            f"test_{slug.replace('-', '_')}_oracle.py",
        }
        for t in required_tests:
            if not (tests_dir / t).exists():
                errors.append(f"tests/{t} missing")

    # TODO/FIXME
    todos = find_todo_outside_changelog(skill_dir, body)
    if todos:
        errors.append(f"TODO/FIXME found outside changelog ({len(todos)}): first 3: {todos[:3]}")

    # Citations vs manifest
    manifest = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", body, re.S)
    if manifest:
        manifest_text = manifest.group(1)
        cites = set(CITE_PATTERN.findall(body))
        for c_label, c_section in cites:
            if c_label not in manifest_text:
                warnings.append(f"citation [{c_label} §{c_section}] not found in §10 manifest")

    return (0 if not errors else 1), errors + ["WARN: " + w for w in warnings]


def main(argv: Iterable[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", help="skill dir(s) to lint")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    total_fail = 0
    for raw in args.paths:
        p = Path(raw)
        if not p.is_dir():
            print(f"SKIP: {p} is not a directory")
            continue
        code, msgs = lint_skill(p)
        status = "PASS" if code == 0 else "FAIL"
        if code != 0 or not args.quiet:
            print(f"\n[{status}] {p}")
            for m in msgs:
                print(f"  - {m}")
        total_fail += code
    return 1 if total_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
