#!/usr/bin/env python3
"""Deterministic generator for the UC-01 addressable-specification register.

Emits all 22 addressable implementation specifications of 45 CFR 164 Subpart C
(vendored below from docs/hipaa-security-rule-fact-sheet.md §0 — the fact sheet
is the source of truth; tests diff this table against it) with the engagement's
documented assessment inputs. Disposition is NOT in the seed — it is derived by
the skill (see tests/hipaa_security_rule_stub.py) per §164.306(d)(3):

    reasonable_and_appropriate == true   -> implement
    false + alternative present          -> alternative_measure
    false + no alternative + justification -> not_reasonable_documented

Usage: python3 gen_addressable_register.py --seed 42 --out ../seeds/uc-01-addressable-register.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

# (spec_id, name, family) — all 22 addressable specs. Vendored from the fact sheet.
ADDRESSABLE_SPECS = [
    ("164.308(a)(3)(ii)(A)", "Authorization and/or supervision", "administrative"),
    ("164.308(a)(3)(ii)(B)", "Workforce clearance procedure", "administrative"),
    ("164.308(a)(3)(ii)(C)", "Termination procedures", "administrative"),
    ("164.308(a)(4)(ii)(B)", "Access authorization", "administrative"),
    ("164.308(a)(4)(ii)(C)", "Access establishment and modification", "administrative"),
    ("164.308(a)(5)(ii)(A)", "Security reminders", "administrative"),
    ("164.308(a)(5)(ii)(B)", "Protection from malicious software", "administrative"),
    ("164.308(a)(5)(ii)(C)", "Log-in monitoring", "administrative"),
    ("164.308(a)(5)(ii)(D)", "Password management", "administrative"),
    ("164.308(a)(7)(ii)(D)", "Testing and revision procedures", "administrative"),
    ("164.308(a)(7)(ii)(E)", "Applications and data criticality analysis", "administrative"),
    ("164.310(a)(2)(i)", "Contingency operations", "physical"),
    ("164.310(a)(2)(ii)", "Facility security plan", "physical"),
    ("164.310(a)(2)(iii)", "Access control and validation procedures", "physical"),
    ("164.310(a)(2)(iv)", "Maintenance records", "physical"),
    ("164.310(d)(2)(iii)", "Accountability", "physical"),
    ("164.310(d)(2)(iv)", "Data backup and storage", "physical"),
    ("164.312(a)(2)(iii)", "Automatic logoff", "technical"),
    ("164.312(a)(2)(iv)", "Encryption and decryption", "technical"),
    ("164.312(c)(2)", "Mechanism to authenticate electronic protected health information", "technical"),
    ("164.312(e)(2)(i)", "Integrity controls", "technical"),
    ("164.312(e)(2)(ii)", "Encryption", "technical"),
]

# Engagement assessment for CareSync Relay (fully remote 40-person SaaS BA on AWS).
# spec_id -> (decision_required, reasonable_and_appropriate, alternative, justification)
ASSESSMENT = {
    "164.308(a)(3)(ii)(A)": (True, True, None,
        "Engineering leads supervise ePHI-adjacent work; access reviewed weekly"),
    "164.308(a)(3)(ii)(B)": (False, True, None,
        "Background check and role review at hire"),
    "164.308(a)(3)(ii)(C)": (True, True, None,
        "Same-day deprovisioning runbook through the IdP"),
    "164.308(a)(4)(ii)(B)": (False, True, None,
        "Role-based grants in the IdP; documented approval flow"),
    "164.308(a)(4)(ii)(C)": (False, True, None,
        "Quarterly access recertification; changes ticketed"),
    "164.308(a)(5)(ii)(A)": (False, True, None,
        "Monthly security-reminder posts in company chat"),
    "164.308(a)(5)(ii)(B)": (False, True, None,
        "Managed EDR on all endpoints"),
    "164.308(a)(5)(ii)(C)": (True, False,
        "IdP anomalous-login alerting reviewed weekly; centralized SSO makes per-application "
        "log-in review redundant",
        "Per-application log-in monitoring is not reasonable and appropriate for a 40-person "
        "single-sign-on environment"),
    "164.308(a)(5)(ii)(D)": (True, False,
        "Passwordless WebAuthn with IdP-enforced MFA replaces password creation/rotation "
        "procedures",
        "Password management procedures are superseded by passwordless authentication"),
    "164.308(a)(7)(ii)(D)": (True, True, None,
        "Annual disaster-recovery tabletop plus restore test"),
    "164.308(a)(7)(ii)(E)": (False, True, None,
        "Criticality ranking maintained in the DR plan"),
    "164.310(a)(2)(i)": (False, False, None,
        "Fully remote organization; no facility houses ePHI systems. Facility-level "
        "contingency operations are the cloud provider's responsibility, evidenced by the "
        "provider's SOC 2 report"),
    "164.310(a)(2)(ii)": (True, False, None,
        "Fully remote organization; no facility houses ePHI systems. Workstation protections "
        "are addressed under 164.310(b)-(c)"),
    "164.310(a)(2)(iii)": (False, False, None,
        "No facility access to control or validate; provider data-center controls inherited "
        "and reviewed annually"),
    "164.310(a)(2)(iv)": (True, False, None,
        "No organization-controlled facility; provider maintenance records are covered by the "
        "provider's SOC 2 report"),
    "164.310(d)(2)(iii)": (False, True, None,
        "MDM asset register tracks every endpoint"),
    "164.310(d)(2)(iv)": (True, False,
        "Zero-ePHI-on-endpoints policy enforced by MDM and DLP; nothing to copy before moving "
        "equipment",
        "Pre-movement backup is not reasonable and appropriate because endpoints are barred "
        "from storing ePHI; the equivalent measure is the enforced zero-local-storage policy"),
    "164.312(a)(2)(iii)": (True, True, None,
        "15-minute idle session timeout enforced at the IdP and in the application"),
    "164.312(a)(2)(iv)": (True, True, None,
        "Encryption at rest: AES-256 via cloud KMS on every datastore holding ePHI — "
        "reasonable and appropriate given cloud hosting and 12 covered-entity customers"),
    "164.312(c)(2)": (True, True, None,
        "Object versioning plus checksum validation on ePHI stores"),
    "164.312(e)(2)(i)": (False, True, None,
        "TLS with integrity protection on all service-to-service traffic"),
    "164.312(e)(2)(ii)": (True, True, None,
        "TLS 1.2+ enforced on every external connection carrying ePHI"),
}


def build_register() -> list[dict]:
    register = []
    for spec_id, name, family in ADDRESSABLE_SPECS:
        decision_required, ra, alternative, justification = ASSESSMENT[spec_id]
        register.append({
            "spec_id": spec_id,
            "name": name,
            "family": family,
            "decision_required": decision_required,
            "reasonable_and_appropriate": ra,
            "alternative": alternative,
            "justification": justification,
        })
    return register


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42, help="determinism marker (content is fixed)")
    ap.add_argument("--out", default="../seeds/uc-01-addressable-register.json")
    args = ap.parse_args()
    out = Path(args.out)
    out.write_text(json.dumps(build_register(), indent=1) + "\n")
    print(f"wrote {out} ({len(ADDRESSABLE_SPECS)} specs)")


if __name__ == "__main__":
    main()
