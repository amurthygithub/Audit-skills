"""Cross-document consistency checks, parametrized over every on-Spine skill (SOX-634).

Replaces the six per-skill test_<slug>_consistency.py wrapper files with one
parametrized module. Skills are auto-discovered from skills/*/SKILL.md, so a
new skill is covered the moment it lands on disk.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from test_consistency_lib import (
    test_chunk_frontmatter_schema as _chunk_frontmatter_schema,
    test_cross_skill_references_resolve as _cross_skill_references_resolve,
    test_industry_index_sync as _industry_index_sync,
    test_manifest_bidirectional as _manifest_bidirectional,
    test_routing_table_bidirectional as _routing_table_bidirectional,
    test_use_case_index_sync as _use_case_index_sync,
)

REPO = Path(__file__).resolve().parent.parent
SKILLS = sorted(
    p.parent for p in (REPO / "skills").glob("*/SKILL.md") if p.parent.name != "TEMPLATE"
)
SKILL_IDS = [s.name for s in SKILLS]

CHECKS = {
    "routing_table_bidirectional": _routing_table_bidirectional,
    "chunk_frontmatter_schema": _chunk_frontmatter_schema,
    "manifest_bidirectional": _manifest_bidirectional,
    "cross_skill_references_resolve": _cross_skill_references_resolve,
    "industry_index_sync": _industry_index_sync,
    "use_case_index_sync": _use_case_index_sync,
}


@pytest.mark.parametrize("skill_dir", SKILLS, ids=SKILL_IDS)
@pytest.mark.parametrize("check", CHECKS.values(), ids=CHECKS.keys())
def test_consistency(check, skill_dir: Path):
    check(skill_dir)
