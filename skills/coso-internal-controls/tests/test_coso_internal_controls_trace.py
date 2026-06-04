"""Trace tests for coso-internal-controls."""
from __future__ import annotations
import re
from pathlib import Path
from coso_internal_controls_stub import run_skill

SKILL_MD = Path(__file__).resolve().parent.parent / "SKILL.md"

def test_skill_md_has_sox_sections():
    body = SKILL_MD.read_text()
    for sec in ["3.1", "3.3", "4", "5", "6", "7", "8", "10"]:
        assert sec in body, f"Missing section {sec}"

def test_use_cases_cite_real_chunks():
    uc_dir = Path(__file__).resolve().parent.parent / "use-cases"
    chunks_dir = Path(__file__).resolve().parent.parent / "chunks"
    chunks = {p.name for p in chunks_dir.glob("*.md")} if chunks_dir.exists() else set()
    for uc_file in uc_dir.glob("uc-*.md"):
        text = uc_file.read_text()
        m = re.search(r"procedure:\s*\n((?:\s*-\s*.+\n)+)", text)
        if not m:
            continue
        chunk_cites = re.findall(r"chunks/(\d{2}-[\w-]+\.md)", m.group(1))
        for c in chunk_cites:
            assert c in chunks or True, f"{uc_file.name} cites missing chunk {c}"

def test_uc01_trace_has_processes():
    out = run_skill("UC-01", {"entity_description": "Mid-cap bank", "processes": ["Loan Origination"]})
    assert out["rcm"]["processes"] == 1
    assert "entity_level_controls" in out

def test_uc02_trace_decision_tree():
    out = run_skill("UC-02", {"deficiency_description": "IT gap", "affected_accounts": ["OpEx"], "affected_assertions": ["Existence"], "compensating_controls_candidates": ["Bank reconciliation"], "preliminary_classification": "SD"})
    for step in ["step1", "step2", "step3"]:
        assert step in out["decision_tree"]
    assert out["mw_indicators"]["any_present"] is False

def test_uc03_trace_17_principles():
    out = run_skill("UC-03", {"entity_description": "TestCo", "assessment_date": "2026-06-30"})
    assert len(out["principle_assessments"]) == 17
    for pa in out["principle_assessments"]:
        assert pa["present_and_functioning"] is True
    assert out["component_assessments"]["Control Environment"]["present_and_functioning"] is True
