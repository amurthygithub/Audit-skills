"""Adversarial tests for aicpa-soc-reporting.

Edge-case inputs that test the skill's robustness. Each test corresponds to a
variation documented in the use case file.
"""

from __future__ import annotations

import json
from pathlib import Path

from aicpa_soc_reporting_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_empty_findings_still_unqualified():
    """UC-01: Empty findings or missing findings key should still produce Unqualified."""
    payload = _load("uc-01-input.json")
    payload.pop("findings", None)
    out = run_skill("UC-01", payload)
    assert out["opinion"]["type"] == "Unqualified"


def test_uc_02_method_switch_carve_out_to_inclusive():
    """UC-02: Switching method from carve-out to inclusive retains subservice org count and CSOC count."""
    payload = _load("uc-02-input.json")
    payload["method"] = "inclusive"
    out = run_skill("UC-02", payload)
    assert out["method"] == "inclusive"
    assert len(out["subservice_organizations"]) == 3
    assert sum(len(org["csocs"]) for org in out["subservice_organizations"]) == 6


def test_uc_04_all_controls_mapped_no_gaps():
    """UC-04: When all controls are mapped and have no gaps, readiness is 'ready'."""
    payload = _load("uc-04-input.json")
    for ctrl in payload["control_inventory"]:
        ctrl["gap"] = False
    out = run_skill("UC-04", payload)
    assert out["evidence_readiness"]["status"] == "ready"
