"""Grounding tests for hipaa-security-rule.

Spot-checks that citations in the body of SKILL.md resolve to the
§10 References & Citation Manifest, and that the manifest covers the core
primary sources (45 CFR 164 Subpart C, the 2025 NPRM, NIST SP 800-66r2).
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"
# Labels may start with a digit (e.g. CFR-45-164-Subpart-C) and contain
# mixed case (Subpart), unlike the all-caps NIST labels.
CITE_PATTERN = re.compile(r"\[([A-Za-z0-9][A-Za-z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-()]+)\]")


def _get_manifest_text() -> str:
    text = SKILL_MD.read_text()
    m = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1) if m else ""


def test_manifest_present():
    """SKILL.md must have a §10 References & Citation Manifest section."""
    assert _get_manifest_text(), "Missing §10 References & Citation Manifest"


def test_core_subpart_c_in_manifest():
    """CFR-45-164-Subpart-C should appear in the manifest as the primary citation."""
    manifest = _get_manifest_text()
    assert "CFR-45-164-Subpart-C" in manifest, (
        "Primary citation CFR-45-164-Subpart-C missing from manifest"
    )


def test_in_body_citations_resolve_to_manifest():
    """Every [LABEL §X] citation in SKILL.md should be resolvable in the manifest."""
    text = SKILL_MD.read_text()
    cites = set(CITE_PATTERN.findall(text))
    manifest = _get_manifest_text()
    for label, section in cites:
        assert label in manifest, f"Citation [{label} §{section}] not in manifest"


def test_nprm_manifest_entry():
    """The 2025 Security Rule NPRM (90 FR 898, PROPOSED only) should be in the manifest."""
    manifest = _get_manifest_text()
    has_nprm = "HIPAA-Security-NPRM-2025" in manifest or "NPRM" in manifest
    assert has_nprm, "2025 Security Rule NPRM entry missing from manifest"


def test_800_66r2_in_manifest():
    """NIST SP 800-66r2 (the current implementation guide) should be in the manifest."""
    manifest = _get_manifest_text()
    assert "800-66" in manifest, "NIST SP 800-66r2 reference missing from manifest"
