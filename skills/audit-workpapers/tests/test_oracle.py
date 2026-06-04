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
    """UC-01: MUS sample size = 75, sampling interval = $166,667, BP = $500,001."""
    payload = _load("uc-01-input.json")
    out = run_skill("UC-01", payload)

    mus = out["mus_evaluation"]
    assert mus["sample_size"] == 75
    assert mus["sampling_interval"] == 166667
    assert mus["reliability_factor"] == 3.00
    assert mus["basic_precision"] == 500001
    assert mus["upper_limit_misstatement"] == 500001
    assert "ULM" in mus["upper_limit_conclusion"]
    assert out["classification"] == "MUS_SAMPLE_SIZE_75"


def test_uc_02_oracle():
    """UC-02: 5-part C-C-C-E-R finding with severity = Significant Deficiency."""
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)

    finding = out["finding"]
    assert finding["severity"] == "Significant Deficiency"
    assert finding["finding_id"] == 3
    assert finding["wp_index"] == "C-4.2"
    assert finding["assertion"] == "Completeness (Accounts Payable)"
    assert out["ccc_er_complete"] is True
    assert out["classification"] == "SIGNIFICANT_DEFICIENCY"
    for part in ["condition", "criteria", "cause", "effect", "recommendation"]:
        assert finding[part], f"Missing C-C-C-E-R part: {part}"
    assert "16%" in finding["condition"]
    assert "ASC 606" in finding["criteria"]
    assert "Implement ERP" in finding["recommendation"]


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
    assert td["ria_implication"] == "Moderate"
    assert td["rf_implication"] == pytest.approx(2.31)
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
