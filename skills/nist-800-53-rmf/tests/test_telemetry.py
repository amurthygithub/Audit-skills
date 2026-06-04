"""Telemetry tests for nist-800-53-rmf.

Verifies that the skill's instrumentation stub emits valid SkillInvocation
events and that the schema validates.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

import jsonschema
import pytest

SCHEMA = json.loads((Path(__file__).resolve().parent.parent / "telemetry" / "schema.json").read_text())


def test_schema_is_valid_json():
    """The schema itself must be valid JSON Schema."""
    jsonschema.Draft7Validator.check_schema(SCHEMA)


def test_schema_required_fields():
    """Schema requires all Spine-mandated fields."""
    required = SCHEMA["required"]
    for field in [
        "skill", "skill_version", "use_case_id", "industry", "model",
        "input_tokens", "output_tokens", "total_tokens", "latency_ms",
        "cache_hit", "classification", "oracle_result", "timestamp", "redaction_applied",
    ]:
        assert field in required, f"Schema missing required field: {field}"


def _full_event(**overrides):
    base = {
        "skill": "nist-800-53-rmf",
        "skill_version": "0.1.0",
        "use_case_id": "UC-01",
        "industry": "public-sector",
        "model": "gpt-4o",
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0,
        "latency_ms": 0,
        "cache_hit": False,
        "classification": "MODERATE",
        "oracle_result": "n/a",
        "timestamp": "2026-06-03T00:00:00+00:00",
        "redaction_applied": False,
    }
    base.update(overrides)
    return base


def test_skill_name_pattern():
    """skill field must be kebab-case."""
    inv = _full_event(skill="nist-800-53-rmf")
    jsonschema.validate(inv, SCHEMA)
    bad = _full_event(skill="NIST 800-53 RMF")
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, SCHEMA)


def test_use_case_id_pattern():
    inv = _full_event(use_case_id="UC-01")
    jsonschema.validate(inv, SCHEMA)
    bad = _full_event(use_case_id="uc-1")
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, SCHEMA)


def test_industry_enum():
    for ind in ["financial-services", "healthcare", "saas-technology", "public-sector", "other"]:
        inv = _full_event(industry=ind)
        jsonschema.validate(inv, SCHEMA)
    bad = _full_event(industry="banking")
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, SCHEMA)


def test_oracle_result_enum():
    for v in ["pass", "fail", "skipped", "n/a"]:
        inv = _full_event(oracle_result=v)
        jsonschema.validate(inv, SCHEMA)
    bad = _full_event(oracle_result="yes")
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(bad, SCHEMA)


def test_instrument_emits_event():
    """The instrumentation stub actually emits a SkillInvocation event."""
    with tempfile.TemporaryDirectory() as tmp:
        os.environ["SOXFLOW_TELEMETRY_PATH"] = str(Path(tmp) / "events.jsonl")
        # Import the instrumentation module from the template (telemetry stub)
        from telemetry.instrument import instrumented, SkillInvocation

        @instrumented(skill="nist-800-53-rmf", skill_version="0.1.0", default_use_case_id="UC-01", default_industry="public-sector")
        def fake_run(payload, **kwargs):
            return {"classification": "MODERATE", "input_tokens": 100, "output_tokens": 50}

        out = fake_run({"system_name": "Test"})
        assert out["classification"] == "MODERATE"

        events_file = Path(tmp) / "events.jsonl"
        assert events_file.exists()
        lines = events_file.read_text().strip().splitlines()
        assert len(lines) == 1
        event = json.loads(lines[0])
        jsonschema.validate(event, SCHEMA)
        assert event["skill"] == "nist-800-53-rmf"
        assert event["classification"] == "MODERATE"
        assert event["use_case_id"] == "UC-01"
