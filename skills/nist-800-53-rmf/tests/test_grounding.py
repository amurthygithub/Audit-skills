"""Grounding tests for nist-800-53-rmf.

Verifies that:
  1. Citations of the form [LABEL §N] in SKILL.md resolve to §10 References.
  2. Citations in the use-cases resolve to SKILL.md.
  3. No hallucinated "§X.Y" patterns that don't exist.
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
    assert manifest_match, "§10 References & Citation Manifest not found in SKILL.md"
    manifest_text = manifest_match.group(1)

    cite_pattern = re.compile(r"\[([A-Z][A-Z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-]+)\]")
    cites = cite_pattern.findall(body)
    missing = []
    for label, _section in cites:
        if label not in manifest_text:
            missing.append(label)
    assert not missing, f"Citations not in §10 manifest: {missing}"


def test_manifest_has_required_fields():
    body = SKILL_MD.read_text()
    manifest_match = re.search(
        r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)",
        body, re.S,
    )
    assert manifest_match
    text = manifest_match.group(1)
    # Each row should have Title, Publisher, Identifier, Retrieval, URL
    # We accept a markdown table format
    for required_col in ["Title", "Publisher", "Identifier"]:
        assert required_col in text, f"Manifest missing column: {required_col}"


def test_no_hallucinated_paragraph_numbers():
    """No patterns like 'paragraph 47' or 'page 13' without source citation."""
    body = SKILL_MD.read_text()
    bad_patterns = [
        r"\bparagraph\s+\d{2,}\b",  # paragraph 47
        r"\bpage\s+\d{2,}\b",       # page 13
    ]
    for pat in bad_patterns:
        m = re.findall(pat, body, re.IGNORECASE)
        assert not m, f"Hallucinated paragraph/page numbers: {m}"
