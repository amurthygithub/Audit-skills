# CSF 2.0 — Wave 2 Plan (SHIPPED)

## Status

Wave 1 and Wave 2 both SHIPPED (commit `144a190`, merged via PR #24): 4 industry views,
3 use cases, 76 tests passing. Linear ticket SOX-569 closed 2026-06-09.
This document is retained as a historical planning artifact — the plan below was executed.

## What Wave 2 ships

### 4 industry views (`skills/nist-csf-2/industries/`)

| Slug | File | Anchor question |
|---|---|---|
| financial-services | `financial-services.md` | "How does a regulated bank use CSF 2.0 alongside OCC Heightened Standards, FFIEC CAT, and SOX 404?" |
| public-sector | `public-sector.md` | "How does a US federal civilian agency use CSF 2.0 alongside FISMA/NIST 800-37 RMF, BOD 18-01, and CISA CPG?" |
| saas-technology | `saas-technology.md` | "How does a Series-A SaaS use CSF 2.0 alongside SOC 2 + customer security questionnaires (CAIQ/SIG Lite/VSAQ)?" |
| manufacturing | `manufacturing.md` | "How does a discrete manufacturer (think DoD supplier) use CSF 2.0 alongside CMMC L2, NIST 800-171, and IEC 62443?" |
| _index.md | _index.md | Routing table — which industry file for which context |

**Healthcare deliberately deferred to v0.3.x** (per csf-2-design.md §3 — Wave 2 ships 4 industries, healthcare is the 5th once the data/crosswalks/hipaa-to-csf.json is in place from Wave 3).

### 3 use-cases (`skills/nist-csf-2/use-cases/`)

| UC ID | Title | Industry | Inputs (JSON shape) | Expected outputs | Oracle assertions |
|---|---|---|---|---|---|
| UC-01 | First Organizational Profile (Tier 1→3 with GOVERN gap) for Series-A SaaS | saas-technology | `{"org": {...}, "current_practices": {...}, "target_tier": 3}` | Current Profile YAML, Target Profile YAML, 9-Subcategory roadmap | Subcategory count, Tier by Function, roadmap prioritization |
| UC-02 | Board maturity report (6-function radar + 12-mo $ plan) for $20B bank | financial-services | `{"org": {...}, "function_scores": {...}, "investment_capacity": "$2M"}` | Board report (markdown), 6-function radar (text), 12-month budget table | Function scores, dollar totals, recommended sequencing |
| UC-03 | Current/Target → 800-53 Mod gap for 14 lagging Subcategories (DoD supplier) | manufacturing | `{"org": {...}, "lagging_subcategories": [...14 IDs...], "cmmc_target": "L2"}` | Gap analysis table, 800-53 control crosswalk, CMMC L2 readiness check | All 14 subcategories covered, control mappings correct per NIST IR |

**Frontmatter contract (enforced by `lint_skill.py:260`):** `uc_id`, `title`, `industries`, `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status`

### 9 test files (`skills/nist-csf-2/tests/`)

| File | Pattern | Tests |
|---|---|---|
| `test_nist_csf_2_lint.py` | runs `tools/lint_skill.py` against the skill | 1 |
| `test_nist_csf_2_oracle.py` | UC-01/02/03 oracle assertions | 3-4 |
| `test_nist_csf_2_grounding.py` | spot-checks citations resolve to manifest | 4-6 |
| `test_nist_csf_2_trace.py` | end-to-end: input JSON → run_skill → output dict has expected keys | 3-4 |
| `test_nist_csf_2_metamorphic.py` | permutation invariants (e.g., reordering inputs doesn't change outputs) | 2-3 |
| `test_nist_csf_2_adversarial.py` | invalid inputs fail gracefully (e.g., unknown industry key) | 2-3 |
| `test_nist_csf_2_telemetry.py` | event emission on stub call | 1-2 |
| `test_nist_csf_2_consistency.py` | wraps the shared `test_consistency_lib.py` (needs `conftest.py:SKILLS` update) | 6 |
| `test_nist_csf_2_chunks.py` | smoke test for chunk loadability (mirrors audit-workpapers pattern) | 8 (one per chunk) |
| `nist_csf_2_stub.py` | stub executor — `def run_skill(uc_id, payload) -> dict` | n/a |

**Target: 30-40 tests** (matches the 38-test target in csf-2-design.md §5.10).

**conftest.py:23-29 update required on Day 1** to add `"nist-csf-2"` to the `SKILLS` tuple.

### 4 docs files (`skills/nist-csf-2/docs/`)

| File | Purpose |
|---|---|
| `architecture.md` | How the skill is structured: router + 8 chunks + 4 industries + 3 UCs + tests + telemetry + data |
| `limits-and-disclaimers.md` | What the skill is NOT a substitute for (formal attestation, regulatory filing, etc.) |
| `changelog.md` | v0.1.0 = Wave 1 + 2 + 3 (this Wave 2 PR is the v0.1.0 milestone) |
| `acceptance-gate.md` | Per the design doc §5.11: this is where the source-of-truth verification report lives |

### 4 telemetry files (`skills/nist-csf-2/telemetry/`)

| File | Purpose |
|---|---|
| `schema.json` | Event schema (mirror the 5 on-Spine skills' format) |
| `instrument.py` | Stub instrumentation |
| `redaction.md` | PII redaction policy (org names, financial figures, etc.) |
| `baseline.md` | Expected event volumes and latencies |

### README.md (`skills/nist-csf-2/README.md`)

Consumer one-pager — same shape as the 5 on-Spine skills' READMEs. Three integration paths: system prompt, packaged skill+telemetry, managed service.

## Build sequence (5 days)

1. **Day 1 (conftest + 4 industries):** Add `nist-csf-2` to `conftest.py:SKILLS`. Build 4 industry files in parallel (4 agents). Run lint to confirm pass.
2. **Day 2 (3 UCs + skill_stub):** Build 3 UC frontmatters + procedure + oracle sections in parallel (3 agents). Build `nist_csf_2_stub.py` separately. Smoke test that stub loads.
3. **Day 3 (9 test files + 4 telemetry + 4 docs + README):** Build test files in parallel (1 agent per file or one agent for all 9). Build telemetry + docs + README in parallel.
4. **Day 4 (data/ + crosswalks):** Build `data/generators/gen_profile.py` + `data/seeds/uc-0{1,2,3}-input.json`. Skip `data/crosswalks/*.json` (Wave 3).
5. **Day 5 (§5.11 verification gate):** Source-of-truth verification pass. Webfetch NIST CSF 2.0 sources; re-verify industry facts (FFIEC CAT exists? OCC Heightened Standards current version? CMMC L2 final rule status?); re-verify UC oracles. **Non-negotiable** — per the lesson codified in csf-2-fix-report.md.

## Risks for Wave 2

- **Industry facts have a higher error rate than framework facts.** "The Tier scale is 1-4" is a NIST fact; "FFIEC CAT is the audit framework for banks" is also NIST-adjacent but more interpretation-dependent. Wave 2 verification needs to be harder on industries than Wave 1 was on the framework.
- **Manufacturing CMMC L2 has changed** (32 CFR Part 170 final rule, Oct 2024). Verify the current version of CMMC L2 vs L1 vs L3. Do not assume CSF 2.0 → CMMC L2 mapping is static.
- **Healthcare deferral is a real gap.** v0.1.0 will ship without a healthcare industry. Decide explicitly whether to backfill in v0.1.1 or accept the gap.

## Open questions (RESOLVED 2026-06-07)

1. **Healthcare in v0.1.0 or v0.1.1?** → **Defer to v1.0 (not v0.1.1)**. Reasoning: v1.0 is the appropriate milestone for the full 5-industry + HIPAA-crosswalk build (CMMC L2 final rule settled, healthcare data-sharing rules clarified, NIST healthcare-specific QSG matured). v0.1.x ships the 4 high-adoption industries (financial, public, SaaS, manufacturing); v0.2.x adds depth; v1.0 is when the 5th industry lands.
2. **Industry file order in frontmatter** — alphabetical (current convention; no change).
3. **UC frontmatter `frameworks` field** — **add** (e.g., `frameworks: [NIST-CSF-2.0, NIST-SP-800-53-Rev5.1.1]` for UC-03). Lint doesn't require it but cross-skill filtering benefits.
4. **Build against the spec or the design doc?** — **Build against the spec** (`csf-2-file-requirements.md` is the build contract, `csf-2-design.md` is the why-doc). Precedent set at m1057 when build agents were dispatched with the spec as primary reference.

## Out of scope for Wave 2 (defer to Wave 3)

- `data/crosswalks/*.json` (csf-to-800-53-mod.json, csf-to-800-171-r3.json, csf-to-iso27001-2022.json, csf-2-0-subcategories.json, csf-to-hipaa.json) — these need the Wave 2 UCs to land first so the data shapes are right
- `assets/` folder — only if a chunk needs a diagram that doesn't fit in 200 lines
- Healthcare industry — Wave 3 (depends on `data/crosswalks/csf-to-hipaa.json`)

## Estimated effort

- Day 1: 2-3 hours (4 parallel industry agents + conftest update)
- Day 2: 2-3 hours (3 parallel UC agents + stub)
- Day 3: 3-4 hours (9 test files + 4 docs + 4 telemetry + README; can be parallel-heavy)
- Day 4: 1-2 hours (data/ generators + seeds)
- Day 5: 2-3 hours (verification gate)
- **Total: 10-15 hours** (one full focused day, or spread across 2-3 sessions)

## Definition of done (Wave 2)

- [ ] `conftest.py:SKILLS` includes `"nist-csf-2"`
- [ ] 4 industry files in `skills/nist-csf-2/industries/` + `_index.md`
- [ ] 3 UC files in `skills/nist-csf-2/use-cases/` + `_index.md` with all 9 required frontmatter fields
- [ ] 9 test files in `skills/nist-csf-2/tests/` (lint, oracle, grounding, trace, metamorphic, adversarial, telemetry, consistency, chunks) + `nist_csf_2_stub.py`
- [ ] 4 docs files in `skills/nist-csf-2/docs/` (architecture, limits-and-disclaimers, changelog, acceptance-gate)
- [ ] 4 telemetry files in `skills/nist-csf-2/telemetry/` (schema.json, instrument.py, redaction.md, baseline.md)
- [ ] `README.md` at skill root
- [ ] `data/generators/` + `data/seeds/` populated
- [ ] 30+ tests passing locally
- [ ] `python3.11 tools/lint_skill.py skills/nist-csf-2` returns PASS (or only Wave 3-scope warnings)
- [ ] §5.11 source-of-truth verification report committed
- [ ] Update `ci.yml` to add `skills/nist-csf-2` to the lint command
- [ ] PR opened, all 3 CI checks green
- [ ] SOX-569 closed (or transitioned to Wave 3 for the data/crosswalks work)
