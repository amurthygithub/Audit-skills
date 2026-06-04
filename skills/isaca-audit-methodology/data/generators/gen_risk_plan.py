#!/usr/bin/env python3
"""Generate synthetic ISACA audit risk assessment and planning seeds.

Usage:
    python data/generators/gen_risk_plan.py --seed 42 --system bank > data/seeds/uc-03-input.json
    python data/generators/gen_risk_plan.py --seed 42 --system saas  > data/seeds/uc-01-input.json
    python data/generators/gen_risk_plan.py --seed 42 --system gov   > data/seeds/uc-02-input.json
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

PROFILES = {
    "bank": {
        "organization": "Regional commercial bank, $12B assets, 2,500 employees",
        "enterprise_strategy": "Compliance-focused",
        "industry": "financial-services",
        "risk_profile": {
            "regulatory_risk": "High",
            "technology_risk": "Moderate",
            "vendor_risk": "High",
            "threat_landscape": "Normal",
            "compliance_requirements": "High",
        },
        "it_issues": [
            "Legacy core banking platform",
            "Vendor concentration risk",
            "Manual compliance processes",
        ],
        "processes_in_scope": ["APO13", "BAI07", "DSS01", "MEA03"],
        "current_evidence": {
            "APO13": 2.5,
            "BAI07": 3.0,
            "DSS01": 3.0,
            "MEA03": 3.5,
        },
        "target_maturity": 4.0,
        "assessment_date": "2026-06-03",
        "sample_results": [
            {"application": "CoreBank-LoanOrig", "compliant": True, "finding": None},
            {"application": "CoreBank-WireTransfer", "compliant": False, "finding": "No recertification in 9 months"},
            {"application": "CoreBank-DepositLedger", "compliant": False, "finding": "No recertification in 12 months"},
            {"application": "CoreBank-FraudMonitor", "compliant": False, "finding": "No recertification in 6 months"},
            {"application": "CoreBank-CustomerPortal", "compliant": True, "finding": None},
        ],
        "finding_context": {
            "title": "Inadequate Access Recertification for Critical Applications",
            "condition": "No periodic access recertification for 3 of 5 critical applications",
            "actual_effect": "12% of terminated employees retained active access avg 45 days",
            "application_category": "Core Banking Applications",
            "itgc_category": "Access Controls",
        },
    },
    "saas": {
        "organization": "SaaS company with 500 employees, SOC 2 Type II in place, multi-tenant architecture",
        "enterprise_strategy": "Growth",
        "industry": "saas-technology",
        "risk_profile": {
            "regulatory_risk": "Moderate",
            "technology_risk": "Moderate",
            "vendor_risk": "Low",
            "threat_landscape": "Normal",
            "compliance_requirements": "Normal",
        },
        "it_issues": [
            "Multi-tenant data isolation",
            "Rapid release cadence vs change control",
        ],
        "processes_in_scope": ["APO13", "BAI07", "DSS01"],
        "current_evidence": {
            "APO13": 2.5,
            "BAI07": 3.0,
            "DSS01": 3.0,
        },
        "target_maturity": 4.0,
        "assessment_date": "2026-06-03",
        "sample_results": [
            {"application": "SaaS-Identity", "compliant": True, "finding": None},
            {"application": "SaaS-Billing", "compliant": False, "finding": "Missing SoD review"},
            {"application": "SaaS-API", "compliant": False, "finding": "No quarterly recertification"},
            {"application": "SaaS-Admin", "compliant": True, "finding": None},
        ],
        "finding_context": {
            "title": "ITGC Access Control Deficiency in SaaS Platform",
            "condition": "Quarterly recertification missing for 2 of 4 critical services",
            "actual_effect": "Stale access for 8% of users exceeding 60 days",
            "application_category": "SaaS Platform Services",
            "itgc_category": "Access Controls",
        },
    },
    "gov": {
        "organization": "State-level public health agency, 3,200 employees, interagency data sharing",
        "enterprise_strategy": "Compliance-focused",
        "industry": "public-sector",
        "risk_profile": {
            "regulatory_risk": "High",
            "technology_risk": "High",
            "vendor_risk": "Moderate",
            "threat_landscape": "High",
            "compliance_requirements": "High",
        },
        "it_issues": [
            "Legacy mainframe for vital records",
            "Interagency MOU-driven access sharing",
            "NIST 800-53 compliance required",
        ],
        "processes_in_scope": ["APO13", "DSS01", "DSS04", "APO12", "MEA03"],
        "current_evidence": {
            "APO13": 2.0,
            "DSS01": 2.5,
            "DSS04": 2.5,
            "APO12": 3.0,
            "MEA03": 3.0,
        },
        "target_maturity": 4.0,
        "assessment_date": "2026-06-03",
        "sample_results": [
            {"application": "Gov-EHR", "compliant": False, "finding": "Missing ATO renewal"},
            {"application": "Gov-VitalRecords", "compliant": False, "finding": "No audit logging enabled"},
            {"application": "Gov-LabResults", "compliant": False, "finding": "Unpatched critical vuln"},
            {"application": "Gov-Surveillance", "compliant": True, "finding": None},
            {"application": "Gov-Finance", "compliant": False, "finding": "Segregation of duties gap"},
        ],
        "finding_context": {
            "title": "Multiple ITGC Failures in Public Health Systems",
            "condition": "4 of 5 systems have critical ITGC deficiencies",
            "actual_effect": "ATO expired; unpatched vulnerabilities; segregation of duties gaps",
            "application_category": "Public Health Systems",
            "itgc_category": "Multiple Categories",
        },
    },
}


def gen_seed(system: str, seed: int) -> dict:
    profile = PROFILES[system]
    random.seed(seed)
    return {
        "organization": profile["organization"],
        "enterprise_strategy": profile["enterprise_strategy"],
        "industry": profile["industry"],
        "risk_profile": profile["risk_profile"],
        "it_issues": profile["it_issues"],
        "processes_in_scope": profile["processes_in_scope"],
        "current_evidence": profile["current_evidence"],
        "target_maturity": profile["target_maturity"],
        "assessment_date": profile["assessment_date"],
        "sample_results": profile["sample_results"],
        "finding_context": profile["finding_context"],
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--system", choices=list(PROFILES), required=True)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)
    out = gen_seed(args.system, args.seed)
    text = json.dumps(out, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")
    else:
        sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
