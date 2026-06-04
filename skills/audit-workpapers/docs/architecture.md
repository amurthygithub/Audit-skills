# Architecture -- audit-workpapers

## 1. Purpose

This skill encodes PCAOB, AICPA, IAASB, and ISACA audit workpaper standards into a single executable playbook. It supports workpaper creation, sampling methodology (MUS/attribute/variables), audit evidence documentation, finding documentation in 5-part C-C-C-E-R format, audit risk model calculations, opinion determination, electronic workpaper controls, and quality/compliance review.

## 2. Invocation Model

The skill uses the Tier 0 Spine router + chunks pattern. SKILL.md is a 184-line router loaded always. The 7 chunk files (each <=200 lines) are loaded on demand per the routing table in SKILL.md section 11. Industry views and use cases provide context.

```python
# Production invocation (stub in v0.2.0)
from skill_stub import run_skill
out = run_skill(use_case_id="UC-01", payload={...}, model="gpt-4o")
```

## 3. Components

- SKILL.md -- router (184 lines, always loaded; <=300 line limit)
- chunks/ -- 7 files: 01-standards-and-structure, 02-evidence-and-reperformance, 03-sampling, 04-risk-and-opinion, 05-finding-and-workflow, 06-outputs-electronic-review, 07-qc-compliance-cross-refs
- industries/ -- financial-services, public-sector, saas-technology
- use-cases/ -- UC-01 (MUS sampling AR), UC-02 (5-part finding AP cutoff)
- data/ -- README, generators, seeds
- tests/ -- conftest, test_lint, test_oracle
- telemetry/ -- schema.json, instrument.py, redaction.md, baseline.md
- docs/ -- architecture, limits-and-disclaimers, changelog, acceptance-gate

## 4. Data Flow

caller payload -> skill entrypoint -> SKILL.md router -> chunk routing -> LLM (prod) / stub -> structured output -> telemetry event -> oracle check

## 5. Review Protocol (3 cycles)

- Cycle 1: Structure & completeness -- linter (Tier 0a) enforces folder/section/frontmatter contracts.
- Cycle 2: Factual verification -- test_grounding verifies citations- Cycle 2:ce verifies procedure references.
- Cycle 3: Production readiness -- test_oracle passes; telemetry validates; baseline populated.

## 6. Migration from pre-Spine

This skill was retrofitted from a 2,060-line monolithic SKILL.md.bak onto the Tier 0 Spine (router + chunks pattern) on 2026-06-03. The original content was preserved in SKILL.md.bak.
