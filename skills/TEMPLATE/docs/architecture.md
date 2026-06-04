# Architecture (TEMPLATE)

> This file is the **shell** every skill copies. Replace placeholders with skill-specific content.

## 1. Purpose

What this skill encodes. One paragraph. Cite the source standards.

## 2. Invocation Model

How a caller invokes the skill. Show the function signature and a minimal example.

```python
from skills.<name>.run import run_skill

out = run_skill(
    use_case_id="UC-01",
    industry="financial-services",
    payload={...},
    model="gpt-4o",
)
```

## 3. Components

- `SKILL.md` — the playbook (system prompt / RAG context).
- `industries/` — industry-specific scoping notes.
- `use-cases/` — worked examples (oracles).
- `data/` — synthetic inputs (deterministic).
- `tests/` — oracle / grounding / trace / metamorphic / judge / adversarial / telemetry / lint.
- `telemetry/` — instrumentation, schema, baseline.
- `docs/` — this file plus limits, changelog, acceptance.

## 4. Data Flow

```
caller payload ──► skill entrypoint ──► SKILL.md prompt assembly
                          │
                          ▼
                   LLM invocation (instrumented)
                          │
                          ▼
                  structured output + classification
                          │
                          ▼
                  oracle check (in tests) + telemetry emit
```

## 5. Review Protocol (3-cycle)

- **Cycle 1 — Structure & completeness:** Section contract, frontmatter contract, folder contract.
- **Cycle 2 — Factual verification:** Citations resolve, no hallucinated paragraph numbers, cross-skill alignment.
- **Cycle 3 — Production readiness:** Math verification, telemetry baseline, acceptance gate, reviewer sign-off.

## 6. Extensibility

- **Adding a use case:** Copy `use-cases/_template.md`, add to `_index.md`, add seed under `data/seeds/`, add a test in `tests/test_oracle.py`, run linter.
- **Adding an industry:** Add a file under `industries/`, register in `_index.md`, link from each relevant use case.
- **Bumping version:** Update `SKILL.md` `version:`, append to `docs/changelog.md`, re-run linter + tests + baseline.
