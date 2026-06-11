# audit-workpapers

**Encode PCAOB AS 1215/AS 1105/AS 2315/AS 3105, AICPA AU-C 230, ISA 230, COSO ICIF-2013, and ISACA ITAF audit workpaper standards into your AI agent.**

Status: **draft v0.2.0**, on Tier 0 Spine, 44 tests passing, linter-clean. The skill uses the **router + chunks pattern** -- SKILL.md is the router, the deep-dive content lives in 9 chunk files loaded on demand. Retrofitted from a 2,060-line monolithic SKILL.md on 2026-06-03.

## Acronym key

| Acronym | Meaning |
|---|---|
| **BV** | Book value (population recorded amount) |
| **TM** | Tolerable misstatement |
| **RIA** | Risk of incorrect acceptance |
| **SI** | Sampling interval (BV ÷ sample size, or TM ÷ reliability factor) |
| **BP** | Basic precision (reliability factor × SI) |
| **ULM** | Upper limit on misstatement |
| **TD** | Tolerable deviation rate (= the risk of incorrect acceptance for an attribute test) |
| **PM** | Performance materiality · **RF** Reliability factor · **PEO/PFO** principal executive/financial officer |
| **C-C-C-E-R** | Condition · Criteria · Cause · Effect · Recommendation (the 5-part finding) |

---

## 30-second quick start (Path 1 -- system prompt)

```bash
git clone https://github.com/amurthygithub/Audit-skills.git
cd Audit-skills
pip install openai
export OPENAI_API_KEY=sk-...   # required: the quickstart calls the OpenAI API (Path 1)
```

```python
from openai import OpenAI

with open("skills/audit-workpapers/SKILL.md") as f:
    system_prompt = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "DESIGN a MUS sampling workpaper for AR. BV=$12.5M, RIA=5%, TM=$500K."},
    ],
)
print(response.choices[0].message.content)
```

The skill body handles sampling plan design, ULM calculation, finding documentation, and workpaper structure.

---

## Path 2 — packaged skill + telemetry

Every skill ships a deterministic reference executor (`tests/audit_workpapers_stub.py`) — the same one the test suite's oracle runs against — plus telemetry instrumentation. Run it against the shipped UC-01 seed:

```python
import sys, json
sys.path.insert(0, "skills/audit-workpapers")        # telemetry package
sys.path.insert(0, "skills/audit-workpapers/tests")  # stub executor

from audit_workpapers_stub import run_skill
from telemetry.instrument import instrumented

# Wrap with telemetry — every call appends a SkillInvocation event
# to telemetry/events.jsonl (override with SOXFLOW_TELEMETRY_PATH)
@instrumented(skill="audit-workpapers", skill_version="0.2.0",
              default_use_case_id="UC-01", default_industry="financial-services")
def design_sampling(payload):
    return run_skill("UC-01", payload)

payload = json.load(open("skills/audit-workpapers/data/seeds/uc-01-input.json"))
result = design_sampling(payload)

print(result["classification"])                          # → "MUS_SAMPLE_SIZE_75"
print(result["mus_evaluation"]["sample_size"])           # → 75
print(result["mus_evaluation"]["sampling_interval"])     # → 166667
```

Verify it works:

```bash
pytest skills/audit-workpapers/tests/ -q
# → 42 passed
```

---

## 5-minute deep dive

### Industry use cases

| Scenario | Industry | What the skill produces |
|----------|----------|------------------------|
| AR MUS sampling workpaper | Financial services | Sample size 75, SI=$166,667, ULM evaluation, conclusion |
| AP cutoff 5-part finding | Public sector / SaaS | C-C-C-E-R, severity = Significant Deficiency |
| Revenue TD calculation | Public-company | AR=5%, IR=80%, CR=60%, AP=50% => TD=20.8% |
| ICFR material weakness | Financial services | MW indicator analysis, compensating control evaluation |
| IPE validation log | SaaS / technology | Completeness/accuracy testing, source x purpose classification |
| Engagement completion doc | Public-company | Per AS 1215.13, full 5W1H sign-off, EQR review |

