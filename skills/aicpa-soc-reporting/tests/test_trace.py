
"""Trace tests for aicpa-soc-reporting.

Verifies that skill output references the right sections of SKILL.md for each
decision, so the audit trail is intact.
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_MD = Path(__file__).resolve().parent.parent / "SKILL.md"

EXPECTED_SECTIONS = {
    "UC-01": ["3.1", "3.3", "4", "6", "7", "8"],
    "UC-02": ["3.2", "4", "6"],
    "UC-03": ["3.2", "4", "5", "8"],
    "UC-04": ["3.1", "3.3", "4", "6"],
}


def test_skill_md_referenced_sections_exist():
    body = SKILL_MD.read_text()
    for uc, sections in EXPECTED_SECTIONS.items():
        for sec in sections:
            assert sec in body, f"UC {uc} references section {sec} but not found in SKILL.md"



def test_use_cases_cite_skill_sections():
    """Each use case"s procedure must cite real SKILL.md sections or chunks/ files.

    Note: in the chunks layout, deep sections like 3.6, 4.2 live in chunk files,
    not in SKILL.md. The test only checks the structured procedure: frontmatter
    field (which is the canonical citation) and accepts:
      - a chunks/NN-*.md reference (resolves to a real chunk), OR
      - a SKILL.md X.Y reference that resolves to a section in SKILL.md.
    Walk-through prose that mentions X.Y in passing is allowed but not validated.
    """
    uc_dir = Path(__file__).resolve().parent.parent / "use-cases"
    body = SKILL_MD.read_text()
    chunks_dir = Path(__file__).resolve().parent.parent / "chunks"
    chunks = {p.name for p in chunks_dir.glob("*.md")} if chunks_dir.exists() else set()
    for uc_file in uc_dir.glob("uc-*.md"):
        text = uc_file.read_text()
        # Extract YAML frontmatter between first two --- markers
        fm_parts = text.split("---")
        if len(fm_parts) >= 3:
            fm_text = fm_parts[1]
        else:
            fm_text = text

        # Check for procedure field in frontmatter
        m = re.search(r"procedure:\s*\n((?:\s*-\s*.+\n)+)", fm_text)
        assert m, f"{uc_file.name} has no valid procedure field in frontmatter"
        procedure_block = m.group(1)
        chunk_cites = re.findall(r"chunks/([\d]{2}-[\w-]+\.md)", procedure_block)
        section_cites = re.findall(r"SKILL\.md\s*\u00a7\s*([\d.]+)", procedure_block)
        for c in chunk_cites:
            assert c in chunks, f"{uc_file.name} cites chunks/{c} but file does not exist"
        for s in section_cites:
            assert s in body, f"{uc_file.name} procedure cites SKILL.md section {s}"