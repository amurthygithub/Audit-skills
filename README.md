# Audit Skills for AI Agents

Production-grade audit, compliance, and security skills for AI agents. Encode ISACA, COSO, AICPA, PCAOB, NIST 800-53, FedRAMP, and related frameworks as structured prompts with executable decision logic, output templates, anti-hallucination safeguards, and per-skill telemetry.

**For implementation partners** (audit firms, GRC consultancies, managed security providers): use these to draft SSPs, SARs, walkthroughs, SOC reports, sampling workpapers 10× faster, with audit-grade output.

**For product companies** (GRC tools, audit platforms, compliance SaaS, dev platforms): embed audit/compliance expertise into your product without hiring domain experts for every framework.

**For auditees** (SaaS, healthcare, fintech preparing for SOC 2, FedRAMP, SOX): the same skills, used from the auditee's side — questionnaire reuse (CAIQ, SIG Lite, VSAQ), auditee preparation playbooks, evidence bundling.

---

## What's in this release (v0.2.0)

The library grew from "system-prompt-sized SKILL.md files" to a full **Tier 0 Spine** architecture: every skill ships as a router + on-demand chunks + industries + use cases + synthetic data + tests + telemetry + docs.

| | v0.1.0 | **v0.2.0** |
|---|--------|------------|
| Skills on the Spine | 1 (NIST) | **5 (NIST, ISACA, COSO, AICPA SOC, workpapers)** |
| Chunks per skill | 0 (monolithic) | **7–8 (router + on-demand deep-dive)** |
| Industry views | 4 (NIST only) | **3–4 per skill** |
| Use cases (worked examples) | 3 (NIST only) | **3–4 per skill** |
| Test files per skill | 7 | **9 (added grounding + trace consistency)** |
| Total tests passing | 23 | **156** |
| Shared consistency library | — | **`tests/test_consistency_lib.py` (6 functions)** |
| Cross-framework crosswalks | 0 | **14 (HIPAA, PCI, ISO 27001, SOC 2, CSF, CMMC, CJIS, IRS 1075, …)** |
| CAIQ / SIG Lite / VSAQ support | — | **`chunks/08-questionnaire-reuse.md` in every skill** |
| Board-ready audit committee deck | — | **`aicpa-soc-reporting/assets/board_deck_template.md`** |

**New library this release: NIST 800-53 RMF** — full Risk Management Framework (SP 800-37 Rev 2), FIPS 199 categorization, 800-53A assessment, FedRAMP authorization, 14-framework crosswalks.

---

## Skills in this library

| Skill | Status | Tests | Framework | Top use cases |
|-------|--------|-------|-----------|---------------|
| **[nist-800-53-rmf](skills/nist-800-53-rmf/README.md)** | v0.2.0 on Spine | 23 | NIST 800-53 Rev 5/5.1.1, SP 800-37 Rev 2, FIPS 199, FedRAMP | FedRAMP Moderate categorization, agency ATO with conditions, SOC 2 → 800-53 crosswalk, CAIQ/SIG Lite reuse |
| **[isaca-audit-methodology](skills/isaca-audit-methodology/README.md)** | v0.2.0 on Spine | 37 | ISACA CISA CRM 28th Ed, COBIT 2019, ITAF, ISACA Code of Ethics | IT audit planning, ITGC/ITAC testing, COBIT maturity assessment, 5-part observation |
| **[coso-internal-controls](skills/coso-internal-controls/README.md)** | v0.2.0 on Spine | 31 | COSO 2013 ICIF, COSO 2017 ERM, SOX 404, PCAOB AS 2201 | ICFR assessment, deficiency classification (MW/SD/D), walkthroughs, RCM |
| **[aicpa-soc-reporting](skills/aicpa-soc-reporting/README.md)** | v0.2.0 on Spine | 26 | AICPA SOC 1/2/3, TSP §100, SSAE 18/21 | SOC 1/2/3 examinations, TSC mapping, opinion determination, CUEC/CSOC |
| **[audit-workpapers](skills/audit-workpapers/README.md)** | v0.2.0 on Spine | 39 | PCAOB AS 1215, AU-C 230, AICPA SAS | Workpaper documentation, evidence hierarchy, sampling, 5-part findings |

