"""Pytest configuration for nist-800-53-rmf.

Adds the skill root to sys.path so tests can import from telemetry/ directly.
"""

from __future__ import annotations

import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT))
