"""Oracle tests for pci-dss-assessment (derivability pattern, SOX-637).

Every assertion recomputes independently from the seed facts and checks the stub
agrees, plus a standing fact-sheet inventory-diff (process v3 rule 3).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from pci_dss_assessment_stub import WORKSHEET_ELEMENTS, run_skill

SKILL_ROOT = Path(__file__).resolve().parent.parent
SEEDS = SKILL_ROOT / "data" / "seeds"
FACT_SHEET = SKILL_ROOT.parent.parent / "docs" / "pci-dss-assessment-fact-sheet.md"


def _load(name: str):
    return json.loads((SEEDS / name).read_text())


def _fact_sheet_data() -> dict:
    m = re.search(r"```yaml\n(.*?)\n```", FACT_SHEET.read_text(), re.DOTALL)
    assert m, "fact sheet §0 yaml block not found"
    return yaml.safe_load(m.group(1))


def test_uc_01_oracle():
    """UC-01: SAQ eligibility derived from payment-page architecture (B19 -> A-EP)."""
    payload = _load("uc-01-input.json")
    out = run_skill("UC-01", payload)
    pp, ent = payload["payment_page"], payload["entity"]

    # Independent recompute of the decision
    if ent.get("is_service_provider"):
        saq = "ROC"
    elif pp["merchant_servers_touch_pan"]:
        saq = "ROC"
    elif (pp["outsourced_to_compliant_third_party"] and pp["method"] in ("redirect", "iframe")
          and not pp["merchant_javascript_on_payment_page"]):
        saq = "SAQ A"
    elif pp["outsourced_to_compliant_third_party"] and not pp["merchant_servers_touch_pan"]:
        saq = "SAQ A-EP"
    else:
        saq = "ROC"
    assert out["saq_eligibility"] == saq == "SAQ A-EP"  # the B19 scenario
    # Client-side script requirements apply on A-EP / ROC, not pure SAQ A
    assert out["client_side_script_requirements_apply"] == (
        ["6.4.3", "11.6.1"] if saq in ("SAQ A-EP", "ROC") else [])
    assert out["classification"] == f"VALIDATION_{saq.replace(' ', '_')}"
    assert "brand" in out["brand_caveat"].lower()

    expected = _load("uc-01-expected.json")
    assert expected["saq_eligibility"] == saq
    assert expected["client_side_script_requirements_apply"] == out["client_side_script_requirements_apply"]


def test_uc_02_oracle():
    """UC-02: in-scope count from CDE+connected tags; customized approach needs a TRA."""
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)
    inv = payload["system_inventory"]

    cde = sum(1 for s in inv if s["scope_tag"] == "cde")
    in_scope = sum(1 for s in inv if s["scope_tag"] in ("cde", "connected"))
    assert out["total_systems"] == len(inv)
    assert out["cde_systems"] == cde
    assert out["in_scope_systems"] == in_scope
    assert out["out_of_scope_systems"] == len(inv) - in_scope
    # footing: in + out == total
    assert out["in_scope_systems"] + out["out_of_scope_systems"] == out["total_systems"]
    assert out["classification"] == f"ROC_IN_SCOPE_{in_scope}"

    ca = payload["customized_approach_requests"]
    assert out["customized_approach_accepted"] == [r["requirement"] for r in ca
                                                   if r["targeted_risk_analysis_present"]]
    assert out["customized_approach_rejected_no_tra"] == [r["requirement"] for r in ca
                                                          if not r["targeted_risk_analysis_present"]]

    expected = _load("uc-02-expected.json")
    assert expected["in_scope_systems"] == in_scope and expected["cde_systems"] == cde


def test_uc_03_oracle():
    """UC-03: compensating-control worksheet completeness + control-type classification."""
    payload = _load("uc-03-input.json")
    out = run_skill("UC-03", payload)
    pcc = payload["proposed_compensating_control"]

    present = sum(1 for e in WORKSHEET_ELEMENTS if pcc.get(e))
    missing = [e for e in WORKSHEET_ELEMENTS if not pcc.get(e)]
    assert out["worksheet_elements_present"] == present
    assert out["missing_elements"] == missing
    assert out["worksheet_complete"] == (not missing)
    # constraint-driven against an existing requirement -> compensating control (not customized)
    kind = ("compensating_control"
            if payload["constraint"]["legitimate_business_or_technical_constraint"]
            else "customized_approach")
    assert out["control_type"] == kind == "compensating_control"
    assert len(WORKSHEET_ELEMENTS) == 4  # Appendix C: exactly four elements
    assert out["classification"] == f"COMP_CONTROL_{'COMPLETE' if not missing else 'INCOMPLETE'}"

    expected = _load("uc-03-expected.json")
    assert expected["worksheet_complete"] == out["worksheet_complete"]
    assert expected["control_type"] == out["control_type"]


def test_fact_sheet_inventory_diff():
    """The skill's stated counts must match the fact sheet §0 — standing inventory-diff gate."""
    fs = _fact_sheet_data()
    c = fs["counts"]
    # Footing invariants on the inventory itself
    assert c["goals"] == 6
    assert c["principal_requirements"] == 12
    assert c["defined_requirements_depth3"] + c["defined_requirements_depth4"] == \
        c["defined_requirements_main_body"] == 249
    assert c["saq_types"] == 10
    # Every principal requirement identifier present and well-formed
    reqs = [r for r in fs["identifiers"] if r["code"].startswith("Req ")]
    assert len(reqs) == 12
    nums = sorted(int(r["code"].split()[1]) for r in reqs)
    assert nums == list(range(1, 13))
    # All 10 SAQ types present in the identifier list
    saqs = [r for r in fs["identifiers"] if r["code"].startswith("SAQ ")]
    assert len(saqs) == 10
