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

SKILLS = (
    "nist-800-53-rmf",
    "isaca-audit-methodology",
    "coso-internal-controls",
    "aicpa-soc-reporting",
    "audit-workpapers",
)


def pytest_configure(config):  # noqa: ARG001 — pytest hook signature
    repo_root = Path(__file__).resolve().parent
    for skill in SKILLS:
        skill_root = repo_root / "skills" / skill
        if not skill_root.is_dir():
            continue
        path = str(skill_root)
        if path not in sys.path:
            sys.path.insert(0, path)
