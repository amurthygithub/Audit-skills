#!/usr/bin/env python3
"""README / category-pointer sync gate (added 2026-06-11 after the M5-cycle-1
sweep found the root README's banner, CI line, quickstart, and one per-skill
test count all stale — per-PR updates had been partial).

Catches the count/listing drift class that the pointer-drift test (which checks
presence only) misses. Compares the README's CLAIMED numbers against reality:

  - every on-disk skill appears in the README skills table and the category
    pointer (body list + frontmatter description);
  - each skill's test-count cell in the README table == its actual collected
    test count;
  - the README banner / CI / quickstart repo-wide test count == actual repo-wide
    collected count.

Test counts are read via `pytest --collect-only` (the same collection CI runs).
Run standalone, or via tests/test_readme_sync.py in CI.

Usage: python3 tools/check_readme_sync.py
Exit 0 if in sync; 1 otherwise (prints every mismatch).
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
README = REPO / "README.md"
POINTER = REPO / "skills" / "SKILL.md"


def on_disk_skills() -> list[str]:
    return sorted(p.parent.name for p in (REPO / "skills").glob("*/SKILL.md")
                  if p.parent.name != "TEMPLATE")


def collected_count(target: str) -> int:
    """Run pytest --collect-only and return the test count for a path."""
    out = subprocess.run(
        [sys.executable, "-m", "pytest", target, "--collect-only", "-q", "-p", "no:asyncio"],
        cwd=str(REPO), capture_output=True, text=True)
    m = re.search(r"(\d+) tests? collected", out.stdout)
    if not m:
        # fall back to the last "N test" token (older pytest phrasing)
        m = re.search(r"(\d+) test", out.stdout.splitlines()[-1] if out.stdout else "")
    return int(m.group(1)) if m else -1


def readme_table_counts(text: str) -> dict[str, int]:
    """Map skill slug -> claimed test count from the README skills table."""
    counts = {}
    for m in re.finditer(r"\[([a-z0-9-]+)\]\(skills/\1/README\.md\)\*{0,2}\s*\|[^|]*\|\s*(\d+)\s*\|", text):
        counts[m.group(1)] = int(m.group(2))
    return counts


def readme_repo_total(text: str) -> int | None:
    m = re.search(r"\*\*(\d+) tests repo-wide", text)
    return int(m.group(1)) if m else None


def main() -> int:
    fails: list[str] = []
    skills = on_disk_skills()
    readme = README.read_text(encoding="utf-8")
    pointer = POINTER.read_text(encoding="utf-8")

    # 1. Every skill listed in README table + pointer body + pointer description
    table = readme_table_counts(readme)
    for s in skills:
        if s not in table:
            fails.append(f"README skills table missing '{s}'")
        if f"**{s}**" not in pointer:
            fails.append(f"category pointer body missing '{s}'")
    # pointer description must name PCI/HIPAA/etc. — require each slug's distinctive
    # token to appear in the frontmatter description line
    desc = re.search(r'description:\s*"(.*?)"', pointer, re.DOTALL)
    desc_text = desc.group(1) if desc else ""
    DESC_TOKENS = {  # slug -> a token that must appear in the description
        "pci-dss-assessment": "PCI", "hipaa-security-rule": "HIPAA",
        "nist-csf-2": "CSF", "nist-800-53-rmf": "800-53",
        "aicpa-soc-reporting": "SOC", "coso-internal-controls": "COSO",
        "isaca-audit-methodology": "ISACA", "audit-workpapers": "Workpapers",
    }
    for s in skills:
        tok = DESC_TOKENS.get(s)
        if tok and tok not in desc_text:
            fails.append(f"category pointer DESCRIPTION omits {s} (token '{tok}')")

    # 2. Per-skill test-count cells == actual collected
    for s in skills:
        actual = collected_count(f"skills/{s}/tests/")
        claimed = table.get(s)
        if claimed is not None and claimed != actual:
            fails.append(f"README test count for {s}: claims {claimed}, actual {actual}")

    # 3. Repo-wide total
    repo_actual = collected_count("skills/ tests/".split()[0]) if False else None
    out = subprocess.run(
        [sys.executable, "-m", "pytest", "skills/", "tests/", "--collect-only", "-q", "-p", "no:asyncio"],
        cwd=str(REPO), capture_output=True, text=True)
    m = re.search(r"(\d+) tests? collected", out.stdout)
    repo_actual = int(m.group(1)) if m else -1
    claimed_total = readme_repo_total(readme)
    if claimed_total is not None and claimed_total != repo_actual:
        fails.append(f"README banner repo-wide total: claims {claimed_total}, actual {repo_actual}")
    # CI line + quickstart echo the same number
    for label, pat in [("CI line", r"pytest skills/ tests/ -q\` \((\d+) tests\)"),
                       ("quickstart", r"(\d+) passed across all (\d+) skills")]:
        mm = re.search(pat, readme)
        if mm and int(mm.group(1)) != repo_actual:
            fails.append(f"README {label}: claims {mm.group(1)}, actual {repo_actual}")
        if label == "quickstart" and mm and int(mm.group(2)) != len(skills):
            fails.append(f"README quickstart skill count: claims {mm.group(2)}, actual {len(skills)}")

    if fails:
        print(f"[FAIL] README/pointer sync — {len(fails)} drift item(s):")
        for f in fails:
            print(f"  - {f}")
        return 1
    print(f"[PASS] README/pointer in sync ({len(skills)} skills, {repo_actual} tests)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
