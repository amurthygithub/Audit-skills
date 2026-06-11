#!/usr/bin/env python3
"""Deterministic generator for the UC-02 system inventory (Ironvale Retail).

Emits a CDE-tagged inventory; the scope counts the oracle asserts are computed
from the scope_tag distribution (in-scope = cde + connected). Content fixed;
--seed is a determinism marker.

Usage: python3 gen_system_inventory.py --seed 42 --out ../seeds/uc-02-input.json
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

SYSTEMS = [
    ("POS-terminals", "cde"), ("payment-switch", "cde"), ("card-vault", "cde"),
    ("store-controller", "cde"), ("e-comm-web", "cde"),
    ("auth-AD", "connected"), ("siem", "connected"), ("jump-host", "connected"),
    ("patch-server", "connected"), ("backup", "connected"),
    ("corp-email", "out"), ("hr-system", "out"), ("guest-wifi", "out"), ("dev-sandbox", "out"),
]


def build() -> dict:
    return {
        "use_case": "UC-02",
        "entity": {"name": "Ironvale Retail", "role": "merchant", "level": "L1 (brand-defined)",
                   "annual_transactions": 8_000_000, "validation": "ROC"},
        "system_inventory": [{"system": s, "scope_tag": t} for s, t in SYSTEMS],
        "customized_approach_requests": [
            {"requirement": "8.3.6", "topic": "password length/complexity",
             "targeted_risk_analysis_present": True,
             "rationale": "passphrase policy + adaptive lockout meets/exceeds the stated objective"}],
        "as_of_date": "2026-06-11",
        "notes": "scope convention: in-scope = cde + connected/security-impacting; out = "
                 "segmented & validated out of scope. Customized approach (Appendix D) requires "
                 "a documented Targeted Risk Analysis (TRA); distinct from a compensating control.",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="../seeds/uc-02-input.json")
    args = ap.parse_args()
    Path(args.out).write_text(json.dumps(build(), indent=1) + "\n")
    inv = build()["system_inventory"]
    print(f"wrote {args.out} ({len(inv)} systems; "
          f"{sum(1 for s in inv if s['scope_tag'] in ('cde','connected'))} in-scope)")


if __name__ == "__main__":
    main()
