"""Sanity gate for repo-level skill listings (added after the 2026-06-10 pre-M4
sweep found skills/SKILL.md listing 4 of 7 skills with counts the vetting sweep
had corrected elsewhere — nothing covered files outside skill directories).

Rule: every on-Spine skill must be listed in the category pointer
(skills/SKILL.md) and in the root README's skills table; the pointer must not
name skills that don't exist on disk.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POINTER = REPO / "skills" / "SKILL.md"
README = REPO / "README.md"


def _on_disk_skills() -> set[str]:
    return {p.parent.name for p in (REPO / "skills").glob("*/SKILL.md")
            if p.parent.name != "TEMPLATE"}


def test_category_pointer_lists_every_skill():
    text = POINTER.read_text()
    missing = [s for s in sorted(_on_disk_skills()) if f"**{s}**" not in text]
    assert not missing, f"skills/SKILL.md missing skill(s): {missing}"


def test_category_pointer_names_only_real_skills():
    text = POINTER.read_text()
    named = set(re.findall(r"\*\*([a-z0-9][a-z0-9-]+)\*\*", text))
    phantom = sorted(named - _on_disk_skills())
    assert not phantom, f"skills/SKILL.md names non-existent skill(s): {phantom}"


def test_readme_skills_table_lists_every_skill():
    text = README.read_text()
    missing = [s for s in sorted(_on_disk_skills())
               if f"[{s}](skills/{s}/README.md)" not in text]
    assert not missing, f"README.md skills table missing skill(s): {missing}"
