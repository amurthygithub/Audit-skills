"""Oracle tests for coso-internal-controls."""
from __future__ import annotations
import json
from pathlib import Path
from skill_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"

def _load(name):
    return json.loads((DATA / name).read_text())

def test_uc_01_oracle():
    payload = _load("uc-01-input.json")
    out = run_skill("UC-01", payload)
    assert out["rcm"]["processes"] == 3
    assert out["rcm"]["total_controls_identified"] == 45
    assert out["rcm"]["key_controls"] == 28
    assert out["rcm"]["deficiencies_identified"] == 3
    assert len(out["deficiencies"]) == 3
    assert out["deficiencies"][0]["classification"] == "Significant Deficiency"
    assert out["entity_level_controls"]["P1_integrity_commitment"]["present"] is True
    assert out["management_icfr_report"]["conclusion"] == "Effective, subject to remediation"

def test_uc_02_oracle():
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)
    assert out["classification"] == "Significant Deficiency"
    assert out["decision_tree"]["step1"]["conclusion"] == "Deficiency exists."
    assert out["decision_tree"]["step2"]["conclusion"] == "Reasonable possibility exists."
    assert out["mw_indicators"]["any_present"] is False
    assert len(out["compensating_control_analysis"]) == 3
    assert out["remediation"]["owner"] == "IT Security Manager"

def test_uc_03_oracle():
    payload = _load("uc-03-input.json")
    out = run_skill("UC-03", payload)
    assert len(out["principle_assessments"]) == 17
    for pa in out["principle_assessments"]:
        assert pa["present_and_functioning"] is True
    assert len(out["component_assessments"]) == 5
    assert out["component_assessments"]["Control Environment"]["present_and_functioning"] is True
    assert "All 17 principles" in out["overall"]
