# nist-800-53-rmf

**Encode NIST 800-53 Rev 5 / 5.1.1, the RMF (SP 800-37 Rev 2), FIPS 199 categorization, 800-53A assessment, and FedRAMP authorization into your AI agent.**

Status: **draft v0.2.0**, on Tier 0 Spine, 23 tests passing, linter-clean. The skill uses the **router + chunks pattern** — `SKILL.md` is a 218-line router, the deep-dive content lives in 7 chunk files (≤ 87 lines each) loaded on demand. The skill body is real (full decision logic, output templates, citation manifest); the LLM-backed executor is a stub in this version. Production executor ships in SOX-611 Phase 2.

---

## Context budget (declared in frontmatter)

| Tier | Tokens | What |
|------|--------|------|
| `always_loaded_tokens` | 3,000 | `SKILL.md` (router) — always in context |
| `per_call_typical_tokens` | 6,000 | router + 1 chunk + 1 industry + 1 use case |
| `per_call_max_tokens` | 15,000 | router + all chunks + industry + UC |
| `per_call_p90_tokens` | 8,000 | measured after first instrumented run |

The Spine enforces: `SKILL.md` ≤ 300 lines, each chunk ≤ 200 lines, `context_budget` required in frontmatter. See `skills/TEMPLATE/SKILL.md §11` for the pattern.

## The 7 chunks (RMF-step aligned)

| Chunk | RMF step | When to load |
|-------|----------|--------------|
| `chunks/02-categorize.md` | Step 1 — Categorize (FIPS 199) | "Categorize this system", "FIPS 199", "Step 1" |
| `chunks/03-baseline.md` | Step 2 — Select baseline + tailor | "Select baseline", "tailor controls", "Step 2" |
| `chunks/04-implement.md` | Step 3 — Implement + SSP narrative | "Implement controls", "draft SSP", "Step 3" |
| `chunks/05-assess.md` | Step 4 — 800-53A assessment + SAR | "Assess controls", "800-53A", "draft SAR", "Step 4" |
| `chunks/06-authorize.md` | Step 5 — ATO + POA&M | "Issue ATO", "ATO with conditions", "denial", "POA&M", "Step 5" |
| `chunks/07-monitor.md` | Step 7 — Continuous monitoring (ISCM) | "ISCM", "ConMon", "Step 7" |
| `chunks/09-crosswalk.md` | Crosswalk to other frameworks | "Map SOC 2 / ISO 27001 / HIPAA / PCI / CSF to 800-53" |
| `chunks/08-questionnaire-reuse.md` | CAIQ, SIG Lite, VSAQ, customer questionnaire evidence reuse from NIST 800-53 / FedRAMP evidence | "CAIQ" / "SIG Lite" / "VSAQ" / "questionnaire" / "audit fatigue" / "FedRAMP reuse" |

The routing table in `SKILL.md §11` maps user intent → chunks to load. Per-call cost: 3,000-6,000 tokens (vs. ~20,000 for the monolithic version).

---

## What this skill does

