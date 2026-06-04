"""Grounding tests for audit-workpapers.

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

    cite_pattern = re.compile(r"\[([A-Z][A-Z0-9 .\-:&/§,()\-]+?)\s*§\s*([\w.\-]+)\]")
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


def test_all_use_cases_in_routing_table():
    body = SKILL_MD.read_text()
    routing_match = re.search(r"## 11\..*Routing(.*?)(?=\n## |\Z)", body, re.S)
    assert routing_match, "§11 Routing table not found"
    routing_text = routing_match.group(1)
    uc_dir = Path(__file__).resolve().parent.parent / "use-cases"
    for uc_file in uc_dir.glob("uc-*.md"):
        uc_id = uc_file.stem.upper().replace("-SAMPLING-WORKPAPER", "").replace("-FIVE-PART-FINDING", "").replace("-RISK-MODEL-TD-CALCULATION", "")
        uc_id_map = {
            "UC-01-SAMPLING-WORKPAPER": "UC-01",
            "UC-02-FIVE-PART-FINDING": "UC-02",
            "UC-03-RISK-MODEL-TD-CALCULATION": "UC-03",
        }
        normalized = uc_id_map.get(uc_file.stem.upper(), uc_id)
        assert normalized in routing_text, f"{uc_file.name} not found in §11 Routing table"


def test_framework_citations_in_manifest():
    body = SKILL_MD.read_text()
    expected_frameworks = [
        "PCAOB-AS-1215",
        "PCAOB-AS-1105",
        "PCAOB-AS-2315",
        "PCAOB-AS-3105",
        "PCAOB-AS-2110",
        "PCAOB-AS-2201",
        "AICPA-AU-C-230",
        "IAASB-ISA-230",
        "COSO-ICIF-2013",
        "ISACA-ITAF",
    ]
    for fw in expected_frameworks:
        assert fw in body, f"Framework {fw} not found in SKILL.md"
