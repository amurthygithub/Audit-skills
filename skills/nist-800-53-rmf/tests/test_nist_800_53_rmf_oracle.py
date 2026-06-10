"""Oracle tests for nist-800-53-rmf.

Each test loads the seed input, runs the skill (via skill_stub), and asserts
that the output matches the expected fixture per the UC's oracle field.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from nist_800_53_rmf_stub import run_skill

DATA = Path(__file__).resolve().parent.parent / "data" / "seeds"


def _load(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def test_uc_01_oracle():
    """UC-01: FIPS 199 categorization = MODERATE, baseline = MODERATE, inheritance correct."""
    payload = _load("uc-01-input.json")
    expected = _load("uc-01-expected.json")
    out = run_skill("UC-01", payload)

    # Oracle assertions per UC-01 frontmatter
    assert out["fips_199_categorization"]["overall"] == "MODERATE"
    assert out["baseline"]["baseline"] == "MODERATE"
    assert out["fips_199_categorization"]["system_security_category"] == {
        "c": "MODERATE", "i": "MODERATE", "a": "LOW"
    }
    # Sanity: expected fixture has the same overall
    assert expected["fips_199_categorization"]["overall"] == "MODERATE"
    assert expected["baseline"]["baseline"] == "MODERATE"


def test_uc_02_oracle():
    """UC-02: SAR 22 findings, ATO with conditions, residual risk = MODERATE."""
    payload = _load("uc-02-input.json")
    findings = _load("uc-02-findings.json")
    payload["findings"] = findings
    expected = _load("uc-02-expected.json")
    out = run_skill("UC-02", payload)

    # Oracle assertions per UC-02 frontmatter
    assert out["sar"]["total_findings"] == 22
    assert out["ato_decision"]["decision"] == "AUTHORIZE_WITH_CONDITIONS"
    assert out["ato_decision"]["residual_risk"] == "MODERATE"
    # Severity distribution sums to 22
    assert sum(out["sar"]["severity_distribution"].values()) == 22
    # Sanity vs expected
    assert expected["ato_decision"]["decision"] == "AUTHORIZE_WITH_CONDITIONS"


def test_uc_03_oracle():
    """UC-03 (SOX-637, non-circular): the stub's summary must be DERIVABLE from the
    shipped crosswalk + gap register — this test recomputes everything independently
    from the seed files and asserts the stub agrees, plus footing invariants."""
    payload = _load("uc-03-input.json")
    crosswalk = json.loads((DATA.parent / "crosswalks" / "soc2-to-800-53-mod.json").read_text())
    gap_register = _load("uc-03-gap-list.json")
    payload["crosswalk"] = crosswalk
    payload["gap_register"] = gap_register
    out = run_skill("UC-03", payload)

    # Independent recomputation from the seeds (not via the stub)
    mapped_ids = set()
    for m in crosswalk["mappings"]:
        for c in m["nist_800_53_id"].split(","):
            if c.strip():
                mapped_ids.add(c.strip())
    pure = [g for g in gap_register if g["disposition"] == "gap"]
    strengthen = [g for g in gap_register if g["disposition"] == "strengthen"]

    cs = out["crosswalk_summary"]
    gs = out["gap_register_summary"]
    assert cs["soc2_common_criteria"] == 9
    assert cs["sample_mappings"] == len(crosswalk["mappings"])
    assert cs["unique_mapped_control_ids"] == len(mapped_ids)
    # No overlap percentage may be emitted — it is not derivable from a sample
    assert "overlap_pct" not in cs and "mapped_controls" not in cs
    # Footing invariants
    assert gs["total_records"] == len(gap_register)
    assert gs["pure_gaps"] + gs["strengthen_partial_coverage"] == gs["total_records"]
    assert gs["pure_gaps"] == len(pure) and gs["strengthen_partial_coverage"] == len(strengthen)
    assert sum(gs["by_priority"].values()) == gs["total_records"]
    # One disposition per control: every 'gap' record is unmapped; every 'strengthen' is mapped
    assert all(g["control_id"] not in mapped_ids for g in pure)
    assert all(g["control_id"] in mapped_ids for g in strengthen)
    assert out["baseline"]["baseline"] == "MODERATE"
    # Expected-output seed must foot to the same computed values
    expected = _load("uc-03-expected.json")
    assert expected["gap_register_summary"]["total_records"] == gs["total_records"]
    assert expected["crosswalk_summary"]["unique_mapped_control_ids"] == cs["unique_mapped_control_ids"]


@pytest.mark.parametrize("uc_id,expected_overall", [
    ("UC-01", "MODERATE"),
])
def test_uc_01_categorization_pattern(uc_id, expected_overall):
    """Verify the categorization pattern: high-water mark across C/I/A."""
    payload = _load("uc-01-input.json")
    out = run_skill(uc_id, payload)
    cia = out["fips_199_categorization"]["system_security_category"]
    overall = max(cia.values(), key=lambda x: ["LOW", "MODERATE", "HIGH"].index(x))
    assert overall == expected_overall
