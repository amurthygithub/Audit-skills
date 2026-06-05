# Architecture - isaca-audit-methodology

## 1. Purpose

This skill encodes ISACA CISA methodology, COBIT 2019, ITAF standards, ITGC/ITAC testing, risk-based audit planning, 5-part audit observations, COBIT maturity assessment, and cross-framework mapping into a single executable playbook.

## 2. Invocation Model

```python
from skill_stub import run_skill  # replace with real entrypoint in production

out = run_skill(
    use_case_id="UC-01",
    payload={
        "organization": "SaaS company, 500 employees, SOC 2 Type II",
        "scope": ["APO13", "BAI07", "DSS01"],
    },
    model="gpt-4o",
)
```

## 3. Components

- `SKILL.md` - router (~200 lines, always loaded).
- `chunks/` - 7 deep-dive files (loaded on demand per S11 routing table):
  - `01-framework-and-cisa.md` - ISACA framework and CISA 5 domains
  - `02-cobit-2019.md` - COBIT 2019 governance/management objectives
  - `03-itaf-and-maturity.md` - ITAF standards and COBIT maturity models
  - `04-itgc-itac.md` - ITGC and ITAC categories and procedures
  - `05-risk-and-planning.md` - Risk-based audit planning and scoring
  - `06-observation-and-lifecycle.md` - 5-part observation and audit lifecycle
  - `07-outputs-and-cross-refs.md` - Output templates and cross-references
- `industries/` - financial-services.md, saas-technology.md, public-sector.md (3 industry views).
- `use-cases/` - UC-01 (COBIT maturity), UC-02 (5-part observation) (2 stub use cases).
- `data/` - README.md; generators and seeds planned.
- `tests/` - conftest.py, test_lint.py.
- `telemetry/` - schema.json, instrument.py, redaction.md, baseline.md.
- `docs/` - architecture.md, limits-and-disclaimers.md, changelog.md, acceptance-gate.md.

## 4. Data Flow

```
caller payload -> skill entrypoint -> skill body
                       |                  |
                       v                  v
               instrumented decorator    LLM (production) / stub
                       |                  |
                       v                  v
               SkillInvocation event -> telemetry/events.jsonl
                       |
                       v
               structured output (maturity, finding, risk score)
                       |
                       v
               oracle check (tests/test_oracle.py)
```

In production, the LLM call replaces the stub. Telemetry emission is identical. Oracle tests run against either.

## 5. Review Protocol (3 cycles)

- **Cycle 1 - Structure & completeness:** linter enforces folder contract, section contract, frontmatter contract.
- **Cycle 2 - Factual verification:** test_grounding.py verifies citations; test_trace.py verifies procedure references.
- **Cycle 3 - Production readiness:** test_oracle passes; test_telemetry schema validates; baseline populated after run.

## 6. Extensibility

- **Adding a use case:** Copy a stub, assign `uc_id` UC-NN, add a seed under `data/seeds/`, add tests.
- **Adding an industry:** Add file under `industries/`, register in `_index.md`, link from relevant UC.
- **Bumping version:** Update `SKILL.md` `version:`, append to `docs/changelog.md`, re-run linter + tests.

## 7. Migration from pre-Spine

This skill was retrofitted from a 1,662-line monolithic SKILL.md (preserved as `SKILL.md.bak`) to the Tier 0 Spine router + chunks pattern in v0.2.0.
