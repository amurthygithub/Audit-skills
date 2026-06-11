# Audit Skills for AI Agents

Production-grade audit, compliance, and security skills for AI agents. Encode ISACA, COSO, AICPA, PCAOB, NIST 800-53, FedRAMP, and related frameworks as structured prompts with executable decision logic, output templates, anti-hallucination safeguards, and per-skill telemetry.

**For implementation partners** (audit firms, GRC consultancies, managed security providers): use these to draft SSPs, SARs, walkthroughs, SOC reports, sampling workpapers 10× faster, with audit-grade output.

**For product companies** (GRC tools, audit platforms, compliance SaaS, dev platforms): embed audit/compliance expertise into your product without hiring domain experts for every framework.

**For auditees** (SaaS, healthcare, fintech preparing for SOC 2, FedRAMP, SOX): the same skills, used from the auditee's side — questionnaire reuse (CAIQ, SIG Lite, VSAQ), auditee preparation playbooks, evidence bundling.

---

## What's in this release (v0.3.3)

v0.3.3 ships the library's **8th skill — pci-dss-assessment — and a measured-reliability eval harness**:

- **PCI DSS v4.0.1 skill (born-vetted).** SAQ selection, CDE scoping & segmentation, ROC/AOC validation, the defined-vs-customized-vs-compensating-control distinction. Built under a new third source-licence class (PCI "Read and Copy" — machine-verifiable against a local licensed copy, repo stores paraphrase + IDs only). The §5.11 machine-verification against that copy caught a CRITICAL nothing else could: the Compensating Controls Worksheet has **six** Appendix-C rows, not four — an error that had been hardcoded into the test oracle and self-cited in its own acceptance gate (the trust-anchor fabrication class CI cannot otherwise catch).
- **Shared eval harness with measured reliability rows.** One runner all skills plug into (`evals/`), oracle-labeled cases, and the first published pass-rate measurements over N≥20 runs across two consumer models (Haiku 4.5 + Sonnet 4.6) — "fully tested" now means a measured pass rate, not a smoke test.
- **Licensed-source workflow (process v3.1).** Three source-licence classes codified (public-domain → vendor; read-and-copy → machine-verify locally; AI-restricted → human-verify), with a source manifest and a human-verification worksheet for licensed standards.

**v0.3.2 recap:** shipped the **7th skill — hipaa-security-rule — the first born-vetted under process v3**; first-pass verification found **zero CRITICAL/HIGH/MEDIUM factual errors** (the six retrofitted skills averaged ~6 CRITICAL clusters each). Also:

- **Complete HIPAA ↔ 800-53 crosswalk** — the 12-row partly-wrong seed replaced by the full authoritative mapping extracted from the NIST CPRT REST API (68 Security Rule elements → 279 OLIR rows → 108 controls, Required/Addressable designations, no invented strength ratings; extraction archived with provenance and regenerable).
- **Healthcare UC for nist-800-53-rmf (UC-04)** — FIPS-199 categorization with a clinical availability floor (house convention, oracle-pinned): patient-safety-relevant systems can never be rated A: LOW on a manual-workaround rationale.
- **Three errors documented in NIST's own publications** along the way (SP 800-66r2 footnote misdating PL 116-321; CPRT carrying a pre-Omnibus citation; plus the persona-refutation pattern now at 5-for-5 — live sources beat expert recall every time).

**v0.3.1 recap:** completes the consumer-ready (G4.5) vetting sweep across all 6 skills and hardens the build process around what the sweep found:

