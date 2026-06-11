"""Grounding tests for pci-dss-assessment.

Spot-checks that citations in the body of SKILL.md resolve to the
§10 References & Citation Manifest, and that the manifest covers the core
primary sources (the PCI SSC document library, the v4.0.1 blog announcement,
and the NIST OLIR crosswalk anchor).
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"
# Labels may start with a digit (e.g. PCI-DSS-v4-0-1) and contain mixed case,
# matching the hipaa CITE_PATTERN so a [LABEL §X] citation resolves the same way.
CITE_PATTERN = re.compile(r"\[([A-Za-z0-9][A-Za-z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-()]+)\]")


def _get_manifest_text() -> str:
    text = SKILL_MD.read_text()
    m = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1) if m else ""


def test_manifest_present():
    """SKILL.md must have a §10 References & Citation Manifest section."""
    assert _get_manifest_text(), "Missing §10 References & Citation Manifest"


def test_core_standard_in_manifest():
    """The PCI SSC document library should appear in the manifest as the primary citation."""
    manifest = _get_manifest_text()
    assert "PCI-SSC-Document-Library" in manifest, (
        "Primary citation PCI-SSC-Document-Library missing from manifest"
    )


def test_in_body_citations_resolve_to_manifest():
    """Every [LABEL §X] citation in SKILL.md should be resolvable in the manifest."""
    text = SKILL_MD.read_text()
    cites = set(CITE_PATTERN.findall(text))
    manifest = _get_manifest_text()
    for label, section in cites:
        assert label in manifest, f"Citation [{label} §{section}] not in manifest"


def test_version_announcement_manifest_entry():
    """The v4.0.1 "Just Published" blog (the only active version) should be in the manifest."""
    manifest = _get_manifest_text()
    has_blog = "PCI-SSC-Blog-v401" in manifest or "v4.0.1" in manifest or "v4_0_1" in manifest
    assert has_blog, "v4.0.1 version announcement entry missing from manifest"


def test_olir_crosswalk_anchor_in_manifest():
    """The NIST OLIR crosswalk anchor (no rows in v1) should be in the manifest."""
    manifest = _get_manifest_text()
    has_olir = "NIST-OLIR" in manifest or "OLIR" in manifest
    assert has_olir, "NIST OLIR crosswalk anchor missing from manifest"
