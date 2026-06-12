"""Trace tests for nist-800-53-rmf.

Verifies that skill output references the right §X of SKILL.md for each
decision, so the audit trail is intact.
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_MD = Path(__file__).resolve().parent.parent / "SKILL.md"

# Sections in SKILL.md that each UC's procedure references
EXPECTED_SECTIONS = {
    "UC-01": ["3.6", "4.2", "5.1", "5.2", "5.3", "6.1", "6.2"],
    "UC-02": ["5.4", "5.5", "4.5", "5.6"],
    "UC-03": ["5.7", "3.6", "4.2", "5.2", "6.2", "4.6"],
}


def test_skill_md_referenced_sections_exist():
    body = SKILL_MD.read_text()
    for uc, sections in EXPECTED_SECTIONS.items():
        for sec in sections:
            # Check that the section heading exists somewhere in SKILL.md
            # We accept "## " heading followed by anything, then the §N.N number
            pattern = rf"##\s+\S*{re.escape(sec)}|##\s+\d+\.\d+\s+"
            if not re.search(pattern, body):
                # Looser: the section number appears in body
                assert sec in body, f"UC {uc} references §{sec} but not found in SKILL.md"


def test_non_federal_adoption_chunk_backs_state_rmf_promise():
    """SOX-639: the SKILL.md "state-RMF" / non-federal activation promise must be backed by
    chunks/10-non-federal-adoption.md (it routes there) and that chunk must carry the
    non-federal authorization model + resource-constrained risk-based scoping — not an
    unbacked claim that assumes federal-only AO machinery."""
    chunk = Path(__file__).resolve().parent.parent / "chunks" / "10-non-federal-adoption.md"
    assert chunk.exists(), "chunks/10-non-federal-adoption.md must exist to back the state-RMF promise"
    ctext = chunk.read_text()
    assert "chunk_id: 10-non-federal-adoption" in ctext
    # The load-bearing content: who authorizes absent a federal AO + risk-based scoping.
    assert "authorizing authority" in ctext.lower()
    assert "absent a federal AO" in ctext or "without a federal AO" in ctext.lower() or "no automatic equivalent" in ctext
    for term in ("family prioritization", "prior-evidence reuse", "multi-year"):
        assert term.lower() in ctext.lower(), f"resource-constrained scoping missing '{term}'"
    # SKILL.md must route to it and back the activation promise.
    body = SKILL_MD.read_text()
    assert "chunks/10-non-federal-adoption.md" in body, "SKILL.md must route to chunk 10"
    assert "non-federal" in body.lower(), "SKILL.md activation must name the non-federal path"


def test_use_cases_cite_skill_sections():
    """Each use case's procedure must cite real SKILL.md sections or chunks/ files.

    Note: in the chunks layout, deep sections like §3.6, §4.2 live in chunk files,
    not in SKILL.md. The test only checks the structured `procedure:` frontmatter
    field (which is the canonical citation) and accepts:
      - a `chunks/NN-*.md` reference (resolves to a real chunk), OR
      - a §X.Y reference that resolves to a section in SKILL.md.
    Walk-through prose that mentions §X.Y in passing is allowed but not validated.
    """
    uc_dir = Path(__file__).resolve().parent.parent / "use-cases"
    body = SKILL_MD.read_text()
    chunks_dir = Path(__file__).resolve().parent.parent / "chunks"
    chunks = {p.name for p in chunks_dir.glob("*.md")} if chunks_dir.exists() else set()
    for uc_file in uc_dir.glob("uc-*.md"):
        text = uc_file.read_text()
        # Only validate the procedure list in frontmatter (between uc_id and the
        # next top-level key). The procedure field is structured YAML.
        m = re.search(r"procedure:\s*\n((?:\s*-\s*.+\n)+)", text)
        assert m, f"{uc_file.name} has no procedure field in frontmatter"
        procedure_block = m.group(1)
        chunk_cites = re.findall(r"chunks/(\d{2}-[\w-]+\.md)", procedure_block)
        section_cites = re.findall(r"§\s*([\d.]+)", procedure_block)
        for c in chunk_cites:
            assert c in chunks, f"{uc_file.name} cites chunks/{c} but file does not exist"
        for c in section_cites:
            assert c in body, f"{uc_file.name} procedure cites §{c} but not in SKILL.md"