- **6/6 skills G4.5-vetted.** Every skill went through practitioner-persona vetting plus live-source verification of every factual claim — ~37 CRITICAL and ~80 HIGH verified findings fixed (fabricated control IDs, invented statutes and SLAs, stale editions, use-case docs that contradicted their own test fixtures). Per-skill evidence lives in `skills/*/docs/persona-review.md` and `docs/acceptance-gate.md`.
- **Process v3.** The sweep's lessons are baked into the verification prompts (`prompts/`), `AGENTS.md`, and the linter: currency claims are always settled by a live fetch (reviewer consensus was refuted 4× — every time on post-cutoff events), framework catalogs get full inventory-diffs instead of spot checks (offsetting errors defeat sampling), anti-hallucination and limits sections are verified *first* (that's where fabrications concentrated), house conventions are labeled instead of attributed to publications, and a verification ✓ without a verbatim source quote doesn't count.
- **Derivability oracles.** Use-case expected outputs are now recomputed independently from the shipped seed data instead of echoing fixture numbers — non-circular tests (e.g., the SOC 2 → 800-53 crosswalk summary is computed from the crosswalk + gap register, and overlap percentages that aren't derivable from a sample are no longer emitted).
- **Citation registry refresh.** All 76 registry URLs liveness-checked; dead links replaced with live equivalents.

**v0.3.0 recap:** added NIST CSF 2.0, a three-round §5.11 source-of-truth verification pass across all skills, a pre-build Day 0 research phase, auto-loaded AGENTS.md instructions, and a fact-sheet template for future skill builds. The library now has a builder and is a skill factory, not just a static collection.

| | v0.2.1 | **v0.3.0** |
|---|--------|------------|
| Skills on the Spine | 5 | **6 (NIST CSF 2.0 added)** |
| Chunks per skill | 7–9 | **7–9** |
| Industry views | 3–4 per skill | **3–4 per skill (NIST CSF 2.0: 4 new)** |
| Use cases (worked examples) | 3–4 per skill | **3–4 per skill (NIST CSF 2.0: 3 new)** |
| Total tests passing | 190 | **297** |
| CI/CD checks | 3 | **3 (unchanged)** |
| §5.11 factual verification | — | **3 rounds across all 6 skills (50+ findings fixed)** |
| G4.5 consumer-ready vetting | — | **6/6 skills persona-vetted + live-source verified (2026-06; ~37 CRITICAL / ~80 HIGH verified findings resolved — LLM-vetted: a filter, not a certification; per-skill evidence in `skills/*/docs/persona-review.md`)** |
| Day 0 pre-build research | — | **`docs/fact-sheet-template.md` (research before build)** |
| Agent runtime instructions | — | **`AGENTS.md` (auto-loaded via `opencode.json`)** |
| Builder documentation | — | **`docs/skill-design-template.md` (15-section, Day 0–9 build sequence)** |

**v0.2.1 highlights (still accurate):** CI/CD with 3 status checks, branch protection, PR template + CONTRIBUTING, whitespace linter rule, shared `test_consistency_lib.py` for cross-document drift, 14-framework crosswalks, questionnaire reuse (CAIQ/SIG Lite/VSAQ), board deck template.

---

## Skills in this library

| Skill | Status | Tests | Framework | Top use cases |
|-------|--------|-------|-----------|---------------|
| **[nist-800-53-rmf](skills/nist-800-53-rmf/README.md)** | v0.3.0 on Spine | 28 | NIST SP 800-53 Rev 5, SP 800-37 Rev 2, FIPS 199, FedRAMP | FedRAMP Moderate categorization, agency ATO with conditions, SOC 2 → 800-53 crosswalk, CAIQ/SIG Lite reuse |
| **[isaca-audit-methodology](skills/isaca-audit-methodology/README.md)** | v0.3.0 on Spine | 36 | ISACA CISA CRM, COBIT 2019 (11 design factors), ITAF 5th Ed, ISACA Code of Ethics | IT audit planning, ITGC/ITAC testing, COBIT maturity assessment, 5-part observation |
| **[coso-internal-controls](skills/coso-internal-controls/README.md)** | v0.3.0 on Spine | 30 | COSO 2013 ICIF (17 principles, 71 PoF), COSO 2017 ERM, SOX 404, PCAOB AS 2201 | ICFR assessment, deficiency classification (MW/SD/D), walkthroughs, RCM (with Risk ID) |
| **[aicpa-soc-reporting](skills/aicpa-soc-reporting/README.md)** | v0.3.0 on Spine | 25 | AICPA SOC 1/2/3, TSP §100 (33 common criteria, 61 total), SSAE 21 | SOC 1/2/3 examinations, TSC mapping, opinion determination, CUEC/CSOC |
| **[audit-workpapers](skills/audit-workpapers/README.md)** | v0.3.0 on Spine | 43 | PCAOB AS 1215/AS 1305/AS 2201/AS 2315, AU-C 230, ISA 230 | Workpaper documentation, evidence hierarchy, sampling (MUS/attribute), 5-part findings, substantive analytical procedures |
| **[nist-csf-2](skills/nist-csf-2/README.md)** | v0.3.0 on Spine | 69 | NIST CSF 2.0 (6 Functions, 22 Categories, 106 Subcategories), CMMC L2, FFIEC CAT | First organizational profile, board maturity report, CSF → 800-53 crosswalk |
| **[hipaa-security-rule](skills/hipaa-security-rule/README.md)** | v0.3.2 on Spine (born-vetted) | 61 | HIPAA Security Rule (45 CFR 164 Subpart C), HITECH, NIST SP 800-66r2 | BA risk analysis + addressable dispositions, hospital OCR readiness, solo-consultant BAA + right-sized checklist |
| **[pci-dss-assessment](skills/pci-dss-assessment/README.md)** | v0.3.2 on Spine (born-vetted) | 62 | PCI DSS v4.0.1 (6 goals, 12 requirements, 10 SAQ types) | SAQ selection (A vs A-EP), ROC + CDE segmentation, compensating-control worksheet |

**523 tests repo-wide (354 skill-local + shared lint/consistency/registry/eval suites), 0 failures. All pass the Tier 0a linter. All 8 skills have passed the G4.5 consumer-ready gate (persona vetting + live-source verification — see each skill's `docs/persona-review.md`).**

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
├── tests/                       # per-skill test files (test_<skill>_<type>.py)
│   ├── test_<skill>_lint.py     # Tier 0a linter
│   ├── test_<skill>_oracle.py   # UC outputs match expected
│   ├── test_<skill>_grounding.py # in-body citations resolve to manifest
│   ├── test_<skill>_trace.py    # UC procedures cite real SKILL.md sections
│   ├── test_<skill>_metamorphic.py # input mutations → expected output mutations
│   ├── test_<skill>_adversarial.py # edge cases (dual classification, etc.)
│   ├── test_<skill>_telemetry.py # schema validation + instrument emits events
│   ├── test_<skill>_consistency.py # routing/frontmatter/manifest/UC sync
│   ├── <skill>_stub.py          # deterministic reference executor
│   └── conftest.py              # adds skill root to sys.path
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

🔁 **Tested against workflows, not just outputs.** 6 skill-specific test files per skill (plus shared root-level lint, consistency, and telemetry-drift suites) cover the full audit lifecycle: oracle (does the right answer come out?), grounding (are citations real?), trace (does the routing match the workflow step?), metamorphic (does it survive rephrasing?), adversarial (does it hold up under pressure?), telemetry (is it instrumented?).

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

## CI/CD and contribution workflow

This repo is hardened for outside contributions.

**Branch protection on `main`:**
- 1 human approval required to merge
- 3 required status checks: `PR title convention`, `Lint skill structure`, `pytest`
- No force-push, no branch deletion
- Linear history (squash-merge only)
- All PR comments must be resolved before merge

**On every PR (`.github/workflows/ci.yml`):**
- `PR title convention` — must match `^(feat|fix|docs|chore)\([a-z0-9][a-z0-9-]+\): .+$`
- `Lint skill structure` — runs `tools/lint_skill.py` on all 8 skills
- `pytest` — runs `pytest skills/ tests/ -q` (523 tests)

**Nightly (`.github/workflows/nightly.yml`):**
- Link rot check on every URL in the §10 References & Citation Manifest sections

**For contributors:**
- Use [the PR template](.github/pull_request_template.md) — 6 fields, ~30 seconds to fill out
- See [CONTRIBUTING.md](CONTRIBUTING.md) for the short version
- Optional: `pip install pre-commit && pre-commit install` for local hooks

**PR title convention** (enforced by CI): `type(skill-slug): description` where `type` is one of `feat`, `fix`, `docs`, `chore`. Examples: `feat(nist-800-53-rmf): add CSF 2.0 crosswalk`, `fix(audit-workpapers): correct AS 2305 citation`, `chore(ci): bump setup-python to v5`.

---

## Project layout

```
Audit-skills/
├── README.md                    # this file
├── LICENSE                      # MIT
├── CONTRIBUTING.md              # contributor one-pager
├── .gitignore
│
├── skills/                      # the skill library
│   ├── SKILL.md                 # category pointer (lists all skills)
│   ├── TEMPLATE/                # Tier 0 Spine scaffold — every new skill starts here
│   ├── nist-800-53-rmf/         # v0.3.0 on Spine (28 tests)
│   ├── isaca-audit-methodology/ # v0.3.0 on Spine (36 tests)
│   ├── coso-internal-controls/  # v0.3.0 on Spine (30 tests)
│   ├── aicpa-soc-reporting/     # v0.3.0 on Spine (25 tests)
│   ├── audit-workpapers/        # v0.3.0 on Spine (42 tests)
│   ├── nist-csf-2/              # v0.3.0 on Spine (69 tests)
│   └── hipaa-security-rule/     # v0.3.2 on Spine, born-vetted (61 tests)
│
├── tests/
│   ├── test_consistency_lib.py  # cross-skill consistency library (6 functions)
│   └── test_consistency.py      # per-skill wrapper
│
├── tools/
│   ├── lint_skill.py            # Tier 0a linter (validates Spine compliance)
│   └── check_link_rot.py        # nightly URL health checker
│
└── .github/
    ├── workflows/
    │   ├── ci.yml               # lint + pytest + PR title check
    │   └── nightly.yml          # link rot scan
    └── pull_request_template.md # 6-field PR template
```

---

## Quality

Each skill is reviewed across multiple cycles:

- **Cycle 1 — Structure & completeness:** the linter (`tools/lint_skill.py`) enforces folder contract, section contract, frontmatter contract, citations, no TODO/FIXME outside changelog.
- **Cycle 2 — Factual verification:** every in-body citation `[LABEL §N]` resolves to `## 10. References & Citation Manifest`. UC procedure references resolve to `SKILL.md` sections.
- **Cycle 3 — Production readiness:** oracle tests pass, telemetry schema validates, baseline measured after instrumented run, reviewer sign-off in `docs/acceptance-gate.md`.
- **Cycle 4 — Multi-lens review:** 5 reviewer lenses (framework fidelity, completeness, usability, convention compliance, cross-skill alignment) + 5 practitioner personas (FedRAMP 3PAO, Big 4 SOX partner, SaaS compliance lead, healthcare CISO, state gov IT audit director).
- **Cycle 5 — Drift detection:** shared `test_consistency_lib.py` catches cross-document drift (routing table, frontmatter schema, manifest, cross-skill references, industry/UC sync).
- **Cycle 6 — G4.5 consumer-ready gate (v0.3.1):** practitioner-persona vetting plus live-source verification of every factual claim, with evidence per row (verbatim source quote, retrieval date). Findings are treated as hypotheses until verified against a live authoritative source — reviewer consensus is a triage signal, never verification. Verification prompts are versioned in `prompts/`.

### Known limitations

- **800-53 control counts** (~156 Low / ~325 Moderate / ~421 High) are approximate; actual count varies with enhancement counting. Verify against the current NIST publication.
- **FedRAMP overlays** — FedRAMP High baseline ≠ NIST 800-53 High baseline. Consult the current FedRAMP Baselines document on fedramp.gov.
- **House conventions are labeled, not hidden** — any scale, weighting, severity rollup, or formula that is not verbatim in a cited source is explicitly marked as a house convention / illustrative heuristic. Framework facts (ITAF series numbers, COSO Points of Focus, TSP criteria counts) were verified against current publications in the v0.3.1 sweep; still verify against the current edition before client use.
- **Auditor vs auditee perspective** — most UCs are auditor-perspective. Auditee playbooks (questionnaire reuse, evidence prep) are growing but not complete.
- **LLM-backed executor** is currently `tests/<skill>_stub.py` (deterministic reference). The production LLM-backed `run.py` ships in a later phase; until then, use Path 1 for real LLM calls.

---

## Quick start

```bash
# 1. Get the skills
git clone https://github.com/amurthygithub/Audit-skills.git
cd Audit-skills

# 2. Install
pip install pytest jsonschema pyyaml

# 3. Verify all skills are healthy (TEMPLATE is the scaffold and is excluded)
python tools/lint_skill.py $(ls -d skills/*/ | grep -v TEMPLATE)
# → [PASS] for each on-Spine skill

# 4. Run the test suite
pytest skills/ tests/ -q
# → 523 passed across all 8 skills

# (Optional) Install all skills into opencode as full packages
./install.sh

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

**Adding a new skill?** First copy [`docs/skill-design-template.md`](docs/skill-design-template.md) to `docs/<your-skill-slug>-design.md` and fill in all 15 sections. The template is a checklist; see [`docs/builds/csf-2/csf-2-design.md`](docs/builds/csf-2/csf-2-design.md) for a fully-filled example. Designs that don't hit all 15 sections are bounced at Monday review.

Before opening a PR, run:
```bash
python tools/lint_skill.py skills/<your-skill>
pytest skills/<your-skill>/tests/ tests/test_consistency_lib.py
```

Both must pass. The consistency library will catch cross-document drift in your PR.

---

## Disclaimer

These skills are AI agent prompt instructions, not professional audit advice. They are designed to assist qualified audit professionals by providing structured frameworks and decision logic. Always exercise professional judgment and verify outputs against current professional standards and regulatory requirements.
