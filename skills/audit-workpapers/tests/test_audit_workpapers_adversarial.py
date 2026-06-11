"""Adversarial tests for audit-workpapers.

Edge-case inputs that test the skill's robustness. Each test corresponds to a
variation documented in the use case file.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from audit_workpapers_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_zero_population():
    """Edge case: zero population value should be handled gracefully."""
    payload = {"population_book_value": 0, "tolerable_misstatement": 500000}
    out = run_skill("UC-01", payload)
    mus = out["mus_evaluation"]
    assert mus["sample_size"] >= 0


def test_uc_01_missing_tm_refuses():
    """Missing tolerable misstatement must REFUSE, never default — a defaulted TM
    sizes the sample against the wrong materiality (SOX-600 harness probe finding;
    abstention is the passing answer)."""
    payload = {"population_book_value": 12500000}
    with pytest.raises(ValueError, match="missing required sampling parameter"):
        run_skill("UC-01", payload)


def test_uc_01_negative_tm_refuses():
    """Negative TM must refuse rather than emit a nonsense negative interval
    (pre-fix behavior: n=0, SI=-66,667)."""
    payload = {"population_book_value": 5000000, "tolerable_misstatement": -200000}
    with pytest.raises(ValueError, match="invalid sampling parameters"):
        run_skill("UC-01", payload)


def test_uc_02_empty_input():
    """Edge case: empty payload should produce a valid finding with defaults."""
    out = run_skill("UC-02", {})
    finding = out["finding"]
    assert finding["severity"] == "Significant Deficiency"
    assert finding["finding_id"] == 3
    assert out["ccc_er_complete"] is True


def test_uc_02_different_severities():
    """All valid severity values produce valid output."""
    for sev in ["Material Weakness", "Significant Deficiency", "Control Deficiency", "Other"]:
        out = run_skill("UC-02", {"severity": sev})
        assert out["finding"]["severity"] == sev
        assert out["classification"] == sev.upper().replace(" ", "_")


def test_uc_03_missing_fields():
    """Edge case: missing risk model fields should use defaults (80/60/50)."""
    out = run_skill("UC-03", {"ar": "5%"})
    td = out["td_calculation"]
    assert td["td_pct"] == pytest.approx(20.8, abs=0.2)


def test_uc_03_zero_risk_factors():
    """Edge case: near-zero risk factors should not crash."""
    out = run_skill("UC-03", {"ar": "5%", "ir": "1%", "cr": "1%", "ap": "1%"})
    assert "td_calculation" in out
    assert out["td_calculation"]["td_pct"] > 0


def test_unknown_use_case():
    """Unknown use case ID returns UNKNOWN gracefully."""
    out = run_skill("UC-99", {})
    assert out["classification"] == "UNKNOWN"
    assert "error" in out


def test_uc_02_extra_fields():
    """Extra fields in payload should not break output."""
    payload = {"finding_id": 7, "wp_index": "F-9.1", "severity": "Material Weakness", "extra_field": "ignored"}
    out = run_skill("UC-02", payload)
    assert out["finding"]["finding_id"] == 7
    assert out["finding"]["wp_index"] == "F-9.1"
    assert out["finding"]["severity"] == "Material Weakness"