### What this skill does

| Function | What the skill produces | Use case |
|----------|------------------------|----------|
| MUS sampling | Sample size, sampling interval, ULM, conclusion | UC-01 |
| Finding documentation | 5-part C-C-C-E-R finding with severity | UC-02 |
| Risk model | TD computation from IR/CR/AP, RIA mapping | UC-03 |
| Workpaper structure | Indexing (A-N), cross-refs, tickmarks, sign-off | (router) |
| Evidence documentation | Evidence hierarchy, re-performance, IPE | (router) |
| Output templates | WP, sampling WP, finding, ECD | (router) |
| Quality/compliance | Checklist, compliance rules, crosswalks | (router) |
| Draft report / recomputation | ICFR report, management letter, re-computation | (router) |

### Who this is for

- **Public-company auditors** performing PCAOB-regulated financial statement and ICFR audits.
- **Internal audit teams** building SOX 404 documentation and control testing workpapers.
- **Pre-IPO companies** establishing workpaper infrastructure for SOX readiness.
- **Government auditors** performing Yellow Book / GAO audits and single audits.
- **IT auditors** documenting ISACA ITAF-compliant IT audit workpapers.
- **Audit quality reviewers** ensuring documentation meets AS 1215 experienced auditor standard.

---

## Industry views

| Industry | File | Posture | Top use cases |
|----------|------|---------|---------------|
| Public-company financial services | industries/financial-services.md | PCAOB-regulated, ICFR/SOX 404, MUS sampling | UC-01, UC-03 |
| Government / public sector | industries/public-sector.md | Yellow Book / GAO, single audit, 5-part findings | UC-02 |
| Pre-IPO SaaS / technology | industries/saas-technology.md | SOX 404 readiness, workpaper infrastructure | UC-01, UC-02 |
| Healthcare provider / payer | industries/healthcare.md | PHI-in-evidence handling, HIPAA retention interplay, patient-AR sampling | UC-01, UC-02 |

---

## Use cases

### UC-01 -- MUS sampling workpaper for accounts receivable
**Scenario:** XYZ Corp. AR = $12.5M. MUS at 5% RIA, TM=$500K. Outputs: sample size 75, SI=$166,667 (display), BP=$500,000 (= TM).
File: use-cases/uc-01-sampling-workpaper.md | Status: draft

### UC-02 -- 5-part finding (C-C-C-E-R) for AP cutoff control gap
**Scenario:** AP cutoff testing reveals 16% deviation rate. Root cause: receiving/AP communication gap. Outputs: 5-part finding, severity = Significant Deficiency.
File: use-cases/uc-02-five-part-finding.md | Status: stub

### UC-03 -- Audit risk model TD calculation for revenue testing
**Scenario:** Complex revenue (ASC 606). AR=5%, IR=80%, CR=60%, AP=50%. Outputs: TD=20.8%, moderate RIA, moderate-large sample.
File: use-cases/uc-03-risk-model-td-calculation.md | Status: stub

---

## Context budget (declared in frontmatter)

| Tier | Tokens | What |
|------|--------|------|
| always_loaded_tokens | 3,000 | SKILL.md (router) -- always in context |
| per_call_typical_tokens | 6,000 | router + 1 chunk + 1 industry + 1 use case |
| per_call_max_tokens | 15,000 | router + all chunks + industry + UC |
| per_call_p90_tokens | 8,000 | measured after first instrumented run |

---

## The 9 chunks (audit domain aligned)

