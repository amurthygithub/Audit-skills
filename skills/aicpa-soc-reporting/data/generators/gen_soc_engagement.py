"""SOC Engagement generator for aicpa-soc-reporting.

Produces structured engagement-scenario payloads from seed configs for use in
oracle, metamorphic, and adversarial test suites. Each call to generate()
consumes a seed JSON and returns a runnable (use_case_id, payload) pair.

Usage:
    from data.generators.gen_soc_engagement import generate

    uc_id, payload = generate("uc-01")  # returns ("UC-01", dict)
"""

from __future__ import annotations

import json
import uuid
from pathlib import Path
from typing import Any

SEEDS = Path(__file__).resolve().parent.parent / "seeds"
SEED_MAP = {
    "uc-01": "uc-01-input.json",
    "uc-02": "uc-02-input.json",
    "uc-03": "uc-03-input.json",
    "uc-04": "uc-04-input.json",
}


def generate(seed_key: str) -> tuple[str, dict[str, Any]]:
    """Load a seed and return (use_case_id, payload).

    Args:
        seed_key: One of "uc-01" through "uc-04".

    Returns:
        Tuple of (UC-XX, hydrated payload dict).

    Raises:
        FileNotFoundError: If the seed file does not exist.
        KeyError: If seed_key is not in SEED_MAP.
    """
    file_name = SEED_MAP[seed_key]
    path = SEEDS / file_name
    if not path.exists():
        raise FileNotFoundError(f"Seed not found: {path}")
    payload = json.loads(path.read_text())
    uc_id = f"UC-{seed_key.split('-')[1]}"
    return uc_id, payload


def generate_all() -> list[tuple[str, dict[str, Any]]]:
    """Yield all known seeds."""
    return [generate(k) for k in sorted(SEED_MAP)]


def generate_with_idempotency_key(seed_key: str) -> tuple[str, dict[str, Any], str]:
    """Generate with a unique idempotency key for trace tracking."""
    uc_id, payload = generate(seed_key)
    key = f"{uc_id}-{uuid.uuid4().hex[:8]}"
    return uc_id, payload, key
