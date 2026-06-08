"""Generates the 3 UC seed JSON files used by the nist-csf-2 skill tests.

Run from the repo root:
    python3.11 skills/nist-csf-2/data/generators/gen_profile.py

This script is deterministic (no RNG) — re-running produces identical
output. The seed files are also committed in data/seeds/ so this
generator is only needed when:
- Bootstrapping a new UC (adding UC-04 etc.)
- Regenerating seeds after a schema change
- Adapting the seeds to a real engagement (modify the script to
  accept command-line overrides)

The 3 seeds are fictional, representative engagements:
- UC-01: 50-FTE Series-A SaaS (DataRelay Inc.) — first Organizational Profile
- UC-02: $20B regional bank (Pinecrest National) — board maturity report
- UC-03: Mid-market DoD supplier (Apex Manufacturing) — CMMC L2 readiness
"""

from __future__ import annotations

import json
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SEEDS_DIR = SKILL_DIR / "seeds"


def write_seed(name: str, payload: dict) -> None:
    SEEDS_DIR.mkdir(parents=True, exist_ok=True)
    (SEEDS_DIR / name).write_text(json.dumps(payload, indent=2) + "\n")
    print(f"Wrote {SEEDS_DIR / name} ({len(json.dumps(payload))} bytes)")


def gen_uc01() -> dict:
    return {
        "uc_id": "UC-01",
        "description": "Series-A SaaS first Organizational Profile — 50-FTE DataRelay Inc. B2B SaaS, building its first CSF 2.0 Current Profile. Target Tier 2 (Risk Informed) across all 6 Functions. The 6 representative Subcategory scores are a sample; a real engagement would carry all 106.",
        "org": {
            "name": "DataRelay Inc.",
            "size": "50 FTE",
            "sector": "saas-technology",
            "founded_year": 2024,
            "product": "B2B data integration SaaS",
            "customers": "Mid-market US companies, 200-2000 FTE",
        },
        "current_practices": {
            "mfa_enforced": True,
            "code_repository": "GitHub (org-owned)",
            "cloud_provider": "AWS (commercial, not GovCloud)",
            "vulnerability_scanning": "Quarterly, via Snyk",
            "incident_response_plan": "Informal, no documented runbook",
            "cyber_steering_committee": False,
            "cybersecurity_policy_published": False,
            "subcategory_owners_assigned": False,
        },
        "target_tier": 2,
        "subcategory_scores": [
            {"subcategory_id": "GV.OC-01", "status": "Not Implemented", "evidence": "Mission documented in company handbook; no formal risk context statement"},
            {"subcategory_id": "GV.PO-01", "status": "Not Implemented", "evidence": "No published cybersecurity policy; founders handle security ad hoc"},
            {"subcategory_id": "ID.AM-01", "status": "Partially Implemented", "evidence": "AWS asset inventory via tags; no formal record-keeping"},
            {"subcategory_id": "PR.AA-01", "status": "Partially Implemented", "evidence": "AWS IAM with groups; no formal access control policy"},
            {"subcategory_id": "PR.AA-03", "status": "Fully Implemented", "evidence": "MFA enforced on all admin and developer accounts since day 1"},
            {"subcategory_id": "PR.DS-01", "status": "Partially Implemented", "evidence": "KMS encryption at rest; data classification not formalized"},
            {"subcategory_id": "DE.CM-01", "status": "Largely Implemented", "evidence": "AWS GuardDuty enabled; SIEM in evaluation; no 24/7 SOC"},
            {"subcategory_id": "RS.MA-01", "status": "Not Implemented", "evidence": "No documented incident response plan; engineer-on-call paged on alerts but no runbook"},
        ],
    }


