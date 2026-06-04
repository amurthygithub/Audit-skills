"""Trace tests for isaca-audit-methodology.

Verifies that skill output references the right section of SKILL.md or chunks/ for each
decision, so the audit trail is intact.
"""

from __future__ import annotations
import json, re
from pathlib import Path

NL = chr(10)

SKILL_MD = Path(__file__).resolve().parent.parent / "SKILL.md"
DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


EXPECTED_SECTIONS = {
    "UC-01": ["2", "3.2", "5", "6", "10"],
    "UC-02": ["3.4", "3.6", "4", "5", "6"],
    "UC-03": ["2", "3.2", "4", "5", "10"],
}


def test_skill_md_referenced_sections_exist():
    body = SKILL_MD.read_text()
    for uc, sections in EXPECTED_SECTIONS.items():
        for sec in sections:
            assert sec in body, f"UC {uc} references section {sec} but not found"


def test_use_cases_cite_skill_sections():
    uc_dir = Path(__file__).resolve().parent.parent / "use-cases"
    body = SKILL_MD.read_text()
    chunks_dir = Path(__file__).resolve().parent.parent / "chunks"
    chunks = {p.name for p in chunks_dir.glob("*.md")} if chunks_dir.exists() else set()
    for uc_file in uc_dir.glob("uc-*.md"):
        text = uc_file.read_text()
        m = re.search("procedure:" + r"\s*" + NL + "((?:\s*-\s*.+" + NL + ")+)", text)
        assert m, f"{uc_file.name} has no procedure field"
        procedure_block = m.group(1)
        chunk_cites = re.findall(r"chunks/(\d{2}-[\w-]+\.md)", procedure_block)
        for c in chunk_cites:
            assert c in chunks, f"{uc_file.name} cites chunks/{c} but file does not exist"


def test_uc_01_stub_output_traceable():
    from skill_stub import run_skill
    payload = _load("uc-01-input.json")
    out = run_skill("UC-01", payload)
    assessment = out.get("maturity_assessment", {})
    assert "processes" in assessment
    for proc in assessment["processes"]:
        assert "id" in proc
        assert "current_maturity" in proc
        assert "target_maturity" in proc
        assert "gap" in proc
        assert proc["gap"] >= 0


def test_uc_02_stub_output_traceable():
    from skill_stub import run_skill
    payload = _load("uc-02-input.json")
    out = run_skill("UC-02", payload)
    obs = out.get("observation", {})
    for field in ("id", "title", "severity", "condition", "criteria", "cause", "effect", "recommendations"):
        assert field in obs, f"UC-02 observation missing field: {field}"
    assert len(obs["recommendations"]) >= 2


def test_uc_03_stub_output_traceable():
    from skill_stub import run_skill
    payload = _load("uc-03-input.json")
    out = run_skill("UC-03", payload)
    assessment = out.get("design_factor_assessment", {})
    for field in ("enterprise_strategy", "risk_profile", "prioritized_objectives"):
        assert field in assessment, f"UC-03 assessment missing field: {field}"
    priorities = [o["priority"] for o in assessment["prioritized_objectives"]]
    assert priorities == sorted(priorities)
