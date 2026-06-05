# isaca-audit-methodology

**Encode ISACA CISA methodology, COBIT 2019, ITAF, ITGC/ITAC testing, risk-based audit planning, and 5-part audit observations into your AI agent.**

Status: **draft v0.2.0**, on Tier 0 Spine, linter-clean target. The skill uses the **router + chunks pattern** - `SKILL.md` is a 198-line router, the deep-dive content lives in 7 chunk files (each <= 200 lines) loaded on demand. The skill body is real (full decision logic, output templates, citation manifest); use cases are stubs.

---

## Context budget (declared in frontmatter)

| Tier | Tokens | What |
|------|--------|------|
| `always_loaded_tokens` | 3,200 | `SKILL.md` (router) - always in context |
| `per_call_typical_tokens` | 6,500 | router + 1 chunk + 1 industry + 1 UC |
| `per_call_max_tokens` | 16,000 | router + all chunks + industry + UC |
| `per_call_p90_tokens` | 8,500 | measured after first instrumented run |

---

## The 7 chunks

| Chunk | Topic | When to load |
|-------|-------|--------------|
| `chunks/01-framework-and-cisa.md` | ISACA Framework and CISA 5 Domains | "ISACA overview", "CISA domains", "CISA certification" |
| `chunks/02-cobit-2019.md` | COBIT 2019 Objectives (40) | "COBIT 2019", "COBIT objectives", "focus area" |
| `chunks/03-itaf-and-maturity.md` | ITAF Standards and Maturity Models | "ITAF", "audit standards", "maturity assessment" |
| `chunks/04-itgc-itac.md` | ITGC and ITAC Testing | "ITGC", "ITAC", "general controls", "application controls" |
| `chunks/05-risk-and-planning.md` | Risk-Based Audit Planning | "risk assessment", "audit plan", "risk score" |
| `chunks/06-observation-and-lifecycle.md` | 5-Part Observations and Audit Lifecycle | "audit observation", "5-part", "audit lifecycle" |
| `chunks/07-outputs-and-cross-refs.md` | Output Templates and Cross-References | "audit report template", "cross-reference", "mapping" |
| `chunks/08-questionnaire-reuse.md` | CAIQ, SIG Lite, VSAQ, customer questionnaire evidence reuse from ISACA/COBIT/ITGC evidence | "CAIQ" / "SIG Lite" / "VSAQ" / "questionnaire" / "ITGC" / "COBIT governance" |

---

## What this skill does

| Capability | What the skill produces | Use case |
|-----------|------------------------|----------|
| COBIT maturity assessment | Process capability assessment (0-5), gap analysis, improvement roadmap | UC-01 |
| ITGC testing | Control effectiveness assessment per 4 categories (access, change, ops, SDLC) | UC-02 |
| ITAC testing | Application control assessment (input, processing, output, data integrity) | UC-02 |
| 5-part observation | Structured finding: Condition, Criteria, Cause, Effect, Recommendation | UC-02 |
| Risk scoring | Risk register with (L x I) x CRF scoring, priority classification | UC-02 |
| Cross-framework mapping | ISACA to COSO, NIST CSF, ISO 27001, AICPA, ITIL | - |

---

## Who this is for

- **IT auditors** performing IS audit engagements per ISACA standards.
- **SaaS companies** pursuing SOC 2 readiness or COBIT maturity assessments.
- **Financial institutions** conducting ITGC testing for SOX 404 compliance.
- **Government agencies** adopting COBIT 2019 for IT governance.
- **GRC platform builders** embedding ISACA methodology without hiring CISA subject-matter experts.

---

## Industry-shaped use cases (stubs)

### Use case 1: SaaS COBIT 2019 maturity assessment

**Scenario:** 500-employee B2B SaaS company with SOC 2 Type II wants COBIT maturity for APO13, BAI07, DSS01.

