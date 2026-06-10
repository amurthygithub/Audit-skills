# isaca-audit-methodology

**Encode ISACA CISA methodology, COBIT 2019, ITAF, ITGC/ITAC testing, risk-based audit planning, and 5-part audit observations into your AI agent.**

Status: **draft v0.2.0**, on Tier 0 Spine. The skill uses the **router + chunks pattern** - `SKILL.md` is the always-loaded router, the deep-dive content lives in 8 chunk files (each <= 200 lines) loaded on demand per §11 routing. Framework facts (COBIT 2019 objective catalog, ITAF standard numbering, CISA domain weights) were verified against live ISACA sources on 2026-06-10 (see `docs/persona-review.md`).

---

## Context budget (declared in frontmatter)

| Tier | Tokens | What |
|------|--------|------|
| `always_loaded_tokens` | 3,200 | `SKILL.md` (router) - always in context |
| `per_call_typical_tokens` | 6,500 | router + 1 chunk + 1 industry + 1 UC |
| `per_call_max_tokens` | 16,000 | router + all chunks + industry + UC |
| `per_call_p90_tokens` | 8,500 | target estimate (telemetry baseline not yet populated) |

---

## The 8 chunks

| Chunk | Topic | When to load |
|-------|-------|--------------|
| `chunks/01-framework-and-cisa.md` | ISACA Framework and CISA 5 Domains (18/18/12/26/26%) | "ISACA overview", "CISA domains", "CISA certification" |
| `chunks/02-cobit-2019.md` | COBIT 2019 Objectives (40: 5/14/11/6/4), design factors, goals cascade | "COBIT 2019", "COBIT objectives", "design factors", "focus area" |
| `chunks/03-itaf-and-maturity.md` | ITAF Standards (1000/1200/1400 series) and Capability/Maturity Models | "ITAF", "audit standards", "maturity assessment" |
| `chunks/04-itgc-itac.md` | ITGC and ITAC Testing | "ITGC", "ITAC", "general controls", "application controls" |
| `chunks/05-risk-and-planning.md` | Risk-Based Audit Planning | "risk assessment", "audit plan", "risk score" |
| `chunks/06-observation-and-lifecycle.md` | 5-Part Observations and Audit Lifecycle | "audit observation", "5-part", "audit lifecycle" |
| `chunks/07-outputs-and-cross-refs.md` | Output Templates and Cross-References | "audit report template", "cross-reference", "mapping" |
| `chunks/08-questionnaire-reuse.md` | CAIQ v4 / SIG / VSAQ evidence reuse | "CAIQ", "SIG", "VSAQ", "customer questionnaire" |

---

## What this skill does

| Capability | What the skill produces | Use case |
|-----------|------------------------|----------|
| COBIT maturity assessment | Process capability assessment (0-5), gap analysis, improvement roadmap | UC-01 |
| ITGC/ITAC testing | Control effectiveness assessment per category, with test procedures | UC-02 |
| 5-part observation | Structured finding: Condition, Criteria, Cause, Effect, Recommendation | UC-02 |
| COBIT design factors | Prioritized governance objectives from the 11 design factors | UC-03 |
| Risk-based planning guidance | 5-step methodology, audit universe, L x I x CRF scoring (house model, labeled) | guidance only (chunk 05) -- no worked UC yet |
| Cross-framework mapping | ISACA to COSO, NIST CSF, ISO 27001, AICPA, ITIL, CCM v4 | - |

---

## Who this is for

- **IT auditors** performing IS audit engagements per ISACA standards.
- **SaaS companies** pursuing SOC 2 readiness or COBIT maturity assessments.
- **Financial institutions** conducting ITGC testing for SOX 404 compliance.
- **Government agencies** adopting COBIT 2019 for IT governance (federal-centric today; state/local + GAGAS layer is a known gap).
- **Healthcare audit teams** (HIPAA crosswalk in `industries/healthcare.md`; worked UC planned).
- **GRC platform builders** embedding ISACA methodology without hiring CISA subject-matter experts.

---

## Worked examples (stubs)

### Use case 1: SaaS COBIT 2019 maturity assessment

**Scenario:** 500-employee B2B SaaS company with SOC 2 Type II wants COBIT maturity for APO13, BAI07, DSS01.

```yaml
classification: "GAP_1.5"
maturity_assessment:
  processes:
    - id: APO13
      name: "Managed Security"
      current_maturity: 2.5   # house convention; official CPM levels are integers
      target_maturity: 4.0
      gap: 1.5
  improvement_roadmap:
    - phase: "Quick Win (1-3 months)"
      gain: 0.5
```

Full deep-dive: [`use-cases/uc-01-saas-maturity-assessment.md`](use-cases/uc-01-saas-maturity-assessment.md).

### Use case 2: ITGC finding in 5-part observation format

**Scenario:** Commercial bank discovers access recertification gap during quarterly ITGC testing.

```yaml
classification: "High"
observation:
  id: "ACC-2026-001"
  severity: "High"   # judgment call, never a mechanical count
  condition: "No recertification for 3 of 5 critical applications"
  criteria: "Company Policy ISP-003 Section 4.2; COBIT 2019 DSS05.04"
  cause:
    root_cause_category: "Technology"
  recommendations:
    - type: "Primary"
      action: "Implement automated IGA tool"
```

Full deep-dive: [`use-cases/uc-02-five-part-observation.md`](use-cases/uc-02-five-part-observation.md).

### Use case 3: COBIT 2019 design factors assessment

**Scenario:** $12B regional bank tailors its governance system using the COBIT 2019 design factors.

