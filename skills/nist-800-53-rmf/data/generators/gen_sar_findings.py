#!/usr/bin/env python3
"""Generate synthetic SAR findings for UC-02.

Deterministic per seed. Produces 22 findings in the expected severity distribution
(4 High, 8 Moderate, 10 Low) unless --n and --severity-dist are overridden.

Usage:
    python data/generators/gen_sar_findings.py --seed 42 --n 22 \\
        --out data/seeds/uc-02-findings.json
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

# Curated finding templates by control family. Each template is fillable with
# the deterministic random.

FINDING_TEMPLATES = [
    # (control_id, severity_pool, description_template, cause, recommendation)
    ("AC-2(4)",  ["High", "Moderate"],
     "Quarterly account review was not performed for the last {quarters} quarters; logs show no review activity.",
     "Operational lapse (process not followed)",
     "Re-perform account review; implement a calendar-tracked quarterly task with sign-off in the GRC tool."),
    ("AC-2(11)", ["Moderate", "Low"],
     "Account usage conditions are not documented in the user account agreement.",
     "Documentation gap",
     "Add usage conditions to the account agreement; track in HRMS."),
    ("AC-2(12)", ["Moderate", "Low"],
     "Account monitoring for atypical usage is not configured for high-risk roles.",
     "Design weakness",
     "Configure SIEM rules for atypical usage; document in monitoring strategy."),
    ("AC-2(13)", ["Low"],
     "Disable accounts for high-risk users is not tested; last test was {months} months ago.",
     "Operational lapse",
     "Add account-disable test to annual incident-response exercise."),
    ("AU-2", ["Moderate"],
     "Application-layer audit events for {event_count} event types are not enabled.",
     "Design weakness",
     "Enable application-layer audit events; forward to central SIEM."),
    ("AU-6(1)", ["Moderate"],
     "Audit log review lacks documented escalation thresholds for anomalies.",
     "Design weakness",
     "Define escalation thresholds; document in IRP; add to runbook."),
    ("AU-9", ["Low"],
     "Audit log protection against tampering is configured but not tested.",
     "Operational lapse",
     "Add quarterly test of log integrity protection."),
    ("CM-2", ["Moderate"],
     "Configuration baseline for {component} is documented but not enforced via automated scanning.",
     "Operational lapse",
     "Deploy SCAP scanning; configure weekly cadence."),
    ("CM-6", ["High", "Moderate"],
     "Configuration settings for {component} deviate from the documented baseline in {deviation_count} instances.",
     "Operational lapse",
     "Remediate deviations; deploy automated configuration scanning."),
    ("CM-7", ["Low"],
     "Least functionality — {service} service is enabled but not documented as required.",
     "Documentation gap",
     "Document justification or disable the service."),
    ("CP-2", ["Low"],
     "Contingency plan is documented but has not been tested in the last {months} months.",
     "Operational lapse",
     "Schedule and execute contingency plan test."),
    ("IA-2(1)", ["Moderate", "Low"],
     "MFA is enforced for {coverage_pct}% of accounts; gap: {gap_accounts}.",
     "Design weakness",
     "Enable MFA for remaining accounts; document exception process."),
    ("IA-5(1)", ["Low"],
     "Password policy does not enforce minimum length of 12 characters.",
     "Design weakness",
     "Update password policy; deploy to identity provider."),
    ("IR-4", ["Moderate"],
     "Incident response plan is documented but does not include automation for the {step} step.",
     "Design weakness",
     "Add automation to the IRP; document in runbook."),
    ("IR-6", ["Low"],
     "Incident reporting thresholds are not documented.",
     "Documentation gap",
     "Document reporting thresholds; align with US-CERT and agency IRP."),
    ("MA-2", ["Low"],
     "Controlled maintenance procedure is documented but maintenance logs are not consistently captured.",
     "Operational lapse",
     "Update maintenance log template; train IT staff."),
    ("MP-6", ["Low"],
     "Media sanitization procedure is documented but not consistently followed.",
     "Operational lapse",
     "Refresh training; add compliance check to media disposal workflow."),
    ("PE-3", ["Low"],
     "Physical access control list review is documented but last review was {months} months ago.",
     "Operational lapse",
     "Schedule physical access list review; document in facility SOP."),
    ("PL-2", ["Low"],
     "SSP is up-to-date but does not include a section on supply chain risk management.",
     "Documentation gap",
     "Add SR family section to SSP."),
    ("PS-3", ["Moderate"],
     "Personnel screening for {role_count} sensitive roles is documented but not consistently performed.",
     "Operational lapse",
     "Add screening to onboarding checklist; audit quarterly."),
    ("RA-3", ["High", "Moderate"],
     "Risk assessment is documented but does not include threat catalog updates from the last 12 months.",
     "Operational lapse",
     "Update risk assessment per 800-30 Rev 1; include current threat catalog."),
    ("SC-7", ["Moderate"],
     "Boundary protection is configured but {rule_count} rules are not reviewed in the last 90 days.",
     "Operational lapse",
     "Schedule quarterly firewall rule review; document in change management."),
    ("SC-8(1)", ["Low"],
     "Cryptographic protection for wireless is N/A but justification is not documented.",
     "Documentation gap",
     "Document scoping decision in SSP §9."),
    ("SC-13", ["Low"],
     "Cryptographic module inventory is documented but does not reference FIPS 140-3 validated modules.",
     "Documentation gap",
     "Update crypto inventory; cite FIPS 140-3 module certificates."),
    ("SI-2", ["High", "Moderate"],
     "Flaw remediation — {vuln_count} high-severity vulnerabilities are past the patch SLA.",
     "Operational lapse",
     "Patch or document compensating control; update POA&M."),
    ("SI-3", ["Low"],
     "Malware protection is deployed; last signature update check was {days} days ago.",
     "Operational lapse",
     "Add daily signature-update check to monitoring."),
    ("SI-4(2)", ["Moderate"],
     "System monitoring — automated tools are deployed but do not include {capability}.",
     "Design weakness",
     "Deploy additional monitoring capability; document in monitoring strategy."),
    ("SR-3", ["Moderate"],
     "Supply chain risk assessment is documented but has not been refreshed in the last 12 months.",
     "Operational lapse",
     "Refresh supply chain risk assessment; include new vendors."),
]


def gen_sar_findings(seed: int, n: int) -> list[dict]:
    random.seed(seed)
    out = []
    for i in range(1, n + 1):
        tmpl = random.choice(FINDING_TEMPLATES)
        control_id, severity_pool, desc, cause, rec = tmpl
        severity = random.choice(severity_pool)
        description = desc.format(
            quarters=random.randint(2, 4),
            months=random.choice([3, 4, 6, 8, 9, 12, 15]),
            component=random.choice(["production database", "application server", "API gateway", "load balancer"]),
            deviation_count=random.randint(3, 12),
            service=random.choice(["FTP", "Telnet", "SMBv1", "SNMPv2"]),
            coverage_pct=random.randint(85, 98),
            gap_accounts=random.randint(2, 25),
            step=random.choice(["detection", "containment", "eradication", "recovery"]),
            event_count=random.randint(3, 12),
            role_count=random.randint(2, 8),
            rule_count=random.randint(5, 25),
            vuln_count=random.randint(1, 7),
            days=random.randint(2, 14),
            capability=random.choice(["file integrity monitoring", "anomaly detection", "threat intelligence feed"]),
        )
        finding = {
            "finding_id": f"SAR-{i:03d}",
            "control_id": control_id,
            "severity": severity,
            "determination": "Other Than Satisfied",
            "description": description,
            "cause": cause,
            "effect": f"Risk to system confidentiality, integrity, or availability from {control_id} deviation.",
            "recommendation": rec,
            "compensating_control": None if random.random() < 0.7 else "Manual review process exists but is not fully effective.",
            "remediation_plan": f"Open POA&M-{i:03d}; remediate within {random.choice([30, 60, 90, 180])} days.",
            "risk_acceptance_required": severity in ("High", "Moderate") and random.random() < 0.3,
        }
        out.append(finding)
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--n", type=int, default=22)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)
    findings = gen_sar_findings(args.seed, args.n)
    text = json.dumps(findings, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")
    else:
        sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
