# Design — fedramp-authorization (SOX-574)

> 15-section design per `docs/skill-design-template.md`. Built on the Day-0 fact sheet
> (`docs/fedramp-authorization-fact-sheet.md`, gate PASS) with Rev 5 baseline counts taken
> directly from the PMO-authored OSCAL profiles. Born-vetted (process v3/v3.1): G4.5 + the eval
> lane ship inside the build PR. Licence class = public (US-government text — machine-verifiable,
> full vendoring permitted, like the eCFR/SEC builds).

## 0. Why this design doc exists

M5 cycle 4's new skill. Effort **M**: the FedRAMP cloud-authorization *program* — Rev 5
baselines, the modernized authorization path, the SSP/SAP/SAR/POA&M package, the 3PAO
assessment, monthly ConMon, and the FedRAMP 20x direction. The design pins the chunk map, the
three UC contracts (ticket B34/B35/B36), the §5.11 plan, and the two hard boundaries: **FedRAMP
is the program layer on top of the NIST SP 800-53 Rev 5 catalog** (owned by `nist-800-53-rmf`),
and the **current governance is the statutory FedRAMP Board, not the retired JAB**.

## 1. Scope & dependencies

### 1.1 Primary source citation

FedRAMP Authorization Act of 2022 (PL 117-263; 44 U.S.C. 3607–3616); OMB M-24-15 (2024-07-25);
fedramp.gov Rev 5 playbook (SSP, ConMon); the PMO-authored OSCAL Rev 5 baseline profiles
(OSCAL-Foundation/fedramp-resources); A2LA 3PAO accreditation (ISO/IEC 17020); NIST SP 800-53
Rev 5 / 800-53B. All public, fetched 2026-06-11. The load-bearing facts are the **baseline
counts** (156/323/410/156) and the **current governance model**.

### 1.2 Structural inventory (counts)

From the fact sheet §0: 4 baselines — **Low 156** (135 base + 21 enh), **Moderate 323** (181 +
142), **High 410** (191 + 219), **LI-SaaS 156** (135 + 21; 66 3PAO-tested + 90 attested);
800-53B baselines 149/287/370; FIPS 199 = 3 impact levels over 3 CIA objectives (high-water
mark); 4 core package artifacts (SSP/SAP/SAR/POA&M); monthly ConMon; remediation SLAs 30/90/180
days (high/moderate/low).

### 1.3 Persona

**IT** (per ticket): cloud-security engineers, CISOs/ISSOs at CSPs pursuing authorization,
agency security reviewers (the sponsoring side), and 3PAO assessors. Both the **CSP-side**
(getting authorized) and the **assessor/agency-side** (granting/leveraging) are in scope.

### 1.4 Effort estimate

**M** (per ticket). 8 chunks, 4 industries, 3 UCs, ~40 tests + eval cases. One build PR.

### 1.5 Dependencies

- Day-0 fact sheet (done; gate PASS).
- **nist-800-53-rmf** — the control catalog + general RMF; one-way cross-reference for the
  "FedRAMP baselines ARE tailored 800-53 controls" boundary. No shared data, no re-teaching.
- hipaa-security-rule / nist-csf-2 — pointers for the health-tech CSP overlap and general cyber.
- Registry: FedRAMP/OMB/statute citations added at G3 (labels: `FEDRAMP-ACT-2022`,
  `OMB-M-24-15`, `FEDRAMP-REV5-BASELINES`, `FEDRAMP-CONMON`, `A2LA-3PAO`, `NIST-800-53R5`).

### 1.6 Out-of-scope (explicit non-goals)

- **The 800-53 Rev 5 control catalog / general RMF** — `nist-800-53-rmf` owns it; this skill
  cites the boundary, never re-teaches the catalog. No control-by-control baseline enumeration
  (300+ rows) in v1 — counts + tailoring relationship only.
- **DoD Impact Levels (IL2/4/5/6) / DISA SRG** — a separate regime; named as adjacent, not covered.
- **StateRAMP / CMMC** — distinct programs that borrow FedRAMP's model; out of scope.
- Authoring a full SSP/SAR document — the skill explains the package + process; document drafting
  is a downstream use case, not a deliverable.
- FedRAMP **20x is labeled emerging direction** everywhere — never asserted as the settled
  Rev 5 process.
- No crosswalk rows in v1 (FedRAMP baselines are 800-53 controls — identity, not a mapping).

## 2. Chunk architecture (8 chunks)

