#!/usr/bin/env python3
"""Generate a synthetic SOC 2 → 800-53 Moderate crosswalk gap list.

Produces ~94 gap controls based on the crosswalk in data/crosswalks/soc2-to-800-53-mod.json
(which is the authoritative reference). The generator is deterministic per seed.

Usage:
    python data/generators/gen_crosswalk_gap.py --seed 42 \\
        --out data/seeds/uc-03-gap-list.json
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

# Curated gap controls (representative; in production, this list is computed
# from the crosswalk in data/crosswalks/soc2-to-800-53-mod.json).
GAP_CONTROLS = [
    ("AT-2", "operational", "Medium", "HR / IT", 60,
     "Document quarterly security awareness training; track in LMS"),
    ("AT-3", "operational", "Medium", "HR", 90,
     "Role-based training for ISSO, developer, admin; track in LMS"),
    ("RA-3", "operational", "High", "CISO", 30,
     "Risk assessment per 800-30 Rev 1; update annually"),
    ("SI-4", "operational", "High", "CISO", 60,
     "Deploy SIEM with continuous monitoring; document in SSP §13"),
    ("SI-4(2)", "operational", "High", "CISO", 60,
     "Add automated threat detection"),
    ("SI-4(7)", "operational", "Medium", "CISO", 90,
     "Add detected-events correlation"),
    ("SR-1", "supply-chain", "High", "Procurement", 90,
     "Document SCRM policy"),
    ("SR-3", "supply-chain", "High", "Procurement", 90,
     "Supply chain risk assessment"),
    ("SR-5", "supply-chain", "Medium", "Procurement", 90,
     "Acquisition strategies and tools"),
    ("SR-6", "supply-chain", "Medium", "Procurement", 90,
     "Supplier assessments and reviews"),
    ("PT-7", "privacy", "Medium", "Privacy Officer", 60,
     "Document PIA; agency approval"),
    ("PT-5", "privacy", "Medium", "Privacy Officer", 60,
     "Privacy notice on data collection"),
    ("AC-2(11)", "enhancement", "Medium", "IT", 60,
     "Account usage conditions documented in handbook"),
    ("AC-2(13)", "enhancement", "Low", "IT", 90,
     "Disable accounts for high-risk users"),
    ("IR-4(1)", "enhancement", "High", "CISO", 60,
     "Automated IR playbook"),
    ("IR-5", "operational", "Medium", "CISO", 60,
     "Incident monitoring"),
    ("IR-6(1)", "operational", "Medium", "CISO", 60,
     "Automated incident reporting"),
    ("PM-9", "program-mgmt", "Medium", "CISO", 90,
     "Risk management strategy"),
    ("PM-10", "program-mgmt", "Medium", "CISO", 90,
     "Authorization process"),
    ("PM-15", "program-mgmt", "Medium", "CISO", 90,
     "Security and privacy groups and associations"),
    ("PM-16", "program-mgmt", "Medium", "CISO", 90,
     "Threat awareness program"),
    ("PM-31", "program-mgmt", "Low", "CISO", 180,
     "Continuous monitoring strategy"),
    ("PM-32", "program-mgmt", "Low", "CISO", 180,
     "Purposing"),
    ("AU-6(3)", "operational", "Medium", "IT", 60,
     "Correlate audit review, analysis, reporting"),
    ("AU-12", "operational", "Medium", "IT", 60,
     "Audit record generation"),
    ("CA-7(1)", "program-mgmt", "Medium", "CISO", 90,
     "Independent assessment"),
    ("CA-7(4)", "program-mgmt", "Medium", "CISO", 90,
     "Risk monitoring"),
    ("CM-3(2)", "operational", "Low", "IT", 90,
     "Testing, training, and monitoring"),
    ("CM-4(1)", "operational", "Low", "IT", 90,
     "Automated configuration deviation detection"),
    ("CM-7(2)", "operational", "Low", "IT", 90,
     "Prevent program execution"),
    ("CP-2(1)", "operational", "Low", "IT", 90,
     "Coordinate with related plans"),
    ("IA-2(2)", "enhancement", "Medium", "IT", 60,
     "Multi-factor authentication to privileged accounts"),
    ("IA-2(8)", "enhancement", "Medium", "IT", 60,
     "Access to accounts — replay resistant"),
    ("IA-4(1)", "operational", "Low", "IT", 60,
     "Automated identifier management"),
    ("IA-5(2)", "operational", "Low", "IT", 60,
     "Public key-based authentication"),
    ("MA-3", "operational", "Low", "IT", 90,
     "Maintenance tools"),
    ("MA-4(1)", "operational", "Low", "IT", 90,
     "Nonlocal maintenance logging"),
    ("MA-5", "operational", "Low", "HR", 90,
     "Maintenance personnel"),
    ("MP-4", "operational", "Low", "IT", 90,
     "Media storage"),
    ("MP-5(4)", "operational", "Low", "IT", 90,
     "Cryptographic protection"),
    ("PE-2(1)", "operational", "Low", "Facilities", 90,
     "Automated facility access records"),
    ("PE-3(1)", "operational", "Low", "Facilities", 90,
     "System access"),
    ("PE-6(1)", "operational", "Low", "Facilities", 90,
     "Intrusion alarms / surveillance equipment"),
    ("PE-8", "operational", "Low", "Facilities", 90,
     "Visitor access records"),
    ("PL-2(3)", "documentation", "Low", "CISO", 90,
     "Plan update with significant changes"),
    ("PL-8(1)", "documentation", "Low", "Enterprise Architect", 90,
     "Security and privacy architectures"),
    ("PL-10", "documentation", "Low", "CISO", 90,
     "Baseline selection"),
    ("PL-11", "documentation", "Low", "CISO", 90,
     "Baseline tailoring"),
    ("PS-2", "operational", "Low", "HR", 60,
     "Position risk designation"),
    ("PS-5", "operational", "Low", "HR", 60,
     "Personnel transfer"),
    ("PS-6", "operational", "Low", "HR", 60,
     "Access agreements"),
    ("PS-7", "operational", "Low", "HR", 60,
     "External personnel security"),
    ("PS-8", "operational", "Low", "HR", 60,
     "Personnel sanctions"),
    ("RA-2", "operational", "High", "CISO", 30,
     "Security categorization"),
    ("RA-5(2)", "operational", "High", "CISO", 30,
     "Update tools"),
    ("RA-5(5)", "operational", "Medium", "CISO", 60,
     "Privileged access"),
    ("RA-5(8)", "operational", "Medium", "CISO", 60,
     "Review historic audit logs"),
    ("RA-5(11)", "operational", "Medium", "CISO", 60,
     "Public disclosure programs"),
    ("SA-4(1)", "operational", "Low", "Procurement", 90,
     "Functional properties of controls"),
    ("SA-4(2)", "operational", "Low", "Procurement", 90,
     "Design and implementation information"),
    ("SA-4(9)", "operational", "Low", "Procurement", 90,
     "Functions, ports, protocols, services in use"),
    ("SA-4(10)", "operational", "Low", "Procurement", 90,
     "Use of approved PIV products"),
    ("SA-9(2)", "operational", "Low", "Procurement", 90,
     "Identification of functions, ports, protocols, services"),
    ("SA-10", "operational", "Medium", "Engineering", 90,
     "Developer configuration management"),
    ("SA-11(1)", "operational", "Medium", "Engineering", 90,
     "Static code analysis"),
    ("SA-11(2)", "operational", "Medium", "Engineering", 90,
     "Threat modeling and vulnerability analysis"),
    ("SA-15(1)", "operational", "Medium", "Engineering", 90,
     "Attack surface review"),
    ("SA-15(3)", "operational", "Medium", "Engineering", 90,
     "Criticality analysis"),
    ("SA-22", "operational", "Medium", "Engineering", 90,
     "Unsupported system components"),
    ("SC-2(1)", "operational", "Low", "Engineering", 90,
     "Restrict internal communications"),
    ("SC-3(1)", "operational", "Low", "Engineering", 90,
     "Hardware enforcement"),
    ("SC-5", "operational", "Low", "IT", 90,
     "Denial-of-service protection"),
    ("SC-7(8)", "operational", "Medium", "IT", 60,
     "Route traffic to authenticated proxy servers"),
    ("SC-7(10)", "operational", "Medium", "IT", 60,
     "Prevent exfiltration of information"),
    ("SC-7(18)", "operational", "Medium", "IT", 60,
     "Fail secure"),
    ("SC-8(4)", "operational", "Medium", "IT", 60,
     "Cryptographic protection of confidentiality — separate channels"),
    ("SC-10", "operational", "Low", "IT", 90,
     "Network disconnect"),
    ("SC-15", "operational", "Low", "IT", 90,
     "Collaborative computing devices"),
    ("SC-20", "operational", "Low", "IT", 90,
     "Address name / address resolution service"),
    ("SC-21", "operational", "Low", "IT", 90,
     "Secure name / address resolution service (recursive or caching resolver)"),
    ("SC-22", "operational", "Low", "IT", 90,
     "Architecture and provisioning for name / address resolution service"),
    ("SC-39", "operational", "Low", "IT", 90,
     "Process isolation"),
    ("SI-2(2)", "operational", "Medium", "IT", 60,
     "Automated flaw remediation status"),
    ("SI-2(4)", "operational", "Medium", "IT", 60,
     "Regression testing"),
    ("SI-4(4)", "operational", "Medium", "CISO", 60,
     "Inbound and outbound communications traffic"),
    ("SI-4(5)", "operational", "Medium", "CISO", 60,
     "System-generated alerts"),
    ("SI-6", "operational", "Medium", "IT", 60,
     "Security and privacy function verification"),
    ("SI-7(1)", "operational", "Medium", "IT", 60,
     "Integrity checks"),
    ("SI-7(7)", "operational", "Medium", "IT", 60,
     "Integration of detection and response"),
    ("SI-8(2)", "operational", "Medium", "IT", 60,
     "Updates"),
    ("SI-10", "operational", "Medium", "Engineering", 60,
     "Information input validation"),
    ("SI-11", "operational", "Medium", "Engineering", 60,
     "Error handling"),
    ("SI-16", "operational", "Low", "Engineering", 90,
     "Memory protection"),
]


def gen_gap_list(seed: int) -> list[dict]:
    random.seed(seed)
    out = []
    for i, (cid, gtype, prio, owner, target_d, action) in enumerate(GAP_CONTROLS, 1):
        out.append({
            "gap_id": f"GAP-{i:03d}",
            "control_id": cid,
            "gap_type": gtype,
            "priority": prio,
            "owner": owner,
            "target_date_days": target_d,
            "remediation_action": action,
            "evidence_refs": [f"docs/remediation/{cid}.md"],
            "status": "Open",
        })
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)
    gap_list = gen_gap_list(args.seed)
    text = json.dumps(gap_list, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")
    else:
        sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
