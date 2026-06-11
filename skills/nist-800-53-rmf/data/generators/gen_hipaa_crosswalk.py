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
FACT_SHEET = REPO_ROOT / "docs" / "hipaa-security-rule-fact-sheet.md"
SET_NAME = "SP 800-53 Rev 5.1.1"

# CPRT element IDs that differ from the current-CFR citations in the fact sheet.
# Most are standard-level shorthand (CPRT drops the trailing "(1)"); 164.308(b)(4)
# is CPRT carrying the PRE-OMNIBUS citation for Written Contract — the 2013 Omnibus
# Rule (78 FR 5694) renumbered it to 164.308(b)(3).
CPRT_TO_CFR_ALIAS = {
    "164.310(a)": "164.310(a)(1)",
    "164.310(d)": "164.310(d)(1)",
    "164.312(a)": "164.312(a)(1)",
    "164.312(c)": "164.312(c)(1)",
    "164.314(a)": "164.314(a)(1)",
    "164.314(b)": "164.314(b)(1)",
    "164.316(b)": "164.316(b)(1)",
    "164.308(b)(4)": "164.308(b)(3)",
}
# §164.314 spec children are designated "(Required)" inline at the (a)(2)/(b)(2)
# level in the regulation; the fact sheet lists only the parent standards.
REQUIRED_314_SPECS = {
    "164.314(a)(2)(i)", "164.314(a)(2)(ii)", "164.314(a)(2)(iii)",
    "164.314(b)(2)(i)", "164.314(b)(2)(ii)", "164.314(b)(2)(iii)", "164.314(b)(2)(iv)",
}


def _fact_sheet_designations() -> dict[str, str]:
    import yaml
    m = re.search(r"```yaml\n(.*?)\n```", FACT_SHEET.read_text(), re.DOTALL)
    fs = yaml.safe_load(m.group(1))
    out = {}
    for row in fs["identifiers"]:
        name = row["name"]
        if "(Standard" in name:
            out[row["code"]] = "Standard"
        elif "(Required)" in name:
            out[row["code"]] = "Required"
        elif "(Addressable)" in name:
            out[row["code"]] = "Addressable"
    return out


def designation_for(cprt_id: str, fs: dict[str, str]) -> tuple[str, str | None]:
    """Return (designation, current_cfr_cite_if_aliased)."""
    if cprt_id in REQUIRED_314_SPECS:
        return "Required", None
    cfr = CPRT_TO_CFR_ALIAS.get(cprt_id)
    key = cfr or cprt_id
    if key not in fs:
        raise KeyError(f"unmapped CPRT element id: {cprt_id}")
    return fs[key], cfr


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
    fs = _fact_sheet_designations()
    mappings = []
    for sr_el in sorted(grouped):
        controls = sorted({c["control_id"] for c in grouped[sr_el]},
                          key=lambda x: (x.split("-")[0], int(re.search(r"-(\d+)", x).group(1))))
        designation, cfr_cite = designation_for(sr_el, fs)
        row = {
            "hipaa_id": sr_el,
            "hipaa_id_note": "verbatim CPRT element identifier (CPRT granularity)",
            "designation": designation,
            "nist_800_53_ids": controls,
            "relationship": "informative_reference_olir",
        }
        if cfr_cite:
            row["current_cfr_cite"] = cfr_cite
            if sr_el == "164.308(b)(4)":
                row["citation_note"] = ("CPRT carries the pre-Omnibus citation; the 2013 "
                                        "Omnibus Rule (78 FR 5694) renumbered Written "
                                        "Contract to 164.308(b)(3)")
        mappings.append(row)
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
