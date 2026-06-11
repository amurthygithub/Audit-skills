"""Oracle tests for fedramp-authorization (derivability, SOX-637).

Each test recomputes the expected output INDEPENDENTLY from the seed facts and
checks the stub agrees — nothing is echoed. The inventory-diff test pins the
baseline counts the chunks state to the fact sheet §0 (the single source of truth,
itself counted from the PMO-authored OSCAL Rev 5 profiles).
"""

from __future__ import annotations

import json
import re
from datetime import date, timedelta
from pathlib import Path

import yaml

from fedramp_authorization_stub import run_skill

ROOT = Path(__file__).resolve().parent.parent
SEEDS = ROOT / "data" / "seeds"
FACT_SHEET = ROOT.parent.parent / "docs" / "fedramp-authorization-fact-sheet.md"

_ORDER = {"Low": 1, "Moderate": 2, "High": 3}
_SLA = {"Critical": 30, "High": 30, "Moderate": 90, "Low": 180}


def _load(name: str):
    return json.loads((SEEDS / name).read_text())


def _fact_sheet():
    m = re.search(r"```yaml\n(.*?)\n```", FACT_SHEET.read_text(), re.DOTALL)
    return yaml.safe_load(m.group(1))


def test_uc_01_oracle():
    """High-water-mark categorization -> baseline selection -> POA&M SLA dates, all derived."""
    payload = _load("uc-01-input.json")
    out = run_skill("UC-01", payload)
    fips = payload["fips199"]
    # Independent recomputation of the overall impact (the high-water mark).
    expect_impact = {v: k for k, v in _ORDER.items()}[max(_ORDER[v] for v in fips.values())]
    assert out["overall_impact"] == expect_impact == "Moderate"
    assert out["baseline"] == "Moderate"
    assert out["baseline_controls"] == 323  # follows from impact, not hardcoded to one value
    assert out["classification"] == "FEDRAMP_MODERATE"
    # Each POA&M deadline = identified_date + the severity SLA, recomputed here.
    for f, item in zip(payload["sar_findings"], out["poam"]):
        d = date.fromisoformat(f["identified_date"])
        assert item["remediation_due"] == (d + timedelta(days=_SLA[f["severity"]])).isoformat()
    assert out["poam_open"] == len(payload["sar_findings"]) == 5
    expected = _load("uc-01-expected.json")
    assert expected["baseline_controls"] == out["baseline_controls"]
    assert [p["remediation_due"] for p in expected["poam"]] == [p["remediation_due"] for p in out["poam"]]


def test_uc_02_oracle():
    """LI-SaaS eligibility derived (Low AND SaaS); the 156 = 66 tested + 90 attested split."""
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)
    fips = payload["fips199"]
    expect_impact = {v: k for k, v in _ORDER.items()}[max(_ORDER[v] for v in fips.values())]
    expect_eligible = expect_impact == "Low" and bool(payload["saas_delivery"])
    assert out["overall_impact"] == expect_impact == "Low"
    assert out["li_saas_eligible"] is expect_eligible is True
    assert out["baseline"] == "LI-SaaS"
    assert out["baseline_controls"] == 156
    assert out["controls_3pao_tested"] + out["controls_attested"] == out["baseline_controls"]
    assert out["controls_3pao_tested"] == 66 and out["controls_attested"] == 90
    assert out["classification"] == "LI_SAAS_ELIGIBLE"
    expected = _load("uc-02-expected.json")
    assert expected["li_saas_eligible"] == out["li_saas_eligible"]


def test_uc_03_oracle():
    """3PAO finding roll-up: findings = CSP-owned failed controls; inherited excluded; counts foot."""
    payload = _load("uc-03-input.json")
    out = run_skill("UC-03", payload)
    controls = payload["controls"]
    expect_findings = [c["id"] for c in controls
                       if c["tested"] and not c["passed"] and not c["inherited"]]
    assert out["findings"] == expect_findings == ["AC-2", "SI-2", "AU-6", "CM-6"]
    assert out["poam_item_count"] == len(expect_findings) == 4
    assert out["inherited_count"] == sum(1 for c in controls if c["inherited"]) == 2
    # A failed-but-inherited control (SC-7, High) is NOT in the CSP's POA&M.
    assert "SC-7" not in out["findings"]
    assert out["findings_by_severity"] == {"High": 2, "Moderate": 1, "Low": 1}
    assert out["has_high_severity_finding"] is True
    assert out["controls_total"] == len(controls)
    expected = _load("uc-03-expected.json")
    assert expected["findings"] == out["findings"]
    assert expected["findings_by_severity"] == out["findings_by_severity"]


def test_fact_sheet_inventory_diff():
    """Baseline counts the chunks state must match the fact sheet §0 (OSCAL-verified)."""
    c = _fact_sheet()["counts"]
    assert c["baseline_low"] == 156
    assert c["baseline_moderate"] == 323
    assert c["baseline_high"] == 410
    assert c["baseline_li_saas"] == 156
    assert c["li_saas_3pao_tested"] + c["li_saas_attested"] == 156
    assert c["nist_800_53b_low"] == 149
    assert c["nist_800_53b_moderate"] == 287
    assert c["nist_800_53b_high"] == 370
    # The stub's framework constants must equal the fact sheet's.
    from fedramp_authorization_stub import BASELINE_CONTROLS, LI_SAAS_CONTROLS
    assert BASELINE_CONTROLS["Low"] == c["baseline_low"]
    assert BASELINE_CONTROLS["Moderate"] == c["baseline_moderate"]
    assert BASELINE_CONTROLS["High"] == c["baseline_high"]
    assert LI_SAAS_CONTROLS == c["baseline_li_saas"]


def test_fact_sheet_identifiers_present():
    """The governance + baseline + package identifiers must be in the fact sheet §0."""
    ids = {r["code"] for r in _fact_sheet()["identifiers"]}
    for must in ("FedRAMP Authorization Act 2022", "44 U.S.C. 3610", "OMB M-24-15",
                 "FedRAMP Moderate", "SSP", "SAP", "SAR", "POA&M", "3PAO", "FIPS 199"):
        assert must in ids, f"{must} missing from fact sheet identifiers"
