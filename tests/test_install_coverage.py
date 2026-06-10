"""install.sh coverage test (SOX-635).

The previous install.sh hardcoded 4 of 6 skills and copied only the SKILL.md
routers. The rewrite auto-discovers skills; this test is the ratchet that
keeps it honest: run the real script into a temp dir and assert every
on-Spine skill lands as a full package.
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILLS = sorted(
    p.parent.name for p in (REPO / "skills").glob("*/SKILL.md") if p.parent.name != "TEMPLATE"
)


def test_install_sh_installs_every_skill_as_full_package(tmp_path):
    env = {**os.environ, "AUDIT_SKILLS_INSTALL_DIR": str(tmp_path)}
    result = subprocess.run(
        ["bash", str(REPO / "install.sh")],
        capture_output=True, text=True, env=env,
    )
    assert result.returncode == 0, f"install.sh failed:\n{result.stdout}\n{result.stderr}"

    assert (tmp_path / "SKILL.md").is_file(), "category-pointer router not installed"

    for name in SKILLS:
        skill = tmp_path / name
        assert (skill / "SKILL.md").is_file(), f"{name}: SKILL.md missing"
        chunks = list((skill / "chunks").glob("*.md"))
        assert chunks, f"{name}: chunks/ missing or empty — install copies full packages, not just routers"
        assert (skill / "use-cases").is_dir(), f"{name}: use-cases/ missing"
        assert not (skill / "tests").exists(), f"{name}: tests/ should be excluded from installs"


def test_install_sh_has_no_hardcoded_skill_list():
    text = (REPO / "install.sh").read_text(encoding="utf-8")
    for name in SKILLS:
        assert f'"{name}"' not in text and f"/{name}/SKILL.md" not in text, (
            f"install.sh hardcodes '{name}' — it must auto-discover skills/*/SKILL.md"
        )