**156 tests across the 5 skills, 0 failures. All pass the Tier 0a linter.**

---

## Architecture — the Tier 0 Spine

Every skill is a folder, not a single file. The same shape, the same contracts, the same linter.

```
skills/<skill-name>/
├── SKILL.md                     # the router (≤ 300 lines, always loaded)
├── README.md                    # consumer one-pager
│
├── chunks/                      # deep-dive content (≤ 200 lines each)
│   ├── 01-<topic>.md
│   ├── 02-<topic>.md
│   └── ...
│
├── industries/                  # industry-shaped views
│   ├── _index.md
│   ├── financial-services.md
│   ├── public-sector.md
│   ├── saas-technology.md
│   └── healthcare.md            # (some skills)
│
├── use-cases/                   # worked examples with input/procedure/oracle
│   ├── _index.md
│   ├── uc-01-...
│   └── ...
│
├── data/
│   ├── generators/              # deterministic Python CLIs (--seed)
│   ├── seeds/                   # fixtures + crosswalks
│   └── crosswalks/              # SOC 2 ↔ 800-53, etc.
│
├── tests/                       # 9 test files = 24–39 tests per skill
│   ├── test_oracle.py           # UC outputs match expected
│   ├── test_trace.py            # UC procedures cite real SKILL.md sections
│   ├── test_grounding.py        # in-body citations resolve to manifest
│   ├── test_metamorphic.py      # input mutations → expected output mutations
│   ├── test_adversarial.py      # edge cases (dual classification, etc.)
│   ├── test_telemetry.py        # schema validation + instrument emits events
│   ├── test_lint.py             # Tier 0a linter
│   ├── test_consistency.py      # routing/frontmatter/manifest/UC sync
│   └── skill_stub.py            # deterministic reference executor
│
├── telemetry/
│   ├── schema.json              # SkillInvocation JSON Schema
│   ├── instrument.py            # @instrumented decorator
│   ├── redaction.md             # PII/NPI/PHI redaction policy
│   └── baseline.md              # p50/p90/p99 token use
│
├── assets/                      # cross-skill assets (e.g. board_deck_template.md)
│
└── docs/
    ├── architecture.md
    ├── limits-and-disclaimers.md
    ├── changelog.md
    └── acceptance-gate.md
```

### Router + chunks — context budget as a first-class concern

The agent's context window is finite. Naively pasting a 2,000-line SKILL.md into a system prompt burns 30K+ tokens on every call. The Spine splits each skill into a **router** (`SKILL.md`, ≤ 300 lines, always loaded) and **chunks** (≤ 200 lines each, loaded on demand). The router's §11 routing table maps user intent to chunks to load. Per-call cost drops to 3,000–6,000 tokens for typical use.

Every skill's frontmatter declares its `context_budget`:

```yaml
context_budget:
  always_loaded_tokens: 3000    # SKILL.md (router)
  per_call_typical_tokens: 6000 # router + 1 chunk + 1 industry + 1 UC
  per_call_max_tokens: 15000    # router + all chunks + industries
  per_call_p90_tokens: 8000     # measured after first instrumented run
```

### Tested against data, workflows, and cross-mappings

🔬 **Tested against data, not just docs.** Every skill ships with synthetic data generators + seed fixtures — FIPS-199 categorizations, control inventories, SAR findings, MUS populations, SOC engagements. Tests run *against* the data, like testing a junior auditor against a known-good reference set.

🔁 **Tested against workflows, not just outputs.** 9 test files per skill cover the full audit lifecycle: oracle (does the right answer come out?), grounding (are citations real?), trace (does the routing match the workflow step?), metamorphic (does it survive rephrasing?), adversarial (does it hold up under pressure?), telemetry (is it instrumented?).