| # | File | Contents (all from fact sheet / public sources) | Est. lines |
|---|------|--------------------------------------------------|-----------|
| 01 | 01-fedramp-and-governance.md | What FedRAMP is (standardized cloud-security authorization); the 2022 Authorization Act (44 USC 3607-3616); the **statutory FedRAMP Board (§3610), NOT the JAB**; OMB M-24-15 (rescinds 2011 memo); the Marketplace; framing: this is the *program* layer on 800-53 | 170 |
| 02 | 02-impact-levels-and-baselines.md | **The spine + the boundary.** FIPS 199 categorization (CIA high-water mark → Low/Moderate/High); the 4 baselines with exact counts (156/323/410/156, base+enh); how FedRAMP **tailors UP** from 800-53B (149/287/370) with FedRAMP additions/parameters; LI-SaaS Tailored (66 tested + 90 attested); the SAME 800-53 control IDs — boundary vs nist-800-53-rmf | 185 |
| 03 | 03-authorization-paths.md | The **current** path: Agency Authorization (operative Rev 5); multi-agency; the single-authorization + **presumption of adequacy** (M-24-15); **JAB P-ATO retired** (legacy P-ATOs re-designated by the PMO); FedRAMP Ready / readiness assessment (RAR) → full assessment → ATO; the authorizing official | 175 |
| 04 | 04-the-authorization-package.md | The package: **SSP** (the "security blueprint," CSP-authored), **SAP** (3PAO-authored plan), **SAR** (3PAO-authored results), **POA&M** (CSP corrective-action plan); who authors what; how they sequence; attachments (FIPS 199 worksheet, contingency/IR plans, scan results) | 165 |
| 05 | 05-3pao-assessment-and-inheritance.md | The 3PAO: independent assessor; **A2LA** accreditation to **ISO/IEC 17020** (Type A or C; Type B prohibited for independence); SAP → control testing & sampling → SAR → risk + recommendation; **control inheritance / leveraging** (IaaS/PaaS → SaaS; inherited controls not re-tested by the leveraging CSP) | 175 |
| 06 | 06-continuous-monitoring.md | **ConMon** = monthly cadence; the three objectives (operational visibility / managed change control / incident response); monthly submission (updated POA&M, system inventory, vuln scan results); scan frequencies; **remediation SLAs 30/90/180 days** (high-critical/moderate/low); significant-change requests; annual/triennial reassessment | 175 |
| 07 | 07-poam-and-risk.md | **POA&M lifecycle**: SAR deficiency → POA&M item; severity → SLA; the three **deviation-request** types (False Positive / Risk Adjustment / Operational Requirement); vendor-dependency & operational-requirement handling; how POA&M drives ConMon and re-authorization; the risk-acceptance role of the AO | 165 |
| 08 | 08-fedramp-20x-and-modernization.md | **FedRAMP 20x (emerging — labeled):** automation-first, outcome-based; **Key Security Indicators (KSIs)**; **machine-readable packages** (RFC 0024); the OSCAL artifacts; presumption-of-adequacy realized; what is **settled (Rev 5)** vs **direction (20x)**; the migration of the OSCAL baselines to the OSCAL Foundation mirror | 160 |

### 2.9 Why 8 chunks

The two concepts consumers get wrong each get a dedicated chunk: the categorization→baseline
count logic + the 800-53 boundary (02), and the current vs retired-JAB governance (01/03). The
package (04) and the 3PAO assessment (05) are the operative process. ConMon (06) and POA&M (07)
are the post-authorization lifecycle — split because POA&M's deviation-request mechanics and
severity SLAs are substantial enough to crowd the ConMon cadence content. 20x (08) is the
volatile/emerging layer, isolated so its "direction not rule" caveat is unambiguous. 7 would
merge ConMon+POA&M and thin the deviation-request detail; 9 would split the package from the
3PAO assessment too finely.

## 3. Industry angles (4)

| Industry | Angle |
|----------|-------|
| saas-technology.md | CSP pursuing **Moderate via Agency Authorization** (B34): SSP ~323 controls, 3PAO SAP/SAR, ~40-item POA&M, monthly ConMon — the most common path |
| public-sector.md | **Sponsoring agency / AO side**: leveraging an authorization package, the **presumption of adequacy**, ConMon oversight, the ATO decision; multi-agency reuse |
| financial-services.md | Fintech / gov-financial SaaS needing the **High baseline** (410): data-impact categorization, stricter ConMon, the High-vs-Moderate delta |
| healthcare.md | Health-tech CSP serving government health systems: **FedRAMP + HIPAA** overlap (the control families that double-count), categorization of PHI workloads |

