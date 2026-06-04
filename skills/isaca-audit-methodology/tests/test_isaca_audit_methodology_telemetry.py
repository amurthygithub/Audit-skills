"""Telemetry tests for isaca-audit-methodology.

Verifies that the skill instrumentation stub emits valid SkillInvocation
events and that the schema validates.
"""

from __future__ import annotations
import json, os, tempfile
from pathlib import Path
import jsonschema, pytest

SCHEMA = json.loads((Path(__file__).resolve().parent.parent / "telemetry" / "schema.json").read_text())

def test_schema_is_valid_json():
    jsonschema.Draft7Validator.check_schema(SCHEMA)

def test_schema_required_fields():
    for field in ["skill","skill_version","use_case_id","industry","model","input_tokens","output_tokens","total_tokens","latency_ms","cache_hit","classification","oracle_result","timestamp","redaction_applied"]:
        assert field in SCHEMA["required"], f"Missing: {field}"

def _full_event(**overrides):
    base = {"skill":"isaca-audit-methodology","skill_version":"0.2.0","use_case_id":"UC-01","industry":"saas-technology","model":"gpt-4o","input_tokens":0,"output_tokens":0,"total_tokens":0,"latency_ms":0,"cache_hit":False,"classification":"GAP_1.5","oracle_result":"n/a","timestamp":"2026-06-03T00:00:00+00:00","redaction_applied":False}
    base.update(overrides)
    return base

def test_skill_name_pattern():
    jsonschema.validate(_full_event(skill="isaca-audit-methodology"), SCHEMA)
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(_full_event(skill="ISACA Audit"), SCHEMA)

def test_use_case_id_pattern():
    jsonschema.validate(_full_event(use_case_id="UC-01"), SCHEMA)
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(_full_event(use_case_id="uc-1"), SCHEMA)

def test_industry_enum():
    for ind in ["financial-services","saas-technology","public-sector","other"]:
        jsonschema.validate(_full_event(industry=ind), SCHEMA)
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(_full_event(industry="banking"), SCHEMA)

def test_oracle_result_enum():
    for v in ["pass","fail","skipped","n/a"]:
        jsonschema.validate(_full_event(oracle_result=v), SCHEMA)
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(_full_event(oracle_result="yes"), SCHEMA)

def test_instrument_emits_event():
    with tempfile.TemporaryDirectory() as tmp:
        os.environ["SOXFLOW_TELEMETRY_PATH"] = str(Path(tmp) / "events.jsonl")
        from telemetry.instrument import instrumented, SkillInvocation
        @instrumented(skill="isaca-audit-methodology",skill_version="0.2.0",default_use_case_id="UC-01",default_industry="saas-technology")
        def fake_run(payload,**kwargs):
            return {"classification":"GAP_1.5","input_tokens":100,"output_tokens":50}
        out = fake_run({"system_name":"Test"})
        assert out["classification"] == "GAP_1.5"
        events_file = Path(tmp) / "events.jsonl"
        assert events_file.exists()
        lines = events_file.read_text().strip().splitlines()
        assert len(lines) == 1
        event = json.loads(lines[0])
        jsonschema.validate(event, SCHEMA)
        assert event["skill"] == "isaca-audit-methodology"
        assert event["classification"] == "GAP_1.5"
        assert event["use_case_id"] == "UC-01"
