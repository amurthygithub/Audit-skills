"""Executors — the pluggable "run the skill" layer (SOX-600 V1).

Two-layer correctness model (validation-harness-design.md §2): the deterministic
stub is the oracle layer; the skill eval asks whether a skill-loaded AGENT
reproduces the oracle's answer. V1 ships:

- StubExecutor — runs the skill's deterministic reference stub. Validates the
  harness plumbing end-to-end and is the auto-labeler for generated cases
  (the oracle-anchored self-labeling flywheel). Pass rate against itself must
  be 100% by construction; anything else is a harness bug.
- LLMExecutor — the V3 slice: load SKILL.md + routed chunks into a model call,
  parse the structured result. NOT implemented in V1; the interface is pinned
  here so cases/validators/reports need no changes when it lands (SOX-602).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


class StubExecutor:
    """Deterministic reference executor: calls skills/<skill>/tests/<slug>_stub.run_skill."""

    name = "stub"

    def __init__(self) -> None:
        self._modules: dict[str, object] = {}

    def _module(self, skill: str):
        if skill not in self._modules:
            slug = skill.replace("-", "_")
            path = REPO_ROOT / "skills" / skill / "tests" / f"{slug}_stub.py"
            if not path.is_file():
                raise FileNotFoundError(f"no stub for skill {skill!r}: {path}")
            spec = importlib.util.spec_from_file_location(f"evals_stub_{slug}", path)
            mod = importlib.util.module_from_spec(spec)
            # stubs import siblings via their tests dir on sys.path
            tests_dir = str(path.parent)
            if tests_dir not in sys.path:
                sys.path.insert(0, tests_dir)
            spec.loader.exec_module(mod)
            self._modules[skill] = mod
        return self._modules[skill]

    def run(self, skill: str, use_case: str, payload: dict) -> dict:
        return self._module(skill).run_skill(use_case, payload)


class LLMExecutor:
    """Skill-loaded agent executor (V3, SOX-602). Interface pinned, not implemented.

    Contract: run() loads skills/<skill>/SKILL.md plus the chunks its routing
    table selects for the case's use case, presents the payload, and parses the
    agent's structured output into the same shape the stub returns. Cases,
    validators, and reports are executor-agnostic by design.
    """

    name = "llm"

    def __init__(self, model: str = "claude-sonnet-4-6") -> None:
        self.model = model

    def run(self, skill: str, use_case: str, payload: dict) -> dict:
        raise NotImplementedError(
            "LLMExecutor is the V3 slice (SOX-602): requires model access, run "
            "budget, and an output-parsing contract. Use --executor stub for "
            "plumbing and oracle labeling."
        )


EXECUTORS = {"stub": StubExecutor, "llm": LLMExecutor}
