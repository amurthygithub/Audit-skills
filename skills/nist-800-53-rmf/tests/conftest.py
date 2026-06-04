"""Per-skill conftest.

Adds this directory to sys.path so that ``from skill_stub import run_skill``
in the test files resolves to the sibling ``skill_stub.py``.
"""
import sys
from pathlib import Path

_DIR = Path(__file__).resolve().parent
if str(_DIR) not in sys.path:
    sys.path.insert(0, str(_DIR))
