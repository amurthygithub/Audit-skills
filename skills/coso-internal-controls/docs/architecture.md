# Architecture — coso-internal-controls

## 1. Purpose

This skill encodes COSO 2013 Internal Control Integrated Framework (ICIF), COSO 2017 ERM, SOX Section 404, PCAOB AS 2201, COSO 2009 Monitoring Guidance, and COSO 2023-2026 emerging technology guidance (Fraud 2nd Edition, ICSR, RPA, GenAI, Blockchain) into a single executable playbook for internal control assessment, ICFR evaluation, walkthroughs, and deficiency classification.

## 2. Invocation Model

This is a stub version. The skill body (SKILL.md + chunks) is complete; the LLM-backed executor ships in SOX-611 Phase 2. Until then, use the skill as a system prompt with the chunks loaded per the routing table in SKILL.md sect.11.

## 3. Components

- `SKILL.md` — the router (214 lines, always loaded).
- `chunks/` — 7 deep-dive files loaded on demand per the routing table.
- `industries/` — financial-services, public-sector, saas-technology (3 industry views).
- `use-cases/` — UC-01 SOX 404 ICFR, UC-02 Deficiency Classification (2 use cases).
- `data/` — data dictionary (README.md).
- `tests/` — conftest.py, test_lint.py.
- `telemetry/` — schema.json, instrument.py, redaction.md, baseline.md.
- `docs/` — architecture.md, limits-and-disclaimers.md, changelog.md, acceptance-gate.md.

## 4. Data Flow

caller prompt -> SKILL.md router -> load relevant chunks per sect.11 routing table -> produce structured output (RcM, principle assessment, deficiency classification, ICFR report).

## 5. Review Protocol (3 cycles)

- Cycle 1: Linter (Tier 0a) enforces folder/section/frontmatter contracts.
- Cycle 2: Grounding (citations resolve to sect.10 manifest).
- Cycle 3: Production readiness (oracle tests pass, telemetry schema validates, baseline populated).

## 6. Extensibility

- Add use case: Copy existing UC, assign uc_id UC-NN, add seed files.
- Add industry: Write industry file, register in industries/_index.md.
- Bump version: Update SKILL.md version, append to changelog.md, re-lint.

## 7. Migration from pre-Spine

This skill was migrated from a monolithic 1,879-line SKILL.md to the router + chunks pattern (Tier 0 Spine) in v0.2.0.
