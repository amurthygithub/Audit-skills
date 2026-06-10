"""Repo-root conftest for pytest.

Every skill ships a ``<slug>_stub.py`` (deterministic reference executor)
and a ``telemetry/`` package at the skill root, plus a ``tests/`` directory
of ``test_<slug>_*`` files. Pytest's default ``import_mode=prepend`` puts
the test file's parent dir (``skills/<x>/tests/``) on ``sys.path`` — not
the skill root — so unqualified imports of either ``<slug>_stub`` or
``telemetry.instrument`` fail with ``ModuleNotFoundError``.

This conftest prepends every on-Spine skill root to ``sys.path`` once at
session start, so both imports resolve to the correct skill.

This module sets ``__test__ = False`` so pytest does not try to collect
it as a test module.
"""
from __future__ import annotations

import sys
from pathlib import Path

__test__ = False  # not a test module — see module docstring

def _discover_skills(repo_root: Path):
    """On-Spine skills, auto-discovered so the list can never go stale."""
    return sorted(
        p.parent
        for p in (repo_root / "skills").glob("*/SKILL.md")
        if p.parent.name != "TEMPLATE"
    )


def pytest_configure(config):  # noqa: ARG001 — pytest hook signature
    repo_root = Path(__file__).resolve().parent
    for skill_root in _discover_skills(repo_root):
        path = str(skill_root)
        if path not in sys.path:
            sys.path.insert(0, path)