```yaml
assessment:
  processes:
    - id: APO13
      current_maturity: 2.5
      target_maturity: 4
      gap: 1.5
  improvement_roadmap:
    - phase: "Quick Win (1-3 months)"
      gain: 0.5
```

Full deep-dive: [`use-cases/uc-01-it-audit-plan-saas.md`](use-cases/uc-01-it-audit-plan-saas.md) (stub).

### Use case 2: ITGC finding in 5-part observation format

**Scenario:** Commercial bank discovers access recertification gap during quarterly ITGC testing.

```yaml
finding:
  id: "ACC-2026-001"
  severity: "High"
  condition: "No recertification for 3 of 5 critical applications"
  criteria: "ISACA S17; Company Policy ISP-003; COBIT APO13.02"
  cause:
    root_cause_category: "Technology"
  recommendations:
    - type: "Primary"
      action: "Implement automated IGA tool"
```

Full deep-dive: [`use-cases/uc-02-five-part-observation.md`](use-cases/uc-02-five-part-observation.md) (stub).

---

## 30-second quick start (Path 1 - system prompt)

```bash
git clone https://github.com/amurthygithub/Audit-skills.git
cd Audit-skills
pip install openai
```

```python
from openai import OpenAI

with open("skills/isaca-audit-methodology/SKILL.md") as f:
    system_prompt = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": """
            Assess the COBIT 2019 maturity of security management (APO13)
            for a SaaS company with SIEM deployed, documented policies,
            but no automated access recertification.
        """},
    ],
)
print(response.choices[0].message.content)
```

---

## Path 2 -- packaged skill + telemetry (Coming in v0.3.0)

Path 2 (packaged skill with `skill_stub.py` executor and telemetry instrumentation) is planned for v0.3.0. Contact us for early access.

Until then, use Path 1 (system prompt) for all LLM calls. The linter and test infrastructure is functional:

```bash
python tools/lint_skill.py skills/isaca-audit-methodology
pytest skills/isaca-audit-methodology/tests/ -v
```

---

## What's in the box

```
skills/isaca-audit-methodology/
  README.md
  SKILL.md                     # router (198 lines, always loaded)
  SKILL.md.bak                 # original 1,662-line monolithic skill

  chunks/                      # deep-dive content (loaded on demand per S11 routing)
    01-framework-and-cisa.md
    02-cobit-2019.md
    03-itaf-and-maturity.md
    04-itgc-itac.md
    05-risk-and-planning.md
    06-observation-and-lifecycle.md
    07-outputs-and-cross-refs.md

  industries/                  # 3 industry-shaped views
    _index.md
    financial-services.md
    saas-technology.md
    public-sector.md

  use-cases/                   # 2 stub use cases
    _index.md
    uc-01-it-audit-plan-saas.md
    uc-02-five-part-observation.md

  data/
    README.md

  tests/
    conftest.py
    test_lint.py

  telemetry/
    schema.json
    instrument.py
    redaction.md
    baseline.md

  docs/
    architecture.md
    limits-and-disclaimers.md
    changelog.md
    acceptance-gate.md
```

---

## Testing

```bash
python tools/lint_skill.py skills/isaca-audit-methodology
pytest skills/isaca-audit-methodology/tests/ -v
```

---

## Cross-skill assets

- **Board-ready audit committee deck**: `aicpa-soc-reporting/assets/board_deck_template.md` — 20-slide template for quarterly board presentations. Cross-referenced by all 5 Tier 0 Spine skills.

## Known limitations

- **ITAF numbering** (S1-S18, G1-G18) is a pedagogical reconstruction. It does NOT correspond to official ISACA ITAF numbering.
- **CISA domain weights** verify against current CISA CRM 28th Ed.
- **COBIT 2019 alignment goals** consult official COBIT documentation.
- **Ethics principle count** may vary (7 or 8 depending on edition).
- **Use cases are stubs** - full test harness not yet built.

---

## Disclaimer

This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source (CISA CRM 28th Ed 2024, COBIT 2019, ITAF 4th Ed, ISACA Code of Professional Ethics).
