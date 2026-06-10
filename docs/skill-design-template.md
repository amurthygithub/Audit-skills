# Skill Design Template

> **Use this for every new skill design document.**
> Status: required template (added 2026-06-05 after the CSF 2.0 design doc formalized the pattern).
> First use: `docs/csf-2-design.md` (1,391 lines, all 15 sections filled in).

## How to use this template

1. **Copy this file** to `docs/<skill-slug>-design.md` (e.g. `docs/iso-27001-design.md`).
2. **Replace every `<...>` placeholder** with the actual value for the new skill.
3. **Fill in every section.** A design doc that doesn't hit all 15 sections is incomplete; the Monday review will bounce it back.
4. **The §15 row in the checklist below is "this template"** — leave it as "Yes (this template)" in your copy.
5. **Reference existing skills** as the load-bearing reference architecture. For most skills, that's `skills/nist-800-53-rmf/` (v0.2.1, 29 tests, all linters green). Read those files first to understand the contract before writing the design.

## Why this template exists

When we shipped the nist-800-53-rmf skill (v0.2.1), we ran:
- 5-lens review (framework fidelity, completeness, usability, convention compliance, cross-skill alignment)
- 5-practitioner review (FedRAMP 3PAO, Big 4 SOX partner, SaaS compliance lead, healthcare CISO, state gov IT audit director)
- 3 fix waves (CRITICAL → HIGH → MEDIUM+LOW)
- Cross-skill consistency library
- CI/CD with 3 required status checks

The CSF 2.0 design doc (`docs/csf-2-design.md`) was structured to mirror those review surfaces, so the build phase doesn't have to re-invent them. This template codifies the structure so every future skill hits the same shape.

A design doc that hits all 15 sections (with the same sub-structure) is reviewable in one sitting and convertible into a build plan without further clarification.

---

## 0. Why this design doc exists

**2-3 sentences.** State the load-bearing rationale for this skill: what gap in the library does it fill, who is the persona, why is it the right next skill to build, what's at risk if we under-design it.

---

## 1. Scope & dependencies

### 1.1 Primary source citation (with URL and retrieval date)

Cite the canonical version of the standard. URL + retrieval date so future re-validation is possible.

### 1.2 Structural inventory (counts)

For the framework, list the structural breakdown (functions, categories, subcategories, controls, etc.). This is what the chunk architecture must cover.

### 1.3 Persona (IT / FIN / GRC / BOTH) with 1-sentence justification

Pull from the Linear issue if there is one. If "BOTH", explain why both IT and another persona need this.

### 1.4 Effort estimate (S/M/L/XL) per Linear

Pull from the Linear issue. Validate against the structural inventory (e.g., 108 subcategories ≠ S).

### 1.5 Dependencies (other skills or Linear issues)

What other skills/Linear issues does this build on? What does this skill need to exist first?

### 1.6 Out-of-scope (explicit non-goals)

What this skill will NOT cover. Critical to prevent scope creep. Example: "Healthcare is explicitly out of scope for v0.1.0; deferred to v0.3.x."

---

## 2. Chunk architecture (7-9 chunks)

For each chunk, list:
- **Filename** (NN-slug.md, ≤200 lines, kebab-case, matches `^\d{2}-[a-z0-9-]+\.md$`)
- **Frontmatter** (chunk_id, parent_skill, topic, load_when)
- **Trigger phrases** — what users say that loads this chunk
- **Cross-references** to other chunks in the same skill + sibling skills

### 2.1 – 2.N: chunks (table form)

| # | Filename | Topic | Triggers | Cross-refs |
|---|----------|-------|----------|-----------|
| 01 | `<NN-slug>.md` | ... | "..." | ... |
| ... | ... | ... | ... | ... |

### 2.N+1: Why 7/8/9 chunks (rationale for the count)

The count is a design decision. Justify it: what drove it (5 functions + crosswalk + governance + reporting? 8 = 6 + governance + reporting + crosswalk?). The "8" choice for CSF 2.0 is documented in the design doc as the rationale.

