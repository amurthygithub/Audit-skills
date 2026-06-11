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
    """Skill-loaded agent executor — measures skill fidelity to the oracle.

    Runs the case through `claude -p` (headless CLI; consumes the operator's
    plan/session limits, no separate API billing). The prompt is fully
    self-contained: SKILL.md + the skill's chunks + the payload + a strict
    JSON-only output contract, with tools disabled — so a run measures what the
    skill TEXT teaches the model, not what the model can dig up.

    Refusal contract: defective inputs must yield {"refusal": "<why>"} — the
    validators map that to the stub's ValueError refusal path.
    """

    name = "llm"

    def __init__(self, model: str = "claude-haiku-4-5-20251001",
                 timeout: int = 180) -> None:
        self.model = model
        self.timeout = timeout

    def _context(self, skill: str) -> str:
        root = REPO_ROOT / "skills" / skill
        parts = [f"===== skills/{skill}/SKILL.md =====\n{(root / 'SKILL.md').read_text()}"]
        for chunk in sorted((root / "chunks").glob("*.md")):
            parts.append(f"===== chunks/{chunk.name} =====\n{chunk.read_text()}")
        return "\n\n".join(parts)

    def _prompt(self, skill: str, use_case: str, payload: dict,
                required_paths: list[str] | None = None) -> str:
        import json as _json
        paths = ""
        if required_paths:
            paths = ("Your JSON object MUST contain exactly these paths (dot = nesting; "
                     "use these key names verbatim):\n  " + "\n  ".join(required_paths)
                     + "\n")
        return (
            "You are an agent that has loaded the following skill. Apply it to the "
            "input exactly as the skill instructs.\n\n"
            f"{self._context(skill)}\n\n"
            f"===== TASK =====\n"
            f"Use case: {use_case}. Input parameters (JSON):\n"
            f"{_json.dumps(payload, indent=1)}\n\n"
            "===== OUTPUT CONTRACT =====\n"
            "Respond with ONLY a single JSON object — no markdown fences, no prose.\n"
            + paths +
            "Numeric values as numbers, classifications as strings.\n"
            "If a required input parameter is missing or invalid such that the skill "
            "says to refuse or ask rather than assume, respond with exactly: "
            '{"refusal": "<one-line reason>"}.'
        )

    def run(self, skill: str, use_case: str, payload: dict,
            required_paths: list[str] | None = None) -> dict:
        import json as _json
        import subprocess
        prompt = self._prompt(skill, use_case, payload, required_paths)
        cmd = ["claude", "-p", prompt, "--model", self.model,
               "--output-format", "json", "--disallowedTools", "*"]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=self.timeout,
                              cwd=str(REPO_ROOT))
        if proc.returncode != 0:
            raise RuntimeError(f"claude CLI failed (rc={proc.returncode}): "
                               f"{proc.stderr[:300]}")
        envelope = _json.loads(proc.stdout)
        text = envelope.get("result", "") if isinstance(envelope, dict) else str(envelope)
        text = text.strip()
        if text.startswith("```"):
            text = text.strip("`")
            text = text[text.find("{"):text.rfind("}") + 1]
        out = _json.loads(text[text.find("{"):text.rfind("}") + 1])
        if isinstance(out, dict) and out.get("refusal"):
            raise ValueError(f"model refusal: {out['refusal']}")
        return out


EXECUTORS = {"stub": StubExecutor, "llm": LLMExecutor}
