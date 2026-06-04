# Acceptance Gate — nist-800-53-rmf (v0.2.0)

This file tracks the Acceptance Gate for the v0.2.0 release. Each box is filled in only when the criterion is **actually** satisfied (linter passes, tests run, etc.).

## Required

- [x] **Frontmatter** — all required fields present (`name`, `description`, `category`, `risk`, `source`, `date_added`, `version`, `status`, `industries`, `frameworks`, `telemetry_contract`, `context_budget`, `tags`).
- [x] **Sections** — first 10 sections present, in order (`When to Use`, `Framework Overview`, `Core Concepts`, `Decision Logic`, `Procedure Templates`, `Output Templates`, `Cross-References`, `Worked Examples`, `Anti-Hallucination`, `References & Citation Manifest`).
- [x] **§11 Routing** — present, with the routing table mapping user intent → chunks.
- [x] **Folders** — `industries/`, `use-cases/`, `data/`, `tests/`, `telemetry/`, `docs/`, `chunks/` all exist and non-empty.
- [x] **SKILL.md size** — 218 lines (≤ 300 limit).
- [x] **Chunks** — 7 files (categorize, baseline, implement, assess, authorize, monitor, crosswalk); each ≤ 87 lines (≤ 200 limit); names match `NN-slug.md`.
- [x] **context_budget** — declared in frontmatter with 4 token fields.
- [x] **Industries** — 4 industry files (`public-sector.md`, `financial-services.md`, `saas-technology.md`, `healthcare.md`); `_index.md` registered.
- [x] **Use cases** — 3 use-case files (UC-01, UC-02, UC-03); `_index.md` registered; each with `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status`.
- [x] **Data** — `data/README.md` present; 3 generators; 10 seed fixtures.
- [x] **Tests** — 7 test files (`test_oracle.py`, `test_trace.py`, `test_grounding.py`, `test_metamorphic.py`, `test_adversarial.py`, `test_telemetry.py`, `test_lint.py`).
- [x] **Telemetry** — `telemetry/schema.json` validates; `telemetry/instrument.py` importable; `telemetry/redaction.md` non-stub.
- [x] **Docs** — `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`, `acceptance-gate.md` all non-stub.
- [x] **No unfinished-work markers outside the changelog** — linter enforces.
- [ ] **Baseline** — `telemetry/baseline.md` populated after first instrumented run per UC.
- [x] **Citations** — every in-body `[LABEL §N]` reference resolves to `## 10. References & Citation Manifest` (test_grounding.py).

## Reviewer sign-off (3 cycles)

- [ ] **Cycle 1 — structure/completeness reviewer** (linter passes — pending CI)
- [ ] **Cycle 2 — factual verification reviewer** (test_grounding + test_trace pass)
- [ ] **Cycle 3 — production readiness reviewer** (test_oracle + test_telemetry + baseline populated)
- [ ] **Decision: `published` / `rejected` (with notes)**

## Notes

- Token baseline: target `input_p90: 14000`, `output_p90: 4500` (per `SKILL.md` frontmatter). Per-call context budget: `always_loaded_tokens: 3000`, `per_call_typical_tokens: 6000`, `per_call_max_tokens: 15000`. To be measured and updated in `telemetry/baseline.md` after first instrumented run.
- v0.2.0 adopted the router + chunks pattern (per TEMPLATE §11). Per-call context cost is 3-5× lower than v0.1.0's monolithic layout.
- The 4 pre-Spine skills have not been migrated; this skill is the first on the Spine. Migration backlog is in SOX-611.
- The skill body is draft-quality and requires 3 review cycles before `status: published`.