def gen_uc02() -> dict:
    return {
        "uc_id": "UC-02",
        "description": "$20B regional bank board cyber maturity report. Six Function radar with RECOVER (DR/BCP) as the lagging Function at T1. Full GOVERN narrative across all 6 GOVERN Categories. 12-month capital plan with 6 investment lines, each mapped to a regulatory anchor (OCC, NY DFS, FFIEC).",
        "org": {
            "name": "Pinecrest National Bank",
            "size": "8500 FTE",
            "sector": "financial-services",
            "assets_usd_billions": 24,
            "branches": 187,
            "primary_regulator": "OCC",
        },
        "function_scores": {
            "governance": "T3",
            "identify": "T3",
            "protect": "T3",
            "detect": "T2",
            "respond": "T2",
            "recover": "T1",
        },
        "govern_narrative": {
            "six_categories_covered": ["GV.OC", "GV.RM", "GV.SC", "GV.PO", "GV.OV", "GV.RR"],
            "board_talking_points": [
                "Mission and regulatory obligations documented (OCC Heightened Standards §III.A)",
                "Risk appetite approved by board Risk Committee, reviewed annually",
                "CISO reports to CRO; quarterly to board; ad hoc on material incidents",
                "Third-party risk program covers 412 critical vendors, including 18 fourth-party dependencies",
                "Cybersecurity policy hierarchy: enterprise policy + 14 domain policies + 47 procedures",
                "Independent assurance: external audit (Big 4) + internal audit (5 FTE) + OCC examination",
            ],
        },
        "investment_capacity_usd": 2_000_000,
        "capital_plan_12mo": [
            {"investment_line": "Identity & Access Management modernization (privileged access management rollout)", "cost_estimate": "$400K", "owner": "CISO", "regulatory_rationale": "OCC Heightened Standards §III.C.3 (third-party access to sensitive systems)"},
            {"investment_line": "Third-party risk management program (continuous monitoring of critical vendors)", "cost_estimate": "$300K", "owner": "TPRM Lead", "regulatory_rationale": "OCC Heightened Standards §III.D (third-party relationship risk); NY DFS §500.11 (third-party service provider security policy)"},
            {"investment_line": "Security operations center uplift (24/7 monitoring + threat intelligence)", "cost_estimate": "$500K", "owner": "SOC Director", "regulatory_rationale": "FFIEC CAT Domain 4 (Continuous Monitoring); FFIEC IT Examination Handbook"},
            {"investment_line": "Disaster recovery & resilience testing (4 recovery exercises, hot-site failover)", "cost_estimate": "$250K", "owner": "BCP Lead", "regulatory_rationale": "FFIEC CAT Domain 5 (Incident Management); OCC Heightened Standards §III.E (operational resilience)"},
            {"investment_line": "Cybersecurity training & awareness (board training + phishing simulation + role-based training)", "cost_estimate": "$150K", "owner": "People Security Lead", "regulatory_rationale": "NY DFS §500.14 (training); FFIEC CAT Domain 7 (Training)"},
            {"investment_line": "GRC tooling consolidation (replacing 3 point tools with 1 platform)", "cost_estimate": "$400K", "owner": "GRC Director", "regulatory_rationale": "OCC Heightened Standards §III.A (governance); reduces audit fatigue for FFIEC examinations"},
        ],
    }