`_index.md` mirrors SKILL.md routing.

## 4. Use cases (3 — ticket B34/B35/B36)

UC seed + oracle contracts; docs written to the tested fixtures. Oracles are **derivability-based**
— the stub computes from seed facts; the oracle recomputes independently; nothing echoed.

### 4.1 UC-01 — SaaS FedRAMP Moderate via Agency Authorization (B34)

Seed: a system with per-objective FIPS 199 impact (e.g., C=Moderate, I=Low, A=Low) and a set of
SAR findings each with a severity and an identified date. Output: the **FIPS 199 categorization**
(overall = **high-water mark** across C/I/A → Moderate); the **selected baseline** (Moderate →
**323 controls**); the **POA&M remediation deadlines** (each finding's due-date = identified-date
+ {high/critical: 30, moderate: 90, low: 180} days). Oracle: overall impact recomputed as
`max(C,I,A)`; baseline count looked up from the level (NOT hardcoded to one value); each POA&M
due-date recomputed from severity + date. Metamorphic: raise any single objective to High →
overall flips to High and baseline → 410.

### 4.2 UC-02 — Cloud vendor LI-SaaS readiness (B35)

Seed: a low-impact SaaS offering — all three CIA objectives = Low and a `saas_delivery: true`
flag (plus a readiness-assessment context). Output: the **LI-SaaS eligibility determination**
(eligible iff overall impact = Low AND SaaS-delivered) and, if eligible, the **Tailored baseline**
(**156 controls = 66 3PAO-tested + 90 CSP-attested**). Oracle: eligibility derived from
`impact == Low and saas_delivery`; the tested/attested split is the fixed Tailored split (cited
to the LI-SaaS baseline doc). Adversarial: impact = Moderate with saas_delivery=true → NOT
LI-SaaS-eligible (must use full Moderate, 323) — a common misconception.

### 4.3 UC-03 — Big-4 3PAO assessment of a Moderate CSP (B36)