🔗 **Cross-mapped across frameworks.** NIST ↔ HIPAA ↔ PCI ↔ ISO 27001 ↔ SOC 2 ↔ CJIS ↔ IRS 1075 ↔ state RMF — point-of-focus granularity, not category handwaves. A finding in one framework resolves to a finding in another.

🧪 **Shared consistency library.** `tests/test_consistency_lib.py` catches cross-document drift the per-skill tests miss: routing table ↔ chunks, manifest ↔ body citations, industry index ↔ SKILL.md list, use-case index ↔ directory. It caught 50+ bugs the first time it ran.

---

## Three ways to use these skills

### Path 1 — System prompt (5 minutes, no code)

```python
from openai import OpenAI

with open("skills/nist-800-53-rmf/SKILL.md") as f:
    skill_md = f.read()

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": skill_md},
        {"role": "user", "content":
            "Categorize this system using FIPS 199: a multi-tenant SaaS that "
            "processes PII for ~250k individuals per year, hosted on AWS "
            "GovCloud, offered to federal agencies."},
    ],
)
print(response.choices[0].message.content)
```

**Limitations:** no version control, no telemetry, no test coverage, full SKILL.md in context on every call.

### Path 2 — Packaged skill with telemetry (1 hour)

```python
import sys
sys.path.insert(0, "skills/nist-800-53-rmf")

from tests.skill_stub import run_skill
from telemetry.instrument import instrumented

result = run_skill(
    use_case_id="UC-01",
    payload={
        "system_name": "CaseFlow Cloud",
        "information_types": [
            {"name": "Case Management Records",
             "cia_baseline": {"c": "MODERATE", "i": "MODERATE", "a": "LOW"}},
        ],
        "cloud_provider": "AWS GovCloud",
        "cloud_fedramp_id": "AGENCYID-CSP-AWS-GC-FEDRAMP-HIGH",
    },
    model="gpt-4o",
)

print(result["fips_199_categorization"]["overall"])  # → "MODERATE"
```

Wrap with telemetry:

```python
@instrumented(skill="nist-800-53-rmf", skill_version="0.2.0")
def categorize(payload, **kwargs):
    return run_skill("UC-01", payload, **kwargs)
```

Every call emits a `SkillInvocation` event to `telemetry/events.jsonl` — your billing line, your latency dashboard, your drift detector, your audit trail.

### Path 3 — Managed service (your product, your pricing)

Wrap the skills in an HTTP API. Customers call `POST /v1/skills/<skill>/<use-case>`. The telemetry is your billing system. The state is your audit trail. (Planned: ARGUS MCP, tracked in Linear under "ARGUS" epic.)

---

## Project layout

```
Audit-skills/
├── README.md                    # this file
├── LICENSE                      # MIT
├── install.sh                   # opencode installer
├── .gitignore
│
├── skills/                      # the skill library
│   ├── SKILL.md                 # category pointer (lists all skills)
│   ├── TEMPLATE/                # Tier 0 Spine scaffold — every new skill starts here
│   ├── nist-800-53-rmf/         # v0.2.0 on Spine (23 tests)
│   ├── isaca-audit-methodology/ # v0.2.0 on Spine (37 tests)
│   ├── coso-internal-controls/  # v0.2.0 on Spine (31 tests)
│   ├── aicpa-soc-reporting/     # v0.2.0 on Spine (26 tests)
│   └── audit-workpapers/        # v0.2.0 on Spine (39 tests)
│
├── tests/
│   └── test_consistency_lib.py  # cross-skill consistency checks
│
├── examples/                    # original scenario walkthroughs (1 per skill)
│
└── tools/
    └── lint_skill.py            # Tier 0a linter (validates Spine compliance)
```

---

## Quality

Each skill was reviewed across multiple cycles before v0.2.0:

