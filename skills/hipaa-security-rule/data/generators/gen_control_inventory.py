#!/usr/bin/env python3
"""Deterministic generator for the UC-02 control inventory (Bellbrook Regional Health).

Emits one record per Subpart C standard — all 22, vendored below from
docs/hipaa-security-rule-fact-sheet.md §0 (tests diff this table against the
fact sheet). Status mix for the fixture: 14 implemented / 6 partial / 2 missing.

Usage: python3 gen_control_inventory.py --seed 42 --out ../seeds/uc-02-control-inventory.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

# (standard_id, name, family) — all 22 Subpart C standards. Vendored from the fact sheet.
STANDARDS = [
    ("164.308(a)(1)", "Security management process", "administrative"),
    ("164.308(a)(2)", "Assigned security responsibility", "administrative"),
    ("164.308(a)(3)", "Workforce security", "administrative"),
    ("164.308(a)(4)", "Information access management", "administrative"),
    ("164.308(a)(5)", "Security awareness and training", "administrative"),
    ("164.308(a)(6)", "Security incident procedures", "administrative"),
    ("164.308(a)(7)", "Contingency plan", "administrative"),
    ("164.308(a)(8)", "Evaluation", "administrative"),
    ("164.308(b)(1)", "Business associate contracts and other arrangements", "administrative"),
    ("164.310(a)(1)", "Facility access controls", "physical"),
    ("164.310(b)", "Workstation use", "physical"),
    ("164.310(c)", "Workstation security", "physical"),
    ("164.310(d)(1)", "Device and media controls", "physical"),
    ("164.312(a)(1)", "Access control", "technical"),
    ("164.312(b)", "Audit controls", "technical"),
    ("164.312(c)(1)", "Integrity", "technical"),
    ("164.312(d)", "Person or entity authentication", "technical"),
    ("164.312(e)(1)", "Transmission security", "technical"),
    ("164.314(a)(1)", "Business associate contracts or other arrangements", "organizational"),
    ("164.314(b)(1)", "Requirements for group health plans", "organizational"),
    ("164.316(a)", "Policies and procedures", "policies-documentation"),
    ("164.316(b)(1)", "Documentation", "policies-documentation"),
]

# Fixture status per standard (engagement finding inputs, not derived).
PARTIAL = {
    "164.308(a)(1)",  # risk analysis exists but is 3 years old, scope excludes 2 acquired clinics
    "164.308(a)(5)",  # training deployed to clinical staff only, not contractors
    "164.310(d)(1)",  # disposal vendor certificates incomplete for imaging devices
    "164.312(a)(1)",  # shared accounts persist in two legacy departmental systems
    "164.312(c)(1)",  # integrity mechanisms on the EHR only, not on the lab system
    "164.314(a)(1)",  # 14 of 212 BAAs predate the Omnibus provisions
}
MISSING = {
    "164.312(b)",     # no audit-control mechanism on the legacy lab system
    "164.308(a)(8)",  # no periodic evaluation program since the 2023 EHR migration
}


def build_inventory() -> list[dict]:
    inventory = []
    for std_id, name, family in STANDARDS:
        status = "missing" if std_id in MISSING else "partial" if std_id in PARTIAL else "implemented"
        inventory.append({
            "standard_id": std_id,
            "name": name,
            "family": family,
            "status": status,
            "evidence_ref": f"engagement-evidence/{std_id.replace('(', '').replace(')', '').replace('.', '-')}/",
        })
    return inventory


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42, help="determinism marker (content is fixed)")
    ap.add_argument("--out", default="../seeds/uc-02-control-inventory.json")
    args = ap.parse_args()
    out = Path(args.out)
    out.write_text(json.dumps(build_inventory(), indent=1) + "\n")
    counts = {}
    for r in build_inventory():
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(f"wrote {out} ({len(STANDARDS)} standards, {counts})")


if __name__ == "__main__":
    main()
