"""Oracle tests for hipaa-security-rule (derivability pattern, SOX-637).

Every assertion recomputes independently from the seed files and checks the
stub agrees, plus footing invariants. No expected number is echoed from the
stub's own code path.
"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

import yaml

from hipaa_security_rule_stub import BAA_REQUIRED_PROVISIONS, run_skill

SKILL_ROOT = Path(__file__).resolve().parent.parent
SEEDS = SKILL_ROOT / "data" / "seeds"
FACT_SHEET = SKILL_ROOT.parent.parent / "docs" / "hipaa-security-rule-fact-sheet.md"


def _load(name: str):
    return json.loads((SEEDS / name).read_text())


def _fact_sheet_data() -> dict:
    text = FACT_SHEET.read_text()
    m = re.search(r"```yaml\n(.*?)\n```", text, re.DOTALL)
    assert m, "fact sheet §0 yaml block not found"
    return yaml.safe_load(m.group(1))


def _fact_sheet_codes() -> set[str]:
    return {row["code"] for row in _fact_sheet_data()["identifiers"]}


def _uc01_payload() -> dict:
    payload = _load("uc-01-input.json")
    payload["risks"] = _load("uc-01-risks.json")
    payload["addressable_register"] = _load("uc-01-addressable-register.json")
    return payload


def _uc02_payload() -> dict:
    payload = _load("uc-02-input.json")
    payload["control_inventory"] = _load("uc-02-control-inventory.json")
    payload["documentation_register"] = _load("uc-02-documentation-register.json")
    return payload


def _uc03_payload() -> dict:
    payload = _load("uc-03-input.json")
    payload["baa_terms"] = _load("uc-03-baa-terms.json")
    return payload


def test_uc_01_oracle():
    """UC-01: risk rollup and 164.306(d)(3) dispositions derivable from seeds."""
    risks = _load("uc-01-risks.json")
    register = _load("uc-01-addressable-register.json")
    out = run_skill("UC-01", _uc01_payload())

    # Independent recomputation: house bands Low <=2 / Medium 3-4 / High >=6.
    bands: dict[str, int] = {}
    for r in risks:
        s = r["likelihood"] * r["impact"]
        b = "High" if s >= 6 else "Medium" if s >= 3 else "Low"
        bands[b] = bands.get(b, 0) + 1
    assert out["risk_summary"]["by_band"] == bands
    assert out["risk_summary"]["total"] == len(risks)
    assert sum(bands.values()) == len(risks)

    # 164.306(d)(3): one disposition per addressable spec, derived from the
    # documented assessment — recomputed here without the stub's helper.
    expected_disp = {}
    for spec in register:
        if spec["reasonable_and_appropriate"]:
            d = "implement"
        elif spec["alternative"]:
            d = "alternative_measure"
        else:
            d = "not_reasonable_documented"
        expected_disp[spec["spec_id"]] = d
    got = {d["spec_id"]: d["disposition"] for d in out["addressable_dispositions"]}
    assert got == expected_disp
    assert len(got) == 22  # all addressable specs dispositioned, none invented

    # Footing: summary == recount; every documented-out spec carries a justification.
    summary: dict[str, int] = {}
    for d in expected_disp.values():
        summary[d] = summary.get(d, 0) + 1
    assert out["disposition_summary"] == summary
    for row in out["addressable_dispositions"]:
        if row["disposition"] == "alternative_measure":
            assert row["alternative"], row["spec_id"]
        if row["disposition"] == "not_reasonable_documented":
            assert row["justification"], row["spec_id"]

    # Ticket B28: 12 decision-required specs; encryption-at-rest decision derived.
    assert out["decision_required_count"] == sum(1 for s in register if s["decision_required"])
    assert out["encryption_at_rest_disposition"] == expected_disp["164.312(a)(2)(iv)"]

    # Every spec_id exists in the fact-sheet identifier list (no fabricated cites).
    codes = _fact_sheet_codes()
    assert all(s["spec_id"] in codes for s in register)

    # Expected-output seed foots to the same computed values.
    expected = _load("uc-01-expected.json")
    assert expected["risk_summary"]["by_band"] == bands
    assert expected["disposition_summary"] == summary
    assert expected["encryption_at_rest_disposition"] == expected_disp["164.312(a)(2)(iv)"]


def test_uc_02_oracle():
    """UC-02: 22-standard readiness matrix; gap priorities derivable; NPRM excluded."""
    inventory = _load("uc-02-control-inventory.json")
    docs = _load("uc-02-documentation-register.json")
    payload = _uc02_payload()
    out = run_skill("UC-02", payload)

    # The matrix covers exactly the fact sheet's 22 standards — no more, no fewer.
    fs = _fact_sheet_data()
    assert fs["counts"]["subpart_c_standards_total"] == 22
    standard_ids = {r["standard_id"] for r in out["readiness_matrix"]}
    codes = _fact_sheet_codes()
    assert len(out["readiness_matrix"]) == 22
    assert standard_ids <= codes
    assert standard_ids == {r["standard_id"] for r in inventory}

    # Status counts recomputed independently.
    sc: dict[str, int] = {}
    for r in inventory:
        sc[r["status"]] = sc.get(r["status"], 0) + 1
    assert out["readiness_summary"] == {"total": 22, **sc}

    # Stale docs recomputed from seed dates vs as_of_date (no wall clock).
    as_of = date(*map(int, payload["as_of_date"].split("-")))
    cycle = payload["review_cycle_years"] * 365.25
    stale = sorted(d["doc_id"] for d in docs
                   if (as_of - date(*map(int, d["last_reviewed"].split("-")))).days > cycle)
    assert out["stale_docs"] == stale

    # Priority heuristic (house convention): missing->High, partial->Medium, stale->Low.
    assert out["gap_priorities"] == {
        "High": sc.get("missing", 0), "Medium": sc.get("partial", 0), "Low": len(stale),
    }
    assert len(out["gap_register"]) == sum(out["gap_priorities"].values())

    # NPRM content never enters the current-law gap register.
    assert out["nprm_items_in_current_law_gaps"] == 0
    assert not any("NPRM" in g["basis"].upper() for g in out["gap_register"])

    # Expected-output seed foots.
    expected = _load("uc-02-expected.json")
    assert expected["readiness"] == {"total": 22, **sc}
    assert expected["stale_docs"] == stale


def test_uc_03_oracle():
    """UC-03: BAA completeness vs 164.314(a)(2)(i) + 164.308(b)(3); right-sized checklist."""
    baa = _load("uc-03-baa-terms.json")
    out = run_skill("UC-03", _uc03_payload())

    # Required-provision set is the regulatory list, stated once in the stub.
    assert set(BAA_REQUIRED_PROVISIONS) == {
        "comply_with_subpart", "subcontractor_flowdown", "incident_reporting", "written_contract",
    }
    present = {c["provision"] for c in baa["proposed_clauses"]}
    missing = sorted(p for p in BAA_REQUIRED_PROVISIONS if p not in present)
    assert out["baa_check"]["missing_provisions"] == missing
    assert missing  # the fixture seeds omissions; a fully-clean BAA is the adversarial case

    # Checklist: every cite exists in the fact sheet; scaled items carry rationale.
    codes = _fact_sheet_codes()
    for item in out["safeguard_checklist"]:
        assert item["cfr_cite"] in codes, item["cfr_cite"]
        if item["scaled_down"]:
            assert item.get("scaling_rationale"), item["cfr_cite"]
    assert out["checklist_summary"]["items"] == len(out["safeguard_checklist"])
    assert out["checklist_summary"]["scaled_down"] == sum(
        1 for i in out["safeguard_checklist"] if i["scaled_down"])

    # Expected-output seed foots.
    expected = _load("uc-03-expected.json")
    assert expected["missing_provisions"] == missing
    assert expected["checklist_items"] == out["checklist_summary"]["items"]
    assert expected["scaled_down_items"] == out["checklist_summary"]["scaled_down"]


def test_fact_sheet_inventory_diff():
    """The seed tables (generators) must match the fact sheet §0 exactly —
    the standing inventory-diff gate (process v3 rule 3)."""
    fs = _fact_sheet_data()
    register = _load("uc-01-addressable-register.json")
    inventory = _load("uc-02-control-inventory.json")
    codes = _fact_sheet_codes()

    # 22 addressable specs: every register row is an Addressable identifier in the sheet.
    addressable_in_sheet = {
        row["code"] for row in fs["identifiers"] if "(Addressable)" in row["name"]
    }
    assert {r["spec_id"] for r in register} == addressable_in_sheet
    assert len(register) == 22

    # 22 standards: every inventory row is a Standard identifier in the sheet.
    standards_in_sheet = {
        row["code"] for row in fs["identifiers"] if "(Standard" in row["name"]
    }
    assert {r["standard_id"] for r in inventory} == standards_in_sheet
    assert len(inventory) == fs["counts"]["subpart_c_standards_total"] == 22

    # Family R/A counts in the sheet foot to the family totals.
    c = fs["counts"]
    assert c["admin_impl_specs_required"] + c["admin_impl_specs_addressable"] == c["admin_impl_specs"] == 21
    assert c["physical_impl_specs_required"] + c["physical_impl_specs_addressable"] == c["physical_impl_specs"] == 8
    assert c["technical_impl_specs_required"] + c["technical_impl_specs_addressable"] == c["technical_impl_specs"] == 7
    assert c["matrix_titled_impl_specs"] == 36 and c["matrix_standards"] == 18
    assert codes  # sanity
