# Architecture — nist-800-53-rmf

## 1. Purpose

This skill encodes NIST SP 800-53 Rev 5, NIST SP 800-37 Rev 2 RMF, FIPS 199, FIPS 200, NIST SP 800-53A Rev 5, and the FedRAMP overlay into a single executable playbook. It supports FIPS 199 categorization, baseline selection, tailoring, implementation documentation, 800-53A assessment, ATO decision logic, and continuous monitoring.

## 2. Invocation Model

```python
from skill_stub import run_skill  # replace with real entrypoint in production

# Categorize + select baseline
out = run_skill(
    use_case_id="UC-01",
    payload={
        "system_name": "CaseFlow Cloud",
        "information_types": [...],
        "cloud_provider": "AWS GovCloud",
        "cloud_fedramp_id": "...",
    },
    model="gpt-4o",
)

# Result shape
# {
#   "classification": "MODERATE",
#   "fips_199_categorization": {...},
#   "baseline": {...},
#   "inheritance_summary": [...],
#   "tailoring_decisions": [...],
# }
```

## 3. Components

- `SKILL.md` — the playbook (decision logic, output templates, cross-references, anti-hallucination disclaimers, citation manifest).
- `industries/` — `public-sector.md`, `financial-services.md`, `saas-technology.md`, `healthcare.md` (4 industry views).
- `use-cases/` — UC-01 FedRAMP Moderate, UC-02 Agency ATO, UC-03 SOC 2 → 800-53 crosswalk (3 worked examples).
- `data/`
  - `generators/` — `gen_fips199.py`, `gen_sar_findings.py`, `gen_crosswalk_gap.py` (deterministic; `--seed`).
  - `seeds/` — `uc-01-input.json`, `uc-01-crm.json`, `uc-01-expected.json`, `uc-02-input.json`, `uc-02-findings.json`, `uc-02-expected.json`, `uc-03-input.json`, `uc-03-gap-list.json`, `uc-03-remediation.json`, `uc-03-expected.json`.
  - `crosswalks/soc2-to-800-53-mod.json` — authoritative reference for UC-03.
- `tests/`
  - `test_oracle.py` — UC-01, UC-02, UC-03 oracle assertions.
  - `test_trace.py` — UC procedure citations resolve to SKILL.md sections.
  - `test_grounding.py` — in-body citations resolve to §10 manifest.
  - `test_metamorphic.py` — input mutations produce expected output mutations.
  - `test_adversarial.py` — edge cases (dual classification, PII volume, inheritance invalidation).
  - `test_telemetry.py` — schema validation + instrumentation emits valid events.
  - `test_lint.py` — Tier 0a linter passes.
- `telemetry/`
  - `schema.json` — SkillInvocation schema (per the Spine).
  - `instrument.py` — re-exports the Spine's `instrumented` decorator + `SkillInvocation` event.
  - `redaction.md` — PII/NPI/PHI redaction policy.
  - `baseline.md` — token baseline (populated after first instrumented run).
- `docs/`
  - `architecture.md` (this file).
  - `limits-and-disclaimers.md`.
  - `changelog.md`.
  - `acceptance-gate.md`.

## 4. Data Flow

```
caller payload ──► skill entrypoint (skill_stub.py) ──► skill body
                          │                                    │
                          ▼                                    ▼
                  instrumented decorator             LLM (production) / stub
                          │                                    │
                          ▼                                    ▼
                  SkillInvocation event ──────► telemetry/events.jsonl
                          │
                          ▼
                  structured output (classification, baseline, etc.)
                          │
                          ▼
                  oracle check (tests/test_oracle.py)
```

In production, the LLM call replaces the stub. The telemetry emission is identical. The output shape is identical. The oracle tests run against either.

## 5. Review Protocol (3 cycles)

- **Cycle 1 — Structure & completeness:** linter (Tier 0a) enforces folder contract, section contract, frontmatter contract.
- **Cycle 2 — Factual verification:** test_grounding.py verifies citations; test_trace.py verifies UC procedure references resolve.
- **Cycle 3 — Production readiness:** test_oracle passes; test_telemetry schema validates; baseline populated after run; reviewer sign-off in `docs/acceptance-gate.md`.

## 6. Extensibility

- **Adding a use case:** Copy `use-cases/_template.md` (or one of the existing UC files), assign `uc_id` UC-NN, add a seed under `data/seeds/`, add tests in `tests/test_oracle.py`.
- **Adding an industry:** Add a file under `industries/`, register in `industries/_index.md`, link from each relevant UC.
- **Bumping version:** Update `SKILL.md` `version:`, append to `docs/changelog.md`, re-run linter + tests + baseline measurement.

## 7. Migration from pre-Spine

The earlier 4 skills (`isaca-audit-methodology`, `coso-internal-controls`, `aicpa-soc-reporting`, `audit-workpapers`) were authored before the Spine. They are missing `telemetry/`, `industries/`, `use-cases/`, `data/`, `tests/`, and the new frontmatter fields. Migrating them to the Spine is tracked in **SOX-611 (Phase 2)**.