def gen_uc03() -> dict:
    return {
        "uc_id": "UC-03",
        "description": "Apex Manufacturing — mid-market DoD supplier (precision-machined aerospace components) preparing for CMMC L2 certification. 14 lagging CSF 2.0 Subcategories are mapped to NIST SP 800-171 Rev 3 controls (the CMMC L2 source standard). CMMC L2 readiness covers all 4 practice domains the org is targeting (Access Control, I&A, Configuration Management, Incident Response) out of the 14 total CMMC L2 domains.",
        "org": {
            "name": "Apex Manufacturing",
            "size": "240 FTE",
            "sector": "manufacturing",
            "products": "Precision-machined aerospace components (turbine blades, structural fittings)",
            "customers": "DoD primes (Lockheed Martin, Northrop Grumman, Raytheon)",
            "facilities": 2,
            "ot_environments": "3 CNC cells, 1 metrology lab, 1 ERP (Made4net)",
        },
        "cmmc_target": "L2",
        "cmmc_l2_assessment_target_date": "2026-09-30",
        "lagging_subcategories": [
            "PR.AA-01", "PR.AA-03", "PR.AA-05", "PR.DS-01", "PR.PS-01", "PR.PS-02", "PR.IR-01",
            "DE.CM-01", "DE.CM-03",
            "RS.MA-01", "RS.AN-03", "RS.CO-02",
            "RC.RP-01", "RC.RP-03",
        ],
        "crosswalk": [
            {"subcategory_id": "PR.AA-01", "primary_800_171_control": "3.1.1", "practice_domain": "Access Control", "secondary_controls": ["3.1.2", "3.1.3"], "evidence_gap": "No documented access control policy; relies on AD group membership"},
            {"subcategory_id": "PR.AA-03", "primary_800_171_control": "3.5.1", "practice_domain": "Identification & Authentication", "secondary_controls": ["3.5.2", "3.5.3"], "evidence_gap": "MFA on IT systems but not on OT HMI terminals"},
            {"subcategory_id": "PR.AA-05", "primary_800_171_control": "3.1.5", "practice_domain": "Access Control", "secondary_controls": ["3.1.6", "3.1.7"], "evidence_gap": "No documented least-privilege review process"},
            {"subcategory_id": "PR.DS-01", "primary_800_171_control": "3.13.1", "practice_domain": "Configuration Management", "secondary_controls": ["3.13.2"], "evidence_gap": "CUI encrypted at rest in transit; no FIPS-validated crypto on legacy CNC controllers"},
            {"subcategory_id": "PR.PS-01", "primary_800_171_control": "3.4.1", "practice_domain": "Configuration Management", "secondary_controls": ["3.4.2", "3.4.3"], "evidence_gap": "No baseline configuration documented for OT systems"},
            {"subcategory_id": "PR.PS-02", "primary_800_171_control": "3.11.1", "practice_domain": "Configuration Management", "secondary_controls": ["3.11.2", "3.11.3"], "evidence_gap": "Quarterly vulnerability scans on IT; no scanning on OT network"},
            {"subcategory_id": "PR.IR-01", "primary_800_171_control": "3.13.1", "practice_domain": "Configuration Management", "secondary_controls": ["3.13.4", "3.13.5"], "evidence_gap": "Flat OT network; no segmentation between IT and OT zones"},
            {"subcategory_id": "DE.CM-01", "primary_800_171_control": "3.3.1", "practice_domain": "Configuration Management", "secondary_controls": ["3.3.2", "3.3.3"], "evidence_gap": "IT monitoring in place; OT monitoring limited to controller logs"},
            {"subcategory_id": "DE.CM-03", "primary_800_171_control": "3.3.1", "practice_domain": "Configuration Management", "secondary_controls": ["3.3.5"], "evidence_gap": "No formal anomaly detection for OT environments"},
            {"subcategory_id": "RS.MA-01", "primary_800_171_control": "3.6.1", "practice_domain": "Incident Response", "secondary_controls": ["3.6.2", "3.6.3"], "evidence_gap": "No documented IR plan; relies on IT generalist for both IT and OT incidents"},
            {"subcategory_id": "RS.AN-03", "primary_800_171_control": "3.6.2", "practice_domain": "Incident Response", "secondary_controls": ["3.6.4"], "evidence_gap": "No root-cause analysis process post-incident"},
            {"subcategory_id": "RS.CO-02", "primary_800_171_control": "3.6.2", "practice_domain": "Incident Response", "secondary_controls": [], "evidence_gap": "No documented breach notification process (DIB reporting per 32 CFR 236)"},
            {"subcategory_id": "RC.RP-01", "primary_800_171_control": "3.8.1", "practice_domain": "Configuration Management", "secondary_controls": ["3.8.2", "3.8.3"], "evidence_gap": "No OT-specific recovery plan; current BCP covers IT only"},
            {"subcategory_id": "RC.RP-03", "primary_800_171_control": "3.8.3", "practice_domain": "Configuration Management", "secondary_controls": [], "evidence_gap": "Recovery testing is annual for IT; never tested for OT"},
        ],
        "cmmc_l2_readiness": [
            {"practice_domain": "Access Control", "controls_assessed": 8, "controls_satisfied": 4, "gap_count": 4, "primary_800_171_controls": ["3.1.1", "3.1.2", "3.1.5", "3.1.6"]},
            {"practice_domain": "Identification & Authentication", "controls_assessed": 6, "controls_satisfied": 3, "gap_count": 3, "primary_800_171_controls": ["3.5.1", "3.5.2", "3.5.3"]},
            {"practice_domain": "Configuration Management", "controls_assessed": 9, "controls_satisfied": 5, "gap_count": 4, "primary_800_171_controls": ["3.4.1", "3.4.2", "3.11.1", "3.11.2"]},
            {"practice_domain": "Incident Response", "controls_assessed": 5, "controls_satisfied": 1, "gap_count": 4, "primary_800_171_controls": ["3.6.1", "3.6.2", "3.6.3", "3.6.4"]},
        ],
    }


def main() -> None:
    write_seed("uc-01-input.json", gen_uc01())
    write_seed("uc-02-input.json", gen_uc02())
    write_seed("uc-03-input.json", gen_uc03())


if __name__ == "__main__":
    main()
