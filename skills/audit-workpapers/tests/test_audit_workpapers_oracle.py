"""Oracle tests for audit-workpapers.

Each test loads the seed input, runs the skill (via skill_stub), and asserts
that the output matches the expected fixture per the UC's oracle field.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from audit_workpapers_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_oracle():
    """UC-01: MUS sample size = 75, sampling interval = $166,667, BP = $500,000 (= TM)."""
    payload = _load("uc-01-input.json")
    out = run_skill("UC-01", payload)

    mus = out["mus_evaluation"]
    assert mus["sample_size"] == 75
    assert mus["sampling_interval"] == 166667
    assert mus["reliability_factor"] == 3.00
    assert mus["basic_precision"] == 500000  # BP = RF x unrounded SI = TM exactly
    assert mus["upper_limit_misstatement"] == 500000
    assert "accept" in mus["upper_limit_conclusion"], "zero-misstatement golden case must conclude acceptance, not a substring match"
    assert out["classification"] == "MUS_SAMPLE_SIZE_75"


def test_uc_02_oracle():
    """UC-02 (SOX-640): the finding parts come FROM the seed (a preparer fills them);
    completeness for both the C-C-C-E-R finding and the 5-field management response is
    computed — recomputed here independently."""
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)
    finding = out["finding"]

    assert finding["severity"] == "Significant Deficiency"
    assert finding["finding_id"] == 3 and finding["wp_index"] == "C-4.2"
    assert finding["assertion"] == payload["assertion"]
    assert out["classification"] == "SIGNIFICANT_DEFICIENCY"

    # Every C-C-C-E-R part is taken from the seed (derivability), not hardcoded.
    for part in ["condition", "criteria", "cause", "effect", "recommendation"]:
        assert finding[part] == payload[part]
    assert out["ccc_er_complete"] is True
    assert finding["finding_missing_parts"] == []
    assert "16%" in finding["condition"]
    assert "AP Policy AP-200" in finding["criteria"]
    assert "ASC 606" not in finding["criteria"], "revenue-recognition criteria on an AP cutoff finding was a verified defect"
    assert "Implement ERP" in finding["recommendation"]

    # Management-response completeness recomputed from the 5 required fields.
    required = ["owner", "remediation_steps", "target_date",
                "operating_effectiveness_evidence", "retest_window"]
    resp = payload["management_response"]
    assert out["management_response_complete"] == all(resp.get(f) for f in required) is True
    assert out["management_response_missing"] == [f for f in required if not resp.get(f)] == []


def test_uc_02_incomplete_finding_and_response_flagged():
    """A preparer's draft missing a C-C-C-E-R part and a response field is flagged
    (the company-side affordance: it tells you what is still missing)."""
    payload = dict(_load("uc-02-input.json"))
    payload["cause"] = ""  # preparer hasn't written the cause yet
    payload["management_response"] = {**payload["management_response"], "retest_window": ""}
    out = run_skill("UC-02", payload)
    assert out["ccc_er_complete"] is False
    assert "cause" in out["finding"]["finding_missing_parts"]
    assert out["management_response_complete"] is False
    assert "retest_window" in out["management_response_missing"]


def test_uc_03_oracle():
    """UC-03: TD = 20.8%, moderate RIA, TD computed correctly."""
    payload = _load("uc-03-input.json")
    out = run_skill("UC-03", payload)

    td = out["td_calculation"]
    assert td["td_pct"] == pytest.approx(20.8, abs=0.1)
    assert td["ar"] == pytest.approx(0.05)
    assert td["ir"] == pytest.approx(0.80)
    assert td["cr"] == pytest.approx(0.60)
    assert td["ap"] == pytest.approx(0.50)
    assert td["ria_pct"] == pytest.approx(20.8, abs=0.1)  # TD IS the RIA (AS 2315)
    assert td["rf_implication"] == pytest.approx(1.61)
    assert "20.8%" in td["td_formula"]
    assert out["classification"] == "TD_20.8"


@pytest.mark.parametrize("uc_id,expected_key", [
    ("UC-01", "mus_evaluation"),
    ("UC-02", "finding"),
    ("UC-03", "td_calculation"),
])
def test_stub_returns_structured_output(uc_id, expected_key):
    """Every UC returns a dict with the expected structured output key."""
    seeds = {"UC-01": "uc-01-input.json", "UC-02": "uc-02-input.json", "UC-03": "uc-03-input.json"}
    payload = _load(seeds[uc_id])
    out = run_skill(uc_id, payload)
    assert expected_key in out
    assert "classification" in out
