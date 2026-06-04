"""Oracle tests for nist-800-53-rmf.

Each test loads the seed input, runs the skill (via skill_stub), and asserts
that the output matches the expected fixture per the UC's oracle field.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from skill_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_oracle():
    """UC-01: FIPS 199 categorization = MODERATE, baseline = MODERATE, inheritance correct."""
    payload = _load("uc-01-input.json")
    expected = _load("uc-01-expected.json")
    out = run_skill("UC-01", payload)

    # Oracle assertions per UC-01 frontmatter
    assert out["fips_199_categorization"]["overall"] == "MODERATE"
    assert out["baseline"]["baseline"] == "MODERATE"
    assert out["fips_199_categorization"]["system_security_category"] == {
        "c": "MODERATE", "i": "MODERATE", "a": "LOW"
    }
    # Sanity: expected fixture has the same overall
    assert expected["fips_199_categorization"]["overall"] == "MODERATE"
    assert expected["baseline"]["baseline"] == "MODERATE"


def test_uc_02_oracle():
    """UC-02: SAR 22 findings, ATO with conditions, residual risk = MODERATE."""
    payload = _load("uc-02-input.json")
    findings = _load("uc-02-findings.json")
    payload["findings"] = findings
    expected = _load("uc-02-expected.json")
    out = run_skill("UC-02", payload)

    # Oracle assertions per UC-02 frontmatter
    assert out["sar"]["total_findings"] == 22
    assert out["ato_decision"]["decision"] == "AUTHORIZE_WITH_CONDITIONS"
    assert out["ato_decision"]["residual_risk"] == "MODERATE"
    # Severity distribution sums to 22
    assert sum(out["sar"]["severity_distribution"].values()) == 22
    # Sanity vs expected
    assert expected["ato_decision"]["decision"] == "AUTHORIZE_WITH_CONDITIONS"


def test_uc_03_oracle():
    """UC-03: 71% overlap, 94 gap controls, baseline MODERATE."""
    payload = _load("uc-03-input.json")
    crosswalk = json.loads((DATA.parent / "crosswalks" / "soc2-to-800-53-mod.json").read_text())
    payload["crosswalk"] = crosswalk
    out = run_skill("UC-03", payload)

    # Oracle assertions per UC-03 frontmatter
    assert out["crosswalk_summary"]["overlap_pct"] in range(68, 76)  # 71 ± 3
    assert 80 <= out["crosswalk_summary"]["gap_controls"] <= 110  # ~94
    assert out["crosswalk_summary"]["soc2_common_criteria"] == 9
    assert out["baseline"]["baseline"] == "MODERATE"


@pytest.mark.parametrize("uc_id,expected_overall", [
    ("UC-01", "MODERATE"),
])
def test_uc_01_categorization_pattern(uc_id, expected_overall):
    """Verify the categorization pattern: high-water mark across C/I/A."""
    payload = _load("uc-01-input.json")
    out = run_skill(uc_id, payload)
    cia = out["fips_199_categorization"]["system_security_category"]
    overall = max(cia.values(), key=lambda x: ["LOW", "MODERATE", "HIGH"].index(x))
    assert overall == expected_overall
