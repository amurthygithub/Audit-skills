"""Metamorphic tests for aicpa-soc-reporting.

Mutation-based: change the input in a known way, verify the output changes
accordingly. Tests invariants of the skill rather than exact outputs.
"""

from __future__ import annotations

import json
from pathlib import Path

from skill_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_tsc_criteria_count_invariant():
    """Adding Privacy category increases criteria count by exactly 8."""
    payload = _load("uc-01-input.json")
    base = run_skill("UC-01", payload)
    base_count = base["engagement"]["criteria_count"]

    payload["tsc_categories"].append("Privacy")
    new = run_skill("UC-01", payload)

    assert new["engagement"]["criteria_count"] == base_count + 8
    assert new["engagement"]["tsc_categories"] == [
        "Security", "Availability", "Confidentiality", "Privacy",
    ]


def test_uc_02_subservice_count_invariance():
    """Changing carrier method does not change subservice count (3 orgs)."""
    payload = _load("uc-02-input.json")
    base = run_skill("UC-02", payload)
    assert len(base["subservice_organizations"]) == 3

    payload["method"] = "inclusive"
    new = run_skill("UC-02", payload)
    assert len(new["subservice_organizations"]) == 3
    assert sum(len(org["csocs"]) for org in new["subservice_organizations"]) == 6


def test_uc_03_gap_period_extension():
    """Extending the gap period by 3 months changes gap_period string but keeps
    4 attestations intact."""
    payload = _load("uc-03-input.json")
    base = run_skill("UC-03", payload)
    base_attestations = len(base["bridge_letter"]["attestations"])

    payload["gap_period"]["end"] = "2026-09-30"
    new = run_skill("UC-03", payload)

    assert new["bridge_letter"]["gap_period"] == "2026-01-01 to 2026-09-30"
    assert len(new["bridge_letter"]["attestations"]) == base_attestations
    assert new["bridge_letter"]["attestations"] == base["bridge_letter"]["attestations"]


def test_uc_04_gap_reduction():
    """Closing one gap reduces gap count by 1 and leaves total count unchanged."""
    payload = _load("uc-04-input.json")
    base = run_skill("UC-04", payload)
    base_gaps = base["gap_analysis"]["gaps_identified"]
    base_total = base["gap_analysis"]["total_controls"]

    for ctrl in payload["control_inventory"]:
        if ctrl["id"] == "CTRL-006":
            ctrl["gap"] = False
            break

    new = run_skill("UC-04", payload)
    assert new["gap_analysis"]["gaps_identified"] == base_gaps - 1
    assert new["gap_analysis"]["total_controls"] == base_total
    assert len(new["remediation_plan"]) == base_gaps - 1


def test_uc_01_add_findings_changes_opinion():
    """UC-01: 3+ exceptions -> Qualified opinion; 0 exceptions -> Unqualified."""
    payload = _load("uc-01-input.json")
    base = run_skill("UC-01", payload)
    assert base["opinion"]["type"] == "Unqualified"

    payload["findings"] = [
        {"exception": True, "severity": "high", "criterion": "CC6.1"},
        {"exception": True, "severity": "moderate", "criterion": "CC7.1"},
        {"exception": True, "severity": "moderate", "criterion": "CC8.1"},
    ]
    new = run_skill("UC-01", payload)
    assert new["opinion"]["type"] == "Qualified"
