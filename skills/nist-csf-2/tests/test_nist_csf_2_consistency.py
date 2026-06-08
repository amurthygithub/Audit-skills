"""nist-csf-2 — cross-document consistency checks.

Wraps the shared tests/test_consistency_lib.py against this skill.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

SKILL_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = SKILL_ROOT.parent.parent

sys.path.insert(0, str(REPO_ROOT / "tests"))
from test_consistency_lib import (  # noqa: E402
    test_chunk_frontmatter_schema as _test_chunk_frontmatter_schema,
    test_cross_skill_references_resolve as _test_cross_skill_references_resolve,
    test_industry_index_sync as _test_industry_index_sync,
    test_manifest_bidirectional as _test_manifest_bidirectional,
    test_routing_table_bidirectional as _test_routing_table_bidirectional,
    test_use_case_index_sync as _test_use_case_index_sync,
)

SIBLINGS = (
    "nist-800-53-rmf",
    "isaca-audit-methodology",
    "coso-internal-controls",
    "aicpa-soc-reporting",
    "audit-workpapers",
)


@pytest.fixture
def skill_dir():
    return SKILL_ROOT


@pytest.fixture
def siblings():
    return SIBLINGS


def test_routing(skill_dir):
    _test_routing_table_bidirectional(skill_dir)


def test_chunk_schema(skill_dir):
    _test_chunk_frontmatter_schema(skill_dir)


def test_manifest(skill_dir):
    _test_manifest_bidirectional(skill_dir)


def test_xref(skill_dir):
    _test_cross_skill_references_resolve(skill_dir)


def test_industries(skill_dir):
    _test_industry_index_sync(skill_dir)


def test_ucs(skill_dir):
    _test_use_case_index_sync(skill_dir)
