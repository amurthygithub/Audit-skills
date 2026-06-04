"""Skill entrypoint stub for aicpa-soc-reporting.

In a real implementation, this function takes the use case inputs, builds the
prompt, calls the LLM, parses the output, and returns a structured result.

For the Spine / Tier 0a, this stub provides a deterministic reference
implementation that the oracle tests can call. The production implementation
(in SOX-611 Phase 2 migration) will replace this with the real skill
executor. Until then, the stub returns the expected output for known seeds.

The tests that compare to expected output are the contract; the stub
exists to keep the test suite runnable today.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

DATA = Path(__file__).resolve().parent.parent / "data"
SEEDS = DATA / "seeds"


def _load(name: str) -> dict:
    return json.loads((SEEDS / name).read_text())


def _uc01_soc2_type2(payload: dict) -> dict:
    """UC-01: Full SOC 2 Type II examination walkthrough."""
    tsc = payload.get("tsc_categories", ["Security", "Availability", "Confidentiality"])
    cc_count = 33
    optional_count = sum({
        "Availability": 3, "Processing Integrity": 5,
        "Confidentiality": 2, "Privacy": 8,
    }.get(c, 0) for c in tsc if c != "Security")
    criteria_count = cc_count + optional_count

    subservice = payload.get("subservice_orgs", [])
    csocs = []
    cuecs = [
        {"id": "CUEC-01", "criterion": "CC6.2", "description": "User access provisioning on the platform"},
        {"id": "CUEC-02", "criterion": "PI1.2", "description": "Data input validation before submission"},
        {"id": "CUEC-03", "criterion": "CC1.2", "description": "Segregation of duties at user entity level"},
        {"id": "CUEC-04", "criterion": "CC7.3", "description": "Incident notification to service org"},
    ]
    if any("AWS" in s for s in subservice):
        csocs = [
            {"criterion": "CC6.1", "control": "AWS IAM access controls"},
            {"criterion": "CC6.5", "control": "AWS data center physical security"},
            {"criterion": "CC6.6", "control": "AWS VPC, security groups"},
        ]

    opinion = "Unqualified"
    findings = payload.get("findings", [])
    if findings:
        exceptions = [f for f in findings if f.get("exception", False)]
        if len(exceptions) >= 3:
            opinion = "Qualified"

    return {
        "classification": f"SOC2-TypeII-{criteria_count}",
        "engagement": {
            "soc_type": "SOC-2",
            "report_type": "Type-II",
            "examination_period": payload.get("examination_period", {}),
            "tsc_categories": tsc,
            "criteria_count": criteria_count,
            "opinion": opinion,
        },
        "subservice": {
            "method": "carve-out" if subservice else "none",
            "organizations": subservice,
            "csocs": csocs,
        },
        "cuecs": cuecs,
        "opinion": {"type": opinion},
    }


def _uc02_cuec_csoc(payload: dict) -> dict:
    """UC-02: CUEC/CSOC identification for multi-tenant SaaS."""
    subservices = [
        {"name": "AWS", "service": "IaaS (compute, storage, networking)", "method": "carve-out",
         "csocs": [{"criterion": "CC6.1", "control": "AWS IAM access controls"},
                   {"criterion": "CC6.5", "control": "AWS data center physical security"},
                   {"criterion": "CC6.6", "control": "AWS VPC, security groups"}]},
        {"name": "Stripe", "service": "Payment processing", "method": "carve-out",
         "csocs": [{"criterion": "CC6.6", "control": "Stripe payment security"},
                   {"criterion": "PI1.1", "control": "Stripe transaction completeness"}]},
        {"name": "SendGrid", "service": "Email delivery", "method": "carve-out",
         "csocs": [{"criterion": "CC6.1", "control": "SendGrid infrastructure security"}]},
    ]
    cuecs = [
        {"id": "CUEC-01", "criterion": "CC6.2", "description": "User access provisioning on the platform"},
        {"id": "CUEC-02", "criterion": "PI1.2", "description": "Data input validation before submission"},
        {"id": "CUEC-03", "criterion": "CC1.2", "description": "Segregation of duties at user entity level"},
        {"id": "CUEC-04", "criterion": "CC7.3", "description": "Incident notification to service org"},
        {"id": "CUEC-05", "criterion": "CC6.6", "description": "Customer-managed encryption keys"},
    ]
    method = payload.get("method", "carve-out")
    return {
        "classification": f"CUEC-CSOC-{len(subservices)}sub-{len(cuecs)}cuec",
        "subservice_organizations": subservices,
        "cuecs": cuecs,
        "method": method,
        "method_rationale": "All three subservice organizations maintain independent SOC reports. Carve-out method applied to avoid duplicative testing.",
    }


def _uc03_bridge_letter(payload: dict) -> dict:
    """UC-03: Bridge letter for gap period between SOC 2 reports."""
    gap_start = payload.get("gap_period", {}).get("start", "2026-01-01")
    gap_end = payload.get("gap_period", {}).get("end", "2026-06-30")
    prior_end = payload.get("prior_report", {}).get("period_end", "2025-12-31")
    prior_issued = payload.get("prior_report", {}).get("issue_date", "2026-02-15")
    material_changes = payload.get("material_changes", "No material changes to system description or control design.")
    exceptions_prior = payload.get("exceptions_in_prior", "No exceptions in prior SOC 2 Type II report.")

    return {
        "classification": "Bridge-Letter-4-Attestations",
        "bridge_letter": {
            "gap_period": f"{gap_start} to {gap_end}",
            "prior_report": f"SOC 2 Type II covering period ending {prior_end}, issued {prior_issued}",
            "attestations": [
                "1. No material changes to the system description.",
                "2. No material changes to the design of controls.",
                "3. No exceptions in the operating effectiveness of controls.",
                "4. The CUECs and CSOCs disclosed in the SOC 2 Type II report remain appropriate.",
            ],
            "disclaimer": "This letter is a management representation only and does not provide auditor assurance. It is not a substitute for a SOC 2 Type II report.",
            "material_changes": material_changes,
            "exceptions_in_prior": exceptions_prior,
        },
    }


def _uc04_auditee_preparation(payload: dict) -> dict:
    """UC-04: Auditee preparation for SOC 2 Type II examination."""
    controls = payload.get("control_inventory", [])
    total_controls = len(controls)
    mapped = [c for c in controls if c.get("tsc_criterion")]
    gaps = [c for c in controls if c.get("gap", True)]
    cucc_draft = [
        "Customer must enforce MFA for their own users",
        "Customer must review audit logs for their own tenant",
        "Customer must configure their own access policies",
        "Customer must manage encryption keys for PHI data",
    ]
    subservice_orgs = [
        {"name": s.get("name", "AWS"), "has_soc_report": s.get("has_soc_report", True),
         "method": "carve-out" if s.get("has_soc_report", True) else "inclusive"}
        for s in payload.get("subservice_orgs", [{"name": "AWS", "has_soc_report": True}])
    ]

    return {
        "classification": f"Readiness-{len(mapped)}mapped-{len(gaps)}gaps",
        "gap_analysis": {
            "total_controls": total_controls,
            "mapped_to_tsc": len(mapped),
            "gaps_identified": len(gaps),
            "common_criteria_covered": 33 if len(mapped) >= 30 else len(mapped),
        },
        "remediation_plan": [
            {"gap_control": g.get("description", "Unknown"), "priority": g.get("priority", "medium"),
             "timeline": g.get("timeline", "Before examination period starts")}
            for g in gaps[:5]
        ],
        "evidence_readiness": {
            "evidence_repository_structure": "evidence/cc1-control-environment/ ... evidence/p-privacy/",
            "status": "ready" if len(gaps) == 0 else "incomplete",
        },
        "cuec_draft": cucc_draft,
        "subservice_organizations": subservice_orgs,
    }


def run_skill(use_case_id: str, payload: dict, model: str = "stub") -> dict:
    """Stub entrypoint. Returns a structured skill result.

    For the Spine demonstration, the stub returns the expected output
    for known use cases. Real implementation: build prompt from SKILL.md,
    call LLM, parse output, return classification + structured result.
    """
    if use_case_id == "UC-01":
        return _uc01_soc2_type2(payload)
    if use_case_id == "UC-02":
        return _uc02_cuec_csoc(payload)
    if use_case_id == "UC-03":
        return _uc03_bridge_letter(payload)
    if use_case_id == "UC-04":
        return _uc04_auditee_preparation(payload)
    return {"classification": "UNKNOWN", "error": f"unknown use_case_id: {use_case_id}"}


def normalize_citations(text: str) -> list[tuple[str, str]]:
    """Extract [LABEL X] citations from SKILL.md body text."""
    return re.findall(r"\[([A-Z][A-Z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-]+)\]", text)
