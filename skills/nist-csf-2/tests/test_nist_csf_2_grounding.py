"""Grounding tests for nist-csf-2.

Spot-checks that citations in the body of SKILL.md and chunks resolve to the
§10 References & Citation Manifest, and that the manifest covers the core
NIST publications.
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"
CITE_PATTERN = re.compile(r"\[([A-Z][A-Z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-]+)\]")


def _get_manifest_text() -> str:
    text = SKILL_MD.read_text()
    m = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1) if m else ""


def test_manifest_present():
    """SKILL.md must have a §10 References & Citation Manifest section."""
    assert _get_manifest_text(), "Missing §10 References & Citation Manifest"


def test_core_csf_2_in_manifest():
    """NIST-CSF-2.0 should appear in the manifest as the primary citation."""
    manifest = _get_manifest_text()
    assert "NIST-CSF-2.0" in manifest, "Primary citation NIST-CSF-2.0 missing from manifest"


def test_in_body_citations_resolve_to_manifest():
    """Every [LABEL §X] citation in SKILL.md should be resolvable in the manifest."""
    text = SKILL_MD.read_text()
    cites = set(CITE_PATTERN.findall(text))
    manifest = _get_manifest_text()
    for label, section in cites:
        assert label in manifest, f"Citation [{label} §{section}] not in manifest"


def test_informative_references_manifest_entry():
    """NIST Informative References spreadsheet (the source of truth for CSF 2.0 crosswalks) should be in the manifest."""
    manifest = _get_manifest_text()
    # The exact label may vary; check for the substance
    has_ir = "Informative References" in manifest or "informative-references" in manifest
    assert has_ir, "NIST Informative References entry missing from manifest"


def test_800_171_rev_3_in_manifest():
    """NIST 800-171 Rev 3 (the CMMC L2 control set) should be in the manifest."""
    manifest = _get_manifest_text()
    assert "800-171" in manifest, "NIST 800-171 Rev 3 reference missing from manifest"
