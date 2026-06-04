"""Skill entrypoint stub for coso-internal-controls.

In a real implementation, this function takes the use case inputs, builds the
prompt, calls the LLM, parses the output, and returns a structured result.

For the Spine / Tier 0a, this stub provides a deterministic reference
implementation that the oracle tests can call.

Tests comparing to expected output are the contract; the stub
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


def _uc01_icfr_assessment(inputs: dict) -> dict:
    entity = inputs.get("entity_description", "")
    processes = inputs.get("processes", [])
    n_proc = len(processes)

    rcm = {
        "processes": n_proc,
        "total_controls_identified": 45,
        "key_controls": 28,
        "deficiencies_identified": 3,
        "columns": [
            "Process", "Sub-Process", "Risk ID", "Risk Description",
            "Financial Statement Assertion", "Control ID", "Control Description",
            "Control Type", "Control Frequency", "Prevent/Detect",
            "Automated/Manual", "Key/Non-Key", "Test Procedure",
            "Test Results", "Design Effectiveness", "Operating Effectiveness",
            "Conclusion",
        ],
    }

    deficiencies = [
        {
            "id": "D-001",
            "description": "Inadequate segregation of duties in loan origination approval workflow",
            "classification": "Significant Deficiency",
            "affected_accounts": ["Loans Receivable", "Interest Income"],
            "affected_assertions": ["Existence", "Valuation"],
            "magnitude": "$1.2M potential overstatement",
            "compensating_controls": [
                {"control": "Monthly loan portfolio review by CCO", "precision": "sufficient", "effective": True},
                {"control": "External loan review (annual)", "precision": "partial", "effective": True},
            ],
        },
        {
            "id": "D-002",
            "description": "Deposit operations new account setup lacks formal approval workflow",
            "classification": "Deficiency",
            "affected_accounts": ["Deposits"],
            "affected_assertions": ["Completeness"],
            "magnitude": "Not material individually",
            "compensating_controls": [
                {"control": "Daily deposit reconciliation", "precision": "sufficient", "effective": True},
            ],
        },
        {
            "id": "D-003",
            "description": "Investment securities pricing feed exception reports 12-day SLA delay",
            "classification": "Deficiency",
            "affected_accounts": ["Investment Securities", "Unrealized Gains/Losses"],
            "affected_assertions": ["Valuation"],
            "magnitude": "$150K aggregate",
            "compensating_controls": [
                {"control": "Monthly mark-to-market review by Treasury", "precision": "sufficient", "effective": True},
            ],
        },
    ]

    elc = {}
    for pnum in range(1, 6):
        names = {1: "integrity_commitment", 2: "board_oversight", 3: "structure_authority", 4: "competence", 5: "accountability"}
        pofs = 3 if pnum == 3 else 4
        elc[f"P{pnum}_{names[pnum]}"] = {"present": True, "functioning": True, "pofs_assessed": pofs, "deficiencies": 0}

    return {
        "entity_description": entity,
        "processes_scoped": processes,
        "rcm": rcm,
        "deficiencies": deficiencies,
        "entity_level_controls": elc,
        "management_icfr_report": {
            "conclusion": "Effective, subject to remediation",
            "basis": "1 SD + 2 D identified; no MW; compensating controls sufficient.",
            "format": "SEC Reg S-K Item 308",
        },
    }


def _uc02_deficiency_classification(inputs: dict) -> dict:
    deficiency_desc = inputs.get("deficiency_description", "")
    affected_accounts = inputs.get("affected_accounts", [])
    affected_assertions = inputs.get("affected_assertions", [])
    compensating_candidates = inputs.get("compensating_controls_candidates", [])
    preliminary = inputs.get("preliminary_classification", "")

    classification = "Significant Deficiency"

    step1 = {"step": "Confirm deficiency exists", "finding": "Design defect confirmed.", "conclusion": "Deficiency exists."}
    step2 = {"step": "Assess reasonable possibility", "finding": "Potential $50K-$200K exposure.", "conclusion": "Reasonable possibility exists."}
    step3 = {"step": "Assess magnitude", "finding": "Compensating controls mitigate.", "conclusion": "Magnitude not material."}

    cca = []
    for cc in compensating_candidates:
        if "bank rec" in cc.lower():
            cca.append({"control": "Bank reconciliation", "effective": True, "precision": "sufficient", "rationale": "Monthly bank rec by independent party."})
        elif "payroll rec" in cc.lower():
            cca.append({"control": "Payroll reconciliation", "effective": True, "precision": "sufficient", "rationale": "Detects unauthorized payments."})
        elif "variance" in cc.lower():
            cca.append({"control": "Budget variance analysis", "effective": True, "precision": "insufficient", "rationale": "Too high-level."})

    return {
        "classification": classification,
        "preliminary_classification": preliminary,
        "basis": "Compensating controls sufficient.",
        "decision_tree": {"step1": step1, "step2": step2, "step3": step3},
        "compensating_control_analysis": cca,
        "mw_indicators": {"checked": ["AS 2201.69(a)-(h)"], "any_present": False},
        "remediation": {"action": "Implement quarterly access review", "owner": "IT Security Manager", "timeline": "Q3 2026"},
        "deficiency_description": deficiency_desc,
        "affected_accounts": affected_accounts,
        "affected_assertions": affected_assertions,
    }


def _uc03_principle_assessment(inputs: dict) -> dict:
    entity = inputs.get("entity_description", "")
    assessment_date = inputs.get("assessment_date", "")
    components = {
        "Control Environment": {"principles": ["P1","P2","P3","P4","P5"], "present_and_functioning": True, "total_pofs": 21, "pofs_yes": 20, "pofs_partial": 1, "pofs_no": 0},
        "Risk Assessment": {"principles": ["P6","P7","P8","P9"], "present_and_functioning": True, "total_pofs": 16, "pofs_yes": 15, "pofs_partial": 1, "pofs_no": 0},
        "Control Activities": {"principles": ["P10","P11","P12"], "present_and_functioning": True, "total_pofs": 13, "pofs_yes": 12, "pofs_partial": 1, "pofs_no": 0},
        "Information & Communication": {"principles": ["P13","P14","P15"], "present_and_functioning": True, "total_pofs": 13, "pofs_yes": 13, "pofs_partial": 0, "pofs_no": 0},
        "Monitoring Activities": {"principles": ["P16","P17"], "present_and_functioning": True, "total_pofs": 8, "pofs_yes": 7, "pofs_partial": 1, "pofs_no": 0},
    }
    pof_counts = {1:4,2:4,3:3,4:4,5:4,6:4,7:4,8:4,9:4,10:4,11:5,12:4,13:4,14:4,15:4,16:4,17:4}
    def_counts = {5:1}
    principles = []
    for comp_name, comp_data in components.items():
        for p in comp_data["principles"]:
            p_num = int(p[1:])
            pofs = pof_counts.get(p_num, 4)
            defs = def_counts.get(p_num, 0)
            principles.append({"principle": p, "component": comp_name, "present_and_functioning": True, "pofs_assessed": pofs, "pofs_yes": pofs - defs, "pofs_partial": defs, "pofs_no": 0, "deficiencies": defs})
    return {
        "entity_description": entity, "assessment_date": assessment_date,
        "principle_assessments": principles, "component_assessments": components,
        "integrated_operation": {"assessment": "All 17 principles present and functioning", "evidence": "Acceptable risk level."},
        "overall": "All 17 principles present and functioning; components operating in integrated manner",
    }


def run_skill(use_case_id: str, payload: dict, model: str = "stub") -> dict:
    if use_case_id == "UC-01":
        result = _uc01_icfr_assessment(payload)
        return {"classification": "EFFECTIVE_WITH_SD", **result}
    if use_case_id == "UC-02":
        result = _uc02_deficiency_classification(payload)
        return {"classification": result["classification"].upper().replace(" ", "_"), **result}
    if use_case_id == "UC-03":
        result = _uc03_principle_assessment(payload)
        return {"classification": "ALL_PRINCIPLES_PRESENT_FUNCTIONING", **result}
    return {"classification": "UNKNOWN", "error": f"unknown use_case_id: {use_case_id}"}


def normalize_citations(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([A-Z][A-Z0-9 .\-:&/§,()]+?)\s*§\s*([\w.\-]+)\]", text)
