#!/usr/bin/env python3
"""Deterministic generator for the HIPAA Security Rule -> SP 800-53 crosswalk seed.

Input: the archived NIST CPRT extraction (docs/builds/sox-638/cprt-extraction.json),
retrieved 2026-06-10 from the CPRT REST API (SP 800-66 Rev 2 framework, OLIR set
SP-800-66-Rev-2-to-SP-800-53-Rev-5.1.1). This generator filters the 800-53 rows,
normalizes control IDs to the skill's house format (zero-padding stripped:
AC-02 -> AC-2; the verbatim CPRT ID is preserved per row), groups by Security Rule
element, and computes the summary FROM the rows (derivability — SOX-637 pattern).

Mappings are OLIR informative references ("supports" semantics). CPRT carries NO
exact/partial strength ratings — none are emitted (SOX-638: the prior 12-row file's
"exact" labels were invented).

Usage: python3 gen_hipaa_crosswalk.py --out ../seeds/hipaa-to-800-53.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
EXTRACTION = REPO_ROOT / "docs" / "builds" / "sox-638" / "cprt-extraction.json"
SET_NAME = "SP 800-53 Rev 5.1.1"


def normalize_control_id(cprt_id: str) -> str:
    """AC-02 -> AC-2 (strip zero padding in the numeric part only)."""
    m = re.fullmatch(r"([A-Z]{2})-0*(\d+)(.*)", cprt_id)
    return f"{m.group(1)}-{m.group(2)}{m.group(3)}" if m else cprt_id


def build() -> dict:
    data = json.loads(EXTRACTION.read_text())
    rows = [r for r in data["rows"] if r["set"] == SET_NAME]
    grouped: dict[str, list[dict]] = {}
    for r in rows:
        grouped.setdefault(r["security_rule_element"], []).append({
            "control_id": normalize_control_id(r["target_id"]),
            "control_id_cprt": r["target_id"],
        })
    mappings = []
    for sr_el in sorted(grouped):
        controls = sorted({c["control_id"] for c in grouped[sr_el]},
                          key=lambda x: (x.split("-")[0], int(re.search(r"-(\d+)", x).group(1))))
        mappings.append({
            "hipaa_id": sr_el,
            "hipaa_id_note": "verbatim CPRT element identifier (CPRT granularity)",
            "nist_800_53_ids": controls,
            "relationship": "informative_reference_olir",
        })
    unique_controls = sorted({c for m in mappings for c in m["nist_800_53_ids"]})
    return {
        "_meta": {
            "source": "NIST CPRT, SP 800-66 Rev 2 framework — OLIR set "
                      "SP-800-66-Rev-2-to-SP-800-53-Rev-5.1.1 (retrieved 2026-06-10)",
            "extraction": "docs/builds/sox-638/cprt-extraction.json",
            "target_catalog": "SP 800-53 Rev 5.1.1",
            "semantics": "OLIR informative references (supports-style). NO exact/partial "
                         "strength ratings exist in the source; none are asserted.",
            "id_normalization": "control IDs zero-padding stripped (AC-02 -> AC-2); "
                                "verbatim CPRT IDs retained in the extraction archive.",
            "generated_by": "data/generators/gen_hipaa_crosswalk.py",
        },
        "mappings": mappings,
        "summary": {
            "security_rule_elements_mapped": len(mappings),
            "mapping_rows": sum(len(m["nist_800_53_ids"]) for m in mappings),
            "unique_800_53_controls": len(unique_controls),
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="../seeds/hipaa-to-800-53.json")
    args = ap.parse_args()
    out = Path(args.out)
    payload = build()
    out.write_text(json.dumps(payload, indent=1) + "\n")
    print(f"wrote {out}: {payload['summary']}")


if __name__ == "__main__":
    main()
