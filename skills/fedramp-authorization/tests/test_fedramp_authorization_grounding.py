"""Grounding tests for fedramp-authorization.

Spot-checks that citations in the body of SKILL.md resolve to the §10
References & Citation Manifest, and that the manifest covers the core primary
sources (the FedRAMP Authorization Act, OMB M-24-15, the Rev 5 baselines, ConMon,
the A2LA 3PAO accreditation, and NIST SP 800-53 Rev 5).
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SKILL_MD = SKILL_DIR / "SKILL.md"
CITE_PATTERN = re.compile(r"\[([A-Za-z0-9][A-Za-z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-()]+)\]")


def _get_manifest_text() -> str:
    text = SKILL_MD.read_text()
    m = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1) if m else ""


def test_manifest_present():
    assert _get_manifest_text(), "Missing §10 References & Citation Manifest"


def test_core_statute_in_manifest():
    manifest = _get_manifest_text()
    assert "FEDRAMP-ACT-2022" in manifest, "FedRAMP Authorization Act citation missing from manifest"


def test_governance_memo_in_manifest():
    manifest = _get_manifest_text()
    assert "OMB-M-24-15" in manifest, "OMB M-24-15 reference missing from manifest"


def test_baselines_and_conmon_in_manifest():
    manifest = _get_manifest_text()
    assert "FEDRAMP-REV5-BASELINES" in manifest, "Rev 5 baselines reference missing from manifest"
    assert "FEDRAMP-CONMON" in manifest, "ConMon reference missing from manifest"


def test_3pao_and_80053_in_manifest():
    manifest = _get_manifest_text()
    assert "A2LA-3PAO" in manifest, "A2LA 3PAO accreditation reference missing from manifest"
    assert "NIST-800-53R5" in manifest, "NIST SP 800-53 Rev 5 reference missing from manifest"


def test_in_body_citations_resolve_to_manifest():
    text = SKILL_MD.read_text()
    cites = set(CITE_PATTERN.findall(text))
    manifest = _get_manifest_text()
    for label, section in cites:
        assert label in manifest, f"Citation [{label} §{section}] not in manifest"
