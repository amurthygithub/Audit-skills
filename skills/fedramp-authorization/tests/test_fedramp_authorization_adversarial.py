"""Adversarial tests for fedramp-authorization — edge cases and the fidelity traps."""

from __future__ import annotations

import json
from pathlib import Path

from fedramp_authorization_stub import run_skill

SEEDS = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name):
    return json.loads((SEEDS / name).read_text())


def test_uc01_missing_fips199_refuses():
    """No FIPS 199 categorization -> cannot select a baseline -> refuse, don't guess."""
    out = run_skill("UC-01", {"sar_findings": []})
    assert out["classification"] == "INSUFFICIENT_INPUT"


def test_uc01_invalid_objective_refuses():
    p = dict(_load("uc-01-input.json"))
    p["fips199"] = {"confidentiality": "Severe", "integrity": "Low", "availability": "Low"}
    out = run_skill("UC-01", p)
    assert out["classification"] == "INSUFFICIENT_INPUT"


def test_uc02_moderate_plus_saas_not_li_saas():
    """The fidelity trap: Moderate impact + SaaS delivery is NOT LI-SaaS-eligible."""
    p = dict(_load("uc-02-input.json"))
    p["fips199"] = {"confidentiality": "Moderate", "integrity": "Moderate", "availability": "Low"}
    out = run_skill("UC-02", p)
    assert out["li_saas_eligible"] is False
    assert out["baseline_controls"] == 323


def test_uc02_low_but_not_saas_not_li_saas():
    """LI-SaaS requires SaaS delivery; a Low-impact non-SaaS takes the full Low baseline (156)."""
    p = dict(_load("uc-02-input.json"))
    p["saas_delivery"] = False
    out = run_skill("UC-02", p)
    assert out["li_saas_eligible"] is False
    assert out["baseline"] == "Low"
    assert out["baseline_controls"] == 156


def test_uc02_missing_saas_flag_refuses():
    out = run_skill("UC-02", {"fips199": {"confidentiality": "Low", "integrity": "Low", "availability": "Low"}})
    assert out["classification"] == "INSUFFICIENT_INPUT"


def test_uc03_inherited_high_finding_excluded_from_csp_poam():
    """A failed-and-inherited High control is the provider's POA&M, not the leveraging CSP's."""
    out = run_skill("UC-03", _load("uc-03-input.json"))
    assert "SC-7" not in out["findings"]  # SC-7 is failed+inherited+High in the seed
    assert out["inherited_count"] == 2


def test_uc03_empty_controls_zero_findings():
    p = dict(_load("uc-03-input.json"))
    p["controls"] = []
    out = run_skill("UC-03", p)
    assert out["poam_item_count"] == 0 and out["findings"] == []
    assert out["classification"] == "SAR_FINDINGS_0"
    assert out["has_high_severity_finding"] is False


def test_unknown_use_case_refuses():
    out = run_skill("UC-99", {})
    assert out["classification"] == "UNKNOWN" and "error" in out
