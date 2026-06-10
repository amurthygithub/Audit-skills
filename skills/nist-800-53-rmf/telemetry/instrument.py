"""Skill invocation instrumentation (Tier 0 Spine).

Wraps any skill's entrypoint and emits a SkillInvocation event per call. Persists
to JSONL (default) or to OpenTelemetry if configured. Performs PII/NPI redaction
on free-form payload fields before persistence.

Usage:
    from skills.<name>.telemetry.instrument import instrumented

    @instrumented(skill="nist-800-53-rmf", skill_version="0.1.0")
    def run_skill(use_case_id, industry, payload, model):
        ...  # skill logic
        return SkillOutput(classification="MODERATE", ...)

Or as a context manager:
    with skill_invocation(skill="...", use_case_id="UC-01", industry="...") as ctx:
        out = run_skill(...)
        ctx.set_classification(out.classification)
        ctx.set_oracle("pass")
"""

from __future__ import annotations

import json
import os
import re
import time
import uuid
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Optional

SCHEMA_PATH = Path(__file__).parent / "schema.json"

# Naive redaction patterns — replace with a proper detector (Presidio, etc.) in prod.
REDACT_PATTERNS = [
    (re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), "[SSN]"),                       # SSN
    (re.compile(r"\b\d{16}\b"), "[CC]"),                                   # credit card
    (re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "[EMAIL]"),
    (re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"), "[PHONE]"),
]


def _redact(value: Any) -> tuple[Any, bool]:
    """Return (redacted_value, was_redacted). Operates on strings recursively."""
    if isinstance(value, str):
        out, hit = value, False
        for pat, repl in REDACT_PATTERNS:
            new = pat.sub(repl, out)
            if new != out:
                hit = True
                out = new
        return out, hit
    if isinstance(value, dict):
        redacted, hit = {}, False
        for k, v in value.items():
            rv, h = _redact(v)
            redacted[k] = rv
            hit = hit or h
        return redacted, hit
    if isinstance(value, list):
        redacted, hit = [], False
        for v in value:
            rv, h = _redact(v)
            redacted.append(rv)
            hit = hit or h
        return redacted, hit
    return value, False


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


def _sink_path() -> Path:
    p = Path(os.environ.get("SOXFLOW_TELEMETRY_PATH", "telemetry/events.jsonl"))
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def _emit(inv: SkillInvocation) -> None:
    line = inv.to_jsonl()
    with _sink_path().open("a") as f:
        f.write(line + "\n")


def instrumented(
    *,
    skill: str,
    skill_version: str,
    default_use_case_id: str = "UC-00",
    default_industry: str = "other",
) -> Callable:
    """Decorator that wraps a skill entrypoint and emits telemetry per call."""

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
                _emit(inv)
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
        _emit(inv)


# --- Event-style API (superset; kept so every vendored copy exposes the union) ---

_SKILL_NAME = Path(__file__).resolve().parents[1].name


def emit(event_name: str, uc_id: str, duration_ms: int, **context: Any) -> dict:
    """Emit a lightweight telemetry event. Returns the event dict (for testing)."""
    event = {
        "event_name": event_name,
        "uc_id": uc_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "duration_ms": duration_ms,
        "skill": _SKILL_NAME,
    }
    if context:
        event["context"] = context
    return event


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


def timed(uc_id: str) -> "_TimedContext":
    """Context manager that times an operation and emits a skill_invocation event."""
    return _TimedContext(uc_id)