| Chunk | Topic | When to load |
|-------|-------|--------------|
| chunks/01-standards-and-structure.md | Standards, indexing (A-N), tickmarks, AS 1215.04-.07, sign-off | "workpaper structure", "indexing", "tickmarks", "AS 1215", "sign-off" |
| chunks/02-evidence-and-reperformance.md | Evidence types/hierarchy (AS 1105), re-performance, IPE validation | "evidence hierarchy", "AS 1105", "re-performance", "IPE validation", "recomputation" |
| chunks/03-sampling.md | MUS/PPS, attribute, variables, non-statistical, ULM evaluation | "sampling plan", "MUS", "attribute sampling", "variables", "ULM" |
| chunks/04-risk-and-opinion.md | Audit risk model (AR=IRxCRxAPxTD), opinion (AS 3105) | "audit risk model", "AR = IR x CR", "TD calculation", "opinion", "material weakness" |
| chunks/05-finding-and-workflow.md | 5-part C-C-C-E-R format, 7-step workflow | "audit finding", "C-C-C-E-R", "workflow", "7-step", "draft a report" |
| chunks/06-outputs-electronic-review.md | Output templates, electronic WP, review | "workpaper templates", "electronic workpapers", "retention", "review" |
| chunks/07-qc-compliance-cross-refs.md | Quality checklist, compliance rules, cross-reference, glossary | "quality checklist", "compliance", "cross-reference", "glossary" |
| chunks/08-questionnaire-reuse.md | CAIQ, SIG Lite, VSAQ, customer questionnaire evidence reuse from audit workpaper evidence | "CAIQ" / "SIG Lite" / "VSAQ" / "questionnaire" / "workpaper evidence" |

Per-call cost: 3,000-6,000 tokens (vs. ~40,000 for the 2,060-line monolithic version).

---

## What is in the box

```
skills/audit-workpapers/
  README.md                     # this file
  SKILL.md                      # the router (always loaded)

  chunks/                       # deep-dive content (loaded on demand)
    01-standards-and-structure.md
    02-evidence-and-reperformance.md
    03-sampling.md
    04-risk-and-opinion.md
    05-finding-and-workflow.md
    06-outputs-electronic-review.md
    07-qc-compliance-cross-refs.md
    08-questionnaire-reuse.md
    09-substantive-analytical-procedures.md

  industries/                   # 4 industry-shaped views
    _index.md
    financial-services.md
    public-sector.md
    saas-technology.md
    healthcare.md

  use-cases/                    # 3 use cases
    _index.md
    uc-01-sampling-workpaper.md
    uc-02-five-part-finding.md
    uc-03-risk-model-td-calculation.md

  data/
    README.md
    generators/gen_mus_population.py
    seeds/uc-01-input.json, uc-02-input.json, uc-03-input.json

  tests/                        # 42 tests via 6 skill-specific files (lint + consistency run from repo root)
    audit_workpapers_stub.py
    test_audit_workpapers_oracle.py
    test_audit_workpapers_{grounding,trace,metamorphic,adversarial,telemetry}.py

  docs/
    architecture.md
    limits-and-disclaimers.md
    changelog.md
    acceptance-gate.md
```

---

## Testing

```bash
# Lint (Tier 0a -- Spine compliance)
python tools/lint_skill.py skills/audit-workpapers
# -> [PASS] skills/audit-workpapers

# Tests (4 across 2 files)
pytest skills/audit-workpapers/tests/ -v
# -> 4 passed
```

---

## Cross-skill assets

- **Board-ready audit committee deck**: `aicpa-soc-reporting/assets/board_deck_template.md` — 20-slide template for quarterly board presentations. Cross-referenced by all 5 Tier 0 Spine skills.

## Known limitations

- **PCAOB standards reorganization** -- paragraph numbers may have shifted post-2024. Verify against current PCAOB publications.
- **Sample size tables** -- illustrative. Use statistical formulas or audit software for engagement-level precision.
- **ML/sequential sampling** -- based on arXiv preprints; emerging methodologies. Validate against current professional standards.
- **LLM executor** -- stub in v0.2.0. Production executor ships in SOX-611 Phase 2.
- **Original 2,060-line SKILL.md** preserved as SKILL.md.bak (archived to _archive/).

---

## Disclaimer

This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source (current PCAOB AS 1215, AS 1105, AS 2315, AS 3105, AICPA AU-C 230, ISA 230, COSO ICIF-2013, and ISACA ITAF).