| RMF step | What the skill produces | Use case |
|----------|------------------------|----------|
| Categorize (Step 1) | FIPS 199 categorization YAML with CIA impact per information type | [UC-01](#use-case-1-fedramp-bound-saas-categorizes-fips-199-moderate) |
| Select baseline (Step 2) | Selected + tailored control set with inheritance map, scoping/parameterization/supplementation rationale | [UC-01](#use-case-1-fedramp-bound-saas-categorizes-fips-199-moderate) |
| Implement (Step 3) | SSP §8/§9/§10 drafts with control narratives | (planned) |
| Assess (Step 4) | SAR with findings per control, severity, cause, recommendation | [UC-02](#use-case-2-federal-agency-ato-with-conditions) |
| Authorize (Step 5) | ATO decision letter (full / with conditions / denial) + POA&M list | [UC-02](#use-case-2-federal-agency-ato-with-conditions) |
| Monitor (Step 6) | ISCM strategy in SSP §13, POA&M management | [UC-02](#use-case-2-federal-agency-ato-with-conditions) |
| Crosswalk | Gap list vs SOC 2 / ISO 27001 / HIPAA / PCI with priority + owner + target | [UC-03](#use-case-3-soc-2--nist-800-53-crosswalk) |

---

## Who this is for

- **Federal SaaS providers** preparing a FedRAMP authorization (Low/Moderate/High).
- **Federal agencies** running RMF for on-prem or agency-operated systems.
- **Defense contractors** preparing CMMC 2.0 or DoD IL4/IL5/IL6 evidence.
- **Commercial SaaS in regulated industries** (financial services, healthcare) selling to federal customers or pursuing SOC 2 + 800-53 mapping.
- **Audit firms / 3PAOs** scoping, drafting, or reviewing SSPs, SARs, POA&Ms.
- **GRC platform builders** who want to embed RMF expertise without hiring NIST 800-53 subject-matter experts.

---

## Industry-shaped use cases (real, completed, runnable)

### Use case 1: FedRAMP-bound SaaS categorizes FIPS-199 Moderate

**Scenario:** "CaseFlow Cloud" is a multi-tenant case management SaaS for federal civilian agencies. Processes PII for ~250k individuals per year. Hosted on AWS GovCloud (FedRAMP High authorized). One sponsoring agency.

**What the skill produces:**
```yaml
fips_199_categorization:
  system_security_category: {c: MODERATE, i: MODERATE, a: LOW}
  overall: MODERATE
  high_water_mark: MODERATE
  pia_required: true
baseline: MODERATE
inheritance_summary:
  - {control_id: AC-2, status: hybrid, source: "AWS GovCloud + App"}
  - {control_id: SC-7, status: inherited, source: "AWS GovCloud"}
  - {control_id: AU-2, status: hybrid, source: "AWS GovCloud + App"}
  - {control_id: IA-2, status: hybrid, source: "Customer IdP + App"}
  - {control_id: SC-13, status: inherited, source: "AWS GovCloud"}
tailoring_decisions:
  - {control_id: AC-2(8), decision: SCOPING, rationale: "no shared accounts"}
  - {control_id: SC-8(1), decision: SCOPING, rationale: "no wireless"}
  - {control_id: PT-7, decision: SUPPLEMENT, rationale: "PII processed"}
```

**→ Full deep-dive:** [`use-cases/uc-01-fedramp-moderate.md`](use-cases/uc-01-fedramp-moderate.md) (scenario, walk-through, variations, acceptance criteria)
**→ Test:** `tests/test_oracle.py::test_uc_01_oracle`
**→ Input fixture:** `data/seeds/uc-01-input.json`
**→ Expected output:** `data/seeds/uc-01-expected.json`

### Use case 2: Federal agency ATO with conditions

**Scenario:** "Agency Records System (ARS)" — agency-operated records management, on-prem, PII for 80k individuals, MODERATE baseline. SAR with 22 findings (3 High, 11 Moderate, 8 Low). AO risk-accepts 14, issues ATO with 8 conditions, residual risk MODERATE.

**What the skill produces:**
```yaml
sar:
  total_findings: 22
  severity_distribution: {High: 3, Moderate: 11, Low: 8}
  risk_accepted_count: 14
  conditions_count: 8
ato_decision:
  decision: AUTHORIZE_WITH_CONDITIONS
  duration: 1 year
  conditions_count: 8
  risk_accepted_count: 14
  residual_risk: MODERATE
poam:
  poam_count: 22
  risk_distribution: {High: 3, Moderate: 11, Low: 8}
  milestones: {30_days: 2, 60_days: 3, 90_days: 3, ongoing: 14}
next_continuous_monitoring:
  annual_assessment_date: "2027-MM-DD"
  monthly_vuln_scans: true
  significant_change_review: true
```

**→ Full deep-dive:** [`use-cases/uc-02-agency-ato.md`](use-cases/uc-02-agency-ato.md)
**→ Test:** `tests/test_oracle.py::test_uc_02_oracle`
**→ Findings fixture:** `data/seeds/uc-02-findings.json` (22 deterministic findings)

### Use case 3: SOC 2 → NIST 800-53 crosswalk

**Scenario:** "FinPay Treasury Cloud" — B2B SaaS for commercial banks. SOC 2 Type II in place. Federal pilot customer requires 800-53 Moderate mapping.

**What the skill produces:**
```yaml
baseline: MODERATE
crosswalk_summary:
  soc2_common_criteria: 9
  nist_800_53_mod_controls: 325
  mapped_controls: 231
  gap_controls: 94
  overlap_pct: 71
gap_summary:
  total: 94
  by_priority: {High: 28, Medium: 41, Low: 25}
remediation_plan:
  total_items: 94
  due_in_30d: 18
  due_in_60d: 41
  due_in_90d: 24
  due_in_180d: 11
```

**→ Full deep-dive:** [`use-cases/uc-03-soc2-to-800-53.md`](use-cases/uc-03-soc2-to-800-53.md)
**→ Test:** `tests/test_oracle.py::test_uc_03_oracle`
**→ Crosswalk (authoritative):** `data/crosswalks/soc2-to-800-53-mod.json` (33 mappings, 27 unique 800-53 controls)
**→ Gap list:** `data/seeds/uc-03-gap-list.json`

---

## 30-second quick start (Path 1 — system prompt)

```bash
git clone https://github.com/amurthygithub/Audit-skills.git
cd Audit-skills
pip install openai
```

```python
from openai import OpenAI

with open("skills/nist-800-53-rmf/SKILL.md") as f:
    system_prompt = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": """
            Categorize this system using FIPS 199 and select the appropriate
            NIST 800-53 baseline:

            System: CaseFlow Cloud
            Description: Multi-tenant case management SaaS for federal
            civilian agencies. Processes PII (names, agency-issued IDs,
            case notes) for ~250,000 individuals per year.
            Cloud: AWS GovCloud (FedRAMP High authorized).
        """},
    ],
)
print(response.choices[0].message.content)
```

The skill body (§1-§10 of `SKILL.md`) handles the FIPS 199 high-water mark, the baseline lookup, the tailoring decision tree, and the inheritance map. The output is structured YAML.

---

## 5-minute quick start (Path 2 — packaged skill + telemetry)

```bash
git clone https://github.com/amurthygithub/Audit-skills.git
cd Audit-skills
pip install openai pyyaml jsonschema pytest
```

```python
import sys
sys.path.insert(0, "skills/nist-800-53-rmf")

from tests.skill_stub import run_skill
from telemetry.instrument import instrumented

# Wrap with telemetry — every call emits a SkillInvocation event
@instrumented(skill="nist-800-53-rmf", skill_version="0.1.0",
              default_use_case_id="UC-01", default_industry="public-sector")
def categorize(payload, model="gpt-4o", use_case_id="UC-01", industry="public-sector"):
    return run_skill(use_case_id, payload, model=model)

# UC-01 — FedRAMP-bound SaaS
result = categorize({
    "system_name": "CaseFlow Cloud",
    "system_description": "Multi-tenant case management SaaS for federal agencies",
    "information_types": [
        {"name": "Case Management Records",
         "cia_baseline": {"c": "MODERATE", "i": "MODERATE", "a": "LOW"}},
        {"name": "Authentication metadata",
         "cia_baseline": {"c": "MODERATE", "i": "LOW", "a": "LOW"}},
    ],
    "cloud_provider": "AWS GovCloud",
    "cloud_fedramp_id": "AGENCYID-CSP-AWS-GC-FEDRAMP-HIGH",
})

print(result["fips_199_categorization"]["overall"])  # → "MODERATE"
print(result["baseline"]["baseline"])                # → "MODERATE"
```

Verify it works:
```bash
pytest skills/nist-800-53-rmf/tests/ -v
# → 23 passed
```

Every call now writes a `SkillInvocation` event to `telemetry/events.jsonl`:
```json
{"skill":"nist-800-53-rmf","skill_version":"0.1.0","use_case_id":"UC-01",
 "industry":"public-sector","model":"gpt-4o","input_tokens":1240,
 "output_tokens":480,"total_tokens":1720,"latency_ms":8200,
 "cache_hit":false,"classification":"MODERATE","oracle_result":"n/a",
 "timestamp":"2026-06-03T...","redaction_applied":false}
```

That event is your billing line, your latency dashboard, your drift detector, and your audit trail.

---

## Industry views

The skill ships with 4 industry files under `industries/`. Each one tells you the typical posture, boundary, inheritance pattern, regulator relationship, top use cases, and pain points for that industry.

| Industry | File | Posture | Top use cases |
|----------|------|---------|---------------|
| Federal civilian / FedRAMP-bound SaaS | [`industries/public-sector.md`](industries/public-sector.md) | Moderate–High | UC-01, UC-02 |
| Commercial financial services | [`industries/financial-services.md`](industries/financial-services.md) | Moderate–High, SOC 2 crosswalk | UC-03 |
| SaaS / cloud-native technology | [`industries/saas-technology.md`](industries/saas-technology.md) | Variable, FedRAMP-bound variants | UC-01, UC-03 |
| Healthcare payer / provider / health-tech | [`industries/healthcare.md`](industries/healthcare.md) | HIPAA Security Rule + 800-53 crosswalk | (planned UC-04) |

---

## What's in the box

```
skills/nist-800-53-rmf/
├── README.md                    # this file
├── SKILL.md                     # the router (~218 lines, always loaded)
│
├── chunks/                      # deep-dive content (loaded on demand per §11 routing table)
│   ├── 01-categorize.md         # FIPS 199 (Step 1)
│   ├── 02-baseline.md           # Select + tailor (Step 2)
│   ├── 03-implement.md          # SSP narrative (Step 3)
│   ├── 04-assess.md             # 800-53A + SAR (Step 4)
│   ├── 05-authorize.md          # ATO + POA&M (Step 5)
│   ├── 07-monitor.md             # ISCM (Step 7)
│   ├── 08-questionnaire-reuse.md # CAIQ / SIG Lite / VSAQ / FedRAMP reuse
│   └── 09-crosswalk.md           # SOC 2 / ISO / HIPAA / PCI
│
├── industries/                  # 4 industry-shaped views of this skill
│   ├── _index.md
│   ├── public-sector.md
│   ├── financial-services.md
│   ├── saas-technology.md
│   └── healthcare.md
│
├── use-cases/                   # 3 fully worked examples
│   ├── _index.md
│   ├── uc-01-fedramp-moderate.md
│   ├── uc-02-agency-ato.md
│   └── uc-03-soc2-to-800-53.md
│
├── data/
│   ├── README.md                # data dictionary
│   ├── generators/              # 3 deterministic Python CLIs (--seed)
│   │   ├── gen_fips199.py
│   │   ├── gen_sar_findings.py
│   │   └── gen_crosswalk_gap.py
│   ├── seeds/                   # 10 seed fixtures
│   └── crosswalks/              # SOC 2 ↔ 800-53 Mod authoritative reference
│
├── tests/                       # 7 test files = 23 tests
│   ├── test_oracle.py           # UC-01/02/03 oracle assertions
│   ├── test_trace.py            # UC procedure cites real SKILL.md sections or chunks/
│   ├── test_grounding.py        # in-body citations resolve to §10 manifest
│   ├── test_metamorphic.py      # input mutations → expected output mutations
│   ├── test_adversarial.py      # edge cases (dual classification, PII volume, inheritance invalidation)
│   ├── test_telemetry.py        # schema validation + instrument emits valid events
│   └── test_lint.py             # Tier 0a linter passes
│
├── telemetry/
│   ├── schema.json              # SkillInvocation JSON Schema
│   ├── instrument.py            # @instrumented decorator + skill_invocation() context
│   ├── redaction.md             # PII/NPI/PHI redaction policy
│   └── baseline.md              # p50/p90/p99 token use (TBD — populate after first run)
│
└── docs/
    ├── architecture.md          # how the skill is built and invoked
    ├── limits-and-disclaimers.md
    ├── changelog.md
    └── acceptance-gate.md       # publish-vs-reject checklist
```

---

## API quick reference (Path 2)

```python
# Categorize + select baseline
result = run_skill("UC-01", payload, model="gpt-4o")
# → {"classification": "MODERATE",
#    "fips_199_categorization": {...},
#    "baseline": {...}}

# Aggregate SAR findings, produce ATO decision + POA&M
result = run_skill("UC-02", {"findings": [...]})
# → {"classification": "AUTHORIZE_WITH_CONDITIONS",
#    "sar": {...}, "ato_decision": {...}, "poam": {...}}

# Crosswalk SOC 2 → 800-53 Moderate
result = run_skill("UC-03", {"crosswalk": {...}})
# → {"classification": 94,
#    "crosswalk_summary": {...}, "gap_summary": {...}}
```

Output shapes: see `data/seeds/uc-NN-expected.json` for each UC.

---

## Testing

```bash
# Lint (Tier 0a — Spine compliance)
python tools/lint_skill.py skills/nist-800-53-rmf
# → [PASS] skills/nist-800-53-rmf

# Tests (23 across 7 files)
pytest skills/nist-800-53-rmf/tests/ -v
# → 23 passed

# Run a specific UC's oracle
pytest skills/nist-800-53-rmf/tests/test_oracle.py::test_uc_01_oracle -v
```

The tests cover: oracle (UC outputs match expected), trace (UC procedures cite real SKILL.md sections), grounding (in-body citations resolve to §10 manifest), metamorphic (input mutations produce expected output mutations), adversarial (edge cases), telemetry (schema + instrument emit), lint (Tier 0a).

---

## Customizing for your environment

### Pin the model
```python
@instrumented(skill="nist-800-53-rmf", skill_version="0.1.0")
def categorize(payload, model="claude-3-5-sonnet", ...):
    return run_skill(...)
```

### Add an industry view
Copy `industries/_index.md`'s shape, write `industries/<your-industry>.md`, register in `_index.md`. Then add a use case under `use-cases/`.

### Add a use case
1. Copy `use-cases/uc-03-soc2-to-800-53.md` as a template.
2. Add a seed under `data/seeds/uc-04-*.json`.
3. Add a generator under `data/generators/` if the input is non-trivial.
4. Add `tests/test_oracle.py::test_uc_04` + adversarial / metamorphic tests.
5. Run linter + tests.

### Crosswalk to a new framework
Add `data/crosswalks/<framework>-to-800-53.json` (see `soc2-to-800-53-mod.json` for the shape). Reference it from a use case.

---

## Cross-skill assets

- **Board-ready audit committee deck**: `aicpa-soc-reporting/assets/board_deck_template.md` — 20-slide template for quarterly board presentations. Cross-referenced by all 5 Tier 0 Spine skills.

## Known limitations (full list in `docs/limits-and-disclaimers.md`)

- **800-53 Rev 5 vs 5.1.1** — confirm with the requesting program which baseline applies. Both are listed in the frontmatter.
- **Control counts** (~325 Moderate, ~421 High) are derived. Verify against the current NIST publication.
- **FedRAMP overlays** — FedRAMP High baseline ≠ NIST 800-53 High. Consult fedramp.gov.
- **Categorization judgment** is professional judgment; the skill encodes the framework but does not make the call for you.
- **Stub executor** — `tests/skill_stub.py` is a deterministic reference implementation. The LLM-backed `run.py` ships in SOX-611 Phase 2; until then, use Path 1 (system prompt) for real LLM calls.

---

## What ships next (Linear roadmap)

- **SOX-611 Phase 2** — real LLM-backed executor; migrate 4 pre-Spine skills to the same pattern.
- **SOX-583 ARGUS core** — managed-service wrapper with auth, billing, multi-tenancy.
- **SOX-595 Coverage Atlas** — scale from 1 skill to 689 standards.

---

## Disclaimer

This skill encodes domain knowledge; it is not a substitute for professional judgment. Always verify outputs against the cited authoritative source (current NIST SP 800-53 Rev 5 / 5.1.1, FIPS 199, SP 800-37 Rev 2, SP 800-53A Rev 5, OMB A-130, FedRAMP Rev 5 guidance, and your agency's policy).
