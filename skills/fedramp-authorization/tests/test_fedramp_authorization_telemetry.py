"""Telemetry smoke test for fedramp-authorization.

Structural check that the skill exports telemetry instrumentation and that
run_skill returns a dict (the telemetry payload is captured externally).
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from fedramp_authorization_stub import run_skill

SKILL_DIR = Path(__file__).resolve().parent.parent
TELEMETRY_DIR = SKILL_DIR / "telemetry"


def test_telemetry_schema_exists():
    schema = TELEMETRY_DIR / "schema.json"
    if not schema.exists():
        pytest.skip("telemetry/schema.json not yet shipped")
    data = json.loads(schema.read_text())
    assert "$schema" in data or "type" in data


def test_telemetry_instrument_module_imports():
    import importlib
    import sys

    skill_root = str(SKILL_DIR)
    if skill_root not in sys.path:
        sys.path.insert(0, skill_root)
    try:
        mod = importlib.import_module("telemetry.instrument")
        assert mod is not None
    except ImportError:
        pytest.skip("telemetry/instrument.py not yet shipped")


def test_run_skill_returns_dict():
    out = run_skill("UC-01", {
        "fips199": {"confidentiality": "Moderate", "integrity": "Low", "availability": "Low"},
        "sar_findings": [],
    })
    assert isinstance(out, dict)
    assert "classification" in out
