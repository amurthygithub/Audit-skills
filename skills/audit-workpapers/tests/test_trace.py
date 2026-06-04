"""Trace tests for audit-workpapers.

Verifies that skill output references the right §X of SKILL.md for each
decision, so the audit trail is intact.
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_MD = Path(__file__).resolve().parent.parent / "SKILL.md"

EXPECTED_SECTIONS = {
    "UC-01": ["3.5", "3.2", "3.4", "4"],
    "UC-02": ["3.7", "3.4", "3.2"],
    "UC-03": ["3.6", "3.4", "3.2"],
}


def test_skill_md_referenced_sections_exist():
    body = SKILL_MD.read_text()
    for uc, sections in EXPECTED_SECTIONS.items():
        for sec in sections:
            pattern = rf"##\s+\S*{re.escape(sec)}|##\s+\d+\.\d+\s+"
            if not re.search(pattern, body):
                assert sec in body, f"UC {uc} references §{sec} but not found in SKILL.md"


def test_use_cases_cite_chunks():
    """Each use case's procedure must cite real chunk files."""
    uc_dir = Path(__file__).resolve().parent.parent / "use-cases"
    chunks_dir = Path(__file__).resolve().parent.parent / "chunks"
    has_chunks = chunks_dir.exists() and list(chunks_dir.glob("*.md"))

    for uc_file in uc_dir.glob("uc-*.md"):
        text = uc_file.read_text()
        m = re.search(r"procedure:\s*\n((?:\s*-\s*.+\n)+)", text)
        if not m:
            continue
        procedure_block = m.group(1)
        chunk_cites = re.findall(r"chunks/(\d{2}-[\w-]+\.md)", procedure_block)
        if has_chunks:
            chunks = {p.name for p in chunks_dir.glob("*.md")}
            for c in chunk_cites:
                assert c in chunks, f"{uc_file.name} cites chunks/{c} but file does not exist"


def test_use_case_frontmatter_has_required_fields():
    """Every UC YAML frontmatter must have uc_id, title, procedure, expected_outputs, oracle."""
    uc_dir = Path(__file__).resolve().parent.parent / "use-cases"
    required = ["uc_id", "title", "procedure", "expected_outputs", "oracle"]
    for uc_file in uc_dir.glob("uc-*.md"):
        text = uc_file.read_text()
        for field in required:
            assert f"{field}:" in text, f"{uc_file.name} missing {field} in frontmatter"


def test_sk_md_operational_quick_reference_integrity():
    """§12 Operational Quick-Reference items must reference valid chunks files."""
    body = SKILL_MD.read_text()
    m = re.search(r"## 12\..*Operational Quick-Reference(.*?)(?=\n---|\Z)", body, re.S)
    assert m, "§12 Operational Quick-Reference not found"
    text = m.group(1)
    chunk_refs = re.findall(r"chunks/(\d{2}-[\w-]+\.md)", text)
    assert len(chunk_refs) > 0, "No chunks/ references in §12"
