---
name: TEMPLATE
description: "TEMPLATE — copy this directory to start a new skill. Provides folder skeleton, frontmatter contract, section requirements, telemetry schema, and acceptance gate. NOT a real skill — used as the Spine that every published skill (e.g., nist-800-53-rmf) is built from."
category: audit
risk: safe
source: custom
date_added: "2026-06-03"
tags: [template, spine, scaffold]
version: 0.1.0
status: template
---

# Skill Template (Tier 0 Spine)

> **This is not a published skill.** It is the scaffold that every published skill is built from.
> To create a new skill: `cp -r skills/TEMPLATE skills/<new-skill-name>`, then replace the placeholders.

---

## 1. Folder Contract (mandatory)

Every published skill MUST have exactly this layout. The linter (Tier 0a, SOX-616) fails on any deviation.

```
skills/<skill-name>/
  SKILL.md                    # Frontmatter + body. See §2.
  chunks/                     # OPTIONAL but REQUIRED if SKILL.md > 300 lines.
                              # Deep-dive files loaded on demand by the LLM agent.
                              # See §11 (Context Budget & Chunks Pattern).
    01-<topic>.md             # Numbered, kebab-case, ≤ 200 lines each.
    02-<topic>.md
    ...
  industries/                 # ≥3 industry-shaped views of the skill.
    _index.md                 # Industry registry (table: name, file, scope, top use-cases)
    financial-services.md     # Required for FIN-touching skills; recommended otherwise.
    healthcare.md             # Required for HIPAA/PHI-touching skills; recommended otherwise.
    saas-technology.md        # Recommended for IT/cyber skills.
    public-sector.md          # Required for FedRAMP/CMMC-touching skills; recommended otherwise.
    manufacturing.md          # Optional.
    retail-ecommerce.md       # Optional.
    energy-utilities.md       # Optional.
  use-cases/                  # ≥3 worked examples with full input/procedure/oracle shape.
    _index.md                 # UC registry (id, title, industries, status, token baseline)
    uc-NN-<slug>.md           # Standard template (see §4).
  data/                       # Synthetic datasets + generators (deterministic, seedable).
    _index.md                 # Dataset registry.
    README.md                 # Data dictionary + PII/NPI redaction policy.
    generators/               # One .py per dataset, --seed CLI.
    seeds/                    # Canonical seed fixtures (small/medium/large/edge).
  tests/                      # Executable test cases.
    conftest.py
    test_oracle.py            # Known-good input → known-good output.
    test_grounding.py         # Citations resolve, no hallucinated paragraph numbers.
    test_trace.py             # Output citations match SKILL.md §X.
    test_metamorphic.py       # Input mutation → expected output mutation.
    test_judge.py             # LLM-as-judge for qualitative outputs.
    test_adversarial.py       # Tricky/edge inputs (compensating controls, dual classification).
    test_telemetry.py         # Token baseline assertions.
    test_lint.py              # Linter self-check.
  telemetry/                  # Instrumentation.
    schema.json               # Per-call event schema (see §6).
    instrument.py             # Decorator/context-manager that wraps skill invocations.
    baseline.md               # p50/p90/p99 token use after first run.
    redaction.md              # PII/NPI redaction rules.
  docs/                       # Long-form documentation.
    architecture.md           # How the skill is built and intended to be invoked.
    limits-and-disclaimers.md # Anti-hallucination, regulatory currency, known gaps.
    changelog.md              # Versioned change log.
    acceptance-gate.md        # Checklist to publish.
```

**Folder-naming rule:** kebab-case. Singular. No spaces. No version suffix in folder name.

**SKILL.md size rule:** If `SKILL.md` exceeds **300 lines**, the `chunks/` folder is **required** and `SKILL.md` must follow the router pattern (§11). The linter enforces this.

---

## 2. SKILL.md Frontmatter Contract

The linter enforces the following YAML fields. All are required unless marked optional.

