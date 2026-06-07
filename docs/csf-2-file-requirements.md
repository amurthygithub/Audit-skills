# CSF 2.0 Skill — File Requirements Specification

> **Use this document as the contract for every file in `skills/nist-csf-2/`.**
> Every build agent reads this. Every reviewer validates against this.
> The design doc (`docs/csf-2-design.md`) is the high-level "what to build"; this doc is the low-level "what each file must contain".
> Status: Required reading for any agent touching this skill. Source of truth: this file.

---

## 0. How to use this document

1. **Build agents:** for each file you create, read the corresponding section here, then implement to the spec. Every "MUST" is enforced. Every "SHOULD" is a strong recommendation. Every "MAY" is judgment.
2. **Review agents:** for each file you review, validate against the corresponding section here. Cite section numbers in your findings.
3. **The lint is the floor, not the ceiling.** Passing `tools/lint_skill.py` is necessary but not sufficient. This spec is the ceiling.

## 1. Architectural rules (apply to every file)

1.1. **Tier 0 Spine compliance.** Every file conforms to the `skills/TEMPLATE/` shape. The linter enforces folder layout, frontmatter shape, section presence, and citation resolution.
1.2. **Path consistency.** Cross-references to sibling skills use the bare backticked form `<sibling>/chunks/<file>.md` (e.g., `` `nist-800-53-rmf/chunks/09-crosswalk.md` ``), as parsed by `tests/test_consistency_lib.py:test_cross_skill_references_resolve`. Cross-references to CSF 2.0 internal chunks use relative paths (`chunks/01-functions-categories.md`).
1.3. **YAML frontmatter in every chunk.** Markdown-table frontmatter (as the contributor's PR #13 used) is **forbidden** — the linter and `test_consistency_lib.py` require parseable YAML.
1.4. **No trailing whitespace.** Enforced by the whitespace rule (PR #15, in `tools/lint_skill.py`). Every file ends with exactly one newline.
1.5. **No TODO/FIXME outside `docs/changelog.md`.** Enforced by the linter.
1.6. **Citations resolve.** Every in-body `[LABEL §N]` citation must be present in `## 10. References & Citation Manifest`. Every manifest label must be cited at least once in the body.
1.7. **Routing table completeness.** Every chunk file in `chunks/` must be referenced in SKILL.md's §11 routing table, and every entry in §11 must point to a real file.
1.8. **Determinism.** All Python generators must accept `--seed N` and produce byte-identical output for the same seed.
1.9. **PII/NPI/PHI redaction.** All seeds and generators produce synthetic data only. No real organization names, real personal data, real account numbers. Use clearly-fake placeholders: `ACME-001`, `John Doe`, `XX-XXXX-1234`.
1.10. **The root `conftest.py` `SKILLS` tuple MUST be updated** to include `'nist-csf-2'` before any test in `skills/nist-csf-2/tests/` is collected. This is a Day 1 task; without it, every test that imports `nist_csf_2_stub` will fail with `ModuleNotFoundError`.

## 2. `SKILL.md` — the router

The router is the first file any consumer reads. It must be ≤300 lines (hard limit) and serve as both documentation AND a loadable LLM system prompt.

### 2.1. Frontmatter (YAML, exact fields)

| Field | Required? | Type | Example |
|-------|-----------|------|---------|
| `name` | YES | string | `nist-csf-2` |
| `description` | YES | string (1-2 sentences) | `NIST Cybersecurity Framework 2.0 (Feb 2024): 6 Functions, 22 Categories, 108 Subcategories, Tiers 1-4, Current/Target Profiles. Use this skill to assess organizational cybersecurity maturity, build a profile, or report to executives.` |
| `category` | YES | enum | `audit-framework` |
| `risk` | YES | enum | `informational` |
| `source` | YES | string | `https://www.nist.gov/cyberframework (Feb 26, 2024)` |
| `date_added` | YES | ISO date | `2026-06-09` (build Day 1) |
| `version` | YES | semver | `0.1.0` |
| `status` | YES | enum | `production` (after Day 5 sign-off) |
| `industries` | YES | array (≥3) | `[financial-services, public-sector, saas-technology, manufacturing]` |
| `frameworks` | YES | array | `[NIST-CSF-2.0, NIST-SP-800-53-Rev5, NIST-SP-800-53-Rev5.1.1, NIST-SP-800-37, NIST-SP-800-171, ISO-27001, HIPAA-Security-Rule, PCI-DSS-4.0.1]` |
| `telemetry_contract` | YES | string | `SkillInvocation v1` |
| `context_budget` | YES | object | (see §2.2) |
| `tags` | YES | array (≥5) | `[csf, cybersecurity-framework, govern, identify, protect, detect, respond, recover, profile, maturity, risk-management]` |

### 2.2. `context_budget` fields

| Sub-field | Required? | Type | Example |
|-----------|-----------|------|---------|
| `always_loaded_tokens` | YES | int | `3500` |
| `per_call_typical_tokens` | YES | int | `7000` |
| `per_call_max_tokens` | YES | int | `16000` |
| `per_call_p90_tokens` | YES | int | `9000` |

### 2.3. Top-level sections (in order)

The SKILL.md must contain at minimum the 10 sections required by the TEMPLATE contract (§1-§10, see `skills/TEMPLATE/SKILL.md:113-129`). §11 Routing is required because `chunks/` will exist. §12 Quick Reference is recommended for the executive-legibility promise; add or omit per the build agent's judgment. Order:

1. **When to Use** — 5-8 bullet triggers, 3-5 negative triggers (when NOT to use)
2. **Framework Overview** — 2-3 paragraph intro to CSF 2.0, mention 6 Functions, Tiers, Profiles
3. **Core Concepts** — Functions/Categories/Subcategories table, Profiles, Tiers, GOVERN function (new in 2.0)
4. **Decision Logic** — when to use CSF vs 800-53 vs other frameworks
5. **Procedure Templates** — points to the 3 UCs
6. **Output Templates** — points to chunks that produce templates
7. **Cross-References** — explicit refs to nist-800-53-rmf, isaca, coso, aicpa, workpapers
8. **Worked Examples** — 3-row table pointing to UCs
9. **Anti-Hallucination Disclaimers** — 5-8 bullets on what this skill is NOT
10. **References & Citation Manifest** — the manifest table
11. **Routing** — the routing table (chunk ↔ triggers)
12. **Quick Reference** — one-line cheat sheet of the 6 Functions

### 2.4. Routing table (§11) — exact format

```markdown
## 11. Routing

| Intent / trigger | Chunk to load |
|------------------|---------------|
| "what is CSF" / "Functions/Categories" / "108 subcategories" / "structure of CSF" | chunks/01-functions-categories.md |
| "Tiers" / "Current/Target Profile" / "profile types" / "what is a Profile" | chunks/02-tiers-and-profiles.md |
| "build a CSF profile" / "first profile" / "Tier assessment" | chunks/03-current-profile.md |
| "where are we weak" / "maturity gap" / "Target profile" | chunks/04-target-profile-and-gap.md |
| "GOVERN function" / "GV." / "risk governance" | chunks/05-govern-function.md |
| "board report" / "executive summary" / "6-function radar" | chunks/06-enterprise-reporting.md |
| "implement CSF" / "how to improve" / "quick wins" | chunks/07-implementation-playbook.md |
| "800-53 crosswalk" / "CSF subcategory mapping" | chunks/08-informative-references-crosswalk.md |
```

### 2.5. Manifest table (§10) — exact format

```markdown
## 10. References & Citation Manifest

| Label | Title | Publisher | Identifier | Retrieval | URL |
|-------|-------|-----------|------------|-----------|-----|
| NIST-CSF-2.0 | Cybersecurity Framework 2.0 | NIST | NIST CSF 2.0 | 2024-02-26 | https://www.nist.gov/cyberframework |
| NIST-SP-800-53-Rev5 | Security and Privacy Controls for Information Systems and Organizations | NIST | Rev 5 | 2024-04-04 | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final |
| ... |
```

Every `[LABEL §N]` citation in the body must have a row in this table. The convention is the same as `skills/nist-800-53-rmf/SKILL.md` §10.

### 2.6. Industries list

Must include at least 3 of: `financial-services`, `public-sector`, `saas-technology`, `manufacturing`, `healthcare`. The build Day 2 plan covers 4: financial-services, public-sector, saas-technology, manufacturing.

## 3. `chunks/NN-slug.md` — the 8 deep-dive files

Each chunk: ≤200 lines, kebab-case filename matching `^\d{2}-[a-z0-9-]+\.md$`, YAML frontmatter, follows the chunk template.

### 3.1. The 8 chunks (locked filenames)

| # | Filename | Frontmatter `topic` | Frontmatter `load_when` | Lines target |
|---|----------|---------------------|--------------------------|--------------|
| 01 | `01-functions-categories.md` | "6 Functions, 22 Categories, 108 Subcategories — the CSF 2.0 structure" | "user asks about CSF structure, functions, categories, subcategories, or the GOVERN function" | ~150 |
| 02 | `02-tiers-and-profiles.md` | "Tiers 1-4 and Profile types: Current, Target, Organizational, Community" | "user asks about Tiers, Profiles, Current Profile, Target Profile, or how to start" | ~150 |
| 03 | `03-current-profile.md` | "Building the Current Profile: what the org does today, by subcategory" | "user asks to build a profile, do a current-state assessment, or wants the first profile" | ~180 |
| 04 | `04-target-profile-and-gap.md` | "Target Profile construction and the gap analysis: Current → Target with priorities" | "user asks about gap analysis, target state, or what to fix first" | ~180 |
| 05 | `05-govern-function.md` | "GOVERN function (new in 2.0): GV.OC, GV.RM, GV.SC, GV.PO, GV.OV, GV.RR" | "user asks about GOVERN, GV. categories, or risk governance at the org level" | ~180 |
| 06 | `06-enterprise-reporting.md` | "Executive reporting: 6-function radar, board-level maturity scorecard, and trend reports" | "user asks for a board report, executive summary, or 6-function radar" | ~150 |
| 07 | `07-implementation-playbook.md` | "Implementation: 90-day, 6-month, 12-month quick wins, sequencing, and resourcing" | "user asks how to implement CSF, prioritization, or resourcing" | ~180 |
| 08 | `08-informative-references-crosswalk.md` | "CSF subcategory → 800-53, 800-171, ISO 27001, HIPAA Security Rule mappings" | "user asks for a crosswalk, mapping, or how CSF relates to 800-53" | ~150 |

### 3.2. Frontmatter for every chunk (exact)

```yaml
---
chunk_id: 01-functions-categories
parent_skill: nist-csf-2
topic: "..."
load_when: "..."
---
```

### 3.3. Each chunk's body — the contract

Every chunk must have:
- A level-1 heading `# Chunk NN — <Topic>` (matches the frontmatter topic)
- A short intro paragraph (2-3 sentences)
- 3-6 level-2 sections, each with concrete content (not generic)
- A "Cross-references" section pointing to other chunks + sibling skills
- An "Anti-hallucination" subsection if the chunk makes specific claims (e.g., crosswalks)

## 4. `industries/` — 4 industry files + index

### 4.1. `_index.md` (required)

A markdown table with one row per industry file:

```markdown
| Industry | File | Key angle |
|----------|------|-----------|
| Financial services | financial-services.md | GOVERN for OCC/FFIEC; PROTECT for GLBA Safeguards Rule; 6-function radar for board |
| ... | ... | ... |
```

### 4.2. Each industry file — frontmatter + body

Each industry file must have:
- YAML frontmatter: `industry`, `key_regulations`, `related_skills`, `subcategories_emphasized` (array of 5-10 CSF subcategory IDs)
- Body: 3-5 level-2 sections
- A "Real-world example" callout
- Cross-references to relevant chunks

## 5. `use-cases/` — 3 worked examples + index

### 5.1. Frontmatter contract (enforced by lint)

```yaml
---
uc_id: UC-01
title: "..."
industries: [...]   # at least 1
procedure: "..."     # 1-3 sentence summary
expected_outputs: [...]  # list of expected output keys
oracle: "..."       # what the right answer is
data_refs: [...]    # which seed JSONs/generators
tests:
  - "test that the output..."
  - ...
status: active
---
```

### 5.2. The 3 UCs (locked)

| UC | Title | Industries | Real-world anchor |
|----|-------|------------|-------------------|
| **UC-01** | First-profile pattern for a Series-A SaaS | saas-technology, financial-services | "Tier 1 → Tier 3 journey, GOVERN gap, 9-subcategory roadmap" |
| **UC-02** | Board maturity report for a $20B regional bank | financial-services | "6-function radar, GV.RM+DE.CM lagging, 12-month $ plan" |
| **UC-03** | Current/Target gap mapped to 800-53 for a DoD supplier | manufacturing, public-sector | "14 lagging subcategories, mapped to 800-53 Mod for CMMC L2 readiness" |

### 5.3. UC body — structure

After the YAML frontmatter:
1. **Scenario** (3-5 sentences): the actual engagement
2. **Inputs** (JSON or structured): what the auditor feeds in
3. **Procedure** (numbered, 5-10 steps): the workflow
4. **Expected outputs** (per the frontmatter `expected_outputs` list)
5. **Oracle** (per the frontmatter `oracle` field): the right answer
6. **Variations** (optional): edge cases and what changes

## 6. `data/` — generators, seeds, crosswalks

### 6.1. `data/generators/gen_*.py` — deterministic Python CLIs

Each generator MUST:
- Accept `--seed N` (default 0)
- Accept `--out path/to/output.json`
- Produce byte-identical output for the same seed
- Use `random.seed(seed)` at the top of the function
- Be runnable from the command line: `python skills/nist-csf-2/data/generators/gen_*.py --seed 42 --out foo.json`
- Include a module-level `if __name__ == "__main__":` block
- No external dependencies beyond stdlib + `jsonschema` (already in CI)

### 6.2. `data/seeds/*.json` — fixture JSONs

Each seed MUST:
- Be valid JSON
- Have a top-level `seed_version` field (semver) — *self-imposed convention, not enforced by the linter or test suite. Exists for future-proofing cross-skill seed diffing.*
- Reference no real organization names, no real personal data
- Match one of the input shapes declared in a UC's `data_refs` field
- Be loadable by the test suite without errors

### 6.3. `data/crosswalks/*.json` — framework mappings

Each crosswalk MUST:
- Be valid JSON
- Use the format `{"from_subcategory": "GV.OC-01", "to_framework": "800-53", "to_controls": ["PM-9", "PM-11"], "rationale": "..."}`
- Include a `mapping_source` URL field for traceability
- Be referenced from `chunks/08-informative-references-crosswalk.md`

**Format divergence note:** The 800-53 RMF skill's `skills/nist-800-53-rmf/data/crosswalks/soc2-to-800-53-mod.json` uses the format `{"soc2_id": ..., "nist_800_53_id": ..., "strength": ..., "note": ...}`. The CSF 2.0 format is intentionally different because CSF subcategories are 1-to-many to controls (vs. SOC 2 → 800-53 which is 1-to-1 to a small set). Any cross-skill parser that consumes crosswalks MUST support both shapes — coordinate with the 800-53 RMF skill maintainer if you need a unified parser.

## 7. `tests/` — 9 test files + stub

### 7.1. The 9 test files (locked)

| File | Tests | What |
|------|-------|------|
| `test_nist_csf_2_lint.py` | 1 | Runs `tools/lint_skill.py`, asserts exit 0 |
| `test_nist_csf_2_oracle.py` | 4-5 | UC-01/02/03 outputs match expected + parametrized stub-output |
| `test_nist_csf_2_grounding.py` | 3-4 | In-body citations resolve, manifest labels cited, no orphans |
| `test_nist_csf_2_trace.py` | 2-3 | UC procedures cite real SKILL.md sections; chunks referenced in SKILL.md exist |
| `test_nist_csf_2_metamorphic.py` | 2-3 | Rephrased inputs produce equivalent outputs; ordering invariance |
| `test_nist_csf_2_adversarial.py` | 3-4 | Tier 0 org, empty profile, contradictory tiers |
| `test_nist_csf_2_telemetry.py` | 5-6 | Schema validates, instrument emits event, name pattern, use-case pattern, industry enum, oracle enum |
| `test_nist_csf_2_consistency.py` | 4-5 | Routing table ↔ chunks, manifest ↔ body, industry/UC sync, cross-skill refs |
| `test_nist_csf_2_08_chunk.py` | 4-5 | Chunk 08 (crosswalk) has frontmatter, fits 200 lines, is in SKILL.md routing. **One chunk-test file is sufficient** (chunk 08 is the most assertion-heavy, with crosswalk JSON shape to validate). The design template's "per-chunk test" pattern is a *target*, not a *requirement* — see `docs/skill-design-template.md` §5 for the rationale. |
| `nist_csf_2_stub.py` | n/a | The deterministic reference executor (called by oracle tests) |

### 7.2. The stub (`nist_csf_2_stub.py`)

MUST:
- Export `def run_skill(uc_id: str, payload: dict) -> dict`
- Accept `UC-01`, `UC-02`, `UC-03`
- Return a dict with the keys listed in the UC's `expected_outputs` frontmatter
- Be deterministic (no random, no LLM, no network)
- Match the oracle assertions in `test_nist_csf_2_oracle.py` exactly

### 7.3. Test target: ≥30 tests, 0 failures

## 8. `telemetry/` — 4 files, shared schema

### 8.1. The 4 files

| File | Content |
|------|---------|
| `schema.json` | The `SkillInvocation` JSON Schema (copy from nist-800-53-rmf, customize `skill_name` to `nist-csf-2`) |
| `instrument.py` | The `@instrumented` decorator (copy from nist-800-53-rmf, customize skill constant) |
| `redaction.md` | PII/NPI/PHI redaction policy (synthetic-only, reference the gen_*.py contract) |
| `baseline.md` | p50/p90/p99 token use — measured after first instrumented run; for v0.1.0 ship with placeholder values, update Day 5 |

## 9. `docs/` — 4 files

| File | Content |
|------|---------|
| `docs/architecture.md` | How the skill is structured (mirror the nist-800-53-rmf version, customized) |
| `docs/limits-and-disclaimers.md` | What this skill is NOT, anti-hallucination, version drift risks |
| `docs/changelog.md` | Initial entry: "v0.1.0 — initial build per design doc csf-2-design.md" |
| `docs/acceptance-gate.md` | Sign-off checklist — all 30 tests pass, linter passes, 5-lens review done, 5-practitioner review done, no open CRITICAL/HIGH findings |

## 10. `README.md` — consumer one-pager

The README is the first file a consumer sees. It MUST:
- Be ≤200 lines
- Have YAML frontmatter: `name`, `description`, `version`, `industries`, `tags`
- Open with a 2-3 sentence summary
- Show 30-second quickstart (Path 1: system prompt)
- Show 5-minute quickstart (Path 2: stub executor)
- List 3 industries with the 1-line angle for each
- List 3 UCs with 1-line scenario for each
- Link to the design doc and the consumer one-pager

## 11. `assets/` — optional, only if needed

The design doc does not require any assets for CSF 2.0. The folder is not required by the linter. Skip unless a chunk needs a diagram.

## 12. Summary checklist (build Day 5 sign-off)

Before declaring v0.1.0 done, every item MUST be true:

- [ ] All 5 skills (incl. new CSF 2.0) pass `python tools/lint_skill.py skills/*/`
- [ ] `pytest skills/ tests/ -q` returns 0 failures, total ≥220 tests (190 existing + ≥30 new)
- [ ] 5-lens review dispatched and all findings addressed or explicitly deferred
- [ ] 5-practitioner review dispatched and all findings addressed or explicitly deferred
- [ ] No open CRITICAL or HIGH findings
- [ ] All MEDIUM and LOW findings either fixed or documented in `docs/changelog.md`
- [ ] `docs/acceptance-gate.md` updated and signed
- [ ] PR opened with all 3 required status checks green
- [ ] LinkedIn post (Wk 5 drip) drafted and ready
- [ ] Linear SOX-569 state moved to Done

---

**This document is the spec. The design doc is the why. The lint is the floor. The reviews are the proof.**

— End of file requirements spec —
