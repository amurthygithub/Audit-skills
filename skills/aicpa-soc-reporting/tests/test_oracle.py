"""Oracle tests for aicpa-soc-reporting.

Each test loads the seed input, runs the skill (via skill_stub), and asserts
that the output matches the expected fixture per the UC frontmatter oracle field.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from aicpa_soc_reporting_stub import run_skill

SKILL = Path(__file__).resolve().parent.parent
SEEDS = SKILL / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((SEEDS / name).read_text())


def test_uc_01_oracle():
    """UC-01: SOC 2 Type II = 38 criteria, Unqualified opinion, 4 CUECs, AWS carve-out."""
    payload = _load("uc-01-input.json")
    out = run_skill("UC-01", payload)
    assert out["classification"] == "SOC2-TypeII-38"
    assert out["engagement"]["criteria_count"] == 38
    assert out["engagement"]["opinion"] == "Unqualified"
    assert len(out["cuecs"]) >= 4
    assert len(out["subservice"]["csocs"]) == 3
    assert out["subservice"]["method"] == "carve-out"
    assert out["opinion"]["type"] == "Unqualified"


def test_uc_02_oracle():
    """UC-02: 3 subservice orgs, 5 CUECs, carve-out method."""
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)
    assert len(out["subservice_organizations"]) == 3
    assert len(out["cuecs"]) == 5
    assert out["method"] == "carve-out"
    assert "carve-out" in out["method_rationale"].lower()
    assert out["subservice_organizations"][0]["name"] == "AWS"
    assert out["classification"].startswith("CUEC-CSOC-")


def test_uc_03_oracle():
    """UC-03: Bridge letter with 4 attestations, gap period, disclaimer."""
    payload = _load("uc-03-input.json")
    out = run_skill("UC-03", payload)
    bl = out["bridge_letter"]
    assert bl["gap_period"] == "2026-01-01 to 2026-06-30"
    assert len(bl["attestations"]) == 4
    assert "management representation" in bl["disclaimer"]
    assert "2025-12-31" in bl["prior_report"]
    assert out["classification"] == "Bridge-Letter-4-Attestations"


def test_uc_04_oracle():
    """UC-04: Auditee preparation = gap analysis, remediation plan, CUEC draft."""
    payload = _load("uc-04-input.json")
    out = run_skill("UC-04", payload)
    assert out["gap_analysis"]["total_controls"] == 10
    assert out["gap_analysis"]["gaps_identified"] > 0
    assert len(out["cuec_draft"]) == 4
    assert len(out["subservice_organizations"]) == 1
    assert out["subservice_organizations"][0]["method"] == "carve-out"
    assert out["evidence_readiness"]["status"] == "incomplete"
    assert "Readiness-" in out["classification"]


def test_all_ucs_referenced_in_index():
    index_path = SKILL / "use-cases" / "_index.md"
    content = index_path.read_text()
    for uc_id in ["UC-01", "UC-02", "UC-03", "UC-04"]:
        assert uc_id in content, f"{uc_id} not found in use-cases/_index.md"
