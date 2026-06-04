"""Telemetry tests for coso-internal-controls."""
from __future__ import annotations
import json, os, tempfile
from pathlib import Path
import jsonschema
import pytest

SCHEMA = json.loads((Path(__file__).resolve().parent.parent / "telemetry" / "schema.json").read_text())

def test_schema_is_valid_json():
    jsonschema.Draft7Validator.check_schema(SCHEMA)

def test_schema_required_fields():
    for field in ["skill","skill_version","use_case_id","industry","model","input_tokens","output_tokens","total_tokens","latency_ms","cache_hit","classification","oracle_result","timestamp","redaction_applied"]:
        assert field in SCHEMA["required"], f"Missing: {field}"

def _full_event(**overrides):
    base = {"skill":"coso-internal-controls","skill_version":"0.2.0","use_case_id":"UC-01","industry":"financial-services","model":"gpt-4o","input_tokens":0,"output_tokens":0,"total_tokens":0,"latency_ms":0,"cache_hit":False,"classification":"EFFECTIVE_WITH_SD","oracle_result":"n/a","timestamp":"2026-06-03T00:00:00+00:00","redaction_applied":False}
    base.update(overrides)
    return base

def test_skill_name_pattern():
    jsonschema.validate(_full_event(skill="coso-internal-controls"), SCHEMA)
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(_full_event(skill="COSO Internal Controls"), SCHEMA)

def test_use_case_id_pattern():
    jsonschema.validate(_full_event(use_case_id="UC-02"), SCHEMA)
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(_full_event(use_case_id="uc-2"), SCHEMA)

def test_industry_enum():
    for ind in ["financial-services","healthcare","saas-technology","public-sector","other"]:
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
        from telemetry.instrument import instrumented
        @instrumented(skill="coso-internal-controls",skill_version="0.2.0",default_use_case_id="UC-01",default_industry="financial-services")
        def fake_run(payload,**kwargs):
            return {"classification":"EFFECTIVE_WITH_SD","input_tokens":100,"output_tokens":50}
        out = fake_run({"entity_description":"Test Bank"})
        assert out["classification"] == "EFFECTIVE_WITH_SD"
        events_file = Path(tmp) / "events.jsonl"
        assert events_file.exists()
        lines = events_file.read_text().strip().splitlines()
        assert len(lines) == 1
        event = json.loads(lines[0])
        jsonschema.validate(event,SCHEMA)
        assert event["skill"] == "coso-internal-controls"
        assert event["classification"] == "EFFECTIVE_WITH_SD"
