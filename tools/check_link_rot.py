#!/usr/bin/env python3
"""Check link rot for citation URLs in skill SKILL.md files.

Walks each skill's `## 10. References & Citation Manifest` table,
HEAD-checks every URL, diffs against a baseline, and emits a report.

Exits 0 if no new hard fails and overall failure rate <= 10%.
Exits 1 otherwise (CI failure).
"""
from __future__ import annotations

import concurrent.futures
import json
import re
import sys
import time
from pathlib import Path
from typing import Iterable

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
BASELINE_PATH = REPO_ROOT / "tools" / ".link_rot_baseline.json"
REPORT_PATH = REPO_ROOT / "link-rot-report.md"

USER_AGENT = "audit-skills-link-rot-checker/0.1"
TIMEOUT_SECONDS = 10
MAX_WORKERS = 10
HARD_FAIL_RATE_THRESHOLD = 0.10  # 10% overall


def find_skill_files() -> list[Path]:
    """Return every skills/*/SKILL.md that has a section-10 manifest."""
    out: list[Path] = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        text = skill_md.read_text(encoding="utf-8")
        if re.search(r"^##\s*10\.\s*References", text, re.MULTILINE):
            out.append(skill_md)
    return out


def extract_urls(skill_md: Path) -> list[tuple[str, str]]:
    """Return [(skill_slug, url), ...] from the section-10 manifest table.

    The manifest is a markdown pipe-table whose last column is the URL.
    We find the table that follows the `## 10.` heading, then take every
    pipe-separated row's last field that looks like an http(s) URL.
    """
    text = skill_md.read_text(encoding="utf-8")
    skill_slug = skill_md.parent.name
    match = re.search(
        r"^##\s*10\.\s*References.*?\n(.*?)(?=^##\s|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        return []
    section = match.group(1)
    urls: list[tuple[str, str]] = []
    for line in section.splitlines():
        if "|" not in line or set(line.strip()) <= {"|", "-", " ", ":"}:
            continue
        cells = [c.strip() for c in line.split("|")]
        # First and last cells are empty (leading/trailing pipe).
        for cell in reversed(cells):
            if re.match(r"^https?://", cell):
                urls.append((skill_slug, cell))
                break
    return urls


def check_url(url: str) -> tuple[str, str]:
    """HEAD-check a URL with redirects, return (url, status_label)."""
    try:
        resp = requests.head(
            url,
            allow_redirects=True,
            timeout=TIMEOUT_SECONDS,
            headers={"User-Agent": USER_AGENT},
        )
    except requests.RequestException as exc:
        return url, f"ERROR:{type(exc).__name__}"
    code = resp.status_code
    if 200 <= code < 300:
        return url, "OK"
    if 300 <= code < 400:
        return url, f"REDIRECT:{code}"
    if code in (404, 410):
        return url, f"HARD_FAIL:{code}"
    if 500 <= code < 600:
        return url, f"SOFT_FAIL:{code}"
    return url, f"OTHER:{code}"


def run_checks(urls: Iterable[str]) -> dict[str, str]:
    pairs: list[tuple[str, str]] = []
    url_list = list(urls)
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for url, status in pool.map(check_url, url_list):
            pairs.append((url, status))
    return dict(pairs)


def load_baseline() -> dict[str, str]:
    if BASELINE_PATH.exists():
        return json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    return {}


def is_hard(status: str) -> bool:
    return status.startswith("HARD_FAIL") or status.startswith("ERROR")


def is_soft(status: str) -> bool:
    return status.startswith("SOFT_FAIL") or status.startswith("REDIRECT") or status.startswith("OTHER")


def write_report(
    new_results: dict[str, str],
    baseline: dict[str, str],
    skill_url_map: dict[str, str],
) -> tuple[int, int, list[str]]:
    """Build markdown report, return (hard_failures, soft_failures, new_hard_fails)."""
    total = len(new_results)
    hard = [u for u, s in new_results.items() if is_hard(s)]
    soft = [u for u, s in new_results.items() if is_soft(s)]
    new_hard = [u for u, s in new_results.items() if is_hard(s) and not is_hard(baseline.get(u, "OK"))]

    lines: list[str] = []
    lines.append("# Link Rot Report")
    lines.append("")
    lines.append(f"- Generated: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
    lines.append(f"- Total URLs checked: {total}")
    lines.append(f"- Hard failures (404/410/timeout): {len(hard)}")
    lines.append(f"- Soft failures (5xx/redirect/other): {len(soft)}")
    lines.append(f"- **New hard failures (regressions): {len(new_hard)}**")
    lines.append("")

    if new_hard:
        lines.append("## New hard failures (action required)")
        lines.append("")
        lines.append("| Skill | URL | Status |")
        lines.append("|-------|-----|--------|")
        for u in new_hard:
            lines.append(f"| {skill_url_map.get(u, '?')} | {u} | {new_results[u]} |")
        lines.append("")

    if hard:
        lines.append("## All hard failures")
        lines.append("")
        lines.append("| Skill | URL | Status |")
        lines.append("|-------|-----|--------|")
        for u in hard:
            lines.append(f"| {skill_url_map.get(u, '?')} | {u} | {new_results[u]} |")
        lines.append("")

    if soft:
        lines.append("## Soft failures (tolerated up to 10% of total)")
        lines.append("")
        for u in soft:
            lines.append(f"- {skill_url_map.get(u, '?')}: {u} ({new_results[u]})")
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(hard), len(soft), new_hard


def main() -> int:
    skill_files = find_skill_files()
    if not skill_files:
        print("No SKILL.md with section-10 manifest found; nothing to check.")
        REPORT_PATH.write_text("# Link Rot Report\n\nNo URLs to check.\n", encoding="utf-8")
        return 0

    skill_url_map: dict[str, str] = {}
    for sf in skill_files:
        for skill, url in extract_urls(sf):
            skill_url_map[url] = skill

    urls = list(skill_url_map.keys())
    print(f"Checking {len(urls)} URLs across {len(skill_files)} skills...")

    results = run_checks(urls)
    baseline = load_baseline()

    hard, soft, new_hard = write_report(results, baseline, skill_url_map)

    # Save new baseline.
    BASELINE_PATH.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    total = len(results)
    fail_rate = (hard + soft) / total if total else 0.0

    print(f"Total: {total}, hard: {hard}, soft: {soft}, new_hard: {len(new_hard)}, fail_rate: {fail_rate:.1%}")
    print(f"Report: {REPORT_PATH}")

    if new_hard:
        print(f"FAIL: {len(new_hard)} new hard failure(s) since last run.")
        return 1
    if fail_rate > HARD_FAIL_RATE_THRESHOLD:
        print(f"FAIL: overall failure rate {fail_rate:.1%} exceeds {HARD_FAIL_RATE_THRESHOLD:.0%}.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
