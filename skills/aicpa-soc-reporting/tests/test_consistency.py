"""AICPA SOC Reporting — cross-document consistency checks.

Wraps the shared tests/test_consistency_lib.py against this skill.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

SKILL_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(SKILL_ROOT.parent.parent / "tests"))
from test_consistency_lib import (  # noqa: E402
    test_chunk_frontmatter_schema as _test_chunk_frontmatter_schema,
    test_cross_skill_references_resolve as _test_cross_skill_references_resolve,
    test_industry_index_sync as _test_industry_index_sync,
    test_manifest_bidirectional as _test_manifest_bidirectional,
    test_routing_table_bidirectional as _test_routing_table_bidirectional,
    test_use_case_index_sync as _test_use_case_index_sync,
)


@pytest.fixture
def skill_dir() -> Path:
    return SKILL_ROOT


def test_routing_table_bidirectional(skill_dir):
    _test_routing_table_bidirectional(skill_dir)


def test_chunk_frontmatter_schema(skill_dir):
    _test_chunk_frontmatter_schema(skill_dir)


def test_manifest_bidirectional(skill_dir):
    _test_manifest_bidirectional(skill_dir)


def test_cross_skill_references_resolve(skill_dir):
    _test_cross_skill_references_resolve(skill_dir)


def test_industry_index_sync(skill_dir):
    _test_industry_index_sync(skill_dir)


def test_use_case_index_sync(skill_dir):
    _test_use_case_index_sync(skill_dir)
