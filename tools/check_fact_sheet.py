#!/usr/bin/env python3
"""G1 gate — fact-sheet completeness checker (SOX-632).

Validates a Day 0 fact-sheet (docs/<slug>-fact-sheet.md) before any build
agent is dispatched. Parses the §0 machine-readable YAML data block and the
numbered prose sections. Exits non-zero on any failure; prints a
human-readable report.

Usage:
    python tools/check_fact_sheet.py docs/<slug>-fact-sheet.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List, Tuple

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


REQUIRED_SECTIONS = list(range(0, 9))  # ## 0. through ## 8.
REQUIRED_TOP_KEYS = {
    "fact_sheet", "counts", "identifiers", "urls",
    "crosswalks", "terminology", "sign_off",
}
REQUIRED_FACT_SHEET_KEYS = {"skill_slug", "framework", "version", "retrieval_date"}
PLACEHOLDER = re.compile(r"<[^>]+>")


def extract_yaml_block(text: str) -> str | None:
    """Return the first ```yaml fence after the '## 0.' heading, if any."""
    m = re.search(r"^## 0\..*?```yaml\n(.*?)\n```", text, re.DOTALL | re.MULTILINE)
    return m.group(1) if m else None


def check_fact_sheet(path: Path) -> Tuple[int, List[str]]:
    msgs: List[str] = []
    fail = 0

    def err(msg: str) -> None:
        nonlocal fail
        fail = 1
        msgs.append(f"FAIL: {msg}")

    text = path.read_text(encoding="utf-8")

    # Numbered prose sections present
    present = {int(m) for m in re.findall(r"^## (\d+)\.", text, re.MULTILINE)}
    for n in REQUIRED_SECTIONS:
        if n not in present:
            err(f"missing section '## {n}.'")

    raw = extract_yaml_block(text)
    if raw is None:
        err("no ```yaml data block found under '## 0.'")
        return fail, msgs

    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        err(f"data block is not valid YAML: {e}")
        return fail, msgs
    if not isinstance(data, dict):
        err("data block must be a YAML mapping")
        return fail, msgs

    missing = REQUIRED_TOP_KEYS - data.keys()
    if missing:
        err(f"data block missing top-level keys: {sorted(missing)}")

    fs = data.get("fact_sheet") or {}
    if not isinstance(fs, dict):
        err("'fact_sheet' must be a mapping")
        fs = {}
    fs_missing = REQUIRED_FACT_SHEET_KEYS - fs.keys()
    if fs_missing:
        err(f"'fact_sheet' missing keys: {sorted(fs_missing)}")
    for k, v in fs.items():
        if isinstance(v, str) and PLACEHOLDER.search(v):
            err(f"fact_sheet.{k} still contains a template placeholder: {v!r}")

    counts = data.get("counts")
    if not isinstance(counts, dict) or not counts:
        err("'counts' must be a non-empty mapping")
    else:
        for k, v in counts.items():
            if not isinstance(v, int):
                err(f"counts.{k} must be an integer, got {v!r}")

    identifiers = data.get("identifiers")
    if not isinstance(identifiers, list) or not identifiers:
        err("'identifiers' must be a non-empty list")
    else:
        for i, row in enumerate(identifiers):
            if not isinstance(row, dict) or not {"code", "name"} <= row.keys():
                err(f"identifiers[{i}] must have 'code' and 'name'")
                continue
            if PLACEHOLDER.search(str(row["code"])):
                err(f"identifiers[{i}].code is a template placeholder: {row['code']!r}")

    urls = data.get("urls")
    if not isinstance(urls, list) or not urls:
        err("'urls' must be a non-empty list")
    else:
        for i, row in enumerate(urls):
            if not isinstance(row, dict) or not {"label", "url", "status", "checked"} <= row.keys():
                err(f"urls[{i}] must have 'label', 'url', 'status', 'checked'")
                continue
            if row["status"] != 200:
                err(f"urls[{i}] ({row['label']}): status must be 200, got {row['status']!r}")
            if PLACEHOLDER.search(str(row["url"])):
                err(f"urls[{i}].url is a template placeholder: {row['url']!r}")

    crosswalks = data.get("crosswalks")
    if crosswalks is None or not isinstance(crosswalks, list):
        err("'crosswalks' must be a list (empty allowed only if the skill encodes no crosswalks)")
    elif not crosswalks:
        msgs.append("WARN: 'crosswalks' is empty — confirm the skill encodes no crosswalk rows")

    terminology = data.get("terminology")
    if not isinstance(terminology, list) or not terminology:
        err("'terminology' must be a non-empty list")

    if data.get("sign_off") is not True:
        err("'sign_off' must be true (complete the §8 checklist first)")

    return fail, msgs


def main(argv: List[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    total_fail = 0
    for raw in argv:
        p = Path(raw)
        if not p.is_file():
            print(f"SKIP: {p} is not a file")
            continue
        code, msgs = check_fact_sheet(p)
        status = "PASS" if code == 0 else "FAIL"
        print(f"\n[{status}] {p}")
        for m in msgs:
            print(f"  - {m}")
        total_fail += code
    return 1 if total_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
