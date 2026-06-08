"""Per-skill wrapper for the shared test_consistency_lib.

This file re-exposes the 6 consistency checks from
tests/test_consistency_lib.py for the nist-csf-2 skill. The shared
library expects a `skill_dir` fixture; this file provides it.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from test_consistency_lib import (
    test_routing_table_bidirectional,
    test_chunk_frontmatter_schema,
    test_manifest_bidirectional,
    test_cross_skill_references_resolve,
    test_industry_index_sync,
    test_use_case_index_sync,
)

SKILL_DIR = Path(__file__).resolve().parent.parent
SIBLINGS = (
    "nist-800-53-rmf",
    "isaca-audit-methodology",
    "coso-internal-controls",
    "aicpa-soc-reporting",
    "audit-workpapers",
)


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def siblings():
    return SIBLINGS


# Re-export the 6 shared tests with the fixtures injected
test_routing = test_routing_table_bidirectional
test_chunk_schema = test_chunk_frontmatter_schema
test_manifest = test_manifest_bidirectional
test_xref = test_cross_skill_references_resolve
test_industries = test_industry_index_sync
test_ucs = test_use_case_index_sync
