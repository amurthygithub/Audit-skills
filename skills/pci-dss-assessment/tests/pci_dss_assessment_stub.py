"""Skill entrypoint stub for pci-dss-assessment.

Deterministic reference executor for the Spine / Tier 0a suite. The seed + oracle
pair is the contract; this stub computes its outputs from the seed facts (no
echoed fixtures — derivability oracles, SOX-637 pattern). The production
LLM-backed executor replaces this later.

House decision conventions implemented here (labeled in the chunks and UC docs;
they are engagement-decision heuristics applying PCI DSS v4.0.1 eligibility
rules, NOT verbatim standard text — PCI is machine-verifiable against the local
licensed copy, but the *routing decision* is the skill's own logic):

  - SAQ selection: service provider -> ROC/SAQ-D-SP; merchant servers touch PAN
    -> full ROC; fully outsourced (redirect/iframe to a compliant TPSP) with no
    merchant script on the page -> SAQ A; merchant controls page scripts but
    servers never receive PAN -> SAQ A-EP; otherwise full ROC. A brand/acquirer
    can mandate ROC regardless (brand-defined; not modeled).
  - Scope: in-scope = CDE + connected/security-impacting; out = segmented-and-
    validated out of scope.
  - Customized approach (Appendix D) requires a Targeted Risk Analysis; a
    compensating control (Appendix B/C) requires the four worksheet elements and
    a legitimate constraint against an existing defined requirement.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

DATA = Path(__file__).resolve().parent.parent / "data"
SEEDS = DATA / "seeds"

WORKSHEET_ELEMENTS = [
    "constraints_documented",
    "objective_of_original_requirement_stated",
    "identified_risk_documented",
    "controls_in_place_described",
]


def _load(name: str) -> Any:
    return json.loads((SEEDS / name).read_text())


def _saq_select(payload: dict) -> dict:
    """SAQ eligibility derived from payment-page architecture (house convention)."""
    ent = payload["entity"]
    pp = payload["payment_page"]
    # A required architecture fact missing -> refuse rather than guess the path.
    required = ("outsourced_to_compliant_third_party", "method",
                "merchant_javascript_on_payment_page", "merchant_servers_touch_pan")
    missing = [k for k in required if k not in pp]
    if missing:
        raise ValueError(f"cannot determine SAQ eligibility: missing payment-page fact(s) "
                         f"{missing} — ask, do not assume an architecture")
    if ent.get("is_service_provider"):
        saq, why = "ROC", "service providers validate via ROC/SAQ-D-SP, not merchant SAQ A/A-EP"
    elif pp["merchant_servers_touch_pan"]:
        saq, why = "ROC", "merchant servers store/process/transmit PAN -> full scope"
    elif (pp["outsourced_to_compliant_third_party"]
          and pp["method"] in ("redirect", "iframe")
          and not pp["merchant_javascript_on_payment_page"]):
        saq, why = "SAQ A", ("fully outsourced payment page (redirect/iframe to compliant "
                             "TPSP); no merchant code touches PAN")
    elif pp["outsourced_to_compliant_third_party"] and not pp["merchant_servers_touch_pan"]:
        saq, why = "SAQ A-EP", ("merchant website controls payment-page elements/scripts (so "
                               "it can affect PAN security) but its servers never receive PAN")
    else:
        saq, why = "ROC", "default to full ROC when no SAQ eligibility is established"
    csr = ["6.4.3", "11.6.1"] if saq in ("SAQ A-EP", "ROC") else []
    return {
        "classification": f"VALIDATION_{saq.replace(' ', '_')}",
        "saq_eligibility": saq,
        "deciding_factor": why,
        "client_side_script_requirements_apply": csr,
        "brand_caveat": "a payment brand or acquirer may mandate a full ROC regardless of SAQ "
                        "eligibility; validation levels are brand-defined, not set by PCI DSS",
    }


def _scope(payload: dict) -> dict:
    """In-scope system count from CDE + connected tags; customized-approach TRA check."""
    inv = payload["system_inventory"]
    cde = [s for s in inv if s["scope_tag"] == "cde"]
    in_scope = [s for s in inv if s["scope_tag"] in ("cde", "connected")]
    ca = payload.get("customized_approach_requests", [])
    accepted = [r["requirement"] for r in ca if r.get("targeted_risk_analysis_present")]
    rejected = [r["requirement"] for r in ca if not r.get("targeted_risk_analysis_present")]
    return {
        "classification": f"ROC_IN_SCOPE_{len(in_scope)}",
        "total_systems": len(inv),
        "cde_systems": len(cde),
        "in_scope_systems": len(in_scope),
        "out_of_scope_systems": len(inv) - len(in_scope),
        "customized_approach_accepted": accepted,
        "customized_approach_rejected_no_tra": rejected,
    }


def _comp_control(payload: dict) -> dict:
    """Compensating-control worksheet completeness + control-type classification."""
    pcc = payload["proposed_compensating_control"]
    constraint = payload["constraint"]
    present = [e for e in WORKSHEET_ELEMENTS if pcc.get(e)]
    missing = [e for e in WORKSHEET_ELEMENTS if not pcc.get(e)]
    # Compensating control: existing defined requirement + legitimate constraint.
    # Customized approach: meet the objective by a different method, no constraint, TRA-driven.
    kind = ("compensating_control"
            if constraint.get("legitimate_business_or_technical_constraint")
            else "customized_approach")
    return {
        "classification": f"COMP_CONTROL_{'COMPLETE' if not missing else 'INCOMPLETE'}",
        "control_type": kind,
        "worksheet_elements_present": len(present),
        "worksheet_complete": not missing,
        "missing_elements": missing,
    }


def run_skill(use_case_id: str, payload: dict, model: str = "stub") -> dict:
    if use_case_id == "UC-01":
        return _saq_select(payload)
    if use_case_id == "UC-02":
        return _scope(payload)
    if use_case_id == "UC-03":
        return _comp_control(payload)
    return {"classification": "UNKNOWN", "error": f"unknown use_case_id: {use_case_id}"}


def normalize_citations(text: str) -> list[tuple[str, str]]:
    """Extract [LABEL §X] citations from SKILL.md body text."""
    return re.findall(r"\[([A-Z][A-Z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-]+)\]", text)
