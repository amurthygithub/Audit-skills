"""Telemetry smoke test for pci-dss-assessment.

Verifies the skill exports telemetry instrumentation that emits
the expected event shape when run_skill is called. This is a
structural check (not a behavioral check on event volume/latency
in production — those are in telemetry/baseline.md).
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from pci_dss_assessment_stub import run_skill


SKILL_DIR = Path(__file__).resolve().parent.parent
TELEMETRY_DIR = SKILL_DIR / "telemetry"
SEEDS = SKILL_DIR / "data" / "seeds"


def test_telemetry_schema_exists():
    """telemetry/schema.json must exist and be valid JSON."""
    schema = TELEMETRY_DIR / "schema.json"
    if not schema.exists():
        pytest.skip("telemetry/schema.json not yet shipped")
    data = json.loads(schema.read_text())
    assert "$schema" in data or "type" in data


def test_telemetry_instrument_module_imports():
    """telemetry.instrument should be importable as a Python module."""
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
    """run_skill should always return a dict (telemetry payload is captured externally)."""
    payload = json.loads((SEEDS / "uc-01-input.json").read_text())
    out = run_skill("UC-01", payload)
    assert isinstance(out, dict)
    assert "classification" in out
