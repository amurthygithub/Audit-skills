#!/usr/bin/env python3
"""Generate synthetic COSO deficiency classification and RcM evaluation seeds.

Usage:
    python data/generators/gen_deficiency.py --seed 42 --system sox404 > data/seeds/uc-01-input.json
    python data/generators/gen_deficiency.py --seed 42 --system deficiency > data/seeds/uc-02-input.json
    python data/generators/gen_deficiency.py --seed 42 --system principles > data/seeds/uc-03-input.json
"""

from __future__ import annotations

import argparse, json, random, sys
from pathlib import Path

PROFILES = {
    "sox404": {
        "entity_description": "Mid-cap public regional bank, accelerated filer, $12B assets. Three significant processes in scope for SOX 404 ICFR assessment: Loan Origination, Deposit Operations, Investment Securities. COSO 2013 ICIF framework applied.",
        "processes": ["Loan Origination", "Deposit Operations", "Investment Securities"],
        "industry": "financial-services",
        "fiscal_year": 2026,
    },
    "deficiency": {
        "deficiency_description": "IT access provisioning for ERP system not properly controlled. Terminated employees retain access average 45 days. No quarterly access review. Affects expenditure and payroll.",
        "affected_accounts": ["Operating Expenses", "Payroll Expense", "Accounts Payable"],
        "affected_assertions": ["Existence", "Completeness"],
        "compensating_controls_candidates": ["Bank reconciliation (monthly, precise)", "Payroll reconciliation (monthly, precise)", "Budget variance analysis (monthly, low precision)"],
        "preliminary_classification": "Significant Deficiency",
        "industry": "financial-services",
    },
    "principles": {
        "entity_description": "Public company performing comprehensive COSO 2013 ICIF assessment. All 17 principles evaluated for presence and functioning, 5 components assessed for integrated operation.",
        "assessment_date": "2026-06-30",
        "industry": "financial-services",
    },
}


def gen_seed(system: str, seed: int) -> dict:
    profile = PROFILES[system]
    random.seed(seed)
    if system == "sox404":
        return {"entity_description": profile["entity_description"], "processes": profile["processes"], "industry": profile["industry"], "fiscal_year": profile["fiscal_year"]}
    elif system == "deficiency":
        return {"deficiency_description": profile["deficiency_description"], "affected_accounts": profile["affected_accounts"], "affected_assertions": profile["affected_assertions"], "compensating_controls_candidates": profile["compensating_controls_candidates"], "preliminary_classification": profile["preliminary_classification"], "industry": profile["industry"]}
    elif system == "principles":
        return {"entity_description": profile["entity_description"], "assessment_date": profile["assessment_date"], "industry": profile["industry"]}
    return {}


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
