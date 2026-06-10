#!/usr/bin/env python3
"""G2 gate — design-doc section checker (SOX-632).

Validates that a skill design doc (docs/<slug>-design.md) contains every
numbered section the template (docs/skill-design-template.md) requires.
Required section numbers are derived from the template at run time, so the
checker never drifts from the template. Exits non-zero on any failure.

Usage:
    python tools/check_design_doc.py docs/<slug>-design.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List, Tuple

TEMPLATE = Path(__file__).resolve().parent.parent / "docs" / "skill-design-template.md"
SECTION_RE = re.compile(r"^## (\d+)\.\s*(.*)$", re.MULTILINE)
MIN_LINES = 200  # a filled design doc is substantial; the CSF 2.0 example is 1,391 lines


def numbered_sections(text: str) -> dict:
    return {int(n): title.strip() for n, title in SECTION_RE.findall(text)}


def check_design_doc(path: Path, template: Path = TEMPLATE) -> Tuple[int, List[str]]:
    msgs: List[str] = []
    fail = 0

    def err(msg: str) -> None:
        nonlocal fail
        fail = 1
        msgs.append(f"FAIL: {msg}")

    if not template.is_file():
        err(f"template not found at {template}")
        return fail, msgs

    required = numbered_sections(template.read_text(encoding="utf-8"))
    text = path.read_text(encoding="utf-8")
    present = numbered_sections(text)

    for n, title in sorted(required.items()):
        if n not in present:
            err(f"missing section '## {n}.' (template: {title})")

    n_lines = text.count("\n") + 1
    if n_lines < MIN_LINES:
        err(f"design doc is {n_lines} lines; a filled doc is at least {MIN_LINES} "
            f"(the template is a checklist, not a form to leave blank)")

    if re.search(r"^# Skill Design Template", text, re.MULTILINE):
        err("doc still carries the template's own title — replace with the skill's design title")

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
        code, msgs = check_design_doc(p)
        status = "PASS" if code == 0 else "FAIL"
        print(f"\n[{status}] {p}")
        for m in msgs:
            print(f"  - {m}")
        total_fail += code
    return 1 if total_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
