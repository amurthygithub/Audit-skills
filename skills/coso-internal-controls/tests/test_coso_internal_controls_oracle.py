"""Oracle tests for coso-internal-controls."""
from __future__ import annotations
import json
from pathlib import Path
from coso_internal_controls_stub import run_skill

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
    assert out["management_icfr_report"]["conclusion"] == "Effective"  # 33-8810: no qualified ICFR conclusions; SD goes to the audit committee, not the report

def test_uc_02_oracle():
    """SOX-641 rework — derivability: the classification is recomputed here from
    the seed facts (assertion-relevance + IPE-independence of each compensating
    control, authority-driven magnitude, lookback) and must equal the stub."""
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)
    d = payload["deficiency"]
    risk = d["assertion_at_risk"]
    affected = set(d["affected_systems"])

    # Independent recompute: no candidate addresses the occurrence assertion AND
    # is independent of the affected ERP -> zero qualifying controls.
    qualifying = [c["control"] for c in payload["compensating_controls_candidates"]
                  if risk in c["assertions_addressed"] and c["relies_on_ipe_from"] not in affected]
    assert qualifying == []
    assert out["qualifying_compensating_controls"] == []
    assert risk == "occurrence" and out["assertion_at_risk"] == "occurrence"

    # Every candidate correctly disqualified (reconciliations: wrong assertion + IPE-impaired).
    for a in out["compensating_control_analysis"]:
        assert a["qualifies"] is False
        assert a["addresses_assertion_at_risk"] is False
        assert a["ipe_impaired_by_deficiency"] is True

    # Pervasive ITGC + material (authority-driven, not-capped) magnitude + no lookback -> MW.
    assert out["itgc_pervasive"] is True
    assert out["magnitude"]["material"] is True  # no hard "unbounded" overclaim
    assert out["lookback"]["performed"] is False and out["lookback"]["rules_out_occurrence"] is False
    assert out["classification"] == "Material Weakness"
    # The conclusion is reached on the ordinary severity test, not an AS 2201.69 indicator.
    assert "ordinary severity test" in out["basis"] and "presumption" not in out["basis"].lower()
    assert out["preliminary_classification"] == "Significant Deficiency"
    assert out["remediation"]["owner"] == "IT Security Manager"


def _add_occurrence_control(payload, tested):
    payload = dict(payload)
    payload["compensating_controls_candidates"] = payload["compensating_controls_candidates"] + [{
        "control": "Independent re-authorization review of terminated-user transactions",
        "assertions_addressed": ["occurrence"], "relies_on_ipe_from": "access-logs",
        "precision_for_own_assertion": "high", "tested_effective": tested}]
    return payload


def test_uc_02_tested_control_plus_clean_lookback_drops_to_deficiency():
    """A tested, precise occurrence-control AND a clean lookback reduce residual risk
    below the SD threshold -> Deficiency (the MW result is fact-driven)."""
    payload = _add_occurrence_control(_load("uc-02-input.json"), tested=True)
    payload["lookback"] = {"performed": True, "improper_transactions_found": False}
    out = run_skill("UC-02", payload)
    assert out["qualifying_compensating_controls"] == [
        "Independent re-authorization review of terminated-user transactions"]
    assert out["classification"] == "Deficiency"


def test_uc_02_untested_qualifying_control_does_not_demote_below_sd():
    """The over-correction the verifier caught: an UNtested qualifying control, with no
    lookback, must NOT collapse MW->D. No mechanical demotion (chunk 07 Step 5) -> SD."""
    payload = _add_occurrence_control(_load("uc-02-input.json"), tested=False)  # not tested
    out = run_skill("UC-02", payload)  # no lookback
    assert out["classification"] == "Significant Deficiency"


def test_uc_02_tested_control_but_no_lookback_stays_sd():
    """Tested+precise qualifying control but residual magnitude still material absent a
    clean lookback -> Significant Deficiency, not Deficiency."""
    payload = _add_occurrence_control(_load("uc-02-input.json"), tested=True)
    out = run_skill("UC-02", payload)  # no lookback
    assert out["classification"] == "Significant Deficiency"

def test_uc_03_oracle():
    payload = _load("uc-03-input.json")
    out = run_skill("UC-03", payload)
    assert len(out["principle_assessments"]) == 17
    for pa in out["principle_assessments"]:
        assert pa["present_and_functioning"] is True
    assert len(out["component_assessments"]) == 5
    assert out["component_assessments"]["Control Environment"]["present_and_functioning"] is True
    assert "All 17 principles" in out["overall"]
