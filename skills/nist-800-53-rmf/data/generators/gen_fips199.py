#!/usr/bin/env python3
"""Generate a synthetic FIPS 199 + 800-53 baseline selection seed.

Usage:
    python data/generators/gen_fips199.py --seed 42 --system caseflow > data/seeds/uc-01-input.json
    python data/generators/gen_fips199.py --seed 42 --system ars     > data/seeds/uc-02-input.json

Output schema: see skills/nist-800-53-rmf/data/README.md
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

PROFILES = {
    "caseflow": {
        "system_name": "CaseFlow Cloud",
        "system_description": (
            "Multi-tenant case management SaaS for federal civilian agencies. "
            "Processes PII including names, contact information, agency-issued identifiers, "
            "and case notes for ~250,000 individuals per year. Hosted on AWS GovCloud "
            "(FedRAMP High authorized). Multi-tenant; per-tenant logical isolation."
        ),
        "information_types": [
            {
                "name": "Case Management Records",
                "sp_800_60_info_type_code": "C.3.5.6",
                "description": "PII, agency case notes, status, attachments",
                "cia_baseline": {"c": "MODERATE", "i": "MODERATE", "a": "LOW"},
                "rationale": (
                    "Confidentiality: serious adverse effect if disclosed "
                    "(privacy, identity theft). Integrity: serious adverse effect if "
                    "modified (case outcomes, due process). Availability: limited "
                    "adverse effect (manual workaround for short outages)."
                ),
            },
            {
                "name": "Authentication metadata",
                "sp_800_60_info_type_code": "C.3.5.5",
                "description": "Login IDs, MFA factor type, last-login timestamp",
                "cia_baseline": {"c": "MODERATE", "i": "LOW", "a": "LOW"},
                "rationale": (
                    "Confidentiality: serious if disclosed in aggregate. Integrity and "
                    "availability: limited impact."
                ),
            },
        ],
        "downstream_consumers": [
            "Sponsoring federal agency (primary)",
            "Other federal agencies via FedRAMP Marketplace P-ATO",
        ],
        "cloud_provider": "AWS GovCloud (US)",
        "cloud_fedramp_id": "AGENCYID-CSP-AWS-GC-FEDRAMP-HIGH",
    },
    "ars": {
        "system_name": "Agency Records System (ARS)",
        "system_description": (
            "Agency-operated records management system on-prem in agency data center. "
            "Processes PII for ~80,000 individuals and case files for agency "
            "adjudicatory proceedings."
        ),
        "information_types": [
            {
                "name": "Adjudicatory Case Files",
                "sp_800_60_info_type_code": "C.3.5.6",
                "description": "PII, case decisions, evidence, exhibits",
                "cia_baseline": {"c": "MODERATE", "i": "MODERATE", "a": "LOW"},
                "rationale": (
                    "Confidentiality: serious if disclosed (due process, privacy). "
                    "Integrity: serious if modified (case outcomes). "
                    "Availability: limited (manual workaround acceptable)."
                ),
            },
            {
                "name": "System logs and audit records",
                "sp_800_60_info_type_code": "C.3.5.7",
                "description": "Audit events, access logs, system logs",
                "cia_baseline": {"c": "MODERATE", "i": "MODERATE", "a": "MODERATE"},
                "rationale": (
                    "All three: integrity required for forensic value, availability "
                    "for incident response, confidentiality for PII embedded in logs."
                ),
            },
        ],
        "downstream_consumers": [
            "Agency Office of Inspector General",
            "Agency Privacy Officer",
            "Audit teams (internal and external)",
        ],
        "cloud_provider": "On-prem (agency data center)",
        "cloud_fedramp_id": None,
    },
    "finpay": {
        "system_name": "FinPay Treasury Cloud",
        "system_description": (
            "B2B SaaS for commercial banks and credit unions; processes wire transfers, "
            "ACH origination, and fraud monitoring. SOC 2 Type II in place; PCI DSS v4.0 "
            "in scope for the wire transfer module."
        ),
        "information_types": [
            {
                "name": "Wire transfer and ACH records",
                "sp_800_60_info_type_code": "D.1.1.1",
                "description": "Wire details, ACH files, fraud signals",
                "cia_baseline": {"c": "MODERATE", "i": "MODERATE", "a": "MODERATE"},
                "rationale": (
                    "All three: wire windows are time-sensitive, integrity is critical, "
                    "and financial PII is sensitive."
                ),
            },
            {
                "name": "Account holder PII",
                "sp_800_60_info_type_code": "D.1.1.2",
                "description": "Names, account numbers, contact information",
                "cia_baseline": {"c": "MODERATE", "i": "LOW", "a": "LOW"},
                "rationale": (
                    "Confidentiality: serious if disclosed (financial PII). "
                    "Integrity/availability: limited."
                ),
            },
        ],
        "downstream_consumers": [
            "Commercial banks (B2B customers)",
            "Federal pilot agency (Treasury)",
            "Card networks (PCI-DSS scope)",
        ],
        "cloud_provider": "AWS (US-East-1, US-West-2)",
        "cloud_fedramp_id": None,
    },
}


def gen_fips199(system: str, seed: int) -> dict:
    profile = PROFILES[system]
    # Deterministic timestamp
    random.seed(seed)
    return {
        "system_name": profile["system_name"],
        "system_description": profile["system_description"],
        "information_types": profile["information_types"],
        "downstream_consumers": profile["downstream_consumers"],
        "cloud_provider": profile["cloud_provider"],
        "cloud_fedramp_id": profile["cloud_fedramp_id"],
        "pia_required": any("PII" in it["description"] or "pii" in it["description"].lower()
                            for it in profile["information_types"]),
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--system", choices=list(PROFILES), required=True)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)
    out = gen_fips199(args.system, args.seed)
    text = json.dumps(out, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")
    else:
        sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
