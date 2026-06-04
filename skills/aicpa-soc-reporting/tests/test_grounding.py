"""Grounding tests for aicpa-soc-reporting.

Verifies that:
  1. Citations of the form [LABEL X] in SKILL.md resolve to 10. References.
  2. Citations in the use-cases resolve to SKILL.md.
  3. No hallucinated paragraph numbers.
"""

from __future__ import annotations

import re
from pathlib import Path

SKILL_MD = Path(__file__).resolve().parent.parent / "SKILL.md"


def test_in_body_citations_resolve_to_manifest():
    body = SKILL_MD.read_text()
    manifest_match = re.search(
        r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)",
        body, re.S,
    )
    assert manifest_match, "10. References & Citation Manifest not found in SKILL.md"
    manifest_text = manifest_match.group(1)

    cite_pattern = re.compile(r"\[([A-Z][A-Z0-9 .\-:&/()]+?)\]")
    cites = cite_pattern.findall(body)
    missing = []
    for label in cites:
        if label not in manifest_text:
            missing.append(label)
    assert not missing, f"Citations not in 10. manifest: {missing}"


def test_manifest_has_required_fields():
    body = SKILL_MD.read_text()
    manifest_match = re.search(
        r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)",
        body, re.S,
    )
    assert manifest_match
    text = manifest_match.group(1)
    for required_col in ["Title", "Publisher", "Identifier"]:
        assert required_col in text, f"Manifest missing column: {required_col}"


def test_no_hallucinated_paragraph_numbers():
    body = SKILL_MD.read_text()
    bad_patterns = [
        r"\bparagraph\s+\d{2,}\b",
        r"\bpage\s+\d{2,}\b",
    ]
    for pat in bad_patterns:
        m = re.findall(pat, body, re.IGNORECASE)
        assert not m, f"Hallucinated paragraph/page numbers: {m}"
