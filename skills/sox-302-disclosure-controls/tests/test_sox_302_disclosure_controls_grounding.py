"""Grounding tests for sox-302-disclosure-controls.

Spot-checks that citations in the body of SKILL.md resolve to the
§10 References & Citation Manifest, and that the manifest covers the core
primary sources (15 U.S.C. 7241; SEC Rules 17 CFR 240.13a-14 / 240.13a-15;
Reg S-K Items 307 and 308).
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"
# Labels may start with a digit, carry a "§" segment (e.g. CFR-17-240.13a-15),
# and mix case (Reg-S-K-Item-307), unlike the all-caps NIST labels.
CITE_PATTERN = re.compile(r"\[([A-Za-z0-9][A-Za-z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-()]+)\]")


def _get_manifest_text() -> str:
    text = SKILL_MD.read_text()
    m = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1) if m else ""


def test_manifest_present():
    """SKILL.md must have a §10 References & Citation Manifest section."""
    assert _get_manifest_text(), "Missing §10 References & Citation Manifest"


def test_core_statute_in_manifest():
    """SOX-302-Statute-15USC7241 should appear in the manifest as the primary citation."""
    manifest = _get_manifest_text()
    assert "SOX-302-Statute-15USC7241" in manifest, (
        "Primary citation SOX-302-Statute-15USC7241 missing from manifest"
    )


def test_in_body_citations_resolve_to_manifest():
    """Every [LABEL §X] citation in SKILL.md should be resolvable in the manifest."""
    text = SKILL_MD.read_text()
    cites = set(CITE_PATTERN.findall(text))
    manifest = _get_manifest_text()
    for label, section in cites:
        assert label in manifest, f"Citation [{label} §{section}] not in manifest"


def test_implementing_rules_in_manifest():
    """The Rule 13a-14 / 13a-15 implementing rules should be in the manifest."""
    manifest = _get_manifest_text()
    assert "CFR-17-240.13a-14" in manifest, "Rule 13a-14 (cert exhibit) missing from manifest"
    assert "CFR-17-240.13a-15" in manifest, "Rule 13a-15 (DC&P/ICFR defs) missing from manifest"


def test_reg_sk_items_in_manifest():
    """Reg S-K Item 307 (DC&P disclosure) and Item 308 (ICFR) should be in the manifest."""
    manifest = _get_manifest_text()
    assert "Reg-S-K-Item-307" in manifest, "Reg S-K Item 307 reference missing from manifest"
    assert "Reg-S-K-Item-308" in manifest, "Reg S-K Item 308 reference missing from manifest"
