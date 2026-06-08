"""Telemetry instrumentation for nist-csf-2.

Stub for the production telemetry emitter. In a real deployment, this module
would emit events to the orchestrating platform's telemetry pipeline (e.g.,
a logging service, an analytics warehouse, or a SIEM).

The schema for events is in schema.json. The redaction policy is in
redaction.md. The expected event volumes and latencies are in baseline.md.
"""

from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCHEMA_PATH = Path(__file__).resolve().parent / "schema.json"


def emit(event_name: str, uc_id: str, duration_ms: int, **context: Any) -> dict:
    """Emit a telemetry event.

    Returns the event dict (for testing). Production should ship to a sink.
    """
    event = {
        "event_name": event_name,
        "uc_id": uc_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "duration_ms": duration_ms,
        "skill": "nist-csf-2",
    }
    if context:
        event["context"] = context
    return event


def timed(uc_id: str):
    """Context manager that times an operation and emits a skill_invocation event.

    Usage:
        with timed("UC-01") as t:
            out = run_skill("UC-01", payload)
            t.set_summary(classification=out["classification"])
    """
    return _TimedContext(uc_id)


class _TimedContext:
    def __init__(self, uc_id: str):
        self.uc_id = uc_id
        self.start = None
        self.summary: dict = {}

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration_ms = int((time.perf_counter() - self.start) * 1000)
        event_name = "skill_invocation" if exc_type is None else "error"
        emit(event_name, self.uc_id, duration_ms, **self.summary)
        return False  # don't suppress exceptions

    def set_summary(self, **kwargs):
        self.summary.update(kwargs)
