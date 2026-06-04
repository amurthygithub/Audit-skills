# Architecture -- aicpa-soc-reporting

## 1. Purpose

This skill encodes the AICPA SOC reporting framework (SOC 1, SOC 2, SOC 3, SOC for Cybersecurity, SOC for Supply Chain) into a single executable playbook. It supports engagement classification, TSC scoping, CUEC/CSOC identification, opinion determination, sampling guidance, report structure templates, management assertions, and bridge letters.

## 2. Invocation Model

The skill follows the Tier 0 Spine router + chunks pattern. `SKILL.md` is a ~290-line router always loaded (~2,800 tokens). Deep-dive content lives in 7 chunks loaded on demand per the routing table in SKILL.md Section 11.

```python
from skill_stub import run_skill  # placeholder until real executor in SOX-611 Phase 2

out = run_skill(
    use_case_id="UC-01",
    payload={
        "system_name": "CloudStack SaaS",
        "tsc_categories": ["Security", "Availability", "Confidentiality"],
        "examination_period": {"start": "2025-01-01", "end": "2025-12-31"},
        "subservice_orgs": ["AWS (IaaS)"],
    },
    model="gpt-4o",
)
# -> {"soc_type": "SOC-2", "report_type": "Type-II", "criteria_count": 38, "opinion": "Unqualified", ...}
```

## 3. Components

- `SKILL.md` -- router (sections 1-12, ~280 lines).
- `chunks/` -- 7 chunks: overview, engagement type decision, TSP criteria, report structures, assertions/bridge, CUEC/CSOC, opinion/lifecycle/sampling.
- `industries/` -- 4 industry views: saas-technology, financial-services, healthcare, public-sector.
- `use-cases/` -- 4 use cases: UC-01 SOC 2 Type II, UC-02 CUEC/CSOC, UC-03 Bridge letter, UC-04 Auditee prep.
- `data/` -- (planned) synthetic datasets, generators, seeds, crosswalks.
- `tests/` -- conftest.py + test_lint.py (Tier 0a).
- `telemetry/` -- schema.json, instrument.py, baseline.md, redaction.md.
- `docs/` -- architecture.md, limits-and-disclaimers.md, changelog.md, acceptance-gate.md.

## 4. Data Flow

```
caller payload --> skill entrypoint (stub) --> skill router
                        |                          |
                        v                          v
                instrumented decorator     load chunks per routing table
                        |                          |
                        v                          v
                SkillInvocation event --> telemetry/events.jsonl
                        |
                        v
                structured output (SOC type, criteria, opinion)
                        |
                        v
                oracle check (tests/test_oracle.py, planned)
```

## 5. Review Protocol (3 cycles)

- Cycle 1 -- Structure & completeness: linter (Tier 0a) enforces folder contract, section contract, frontmatter contract.
- Cycle 2 -- Factual verification: test_grounding.py + test_trace.py (planned).
- Cycle 3 -- Production readiness: test_oracle + test_telemetry + baseline populated.

## 6. Extensibility

- Add use case: copy `use-cases/_index.md` shape, add seed, add test.
- Add industry: add file under `industries/`, register in `_index.md`, link from relevant UC.
- Bump version: update `SKILL.md` version, append to `docs/changelog.md`, re-run linter + tests.

## 7. Migration from pre-Spine

This skill was migrated from a monolithic 1,580-line SKILL.md (now .bak) to the router + 7 chunks pattern. The .bak file is preserved for reference. Migration date: 2026-06-03.
