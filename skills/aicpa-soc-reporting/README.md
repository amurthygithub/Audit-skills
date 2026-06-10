# aicpa-soc-reporting

**Encode AICPA SOC reporting (SOC 1, SOC 2, SOC 3, SOC for Cybersecurity, SOC for Supply Chain) into your AI agent.**

Status: **draft v0.2.0**, on Tier 0 Spine, 7 chunks, 4 use cases, linter-clean. The skill uses the **router + chunks pattern** -- `SKILL.md` is a ~280-line router, the deep-dive content lives in 7 chunk files (<=200 lines each) loaded on demand.

---

## Context budget (declared in frontmatter)

| Tier | Tokens | What |
|------|--------|------|
| `always_loaded_tokens` | 2,800 | `SKILL.md` (router) -- always in context |
| `per_call_typical_tokens` | 5,500 | router + 1 chunk + 1 industry + 1 use case |
| `per_call_max_tokens` | 14,000 | router + all chunks + industry + UC |
| `per_call_p90_tokens` | 7,500 | measured after first instrumented run |

## The 7 chunks

| Chunk | Topic | When to load |
|-------|-------|--------------|
| `chunks/01-soc-overview.md` | SOC types, governing standards, key terminology | "What SOC type applies?" / "SOC 1 vs SOC 2" / "AT-C standards" |
| `chunks/02-engagement-type-decision.md` | Engagement classification, Type I vs Type II | "Classify my SOC engagement" / "Type I or Type II?" |
| `chunks/03-tsp-criteria.md` | All 51 TSC criteria with COSO mapping and cross-framework maps | "TSC criteria" / "CC1.1" / "Privacy criteria" / "map to ISO 27001" |
| `chunks/04-report-structures.md` | SOC 1/2/3/for-Cybersecurity/for-Supply-Chain report templates | "Draft a SOC 2 report" / "report structure" |
| `chunks/05-assertion-bridge.md` | Management assertion templates, bridge letter template | "Management assertion" / "bridge letter" |
| `chunks/06-cuec-csoc-inheritance.md` | CUEC/CSOC identification, inclusive vs carve-out decision | "CUECs" / "CSOCs" / "carve-out vs inclusive" |
| `chunks/07-opinion-lifecycle-sampling.md` | Opinion types, engagement lifecycle (4 phases), sampling guidance, cross-references | "Opinion type" / "qualified opinion" / "sampling" / "engagement lifecycle" |
| `chunks/08-questionnaire-reuse.md` | CAIQ, SIG Lite, VSAQ, customer questionnaire evidence reuse from SOC 2 evidence | "CAIQ" / "SIG Lite" / "VSAQ" / "questionnaire" / "audit fatigue" |

Per-call cost: 2,800-5,500 tokens (vs. ~35,000 for the original monolithic version).

---

## What this skill does

| Capability | What the skill produces | Use case |
|------------|------------------------|----------|
| Engagement classification | SOC type (1/2/3/Cybersecurity/Supply Chain) + Type I/II determination | UC-01 |
| TSC scoping | Criteria list (33 CC + selected A/PI/C/P) with COSO mapping | UC-01 |
| CUEC/CSOC identification | CUEC list, CSOC list, inclusive vs carve-out rationale | UC-02 |
| Report drafting | Complete SOC report with all required sections | UC-01 |
| Opinion determination | Opinion type (Unqualified/Qualified/Adverse/Disclaimer) + exception analysis | UC-01 |
| Management assertions | Type I (2-paragraph) or Type II (3-paragraph) assertion letter | UC-01 |
| Bridge letters | Gap-period bridge letter with 4 attestations | (planned) |
| Cross-framework mapping | TSC to COSO, ISO 27001, NIST 800-53, GDPR, COBIT tables | -- |
| Sampling | Minimum sample sizes by control frequency, deviation rate analysis | UC-01 |
| Engagement lifecycle | 4-phase lifecycle: Scoping, Evidence, Report Issuance, Monitoring | UC-01 |

---

## Industry views

| Industry | File | Posture | Top use cases |
|----------|------|---------|---------------|
| Multi-tenant SaaS | `industries/saas-technology.md` | SOC 2 Type II with carve-out for IaaS | UC-01, UC-02 |
| Financial services | `industries/financial-services.md` | SOC 1 + SOC 2 dual reports, FFIEC/GLBA overlay | UC-01 |
| Healthcare | `industries/healthcare.md` | SOC 2 + Privacy + HITRUST, HIPAA overlay | UC-01 |
| Public sector | `industries/public-sector.md` | SOC 2 complementary to FedRAMP | UC-02 |

---

## Quick start

```bash
git clone https://github.com/amurthygithub/Audit-skills.git
cd Audit-skills
```

### Path 1 -- system prompt (router only)

