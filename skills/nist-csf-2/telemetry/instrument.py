"""Telemetry instrumentation for nist-csf-2.

Stub for the production telemetry emitter. In a real deployment, this module
would emit events to the orchestrating platform's telemetry pipeline (e.g.,
a logging service, an analytics warehouse, or a SIEM).

The schema for events is in schema.json. The redaction policy is in
redaction.md. The expected event volumes and latencies are in baseline.md.

This module exports the same API surface as nist-800-53-rmf/telemetry/instrument.py
(instrumented, SkillInvocation, skill_invocation) so that conftest sys.path
alphabetical ordering does not shadow the real module for sibling skills.
"""

from __future__ import annotations

import json
import os
import time
import uuid
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path
from typing import Any, Callable


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


def _sink_path() -> Path:
    p = Path(os.environ.get("SOXFLOW_TELEMETRY_PATH", "telemetry/events.jsonl"))
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def _emit_jsonl(inv) -> None:
    line = json.dumps(asdict(inv), separators=(",", ":"))
    with _sink_path().open("a") as f:
        f.write(line + "\n")


@dataclass
class SkillInvocation:
    skill: str
    skill_version: str
    use_case_id: str
    industry: str
    model: str = "unknown"
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    latency_ms: int = 0
    cache_hit: bool = False
    classification: str = ""
    oracle_result: str = "n/a"
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    redaction_applied: bool = False
    invocation_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def to_jsonl(self) -> str:
        return json.dumps(asdict(self), separators=(",", ":"))


def instrumented(
    *,
    skill: str,
    skill_version: str,
    default_use_case_id: str = "UC-00",
    default_industry: str = "other",
) -> Callable:
    def deco(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(*args, **kwargs):
            uc = kwargs.pop("use_case_id", default_use_case_id)
            industry = kwargs.pop("industry", default_industry)
            model = kwargs.pop("model", "unknown")
            cache_hit = kwargs.pop("cache_hit", False)
            inv = SkillInvocation(
                skill=skill,
                skill_version=skill_version,
                use_case_id=uc,
                industry=industry,
                model=model,
                cache_hit=cache_hit,
            )
            t0 = time.perf_counter()
            try:
                out = fn(*args, **kwargs)
                inv.latency_ms = int((time.perf_counter() - t0) * 1000)
                if isinstance(out, dict):
                    inv.classification = str(out.get("classification", ""))
                    inv.input_tokens = int(out.get("input_tokens", 0))
                    inv.output_tokens = int(out.get("output_tokens", 0))
                    inv.total_tokens = inv.input_tokens + inv.output_tokens
                    if "oracle_result" in out:
                        inv.oracle_result = out["oracle_result"]
                return out
            finally:
                _emit_jsonl(inv)
        return wrapper
    return deco


@contextmanager
def skill_invocation(
    *,
    skill: str,
    skill_version: str,
    use_case_id: str,
    industry: str,
    model: str = "unknown",
):
    inv = SkillInvocation(
        skill=skill,
        skill_version=skill_version,
        use_case_id=use_case_id,
        industry=industry,
        model=model,
    )
    t0 = time.perf_counter()
    try:
        yield inv
    finally:
        inv.latency_ms = int((time.perf_counter() - t0) * 1000)
        _emit_jsonl(inv)
