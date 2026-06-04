"""Grounding tests for coso-internal-controls.

Verifies that:
  1. Citations of the form [LABEL §N] in SKILL.md resolve to §10 References.
  2. No hallucinated "§X.Y" patterns.
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_MD = Path(__file__).resolve().parent.parent / "SKILL.md"


def test_in_body_citations_resolve_to_manifest():
    body = SKILL_MD.read_text()
    m = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", body, re.S)
    assert m, "§10 not found"
    manifest_text = m.group(1)
    cites = re.findall(r"\[([A-Z][A-Z0-9 .\-:&/\u00a7,()]+?)\s*\u00a7\s*([\w.\-]+)\]", body)
    missing = [l for l, _ in cites if l not in manifest_text]
    assert not missing, f"Cites not in manifest: {missing}"


def test_manifest_has_required_fields():
    body = SKILL_MD.read_text()
    m = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", body, re.S)
    assert m
    for col in ["Title", "Publisher", "Identifier"]:
        assert col in m.group(1), f"Missing column: {col}"


def test_no_hallucinated_paragraph_numbers():
    body = SKILL_MD.read_text()
    for pat in [r"\bparagraph\s+\d{2,}\b", r"\bpage\s+\d{2,}\b"]:
        assert not re.findall(pat, body, re.IGNORECASE), f"Hallucinated: {pat}"
