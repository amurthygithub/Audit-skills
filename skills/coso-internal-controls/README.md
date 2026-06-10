# coso-internal-controls

**Encode COSO 2013 ICIF, COSO 2017 ERM, SOX 404, PCAOB AS 2201, and COSO emerging tech guidance into your AI agent.**

Status: **draft v0.2.0**, on Tier 0 Spine, linter-clean (pending). The skill uses the **router + chunks pattern** — SKILL.md is a 214-line router, the deep-dive content lives in 7 chunk files loaded on demand. The skill body is real (full decision logic, output templates, citation manifest); the LLM-backed executor is a stub. Production executor ships in SOX-611 Phase 2.

---

## Context budget (declared in frontmatter)

| Tier | Tokens | What |
|------|--------|------|
| always_loaded_tokens | 3,000 | SKILL.md (router) — always in context |
| per_call_typical_tokens | 6,000 | router + 1 chunk + 1 industry + 1 use case |
| per_call_max_tokens | 15,000 | router + all chunks + industry + UC |
| per_call_p90_tokens | 8,000 | measured after first instrumented run |

## The 7 chunks

| Chunk | Topic | When to load |
|-------|-------|-------------|
| chunks/01-coso-icif.md | COSO 2013 ICIF — 17 Principles with Points of Focus | "Assess COSO principles", "Evaluate ICIF", "P1-P17" |
| chunks/02-coso-erm-monitoring.md | COSO 2017 ERM + COSO 2009 Monitoring | "Enterprise risk management", "COSO ERM", "Monitoring controls" |
| chunks/03-sox-pcaob.md | SOX 404 + PCAOB AS 2201 Top-Down Approach | "SOX 404", "PCAOB AS 2201", "integrated audit" |
| chunks/04-walkthrough-controls.md | Walkthrough Procedures + ELC Classification | "Walkthrough", "entity-level controls", "ELC" |
| chunks/05-deficiency-classification.md | Control Deficiency Classification Decision Tree | "Classify deficiency", "material weakness", "significant deficiency" |
| chunks/06-rcm-and-reports.md | RcM, Principle Assessment, ICFR Reports | "RcM", "risk and control matrix", "ICFR report" |
| chunks/07-compensating-updates-cross.md | Compensating Controls, Updates, Cross-References | "Compensating control", "RPA", "GenAI", "cross-reference" |
| chunks/08-questionnaire-reuse.md | CAIQ, SIG Lite, VSAQ, customer questionnaire evidence reuse from COSO/SOX 404 evidence | "CAIQ" / "SIG Lite" / "VSAQ" / "questionnaire" / "governance questionnaire" |

## 30-second quick start (Path 1 -- system prompt)

```bash
git clone https://github.com/amurthygithub/Audit-skills.git
cd Audit-skills
pip install openai
```

```python
from openai import OpenAI

with open("skills/coso-internal-controls/SKILL.md") as f:
    system_prompt = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": """
            Evaluate COSO ICIF Principle 10 (control activities) for a financial services firm.
            Assess Points of Focus and determine present/functioning status.
        """},
    ],
)
print(response.choices[0].message.content)
```

The skill body handles COSO ICIF principle evaluation, SOX 404 ICFR assessment, deficiency classification, and RcM output.

---

## Path 2 — packaged skill + telemetry

Every skill ships a deterministic reference executor (`tests/coso_internal_controls_stub.py`) — the same one the test suite's oracle runs against — plus telemetry instrumentation. Run it against the shipped UC-01 seed:

```python
import sys, json
sys.path.insert(0, "skills/coso-internal-controls")        # telemetry package
sys.path.insert(0, "skills/coso-internal-controls/tests")  # stub executor

from coso_internal_controls_stub import run_skill
from telemetry.instrument import instrumented

# Wrap with telemetry — every call appends a SkillInvocation event
# to telemetry/events.jsonl (override with SOXFLOW_TELEMETRY_PATH)
@instrumented(skill="coso-internal-controls", skill_version="0.2.0",
              default_use_case_id="UC-01", default_industry="financial-services")
def assess_icfr(payload):
    return run_skill("UC-01", payload)

payload = json.load(open("skills/coso-internal-controls/data/seeds/uc-01-input.json"))
result = assess_icfr(payload)

print(result["classification"])          # → "EFFECTIVE_WITH_SD"
print(result["rcm"]["key_controls"])      # → 28
```

Verify it works:

```bash
pytest skills/coso-internal-controls/tests/ -q
# → 30 passed
```

---

## What this skill does

| Task | What the skill produces | Use case |
|------|------------------------|----------|
| COSO principle evaluation | Present/functioning assessment per principle with PoF analysis, integrated operation evaluation | — |
| SOX 404 ICFR assessment | RcM (17 columns), walkthrough documentation, deficiency classification | UC-01 |
| Deficiency classification | D/SD/MW classification with 3-step decision tree, MW indicator check, compensating control analysis | UC-02 |
| Management ICFR Report | Complete report per SEC Reg S-K Item 308 | UC-01 |
| Compensating control evaluation | 6-step evaluation with precision test and severity impact | UC-02 |
| Cross-framework mapping | COSO to TSC, COBIT, NIST, ISO 31000, SOX, PCAOB | — |
| Emerging tech assessment | RPA, GenAI, ICSR controls mapped to COSO principles | — |

## Who this is for

- **Public-company financial services** performing SOX 404 ICFR assessments.
- **Pre-IPO SaaS companies** preparing for SOX 404 readiness.
- **Audit firms** scoping, documenting, or reviewing ICFR engagements.
- **Federal/state government** applying COSO via OMB A-123 or Single Audit.
- **GRC platform builders** embedding COSO expertise without hiring COSO SMEs.

## Industry views

| Industry | File | Posture | Top use cases |
|----------|------|---------|---------------|
| Public-company financial services | industries/financial-services.md | SOX 404(a)+(b); full COSO ICIF | UC-01, UC-02 |
| Federal/state government | industries/public-sector.md | OMB A-123; Single Audit | (planned UC-03) |
| Pre-IPO SaaS / technology | industries/saas-technology.md | SOX 404 readiness; RPA/GenAI | UC-02 |

## Testing

```bash
python tools/lint_skill.py skills/coso-internal-controls
pytest skills/coso-internal-controls/tests/ -v
```

## What is in the box

```
skills/coso-internal-controls/
  README.md
  SKILL.md                     # the router (214 lines, always loaded)
  SKILL.md.bak                 # original monolithic 1,879-line version (preserved)
  chunks/                      # 7 deep-dive files loaded on demand
  industries/                  # 3 industry views
  use-cases/                   # 2 worked examples (stub)
  data/                        # data dictionary
  tests/                       # conftest.py, test_lint.py
  telemetry/                   # schema, instrument, redaction, baseline
  docs/                        # architecture, limits, changelog, acceptance-gate
```

## Cross-skill assets

- **Board-ready audit committee deck**: `aicpa-soc-reporting/assets/board_deck_template.md` — 20-slide template for quarterly board presentations. Cross-referenced by all 5 Tier 0 Spine skills.

## Known limitations

- **71 of the Points of Focus** are listed (curated subset).
- **PCAOB AS 2201 paragraph numbers** were reorganized; verify against current PCAOB codification.
- **Materiality thresholds** are entity-specific; the skill cannot determine materiality.
- **Stub executor** — real LLM-backed executor ships in SOX-611 Phase 2.

## Disclaimer

This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source (COSO 2013 ICIF, COSO 2017 ERM, PCAOB AS 2201 current codification, SEC Reg S-K Item 308).