```yaml
---
name: <skill-name>                        # REQUIRED. kebab-case. matches folder name.
description: "<single-sentence activation trigger>"   # REQUIRED. ≤1,200 chars. Be specific.
category: <audit|legal|finance|...>       # REQUIRED. one of registered categories.
risk: <safe|low|medium|high|critical>     # REQUIRED. impact of bad output.
source: "<provenance string>"             # REQUIRED. e.g., "NIST SP 800-53 Rev 5, FIPS 199, OMB A-130"
date_added: YYYY-MM-DD                    # REQUIRED. ISO 8601.
version: <semver>                         # REQUIRED. start at 0.1.0.
status: <draft|review|published|deprecated>  # REQUIRED.
industries: [<list>]                      # REQUIRED. See §3. Min 3.
frameworks: [<list>]                      # REQUIRED. ISO/standard identifiers.
telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"  # REQUIRED. JSON pointer to schema.
token_baseline_target:                    # OPTIONAL. Aspirational baseline; revised by real measurement.
  input_p90: <int>
  output_p90: <int>
context_budget:                          # REQUIRED. See §11.
  always_loaded_tokens: <int>            # tokens of SKILL.md router
  per_call_typical_tokens: <int>         # typical full invocation
  per_call_max_tokens: <int>             # worst case
  per_call_p90_tokens: <int>             # measured after first instrumented run
tags: [<list>]                            # REQUIRED. Min 5. Lowercase.
---
```

**Naming rule:** `name` MUST equal the folder name. `version` is `MAJOR.MINOR.PATCH` and incremented per `docs/changelog.md`.

---

## 3. Body Section Contract

