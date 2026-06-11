#!/usr/bin/env python3
"""Deterministic generator for SAQ-selection boundary cases (eval sampler input).

Sweeps the payment-page architecture axes that flip the SAQ decision and labels
each via the stub (oracle-anchored self-labeling). Emits a JSON list the eval
generator can turn into cases.

Usage: python3 gen_saq_cases.py --out ../seeds/saq-boundary-cases.json
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tests"))
from pci_dss_assessment_stub import run_skill  # noqa: E402

METHODS = ["redirect", "iframe", "direct_post", "inline_js"]


def build() -> list:
    cases = []
    for outsourced in (True, False):
        for method in METHODS:
            for mscript in (True, False):
                for touch in (True, False):
                    payload = {
                        "entity": {"role": "merchant", "is_service_provider": False},
                        "payment_page": {
                            "outsourced_to_compliant_third_party": outsourced,
                            "method": method,
                            "merchant_javascript_on_payment_page": mscript,
                            "merchant_servers_touch_pan": touch},
                    }
                    out = run_skill("UC-01", payload)
                    cases.append({"payment_page": payload["payment_page"],
                                  "expected_saq": out["saq_eligibility"]})
    return cases


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", default="../seeds/saq-boundary-cases.json")
    args = ap.parse_args()
    cases = build()
    Path(args.out).write_text(json.dumps(cases, indent=1) + "\n")
    from collections import Counter
    print(f"wrote {args.out} ({len(cases)} cases; "
          f"{dict(Counter(c['expected_saq'] for c in cases))})")


if __name__ == "__main__":
    main()
