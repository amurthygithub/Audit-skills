"""Grounding tests for isaca-audit-methodology.

Verifies that:
  1. Citations of the form [LABEL] in SKILL.md resolve to section 10 References.
  2. Citations in the use-cases resolve to SKILL.md.
  3. No hallucinated patterns that don't exist.
"""

from __future__ import annotations
import re
from pathlib import Path

SKILL_MD = Path(__file__).resolve().parent.parent / "SKILL.md"


def test_in_body_citations_resolve_to_manifest():
    body_full = SKILL_MD.read_text()
    manifest_match = re.search(r"## 10\.\s*References & Citation Manifest(.*?)(?=\n## |\Z)", body_full, re.S)
    assert manifest_match, "section 10 References & Citation Manifest not found in SKILL.md"
    manifest_text = manifest_match.group(1)

    body_main = body_full.split("---", 2)[-1] if body_full.startswith("---") else body_full
    cite_pattern = re.compile(r"\[([A-Z][A-Z0-9 .\-:&/(),\u00a7]+?)\]")
    raw_cites = cite_pattern.findall(body_main)
    manifest_labels = set(re.findall(r"^\| ([A-Z][A-Za-z0-9\-.]+) ", manifest_text, re.M)) - {"Label"}
    all_cites = []
    for c in raw_cites:
        all_cites.extend(s.strip() for s in c.split(","))
    missing = []
    for c in all_cites:
        if c in manifest_labels:
            continue
        if any(ml.startswith(c) or c.startswith(ml) for ml in manifest_labels):
            continue
        if any(w in c for w in ["\u00a7", "LABEL", "Title"]):
            continue
        missing.append(c)
    assert not missing, f"Citations not in section 10 manifest: {missing}"


def test_manifest_has_required_fields():
    body_full = SKILL_MD.read_text()
    manifold_match = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", body_full, re.S)
    assert manifold_match
    text = manifold_match.group(1)
    for required_col in ["Title", "Publisher", "Identifier"]:
        assert required_col in text, f"Manifest missing column: {required_col}"


def test_no_hallucinated_paragraph_numbers():
    body_full = SKILL_MD.read_text()
    bad_patterns = [r"\bparagraph\s+\d{2,}\b", r"\bpage\s+\d{2,}\b"]
    for pat in bad_patterns:
        m = re.findall(pat, body_full, re.IGNORECASE)
        assert not m, f"Hallucinated paragraph/page numbers: {m}"


def test_isaca_citations_resolve():
    body_full = SKILL_MD.read_text()
    manifold_match = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", body_full, re.S)
    assert manifold_match
    manifest_text = manifold_match.group(1)
    for label in ["CISA-CRM-28E", "COBIT-2019", "ITAF", "ISACA-ETHICS"]:
        assert label in manifest_text, f"Required citation label: {label}"


def test_no_hallucinated_isaca_references():
    body_full = SKILL_MD.read_text()
    manifold_match = re.search(r"## 10\..*References & Citation Manifest(.*?)(?=\n## |\Z)", body_full, re.S)
    assert manifold_match
    manifest_text = manifold_match.group(1)
    bracket_refs = re.findall(r"\[([A-Z][A-Z0-9\- ]{4,})\]", body_full)
    known_prefixes = {"CISA", "COBIT", "ITAF", "ISACA", "COSO", "AICPA", "NIST", "ISO", "ITIL", "NIST-SP"}
    for ref in bracket_refs:
        clean = ref.strip()
        if clean in manifest_text:
            continue
        if not any(clean.startswith(p) for p in known_prefixes):
            continue
        assert clean in manifest_text, f"Reference [{clean}] missing from section 10 manifest"