Full deep-dive: [`use-cases/uc-03-cobit-design-factors.md`](use-cases/uc-03-cobit-design-factors.md).

---

## 30-second quick start (Path 1 - system prompt)

> Path 1 loads ONLY the router. The router's procedure/output sections are pointers into
> `chunks/` -- a bare API call cannot follow them, so expect summary-level answers. For full
> answers, append the chunk files matching your question (per SKILL.md §11) to the system
> prompt. **Data handling:** audit scopes and findings are sensitive (and for government
> users, often disclosure-exempt); only send them to an API endpoint your organization has
> approved.

```bash
git clone https://github.com/amurthygithub/Audit-skills.git
cd Audit-skills
pip install openai   # requires OPENAI_API_KEY; calls are billed to your account
```

```python
from openai import OpenAI

skill_dir = "skills/isaca-audit-methodology"
context = open(f"{skill_dir}/SKILL.md").read()
# Add the chunks your question needs (SKILL.md §11 routing), e.g. for maturity questions:
for chunk in ("02-cobit-2019", "03-itaf-and-maturity"):
    context += "\n\n" + open(f"{skill_dir}/chunks/{chunk}.md").read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": context},
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

## Path 2 — packaged skill + telemetry

Every skill ships a deterministic reference executor (`tests/isaca_audit_methodology_stub.py`) — the same one the test suite's oracle runs against — plus telemetry instrumentation.

> **The stub's output is canned.** It returns seed-derived fixtures (the maturity values come
> from the seed file, not from analyzing your evidence) so the test suite is runnable today.
> It demonstrates output STRUCTURE; it does not perform analysis. The real executor is the
> Phase 2 migration (ARGUS).

```python
import sys, json
sys.path.insert(0, "skills/isaca-audit-methodology")        # telemetry package
sys.path.insert(0, "skills/isaca-audit-methodology/tests")  # stub executor

from isaca_audit_methodology_stub import run_skill
from telemetry.instrument import instrumented

@instrumented(skill="isaca-audit-methodology", skill_version="0.2.0",
              default_use_case_id="UC-01", default_industry="saas-technology")
def assess_maturity(payload):
    return run_skill("UC-01", payload)

payload = json.load(open("skills/isaca-audit-methodology/data/seeds/uc-01-input.json"))
result = assess_maturity(payload)

print(result["classification"])                                   # → "GAP_1.5" (from the seed)
print(result["maturity_assessment"]["processes"][0]["gap"])       # → 1.5
```

Verify it works:

```bash
pytest skills/isaca-audit-methodology/tests/ -q
# → 36 passed
```

(The 36 tests verify output contracts, citation grounding, telemetry, and routing-table
consistency — they do not certify domain correctness by themselves; that is what the G4.5
persona vetting + live-source verification in `docs/persona-review.md` is for.)

---

## What's in the box

```
skills/isaca-audit-methodology/
  README.md
  SKILL.md                     # router (always loaded)

  chunks/                      # deep-dive content (loaded on demand per §11 routing)
    01-framework-and-cisa.md
    02-cobit-2019.md
    03-itaf-and-maturity.md
    04-itgc-itac.md
    05-risk-and-planning.md
    06-observation-and-lifecycle.md
    07-outputs-and-cross-refs.md
    08-questionnaire-reuse.md

  industries/                  # 4 industry-shaped views
    _index.md
    financial-services.md
    saas-technology.md
    public-sector.md
    healthcare.md

  use-cases/                   # 3 worked examples (stubs)
    _index.md
    uc-01-saas-maturity-assessment.md
    uc-02-five-part-observation.md
    uc-03-cobit-design-factors.md

  data/
    README.md
    generators/gen_risk_plan.py
    seeds/uc-01-input.json  uc-02-input.json  uc-03-input.json

  tests/
    isaca_audit_methodology_stub.py     # deterministic reference executor
    test_isaca_audit_methodology_oracle.py
    test_isaca_audit_methodology_grounding.py
    test_isaca_audit_methodology_trace.py
    test_isaca_audit_methodology_metamorphic.py
    test_isaca_audit_methodology_adversarial.py
    test_isaca_audit_methodology_telemetry.py

  telemetry/
    schema.json
    instrument.py
    redaction.md
    baseline.md                # template -- not yet populated

  docs/
    architecture.md
    limits-and-disclaimers.md
    changelog.md
    acceptance-gate.md
    persona-review.md          # G4.5 vetting evidence
```

---

## Testing

```bash
python tools/lint_skill.py skills/isaca-audit-methodology
pytest skills/isaca-audit-methodology/tests/ -v
```

---

## Cross-skill assets

- **Board-ready audit committee deck**: `aicpa-soc-reporting/assets/board_deck_template.md` — 20-slide template for quarterly board presentations. Cross-referenced by all Tier 0 Spine skills.

## Known limitations

- **ITAF**: standard numbers verified against the 4th Edition full text; the current 5th Edition (2026) retains the series — verify titles before citing.
- **Risk scoring model** (L x I x CRF) and design-factor weights are labeled house conventions, not ISACA content.
- **No GAGAS/state-local layer, no public-sector or healthcare worked UC** — tracked as structural tickets.
- **Stub executor is canned** (see Path 2 note); telemetry baseline not yet measured.
- **Use cases are stubs** — the Epic 6 harness (multi-run, multi-model reliability) is not yet built.

---

## Disclaimer

This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative sources (ISACA CISA exam content outline, COBIT 2019, ITAF 5th Edition, ISACA Code of Professional Ethics).
