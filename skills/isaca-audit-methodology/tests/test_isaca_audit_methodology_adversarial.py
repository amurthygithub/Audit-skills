"""Adversarial tests for isaca-audit-methodology.

Edge-case inputs that test the skill's robustness.
"""

from __future__ import annotations

import json
from pathlib import Path

from isaca_audit_methodology_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_empty_processes_in_scope():
    """Empty processes_in_scope gives empty process list but valid structure."""
    payload = _load("uc-01-input.json")
    payload["processes_in_scope"] = []
    out = run_skill("UC-01", payload)
    assert out["classification"] == "GAP_0.0"
    assert out["maturity_assessment"]["processes"] == []


def test_uc_01_unknown_process_id():
    """Unknown process ID should fall back to default maturity."""
    payload = _load("uc-01-input.json")
    payload["processes_in_scope"] = ["XYZ99"]
    out = run_skill("UC-01", payload)
    proc = out["maturity_assessment"]["processes"][0]
    assert proc["id"] == "XYZ99"
    assert proc["current_maturity"] == 2.0


def test_uc_02_missing_sample_results():
    """Missing sample_results should not crash."""
    payload = {"finding_context": {"title": "Test finding"}}
    out = run_skill("UC-02", payload)
    assert "observation" in out
    assert out["observation"]["severity"] in ("Low", "Medium", "High", "Critical")
    assert out["observation"]["sample_summary"]["total_applications"] == 0


def test_uc_02_all_fields_present():
    """All 5 parts of observation must be present."""
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)
    obs = out["observation"]
    for field in ("condition", "criteria", "cause", "effect"):
        assert field in obs
        assert obs[field], f"{field} must not be empty"
    assert len(obs["recommendations"]) >= 1


def test_uc_03_missing_risk_profile():
    """Missing risk_profile should produce defaults."""
    payload = {"enterprise_strategy": "Compliance-focused"}
    out = run_skill("UC-03", payload)
    rp = out["design_factor_assessment"]["risk_profile"]
    assert rp["regulatory_risk"] == "High"
    assert rp["technology_risk"] == "Moderate"
    assert rp["vendor_risk"] == "High"


def test_uc_03_invalid_strategy():
    """Unknown strategy still works."""
    payload = _load("uc-03-input.json")
    payload["enterprise_strategy"] = "SomeUnknownStrategy"
    out = run_skill("UC-03", payload)
    assert out["design_factor_assessment"]["enterprise_strategy"] == "SomeUnknownStrategy"
    assert len(out["design_factor_assessment"]["prioritized_objectives"]) == 5


def test_unknown_use_case():
    """Unknown use case returns UNKNOWN classification."""
    out = run_skill("UC-99", {})
    assert out["classification"] == "UNKNOWN"
    assert "error" in out