Seed: a control-test result set — each control tagged passed/failed and inherited/own (IaaS
inheritance), plus severities for the failures. Output: the **SAR finding roll-up** (findings =
failed controls that are the CSP's **own**, not inherited); the **POA&M item count** (= number
of findings); the **severity rollup** (count by high/moderate/low); the 3PAO **recommendation**
(authorize-with-POA&M vs not, by whether any unmitigated high finding remains). Oracle: findings
recomputed as `[c for c in controls if c.failed and not c.inherited]`; POA&M count = len(findings);
inherited-and-failed controls excluded (the leveraging CSP inherits the provider's remediation).
Metamorphic: marking a failed control `inherited` removes it from the CSP's POA&M.

### 4.4 UC selection rationale

Ticket-specified (B34/B35/B36); covers the **categorization→baseline count** path (the
load-bearing logic), the **LI-SaaS eligibility** path (the most-misunderstood baseline), and the
**3PAO finding→POA&M roll-up with inheritance** (the assessor path). Both CSP-side and
assessor/agency-side personas are exercised.

## 5. Test architecture

| File | Cases | Count |
|------|-------|-------|
| test_fedramp_authorization_lint.py | linter exit 0 | 1 |
| test_fedramp_authorization_oracle.py | UC-01/02/03 derivability + expected-seed agreement | 6 |
| test_fedramp_authorization_grounding.py | citations resolve; manifest bidirectional; registry sync | 4 |
| test_fedramp_authorization_trace.py | UC procedures cite real SKILL.md sections; chunks exist | 3 |
| test_fedramp_authorization_metamorphic.py | objective→High flips baseline; inherited-flag removes POA&M item; finding-order invariance | 4 |
| test_fedramp_authorization_adversarial.py | missing FIPS 199 fact → refuse; Moderate+SaaS ≠ LI-SaaS; JAB never named as current authorizer; 20x labeled emerging; inherited finding excluded; empty control set | 6 |
| test_fedramp_authorization_telemetry.py | schema; instrument; enums | 5 |
| test_fedramp_authorization_consistency.py | routing ↔ chunks; industry/UC index sync; **fact-sheet counts == chunk counts (inventory-diff: 156/323/410/156, 149/287/370)** | 6 |
| test_fedramp_authorization_chunks.py | per-chunk frontmatter, ≤200 lines, in routing | 8 |
| **Total target** | | **43** |

Eval lane: `evals/fedramp-authorization/cases/` with the 3 UC substance cases + 1 categorization
idempotence invariant + the refusal/eligibility perturbation set, oracle-labeled, CI-enforced.

### 5.11 Source-of-truth verification plan

| Fact | Source | Verified by |
|------|--------|-------------|
| Rev 5 baseline counts 156/323/410/156 (base+enh) | PMO OSCAL profiles (OSCAL-Foundation/fedramp-resources) | dispatcher; G4 re-count |
| 800-53B baselines 149/287/370; FedRAMP tailors up | NIST SP 800-53B; fedramp.gov | dispatcher |
| FIPS 199 high-water-mark categorization | FIPS 199; fedramp.gov understanding-baselines | dispatcher |
| FedRAMP Board (§3610) replaced the JAB; JAB P-ATO retired | 44 USC 3610; OMB M-24-15 | dispatcher (currency gate) |
| M-24-15 date 2024-07-25; presumption of adequacy | fedramp.gov/docs/authority/m-24-15 | dispatcher (verify quotes) |
| ConMon monthly; SLAs 30/90/180 | fedramp.gov ConMon overview | dispatcher |
| 3PAO accredited by A2LA to ISO/IEC 17020 | a2la.org/accreditation/fedramp | dispatcher |
| FedRAMP 20x = emerging; KSIs; RFC 0024 | fedramp.gov/20x | dispatcher (label as direction) |

Public, machine-verifiable; the §5.11 agent re-counts the OSCAL profiles and diffs governance
against M-24-15 / 44 USC. **Anti-hallucination/limits sections verified FIRST.** The two highest
risks: (1) presenting the JAB as a current authorizer (it is retired — explicit grep gate), and
(2) a wrong baseline count (inventory-diff gate against the fact sheet).

## 6. PoV analyses — 5 lenses

- **Framework fidelity:** the three fidelity risks — JAB-as-current, wrong baseline counts, and
  20x-as-settled — each get a grep/inventory-diff/adversarial gate.
- **Completeness:** all 4 baselines; both governance eras (what changed); the full package; both
  CSP-side and agency/3PAO-side of the IT audience.
- **Usability:** the categorization→baseline table and the POA&M severity-SLA table are the
  references consumers want; the package sequence is a copy-paste checklist.
- **Spine conventions:** ≤300-line router, ≤200-line chunks, §1–§11, telemetry, house-style §6.
- **Cross-skill:** the 800-53 boundary to nist-800-53-rmf is one-way; health overlap → hipaa.

## 7. PoV analyses — 5 personas

- **CSP ISSO (saas, B34):** wants the categorization→Moderate→323 logic and the package sequence
  exactly right.
- **Cloud-vendor founder (LI-SaaS, B35):** the eligibility test and the 66/90 tested-vs-attested
  split — and the trap that Moderate+SaaS is not LI-SaaS.
- **Big-4 3PAO assessor (B36):** the finding→POA&M roll-up, inheritance, sampling, the SAR
  recommendation logic.
- **Agency authorizing official:** the presumption of adequacy, leveraging, the ATO decision.
- **Compliance skeptic / FedRAMP PMO reviewer:** will check that the JAB is described as retired,
  the counts match the OSCAL profiles, and 20x is labeled emerging — not the current rule.

## 8. Cross-skill alignment table

| Other skill | Touchpoint | Shape |
|-------------|-----------|-------|
| nist-800-53-rmf | FedRAMP baselines = tailored 800-53 Rev 5 controls (same catalog) | one-way reference from chunk 02; no re-teaching the catalog |
| hipaa-security-rule | health-tech CSP: FedRAMP + HIPAA control overlap | pointer in chunk 05 / healthcare.md |
| nist-csf-2 | general cyber posture feeding the SSP | pointer in chunk 01 |
| aicpa-soc-reporting | SOC 2 as adjacent (commercial) assurance vs FedRAMP (federal) | one-line contrast in chunk 01 |

## 9. Data & synthetic content

- `data/seeds/`: uc-01-input/expected (per-objective FIPS 199 + SAR findings), uc-02-input/expected
  (low-impact SaaS eligibility), uc-03-input/expected (control-test set with inheritance).
  Fictional CSPs/systems; no real FedRAMP package data; `as_of_date` where dates matter (POA&M
  deadlines).
- `data/generators/`: `gen_control_results.py --seed` (control-test sets for the eval sampler);
  `gen_fips199.py --seed` (CIA-objective triples for categorization metamorphic cases).
- `data/crosswalks/`: empty v1 (baselines are 800-53 controls — identity, not a mapping).
- Redaction: no real system names / IP / vuln data; seeds are structural facts only.

## 10. Telemetry & docs

Standard Spine set. Docs: architecture.md, limits-and-disclaimers.md (FedRAMP ≠ the 800-53
catalog; FedRAMP Board ≠ JAB; 20x = direction not rule; not legal/authorization advice; counts
are Rev 5 as of 2026-06 — re-verify currency), changelog.md, acceptance-gate.md (≥20 rows from
the fact sheet's verified facts). persona-review.md by G4.5.

## 11. Risk register (top per category)

1. **Fidelity/currency:** JAB presented as a current authorizer → chunk 01/03 + grep gate +
   adversarial test (the FedRAMP Board / M-24-15 model is current).
2. **Fidelity:** a wrong baseline count → inventory-diff gate vs fact-sheet (156/323/410/156).
3. **Fidelity:** FedRAMP 20x presented as the settled rule → label gate + isolated chunk 08.
4. **Fidelity:** LI-SaaS eligibility overclaimed (Moderate+SaaS treated as LI-SaaS) → adversarial.
5. **Completeness:** a package artifact dropped → consistency test asserts SSP/SAP/SAR/POA&M.
6. **Cross-skill:** the 800-53 catalog re-taught here (scope creep) → chunk 02 references
   nist-800-53-rmf, does not re-teach.

## 12. Build sequence

- Day 1: scaffold + SKILL.md + chunks 01-02 (governance + baselines/boundary).
- Day 2: chunks 03-08.
- Day 3: industries; seeds + generators + stub + oracle/metamorphic/adversarial (contract first);
  UC docs to fixtures; eval cases.
- Day 4: remaining tests; lint; consistency (inventory-diff); calibration sweep.
- Day 4.5 (§5.11): verification vs OSCAL profiles / M-24-15 / 44 USC + fix + re-verify.
- Day 5: 5-lens + persona vetting (G4.5) in-PR; smokes; acceptance-gate.
- Day 6: PR, CI, merge; Linear; plan.

## 13. File-by-file plan

`skills/fedramp-authorization/`: SKILL.md, README.md; chunks/01-08; industries/_index + 4
(saas-technology, public-sector, financial-services, healthcare); use-cases/_index +
uc-01-moderate-agency-ato.md, uc-02-li-saas-readiness.md, uc-03-3pao-assessment.md; data/ per §9;
tests/ 9 files + stub + conftest; telemetry/ 4; docs/ 4 + persona-review.md (G4.5);
evals/fedramp-authorization/cases/.

## 14. Open questions for review

1. Reproduce the per-control baseline lists, or counts + tailoring relationship only?
   **Decision: counts + relationship only** — the 300+-row per-control enumeration belongs to
   nist-800-53-rmf's catalog; v1 encodes the four totals (OSCAL-verified) and the boundary.
2. Is "agency-side" an industry or a use-case angle? **Decision: industry** (public-sector.md
   carries the sponsoring-AO angle); the 3PAO assessor is exercised as UC-03, not an industry.
3. LI-SaaS 66/90 split — assert it as a tested count? **Decision: state it, cite the Tailored
   LI-SaaS baseline doc** (it is documented, but NOT a flat OSCAL count — the fact sheet records
   this caveat); the oracle uses the fixed split, not an OSCAL re-derivation.
4. FedRAMP 20x depth? **Decision: one chunk, labeled emerging** — enough to orient (KSIs,
   machine-readable, OSCAL), not a process the skill certifies against.

## 15. Requirements parameters checklist

- [x] §1 scope/deps/out-of-scope; [x] §2 8 chunks ≤200 rationale; [x] §3 4 industries;
- [x] §4 3 UCs with seed+oracle contracts; [x] §5 test arch (43 target) + §5.11 plan;
- [x] §6 5 lenses; [x] §7 5 personas; [x] §8 cross-skill; [x] §9 data (no real package data);
- [x] §10 telemetry/docs; [x] §11 risk register; [x] §12 day plan; [x] §13 file plan;
- [x] §14 open questions resolved; [x] §15 this checklist.

## 16. Sign-off

- Designer: Claude (Opus 4.8) dispatcher, 2026-06-11.
- Fact-sheet gate: PASS. Licence class: public (machine-verifiable, full vendoring permitted).
- Ready for G3: **yes** — build agents receive the fact sheet + this design; the UC seed/oracle
  contracts in §4 are binding, and the baseline counts are the OSCAL-verified single source.