- **Cycle 1 — Structure & completeness:** the linter (`tools/lint_skill.py`) enforces folder contract, section contract, frontmatter contract, citations, no TODO/FIXME outside changelog.
- **Cycle 2 — Factual verification:** every in-body citation `[LABEL §N]` resolves to `## 10. References & Citation Manifest`. UC procedure references resolve to `SKILL.md` sections.
- **Cycle 3 — Production readiness:** oracle tests pass, telemetry schema validates, baseline measured after instrumented run, reviewer sign-off in `docs/acceptance-gate.md`.
- **Cycle 4 — Multi-lens review:** 5 reviewer lenses (framework fidelity, completeness, usability, convention compliance, cross-skill alignment) + 5 practitioner personas (FedRAMP 3PAO, Big 4 SOX partner, SaaS compliance lead, healthcare CISO, state gov IT audit director).
- **Cycle 5 — Drift detection:** shared `test_consistency_lib.py` catches cross-document drift (routing table, frontmatter schema, manifest, cross-skill references, industry/UC sync).

### Known limitations

- **800-53 control counts** (~325 Moderate, ~421 High) are derived; actual count varies with enhancement counting. Verify against the current NIST publication.
- **800-53 5.0 vs 5.1.1** — confirm with the requesting program which baseline applies. Both are listed in the frontmatter.
- **FedRAMP overlays** — FedRAMP High baseline ≠ NIST 800-53 High baseline. Consult the current FedRAMP Baselines document on fedramp.gov.
- **ITAF numbering, COSO Points of Focus, TSP criteria counts** in some skills are pedagogical reconstructions. Always verify against current publications.
- **Auditor vs auditee perspective** — most UCs are auditor-perspective. Auditee playbooks (questionnaire reuse, evidence prep) are growing but not complete.
- **LLM-backed executor** is currently `tests/skill_stub.py` (deterministic reference). The production LLM-backed `run.py` ships in a later phase; until then, use Path 1 for real LLM calls.

---

## Quick start

```bash
# 1. Get the skills
git clone https://github.com/amurthygithub/Audit-skills.git
cd Audit-skills

# 2. Install
pip install pytest jsonschema pyyaml

# 3. Verify all 5 skills are healthy
python tools/lint_skill.py skills/nist-800-53-rmf
python tools/lint_skill.py skills/isaca-audit-methodology
python tools/lint_skill.py skills/coso-internal-controls
python tools/lint_skill.py skills/aicpa-soc-reporting
python tools/lint_skill.py skills/audit-workpapers
# → [PASS] for each

# 4. Run the test suite
pytest skills/*/tests/ tests/test_consistency_lib.py -v
# → 156 + 6 = 162 tests passed

# 5. Use a skill (Path 1 — system prompt)
python -c "
from openai import OpenAI
skill = open('skills/nist-800-53-rmf/SKILL.md').read()
client = OpenAI()
r = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {'role': 'system', 'content': skill},
        {'role': 'user', 'content': 'Categorize CaseFlow Cloud (multi-tenant SaaS, ~250k PII, AWS GovCloud) per FIPS 199.'}
    ],
)
print(r.choices[0].message.content)
"
```

---

## License

MIT — see [LICENSE](LICENSE).

---

## Contributing

Contributions welcome — especially:
- New skills on the Spine (use `skills/TEMPLATE/` as the scaffold)
- New use cases for existing skills (3+ industries per use case recommended)
- Synthetic data generators + seed fixtures
- Cross-framework mappings (HIPAA, PCI, ISO, SOC 2 → 800-53)
- Translations to other languages
- Integration guides for other LLM frameworks (Anthropic, Google, Bedrock, Azure OpenAI)

Before opening a PR, run:
```bash
python tools/lint_skill.py skills/<your-skill>
pytest skills/<your-skill>/tests/ tests/test_consistency_lib.py
```

Both must pass. The consistency library will catch cross-document drift in your PR.

---

## Disclaimer

These skills are AI agent prompt instructions, not professional audit advice. They are designed to assist qualified audit professionals by providing structured frameworks and decision logic. Always exercise professional judgment and verify outputs against current professional standards and regulatory requirements.