The body MUST have, in order, these top-level sections (##):

| § | Title | Required | Notes |
|---|-------|----------|-------|
| 1 | When to Use / Not Use This Skill | YES | Trigger and anti-trigger lists. |
| 2 | Framework Overview | YES | Source, scope, authoritative documents. |
| 3 | Core Concepts / Taxonomy | YES | Domain model the skill encodes. |
| 4 | Decision Logic | YES | Executable (IF/THEN/ELSE) where applicable. |
| 5 | Procedure Templates | YES | Step-by-step playbooks. |
| 6 | Output Templates | YES | What the skill produces; paste-able. |
| 7 | Cross-References | YES | Mappings to other skills/standards. |
| 8 | Worked Examples (high-level) | YES | 1-line summaries; full text in `use-cases/`. |
| 9 | Anti-Hallucination Disclaimers | YES | Explicit caveats. |
| 10 | References & Citation Manifest | YES | Every cited source with retrieval date. |
| 11 | Routing & Context Budget (only if SKILL.md > 300 lines) | YES if applicable | Maps user intent → chunks to load; declares `context_budget`. |

Sections 1-10 are always required and in order. Section 11 is required when the skill uses the chunks pattern (i.e., when the body exceeds 300 lines after §1-§10). Additional sections (e.g., `## 12. Appendix`) are allowed but not required.

---

## 4. Use-Case File Template (`use-cases/uc-NN-<slug>.md`)

Every use case MUST follow this shape so the test harness can parse it.

```markdown
---
uc_id: UC-NN                              # REQUIRED. Unique within skill.
title: "<short title>"                    # REQUIRED.
industries: [<list>]                      # REQUIRED. ≥1.
frameworks: [<list>]                      # REQUIRED.
inputs:                                   # REQUIRED. Free-form but parsed.
  artifact_1: "<description + sample>"
  artifact_2: "<description + sample>"
procedure:                                # REQUIRED. Steps referencing SKILL.md §X.
  - "§5.2 — Categorize system (FIPS 199)"
  - "§5.3 — Select baseline (800-53)"
  - "§6.1 — Produce output"
expected_outputs:                         # REQUIRED. What the oracle asserts.
  artifact_X: "<exact format + sample>"
oracle:                                   # REQUIRED. The test's pass/fail.
  type: <exact_match|schema_match|llm_judge|metamorphic>
  assertion: "<one-line>"
data_refs:                                # REQUIRED. Paths under data/.
  - "data/seeds/uc-NN-input.json"
tests:                                    # REQUIRED. Test files that exercise this UC.
  - "tests/test_oracle.py::test_uc_NN"
token_baseline:                           # OPTIONAL. Measured after run.
  input_p50: <int>
  output_p50: <int>
status: <draft|active|deprecated>         # REQUIRED.
---

# UC-NN — <title>

(full prose walkthrough — scenario, walk-through, decision points, output samples)
```

---

## 5. Test File Convention

Every test file follows pytest naming. Tests MUST be deterministic (use seeds, not network). Tests that require an LLM (judge tests) MUST mock the LLM call in CI and gate the real-LLM run behind an env var.

```python
# tests/test_oracle.py
import json, pathlib, pytest
DATA = pathlib.Path(__file__).parent.parent / "data"
SEEDS = DATA / "seeds"

@pytest.mark.parametrize("uc_id,expected", [
    ("UC-01", {"categorization": "MODERATE", "baseline": "MOD"}),
    ("UC-02", {"ato_decision": "ATO_WITH_CONDITIONS", "poam_count": 22}),
    ("UC-03", {"overlap_pct_min": 70, "gap_controls_max": 100}),
])
def test_uc_oracle(uc_id, expected):
    inp = json.loads((SEEDS / f"{uc_id.lower()}-input.json").read_text())
    out = run_skill(inp)  # imported from the skill's invocation entrypoint
    assert_oracle(out, expected)
```

---

## 6. Telemetry Schema (required fields)

Every skill MUST publish `telemetry/schema.json` with this top-level shape. The instrumentation decorator (`telemetry/instrument.py`) emits one event per invocation.

```json
{
  "$defs": {
    "SkillInvocation": {
      "type": "object",
      "required": [
        "skill", "skill_version", "use_case_id", "industry",
        "model", "input_tokens", "output_tokens", "total_tokens",
        "latency_ms", "cache_hit", "classification",
        "oracle_result", "timestamp", "redaction_applied"
      ],
      "properties": {
        "skill": {"type": "string"},
        "skill_version": {"type": "string"},
        "use_case_id": {"type": "string"},
        "industry": {"type": "string"},
        "model": {"type": "string"},
        "input_tokens": {"type": "integer", "minimum": 0},
        "output_tokens": {"type": "integer", "minimum": 0},
        "total_tokens": {"type": "integer", "minimum": 0},
        "latency_ms": {"type": "integer", "minimum": 0},
        "cache_hit": {"type": "boolean"},
        "classification": {"type": "string", "description": "skill-specific primary output, e.g., MODERATE / ATO_WITH_CONDITIONS / DEFICIENCY_MW"},
        "oracle_result": {"enum": ["pass", "fail", "skipped", "n/a"]},
        "timestamp": {"type": "string", "format": "date-time"},
        "redaction_applied": {"type": "boolean"}
      }
    }
  }
}
```

The redaction field is mandatory: if `true`, the event has been stripped of PII/NPI/PHI; if `false`, the event MUST NOT contain raw inputs.

---

## 7. Acceptance Gate

A skill can be marked `status: published` only when ALL of the following pass:

- [ ] Linter (`tools/lint_skill.py`) passes — frontmatter, sections, folders, citations.
- [ ] ≥3 industry files, ≥3 use-case files, all with status `active`.
- [ ] ≥3 test files, all passing locally and in CI.
- [ ] `telemetry/schema.json` validates.
- [ ] `telemetry/baseline.md` populated after at least one instrumented run on each use case.
- [ ] `docs/architecture.md`, `docs/limits-and-disclaimers.md`, `docs/changelog.md`, `docs/acceptance-gate.md` present and non-stub.
- [ ] No TODO/FIXME outside `docs/changelog.md` (the linter enforces this).
- [ ] `frameworks:` frontmatter list matches citations in §7 of `SKILL.md`.
- [ ] Reviewed by the Reviewer agent (3-cycle protocol, see `docs/architecture.md`).

---

## 8. Versioning

- **MAJOR** — breaking change to the skill's decision logic (e.g., new classification rule).
- **MINOR** — new section, new use case, new industry, backward-compatible.
- **PATCH** — wording fix, citation correction, no semantic change.

`docs/changelog.md` MUST be updated on every change with: date, version, summary, breaking-change flag.

---

## 9. Anti-Hallucination Discipline

Every SKILL.md MUST contain a `## 9. Anti-Hallucination Disclaimers` section that explicitly flags:
- Reconstructed numbering (e.g., ITAF S1-S18, COSO 71/81 Points of Focus).
- Citation dates and "verify against current publication" prompts.
- Any domain where the skill's output should NOT be relied on without human review.
- The line: "This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source."

---

## 10. References & Citation Manifest

`## 10. References & Citation Manifest` lists every source cited in the body, with:
- Title
- Author/Publisher
- Identifier (e.g., "NIST SP 800-53 Rev 5")
- Retrieval date (ISO 8601)
- URL (if public)
- Local copy path (if bundled under `docs/references/`)

The linter verifies that every in-body citation of the form `[XYZ §N]` is listed in this section.

---

## 11. Context Budget & Chunks Pattern

LLM context windows are finite. A monolithic `SKILL.md` of 1,500+ lines costs **~30,000-40,000 tokens per call** even when most of it is irrelevant to the user's question. That kills latency, blows the budget, and hurts quality (context rot).

The Spine enforces a context-budget discipline.

### 11.1 The rule

- **`SKILL.md` MUST be ≤ 300 lines.** If your skill body is longer, split it.
- **Above 300 lines**, the `chunks/` folder is required. `SKILL.md` becomes a **router** — it contains the always-loaded preamble, the routing table, and the references manifest. The chunks are loaded on demand.
- **Each chunk** is numbered (`01-`, `02-`, …), kebab-case, and ≤ 200 lines.
- **Frontmatter `context_budget` is required** (see below). The linter enforces the budget if present.

### 11.2 Router pattern (what `SKILL.md` looks like above 300 lines)

```
SKILL.md (≤ 300 lines, always loaded):
  - frontmatter (with context_budget)
  - §1 When to use / not use
  - §2 Framework overview (one paragraph + table)
  - §3 Core concepts (one screen, links into chunks)
  - §11 Routing table (maps user intent → chunks to load)
  - §12 Operational quick-reference (the minimum cycle)
  - §10 References & citation manifest

chunks/01-categorize.md   (FIPS 199 + decision logic + procedure + output)
chunks/02-baseline.md     (select + tailor)
chunks/03-implement.md    (SSP narrative)
chunks/04-assess.md       (800-53A + SAR)
chunks/05-authorize.md    (ATO + POA&M)
chunks/06-monitor.md      (ISCM)
chunks/07-crosswalk.md    (other frameworks)
```

### 11.3 Routing table (lives in `SKILL.md §11`)

```markdown
## Routing

| User intent | Load chunk(s) | Load industry | Load use-case |
|-------------|---------------|---------------|---------------|
| "Categorize this system" | chunks/01-categorize.md | industries/<match>.md | use-cases/uc-01-... |
| "Help with FedRAMP Moderate" | chunks/01, 02, 03, 04, 05 | industries/public-sector.md | use-cases/uc-01 |
| "Map SOC 2 to 800-53" | chunks/07-crosswalk.md | industries/financial-services.md | use-cases/uc-03 |
| ... | | | |
```

The LLM agent reads the routing table and loads only what's needed. Per-call cost: **3,000-6,000 tokens** instead of 30,000+.

### 11.4 `context_budget` frontmatter (required)

```yaml
context_budget:
  always_loaded_tokens: 3000     # tokens of SKILL.md router (measured or estimated)
  per_call_typical_tokens: 6000  # typical full invocation
  per_call_max_tokens: 15000     # worst case (router + all chunks + industry + UC)
  per_call_p90_tokens: 8000      # measured after first instrumented run
```

The linter enforces the 300-line SKILL.md rule, the existence of `chunks/` when SKILL.md > 300 lines, and the presence of `context_budget` in the frontmatter.

### 11.5 When NOT to use chunks

- **Skill body ≤ 300 lines** — keep it in one file. The overhead of routing is not worth it.
- **Skill is one-question-one-answer** (e.g., a single calculator) — chunks add no value.
- **Skill is brand new and the body is still moving** — keep it monolithic until it stabilizes, then split.

### 11.6 When to use chunks (always, in practice)

- Any skill with **decision logic** (IF/THEN/ELSE branches, ATO logic, deficiency classification).
- Any skill with **multiple procedure sections** (categorize, select, implement, assess, authorize, monitor, …).
- Any skill with **multiple output templates** (FIPS 199, SSP, SAR, POA&M, ATO letter).
- Any skill targeting **> 200 lines of body content** even if no individual section is large.

If in doubt, split. The cost of routing is one routing table; the cost of monolithic context rot is unbounded.