---

## 3. Industry angles (3-4 industries)

For each industry file (financial-services, public-sector, saas-technology, healthcare, manufacturing, etc.), describe:
- **Most-relevant Functions/Categories** for that industry
- **Real-world example** (compliance regime, customer pressure, executive demand)
- **What the view ADDS to the baseline** — which subcategories are emphasized, which are de-emphasized
- **Cross-references** to industry-specific skills (e.g., healthcare.md cites HIPAA Security Rule)

### 3.1 – 3.N: industries (one section each)

### 3.N+1: `_index.md` table

A markdown table summarizing all industries, their key angle, and a 1-line description. The lint test enforces this file exists.

---

## 4. Use cases (3-4 worked examples)

Each use case must follow the frontmatter contract: `uc_id`, `title`, `industries`, `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status`.

For each UC, provide:
- **Real-world scenario** (2-3 sentences)
- **Input JSON shape** (the seed input that exercises the UC)
- **Procedure steps** (numbered)
- **Expected outputs** (what the stub/oracle should produce)
- **Oracle assertion** (the right answer for the test)
- **Data references** (which seeds + generators feed this UC)

### 4.1 – 4.N: UCs (one section each)

### 4.N+1: UC selection rationale

Why these 3-4 UCs? What gaps do they cover? What UCs were considered and rejected (and why)?

---

## 5. Test architecture (6 skill-specific test files, target test count)

The 9-file convention is enforced by the lint. For each test file, list specific test cases:

| File | Test cases (specific) | Count |
|------|----------------------|-------|
| `test_<skill>_lint.py` | runs linter, asserts exit 0 | 1 |
| `test_<skill>_oracle.py` | UC-01 oracle, UC-02 oracle, UC-03 oracle, parametrized stub-output | 4-5 |
| `test_<skill>_grounding.py` | body citation resolves, all manifest labels cited, no orphan labels | 3-4 |
| `test_<skill>_trace.py` | UC procedures cite real SKILL.md sections, chunks referenced in SKILL.md exist | 2-3 |
| `test_<skill>_metamorphic.py` | rephrased inputs → equivalent outputs, ordering invariance | 2-3 |
| `test_<skill>_adversarial.py` | Tier 0 org, empty profile, contradictory tiers | 3-4 |
| `test_<skill>_telemetry.py` | schema validates, instrument emits event, name pattern, use-case pattern, industry enum, oracle enum | 5-6 |
| `test_<skill>_consistency.py` | routing table ↔ chunks, manifest ↔ body, industry/UC sync, cross-skill refs | 4-5 |
| `test_<skill>_NN_chunk.py` (per chunk) | new chunk has frontmatter, fits 200 lines, is in SKILL.md routing | 4-5 |

### 5.10: Test count summary table

| Skill | Tests | Target |
|-------|-------|--------|
| nist-800-53-rmf (reference) | 29 | 29+ |
| THIS SKILL | 0 (design) | 30+ |

### 5.11: Source-of-truth verification plan (REQUIRED)

**This is the step that catches fabricated IDs, wrong counts, and wrong crosswalk rows.** It is a separate pass from the 5-lens review (§6), which catches convention/usability/completeness issues. A skill can pass the 5-lens review and still have every Category code wrong if the build agents wrote from LLM recall instead of authoritative sources.

For each fact the skill encodes, the design must declare the source it will be verified against. Typical source classes:

- **The standard itself** (the NIST CSF 2.0 PDF, the ISO 27001:2022 standard, the HIPAA Security Rule, etc.)
- **An official reference spreadsheet** (NIST's Informative References CSV/XLSX, the SOC 2 TSC mapping, etc.)
- **An official reference tool** (NIST's online CSF Reference Tool, NIST SP 800-53 control catalog, etc.)
- **A regulator publication** (SEC final rules, NY DFS 500, EU DORA, etc.)

For each fact, list:

| Fact | Source URL | Retrieval date | Verified by |
|------|-----------|----------------|-------------|
| CSF 2.0 has 6 Functions (GOVERN, IDENTIFY, ...) | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf | 2024-02-26 | [name of agent] |
| CSF 2.0 has 22 Categories | (same) | (same) | (same) |
| CSF 2.0 has 106 Subcategories | (same, Appendix A) | (same) | (same) |
| GV.OC-01 maps to PM-11 | https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all | (retrieval date) | (same) |
| ... | ... | ... | ... |

**Mandatory minimum**: at least 5 fact rows in this table for facts that the build will encode. For a NIST-style skill, this is usually: the function count, the category count, the subcategory count, the 4 Tier names, and at least 5 representative crosswalk rows. For an ISO-style skill, this is usually: the control family count, the control count, the mandatory clause count, and at least 5 representative control-to-other-framework rows.

**Where the verification pass fits in the build sequence** (see §12): between Day 5 (build complete) and Day 6 (5-lens review). It is a non-negotiable gate. The verification agent must use `webfetch` (or equivalent authoritative-source fetch) for every fact, not LLM recall. The verification report must cite the source URL for every verified fact.

**Why this exists** (the build-process lesson): in the CSF 2.0 build (June 2026), 9 parallel build agents wrote plausible-looking content from general knowledge. A subsequent verification pass found 8 CRITICAL factual errors (fabricated Category codes, wrong subcategory counts, ~10 wrong CSF↔800-53 crosswalk rows). The 5-lens review would NOT have caught these — it checks structural and convention compliance, not factual accuracy. Without this §5.11 step, future skill builds will repeat the same mistake.

---

## 6. PoV analyses — 5 lenses

For each lens, what would the reviewer focus on for THIS skill? Pre-empt the common findings:

### 6.1 Framework fidelity
Is the standard representation accurate? Did we get the new function right? Are subcategory references correct? Are the cross-references to other NIST/ISACA/COSO publications valid?

### 6.2 Completeness
Do we cover all Functions/Categories/Subcategories? Are the new categories (e.g., GOVERN in CSF 2.0) treated as first-class? Is terminology (Current/Target Profile) used consistently?

### 6.3 Usability
Can a non-NIST practitioner (auditor, GRC consultant, executive) read this and act? Is the executive-legible angle preserved? Are the industry views navigable?

### 6.4 Spine convention compliance
Is the router ≤300 lines? Are chunks ≤200 lines? Is `context_budget` declared? Are 3+ industries + 3+ UCs present? Does it pass `tools/lint_skill.py`?

### 6.5 Cross-skill alignment
Are the cross-references to sibling skills correct? Does it match cross-skill conventions for severity tiers, risk formulas, finding format? Is the "5-part finding" pattern used consistently?

---

## 7. PoV analyses — 5 practitioner personas

Mirror the 5-practitioner review that worked for nist-800-53-rmf. The 5 personas are: FedRAMP 3PAO Lead Assessor, Big 4 SOX 404 Audit Partner, SaaS Startup Head of Compliance, Healthcare CISO, State Gov IT Audit Director.

For each persona, what would they specifically check?

### 7.1 FedRAMP 3PAO Lead Assessor
[Free-form, but specific to this skill]

### 7.2 Big 4 SOX 404 Audit Partner
[Free-form]

### 7.3 SaaS Startup Head of Compliance
[Free-form]

### 7.4 Healthcare CISO
[Free-form]

### 7.5 State Gov IT Audit Director
[Free-form]

---

## 8. Cross-skill alignment table

For each sibling skill (nist-800-53-rmf, isaca-audit-methodology, coso-internal-controls, aicpa-soc-reporting, audit-workpapers — and any new skills since this was written), propose the specific cross-references THIS skill should have.

| Sibling skill | THIS skill's chunk | Sibling chunk | Rationale (1 sentence) |
|---------------|-------------------|---------------|------------------------|
| nist-800-53-rmf | ... | ... | ... |
| isaca-audit-methodology | ... | ... | ... |
| ... | ... | ... | ... |

### 8.6: Cross-skill reference shape (consistency library's view)

The `tests/test_consistency_lib.py` library checks for cross-skill references. What shape will these references take? (`../<sibling>/chunks/<file>.md` + cite in body? or `see <sibling>` text reference? or `[CROSS-SKILL: <sibling> §N]` bracket form?)

---

## 9. Data & synthetic content

### 9.1 Directory layout

```
data/
├── README.md
├── generators/         # deterministic Python CLIs (--seed)
├── seeds/              # JSON fixtures
└── crosswalks/         # JSON mappings to other frameworks
```

### 9.2 Generators (deterministic CLIs)

For each generator, list:
- **Filename** (`gen_<thing>.py`)
- **CLI interface** (`--seed N --out path/to/file.json`)
- **Output shape** (what JSON it produces)
- **Determinism property** (same seed → same output)

### 9.3 Seed JSONs

For each seed, list:
- **Filename** (`uc-NN-input.json` or `<thing>.json`)
- **Which UC/feature uses it**
- **Top-level keys** (input shape)

### 9.4 Crosswalk JSONs

For each crosswalk, list:
- **Filename** (`<from>-to-<to>.json`)
- **Mapping structure** (key → list of matching keys, with rationale)
- **Source** (where the mapping was obtained)

### 9.5 PII / NPI / PHI redaction

How is PII handled in seeds? Synthetic data only, or real data with redaction? Where is the redaction logic?

---

## 10. Telemetry & docs

### 10.1 Telemetry (schema, instrument, redaction, baseline)

The 4 telemetry files (`schema.json`, `instrument.py`, `redaction.md`, `baseline.md`) are required by the lint. The schema is shared across all skills (already in the repo). Confirm reuse vs. customization.

### 10.2 Docs (4 files)

The 4 docs files (`architecture.md`, `limits-and-disclaimers.md`, `changelog.md`, `acceptance-gate.md`) are required. List any custom content for each.

### 10.3 What `acceptance-gate.md` should assert

The acceptance-gate doc is the sign-off checklist. What should it assert for THIS skill? (Mirror the 800-53 RMF version, customized for this skill's deliverables.)

---

## 11. Risk register

Pre-empt what the reviewers will find. Top 5 in each lens.

### 11.1 Top 5 framework-fidelity issues
1. ...
2. ...
3. ...
4. ...
5. ...

### 11.2 Top 5 completeness issues
1. ...
2. ...
...

### 11.3 Top 5 usability issues
1. ...
2. ...
...

### 11.4 Top 5 convention issues
1. ...
2. ...
...

### 11.5 Top 5 cross-skill issues
1. ...
2. ...
...

---

## 12. Build sequence — day-by-day plan

| Day | Tasks | Done when |
|-----|-------|-----------|
| **0** | **Pre-build research** (per `docs/fact-sheet-template.md`) — dispatch 1+ research agents to webfetch authoritative sources and produce a fact-sheet. This is the ONLY phase where webfetch is used before the build starts. Output: `<skill>-fact-sheet.md` in `docs/`. | Fact-sheet populated with all counts, identifiers, crosswalk mappings, and live URLs verified. |
| 1 | Scaffold folders, write SKILL.md router (≤300 lines), declare context_budget | `python tools/lint_skill.py skills/<skill>` passes basic checks |
| 2 | Write 8 chunks, 4 industries, 3 UCs, consumer README | All chunks ≤200 lines, all 3 UCs have frontmatter |
| 3 | Write data/generators, data/seeds, data/crosswalks | Generators run with `--seed`, all seeds load |
| 4 | Write 6 skill-specific test files (lint/consistency are root-level, parametrized) | `pytest skills/<skill>/tests/ -q` passes |
| 5 | **Source-of-truth verification** (per §5.11) — compare built files against the Day 0 fact-sheet (which was sourced from live authoritative documents). **Do NOT proceed to lens review until CRITICALs are fixed.** | Verification report shows 0 CRITICAL findings. |
| 6 | 5-lens review (dispatch 5 agents in parallel) — covers structural, completeness, usability, convention, cross-skill | 5 review reports returned |
| 7 | 5-practitioner review (dispatch 5 agents in parallel) | 5 practitioner reports returned |
| 8 | Fix waves 1, 2, 3 (CRITICAL, HIGH, MEDIUM+LOW) | All findings addressed |
| 9 | Re-lint, re-test, re-verify (re-run §5.11), re-review, ship v0.1.0 | All checks green on PR |

### 12.N+1: Optional reviews

For low-risk skills, days 6-8 can be compressed. For high-risk skills, add a 6th lens (e.g., "regulatory risk") or 6th persona (e.g., "CFO").

**Day 0 is non-negotiable.** Pre-build research against live authoritative sources is what prevents fabricated identifiers, wrong counts, and dead URLs from entering the build in the first place. The Day 0 fact-sheet is the single source of truth that every build agent references. Without it, build agents write from LLM recall. The CSF 2.0 build (June 2026) proved this: 9 parallel build agents wrote plausible-looking content, and a subsequent §5.11 pass found 8 CRITICAL factual errors (fabricated Category codes GV.SR/GV.MT, wrong subcategory counts, ~10 wrong crosswalk rows).

**Day 5 is also non-negotiable.** It is a re-verification of the built files against the fact-sheet, catching any drift introduced during the build (build agents may ignore or misunderstand the fact-sheet). The two gates work together: Day 0 prevents errors from entering, Day 5 catches any that slipped through.

---

## 13. File-by-file plan

A 50-60 row table: every file to be created, with its path, the section that specifies it, and a "done when" check. This is the literal build plan.

| # | File path | Spec section | "Done when" check |
|---|-----------|--------------|-------------------|
| 1 | `skills/<skill>/SKILL.md` | §1, §2 | ≤300 lines, all frontmatter fields, §11 routing table present |
| 2 | `skills/<skill>/chunks/01-...md` | §2.1 | ≤200 lines, frontmatter, cited in SKILL.md |
| ... | ... | ... | ... |

---

## 14. Open questions for review

A numbered list of questions to resolve BEFORE the build starts. Typical:
- "Should healthcare be in v0.1.0 or deferred to v0.3.x?"
- "What is the right handling of [edge case]?"
- "Is [specific term] the right label?"

These should be specific, answerable, and not blocking. If a question blocks the design, the design isn't done.

---

## 15. Requirements parameters checklist (this template)

This is the standardized list of parameters that **every** future skill design doc should hit. The design doc author must fill in every section.

| # | Parameter | Section in this doc | Required? |
|---|-----------|---------------------|-----------|
| 1 | **Scope & dependencies** — standard reference, structural inventory, persona, effort estimate, dependencies, out-of-scope | §1 | Yes |
| 1.1 | Primary source citation (with URL and retrieval date) | §1.1 | Yes |
| 1.2 | Structural inventory (counts of functions/categories/subcategories/etc.) | §1.2 | Yes |
| 1.3 | Persona (IT / FIN / GRC / BOTH) with 1-sentence justification | §1.3 | Yes |
| 1.4 | Effort estimate (S/M/L/XL) per Linear | §1.4 | Yes |
| 1.5 | Dependencies (other skills or Linear issues) | §1.5 | Yes |
| 1.6 | Out-of-scope (explicit non-goals) | §1.6 | Yes |
| 2 | **Chunk architecture** — numbered set of 7-9 chunks | §2 | Yes (skills above 300 lines only) |
| 2.1–2.N | For each chunk: filename, frontmatter, trigger phrases, cross-references | §2.1–§2.8 | Yes |
| 2.N+1 | Why 7/8/9 chunks (rationale for the count) | §2.9 | Yes |
| 3 | **Industry angles** — 3-4 industry files | §3 | Yes |
| 3.1–3.N | For each: most-relevant Functions, real-world example, what the view ADDS, cross-references | §3.1–§3.4 | Yes |
| 3.N+1 | `_index.md` table | §3.5 | Yes |
| 4 | **Use cases** — 3-4 worked examples | §4 | Yes |
| 4.1–4.N | For each: frontmatter contract, real-world scenario, input JSON shape, procedure, expected output, oracle | §4.1–§4.3 | Yes |
| 4.N+1 | UC selection rationale | §4.4 | Yes |
| 5 | **Test architecture** — 6 skill-specific test files, target test count | §5 | Yes |
| 5.1–5.9 | For each test file: specific test cases | §5.1–§5.9 | Yes |
| 5.10 | Test count summary table | §5.10 | Yes |
| 5.11 | **Source-of-truth verification plan** (REQUIRED) — at least 5 fact rows with authoritative source URLs, retrieval dates, and verifier names | §5.11 | Yes |
| 6 | **PoV analyses — 5 lenses** | §6 | Yes |
| 6.1 | Framework fidelity | §6.1 | Yes |
| 6.2 | Completeness | §6.2 | Yes |
| 6.3 | Usability | §6.3 | Yes |
| 6.4 | Spine convention compliance | §6.4 | Yes |
| 6.5 | Cross-skill alignment | §6.5 | Yes |
| 7 | **PoV analyses — 5 practitioner personas** | §7 | Yes |
| 7.1–7.5 | For each persona: what they will check, what we pre-empt | §7.1–§7.5 | Yes |
| 8 | **Cross-skill alignment table** | §8 | Yes |
| 8.1–8.N | For each sibling skill: this-skill chunk → other skill chunk + rationale | §8.1–§8.5 | Yes |
| 8.6 | Cross-skill reference shape (consistency library's view) | §8.6 | Yes |
| 9 | **Data & synthetic content** | §9 | Yes |
| 9.1 | Directory layout | §9.1 | Yes |
| 9.2 | Generators (deterministic CLIs) | §9.2 | Yes |
| 9.3 | Seed JSONs | §9.3 | Yes |
| 9.4 | Crosswalk JSONs | §9.4 | Yes |
| 9.5 | PII / NPI / PHI redaction | §9.5 | Yes |
| 10 | **Telemetry & docs** | §10 | Yes |
| 10.1 | Telemetry (schema, instrument, redaction, baseline) | §10.1 | Yes |
| 10.2 | Docs (4 files) | §10.2 | Yes |
| 10.3 | What `acceptance-gate.md` should assert | §10.3 | Yes |
| 11 | **Risk register** | §11 | Yes |
| 11.1 | Top 5 framework-fidelity issues | §11.1 | Yes |
| 11.2 | Top 5 completeness issues | §11.2 | Yes |
| 11.3 | Top 5 usability issues | §11.3 | Yes |
| 11.4 | Top 5 convention issues | §11.4 | Yes |
| 11.5 | Top 5 cross-skill issues | §11.5 | Yes |
| 12 | **Build sequence** — day-by-day plan | §12 | Yes |
| 13 | **File-by-file plan** — table of every file to create | §13 | Yes |
| 14 | **Open questions for review** | §14 | Yes |
| 15 | **Requirements parameters checklist** (this template) | §15 | Yes (this template) |

A future skill design doc that hits all 15 sections (with the same sub-structure) is reviewable in one sitting and convertible into a build plan without further clarification. The 800-53 RMF skill (the load-bearing reference) covered 12 of 15 sections; CSF 2.0 covers all 15. Future skills should aim for 15/15.

---

## 16. Sign-off

- [ ] Design review (Monday) — owner: amurthy
- [ ] Convert to build plan (post-review) — owner: amurthy
- [ ] Begin build (Day 1) — owner: amurthy
- [ ] Ship v0.1.0 (Day N) — owner: amurthy + at least 1 external reviewer

— End of design doc template —
