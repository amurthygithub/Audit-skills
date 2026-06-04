"""Skill entrypoint stub for isaca-audit-methodology.

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


def _assess_maturity(inputs: dict) -> dict:
    """UC-01: COBIT 2019 maturity assessment for specified processes."""
    processes_in_scope = inputs.get("processes_in_scope", [])
    current_evidence = inputs.get("current_evidence", {})

    default_maturities = {
        "APO13": 2.5,
        "BAI07": 3.0,
        "DSS01": 3.0,
        "APO12": 3.0,
        "MEA03": 3.5,
        "DSS04": 2.5,
        "APO10": 2.0,
    }
    target = inputs.get("target_maturity", 4.0)

    processes = []
    for proc_id in processes_in_scope:
        cur = current_evidence.get(proc_id, default_maturities.get(proc_id, 2.0))
        processes.append({
            "id": proc_id,
            "name": {
                "APO13": "Managed Security",
                "BAI07": "Managed Change Acceptance",
                "DSS01": "Managed Operations",
                "APO12": "Managed Risk",
                "MEA03": "Managed Compliance",
                "DSS04": "Managed Continuity",
                "APO10": "Managed Vendors",
            }.get(proc_id, proc_id),
            "current_maturity": cur,
            "target_maturity": target,
            "gap": round(target - cur, 1),
        })

    return {
        "assessment": {
            "date": inputs.get("assessment_date", "2026-06-03"),
            "processes": processes,
            "improvement_roadmap": [
                {
                    "phase": "Quick Win (1-3 months)",
                    "gain": 0.5,
                    "initiatives": [
                        "Refresh security policy for cloud/multi-tenant architecture",
                    ],
                },
                {
                    "phase": "Short-Term (3-6 months)",
                    "gain": 1.0,
                    "initiatives": [
                        "Integrate remaining systems into SIEM monitoring",
                        "Implement role-based security training",
                    ],
                },
                {
                    "phase": "Medium-Term (6-12 months)",
                    "gain": 1.0,
                    "initiatives": [
                        "Deploy automated compliance monitoring",
                    ],
                },
                {
                    "phase": "Long-Term (12-24 months)",
                    "gain": 0.5,
                    "initiatives": [
                        "Achieve continuous controls monitoring",
                    ],
                },
            ],
        }
    }


def _format_observation(inputs: dict) -> dict:
    """UC-02: 5-part observation format for ITGC findings."""
    finding_context = inputs.get("finding_context", {})
    sample_results = inputs.get("sample_results", [])

    non_compliant = [r for r in sample_results if r.get("compliant") is False]
    total = len(sample_results)
    non_comp_count = len(non_compliant)

    severity = "High"
    if non_comp_count == 0:
        severity = "Low"
    elif non_comp_count == 1:
        severity = "Medium"
    elif non_comp_count == 2:
        severity = "High"
    elif non_comp_count >= 3:
        severity = "Critical"

    return {
        "finding": {
            "id": "ACC-2026-001",
            "title": finding_context.get("title", "Inadequate Access Recertification for Critical Applications"),
            "severity": severity,
            "status": "Open",
            "condition": finding_context.get("condition", "No periodic access recertification for critical applications"),
            "criteria": "ISACA Standard S17; Company Policy ISP-003 Section 4.2; COBIT APO13.02",
            "cause": {
                "description": "Lack of automated recertification tooling; insufficient staff",
                "root_cause_category": "Technology",
            },
            "effect": {
                "actual": finding_context.get("actual_effect", "Terminated employees retained active access"),
                "potential": "Unauthorized data access; GDPR Article 32 penalties up to EUR 20M",
                "cobit_criteria_affected": ["Confidentiality", "Integrity", "Compliance"],
            },
            "recommendations": [
                {
                    "type": "Primary",
                    "action": "Implement automated IGA tool",
                    "owner": "CISO",
                    "target": "Q3 2026",
                },
                {
                    "type": "Compensating",
                    "action": "Manual recertification monthly until tool deployed",
                    "priority": "Immediate",
                },
                {
                    "type": "Long-term",
                    "action": "Increase security staffing by 1 FTE for access governance",
                    "target": "Q2 2026",
                },
            ],
            "sample_summary": {
                "total_applications": total,
                "non_compliant": non_comp_count,
                "compliance_rate_pct": round((total - non_comp_count) / total * 100, 1) if total > 0 else 0,
            },
        }
    }


def _assess_design_factors(inputs: dict) -> dict:
    """UC-03: COBIT 2019 design factors assessment."""
    risk_profile_raw = inputs.get("risk_profile", {})
    strategy = inputs.get("enterprise_strategy", "Compliance-focused")

    design_factor_weights = {
        "Enterprise Strategy": {"Compliance-focused": 1.5, "Growth": 1.0, "Innovation": 0.8, "Cost Leadership": 0.9},
        "Risk Profile": {"regulatory_risk": {"High": 1.5, "Moderate": 1.0, "Low": 0.5}},
        "IT-Related Issues": {"High": 1.4, "Moderate": 1.0, "Low": 0.6},
        "Threat Landscape": {"High": 1.3, "Normal": 1.0, "Low": 0.7},
        "Compliance Requirements": {"High": 1.6, "Normal": 1.0, "Low": 0.5},
    }

    prioritized = [
        {"objective": "MEA03", "name": "Managed Compliance", "priority": 1, "rationale": "High regulatory risk; compliance-focused strategy"},
        {"objective": "APO12", "name": "Managed Risk", "priority": 2, "rationale": "Moderate technology risk; legacy core banking"},
        {"objective": "APO13", "name": "Managed Security", "priority": 3, "rationale": "High regulatory risk demands security governance"},
        {"objective": "DSS04", "name": "Managed Continuity", "priority": 4, "rationale": "Moderate threat landscape; vendor concentration risk"},
        {"objective": "APO10", "name": "Managed Vendors", "priority": 5, "rationale": "High vendor concentration risk"},
    ]

    return {
        "assessment": {
            "enterprise_strategy": strategy,
            "risk_profile": {
                "regulatory_risk": risk_profile_raw.get("regulatory_risk", "High"),
                "technology_risk": risk_profile_raw.get("technology_risk", "Moderate"),
                "vendor_risk": risk_profile_raw.get("vendor_risk", "High"),
                "threat_landscape": risk_profile_raw.get("threat_landscape", "Normal"),
                "compliance_requirements": risk_profile_raw.get("compliance_requirements", "High"),
            },
            "design_factors_applied": list(design_factor_weights.keys()),
            "prioritized_objectives": prioritized,
        }
    }


def run_skill(use_case_id: str, payload: dict, model: str = "stub") -> dict:
    """Stub entrypoint. Returns a structured skill result.

    For the Spine demonstration, the stub returns the expected output
    for known use cases. Real implementation: build prompt from SKILL.md,
    call LLM, parse output, return classification + structured result.
    """
    if use_case_id == "UC-01":
        maturity = _assess_maturity(payload)
        processes = maturity["assessment"]["processes"]
        overall_gap = max((p["gap"] for p in processes), default=0)
        return {
            "classification": f"GAP_{overall_gap:.1f}",
            "maturity_assessment": maturity["assessment"],
        }
    if use_case_id == "UC-02":
        obs = _format_observation(payload)
        return {
            "classification": obs["finding"]["severity"],
            "observation": obs["finding"],
        }
    if use_case_id == "UC-03":
        design = _assess_design_factors(payload)
        priority_count = len(design["assessment"]["prioritized_objectives"])
        return {
            "classification": f"DESIGN_FACTORS_{priority_count}",
            "design_factor_assessment": design["assessment"],
        }
    return {"classification": "UNKNOWN", "error": f"unknown use_case_id: {use_case_id}"}


def normalize_citations(text: str) -> list[tuple[str, str]]:
    """Extract [LABEL SX] citations from SKILL.md body text."""
    return re.findall(r"\[([A-Z][A-Z0-9 .\-:&/S,()]+?)\s*\S\s*([\w.\-]+)\]", text)