```python
from openai import OpenAI

with open("skills/aicpa-soc-reporting/SKILL.md") as f:
    system_prompt = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": """
            Classify this scenario:
            CloudStack SaaS provides a cloud-based project management platform.
            Customers are requesting a SOC report for vendor due diligence.
            They use AWS as their IaaS provider. This is their third SOC engagement.
            They have an SLA of 99.9% uptime and handle confidential customer data.
        """},
    ],
)
print(response.choices[0].message.content)
# -> SOC type: SOC 2 Type II, TSC categories: Security + Availability + Confidentiality,
#    Subservice: AWS (carve-out), Criteria count: 38
```

### Path 2 — packaged skill + telemetry

Every skill ships a deterministic reference executor (`tests/aicpa_soc_reporting_stub.py`) — the same one the test suite's oracle runs against — plus telemetry instrumentation. Run it against the shipped UC-01 seed:

```python
import sys, json
sys.path.insert(0, "skills/aicpa-soc-reporting")        # telemetry package
sys.path.insert(0, "skills/aicpa-soc-reporting/tests")  # stub executor

from aicpa_soc_reporting_stub import run_skill
from telemetry.instrument import instrumented

# Wrap with telemetry — every call appends a SkillInvocation event
# to telemetry/events.jsonl (override with SOXFLOW_TELEMETRY_PATH)
@instrumented(skill="aicpa-soc-reporting", skill_version="0.2.0",
              default_use_case_id="UC-01", default_industry="saas-technology")
def scope_examination(payload):
    return run_skill("UC-01", payload)

payload = json.load(open("skills/aicpa-soc-reporting/data/seeds/uc-01-input.json"))
result = scope_examination(payload)

print(result["classification"])                  # → "SOC2-TypeII-38"
print(result["engagement"]["opinion"])           # → "Unqualified"
print(result["engagement"]["criteria_count"])    # → 38
```

Verify it works:

```bash
pytest skills/aicpa-soc-reporting/tests/ -q
# → 25 passed
```

Verify it works:
```bash
python tools/lint_skill.py skills/aicpa-soc-reporting
# -> [PASS] skills/aicpa-soc-reporting

pytest skills/aicpa-soc-reporting/tests/ -v
# -> 1 passed
```

---

## What's in the box

```
skills/aicpa-soc-reporting/
|-- README.md                    # this file
|-- SKILL.md                     # the router (~280 lines, always loaded)
|-- SKILL.md.bak                 # original 1,580-line monolithic (preserved)
|
|-- chunks/                      # deep-dive content (loaded on demand)
|   |-- 01-soc-overview.md       # SOC types, standards, terminology
|   |-- 02-engagement-type-decision.md  # Classification + Type I/II
|   |-- 03-tsp-criteria.md       # All 51 TSC criteria + cross-framework maps
|   |-- 04-report-structures.md  # SOC 1/2/3/Cybersecurity/Supply Chain templates
|   |-- 05-assertion-bridge.md   # Management assertions + bridge letters
|   |-- 06-cuec-csoc-inheritance.md  # CUEC/CSOC + inclusive vs carve-out
|   |-- 07-opinion-lifecycle-sampling.md  # Opinions, lifecycle, sampling
|
|-- industries/                  # 4 industry views
|   |-- _index.md
|   |-- saas-technology.md
|   |-- financial-services.md
|   |-- healthcare.md
|   |-- public-sector.md
|
|-- use-cases/                   # 4 use cases
|   |-- _index.md
|   |-- uc-01-soc2-type2-examination.md
|   |-- uc-02-cuec-csoc-identification.md
|
|-- data/
|   |-- README.md
|
|-- tests/
|   |-- conftest.py
|   |-- test_lint.py
|
|-- telemetry/
|   |-- schema.json
|   |-- instrument.py
|   |-- baseline.md
|   |-- redaction.md
|
|-- docs/
|   |-- architecture.md
|   |-- limits-and-disclaimers.md
|   |-- changelog.md
|   |-- acceptance-gate.md
```

---

## Cross-skill assets

- **Board-ready audit committee deck**: `assets/board_deck_template.md` — 20-slide template for quarterly board presentations. Cross-referenced by all 5 Tier 0 Spine skills.

## Known limitations

- SOC for Cybersecurity and SOC for Supply Chain are emerging products. Guidance is still evolving.
- SOC 1 control objectives are management-defined, not standardized.
- TSC criteria count varies by publication (61-67 sub-criteria). Verify against current TSP Section 100.
- Stub executor -- `tests/skill_stub.py` is a placeholder. The LLM-backed executor ships in SOX-611 Phase 2. Until then, use Path 1 (system prompt) for real LLM calls.
- Full list at `docs/limits-and-disclaimers.md`.

---

## Disclaimer

This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source (current AICPA Professional Standards, TSP Section 100, and applicable AT-C sections).
