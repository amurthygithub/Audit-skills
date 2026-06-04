"""Metamorphic tests for audit-workpapers.

Mutation-based: change the input in a known way, verify the output changes
accordingly. Tests invariants of the skill rather than exact outputs.
"""

from __future__ import annotations

import json
from pathlib import Path

from audit_workpapers_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_sample_size_vs_tm():
    """Metamorphic: halving TM doubles sample size (inverse relationship)."""
    payload = _load("uc-01-input.json")
    base = run_skill("UC-01", payload)
    base_n = base["mus_evaluation"]["sample_size"]

    mutated = dict(payload)
    mutated["tolerable_misstatement"] = 250000
    new = run_skill("UC-01", mutated)
    new_n = new["mus_evaluation"]["sample_size"]

    assert new_n == base_n * 2, f"Halving TM should double sample size: {base_n} -> {new_n}"


def test_uc_01_population_book_value_vs_sample_size():
    """Metamorphic: doubling BV doubles sample size (linear relationship)."""
    payload = _load("uc-01-input.json")
    base = run_skill("UC-01", payload)
    base_n = base["mus_evaluation"]["sample_size"]

    mutated = dict(payload)
    mutated["population_book_value"] = 25000000
    new = run_skill("UC-01", mutated)
    new_n = new["mus_evaluation"]["sample_size"]

    assert new_n == base_n * 2, f"Doubling BV should double sample size: {base_n} -> {new_n}"


def test_uc_02_finding_severity_identity():
    """Metamorphic: same finding always produces same severity classification."""
    payload = _load("uc-02-input.json")
    out1 = run_skill("UC-02", payload)
    out2 = run_skill("UC-02", payload)
    assert out1["classification"] == out2["classification"]
    assert out1["finding"]["severity"] == out2["finding"]["severity"]


def test_uc_03_td_invariant():
    """Metamorphic: if any risk factor increases, TD decreases (more reliance on procedures)."""
    payload = _load("uc-03-input.json")
    base = run_skill("UC-03", payload)
    base_td = base["td_calculation"]["td_pct"]

    mutated = dict(payload)
    mutated["ir"] = "90%"
    new = run_skill("UC-03", mutated)
    new_td = new["td_calculation"]["td_pct"]
    assert new_td < base_td, f"Higher IR means lower TD: {base_td} -> {new_td}"


def test_uc_03_ar_lower_tightens_td():
    """Metamorphic: lower acceptable AR means tighter TD (lower value)."""
    payload = _load("uc-03-input.json")
    base = run_skill("UC-03", payload)
    base_td = base["td_calculation"]["td_pct"]

    mutated = dict(payload)
    mutated["ar"] = "1%"
    new = run_skill("UC-03", mutated)
    new_td = new["td_calculation"]["td_pct"]
    assert new_td < base_td, f"Lower AR should tighten TD: {base_td} -> {new_td}"


def test_uc_03_td_range():
    """TD must be in (0, 100] for reasonable inputs."""
    test_cases = [
        {"ar": "5%", "ir": "80%", "cr": "60%", "ap": "50%"},
        {"ar": "1%", "ir": "50%", "cr": "30%", "ap": "20%"},
        {"ar": "10%", "ir": "50%", "cr": "50%", "ap": "50%"},
    ]
    for tc in test_cases:
        out = run_skill("UC-03", tc)
        td = out["td_calculation"]["td_pct"]
        assert 0 < td <= 100, f"TD out of range: {td} for {tc}"
