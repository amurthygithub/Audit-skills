"""Repo-root conftest for pytest.

Each skill has its own ``skill_stub.py`` at the skill root (e.g.
``skills/nist-800-53-rmf/skill_stub.py``) and its own ``tests/`` directory.
Tests do ``from skill_stub import run_skill`` — unqualified — which means
pytest's default import resolution can't find the per-skill module without
help.

This conftest runs once per test session and prepends every on-Spine skill
root to ``sys.path`` so that the unqualified import resolves to the correct
skill's stub, not the first one Python happens to find on ``sys.path``.
"""
import sys
from pathlib import Path

SKILLS = [
    "nist-800-53-rmf",
    "isaca-audit-methodology",
    "coso-internal-controls",
    "aicpa-soc-reporting",
    "audit-workpapers",
]


def _ensure_skill_paths() -> None:
    repo_root = Path(__file__).resolve().parent
    for skill in SKILLS:
        skill_root = repo_root / "skills" / skill
        if skill_root.is_dir():
            path = str(skill_root)
            if path not in sys.path:
                sys.path.insert(0, path)


_ensure_skill_paths()
