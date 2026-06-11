"""Metamorphic tests for fedramp-authorization."""

from __future__ import annotations

import json
from pathlib import Path

from fedramp_authorization_stub import run_skill

SEEDS = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name):
    return json.loads((SEEDS / name).read_text())


def test_uc01_raising_an_objective_to_high_flips_baseline():
    """Raising any single CIA objective to High moves the high-water mark to High -> 410."""
    p = dict(_load("uc-01-input.json"))
    p["fips199"] = {**p["fips199"], "availability": "High"}
    out = run_skill("UC-01", p)
    assert out["overall_impact"] == "High"
    assert out["baseline_controls"] == 410
    assert out["classification"] == "FEDRAMP_HIGH"


def test_uc01_finding_order_invariance():
    p1 = _load("uc-01-input.json")
    p2 = dict(p1)
    p2["sar_findings"] = list(reversed(p1["sar_findings"]))
    o1, o2 = run_skill("UC-01", p1), run_skill("UC-01", p2)
    assert o1["poam_open"] == o2["poam_open"]
    assert {p["id"]: p["remediation_due"] for p in o1["poam"]} == \
           {p["id"]: p["remediation_due"] for p in o2["poam"]}


def test_uc02_moderate_saas_is_not_li_saas():
    """Raising impact to Moderate makes a SaaS ineligible for LI-SaaS -> full Moderate (323)."""
    p = dict(_load("uc-02-input.json"))
    p["fips199"] = {**p["fips199"], "confidentiality": "Moderate"}
    out = run_skill("UC-02", p)
    assert out["li_saas_eligible"] is False
    assert out["baseline"] == "Moderate"
    assert out["baseline_controls"] == 323


def test_uc03_marking_a_failed_control_inherited_removes_the_poam_item():
    """Inheriting a failed control moves it off the leveraging CSP's POA&M."""
    p = dict(_load("uc-03-input.json"))
    controls = [dict(c) for c in p["controls"]]
    for c in controls:
        if c["id"] == "AC-2":
            c["inherited"] = True  # now provider-owned
    p["controls"] = controls
    out = run_skill("UC-03", p)
    assert "AC-2" not in out["findings"]
    assert out["poam_item_count"] == 3


def test_uc03_control_order_invariance():
    p1 = _load("uc-03-input.json")
    p2 = dict(p1)
    p2["controls"] = list(reversed(p1["controls"]))
    o1, o2 = run_skill("UC-03", p1), run_skill("UC-03", p2)
    assert sorted(o1["findings"]) == sorted(o2["findings"])
    assert o1["findings_by_severity"] == o2["findings_by_severity"]
