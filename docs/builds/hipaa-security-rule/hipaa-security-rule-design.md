# Design — hipaa-security-rule (SOX-572)

> 15-section design per `docs/skill-design-template.md`. Built on the Day 0 fact sheet
> (`docs/hipaa-security-rule-fact-sheet.md`) — **no build agent writes from recall; every
> identifier and count comes from the fact sheet's §0 data block.** First born-vetted skill:
> G4.5 (persona vetting + §5.11 live-source verification) runs INSIDE the build PR (process v3).

## 0. Why this design doc exists

First skill built end-to-end under process v3. The design pins: chunk map, UC contracts
(seed + derivability oracle designed BEFORE docs), the §5.11 verification plan, and explicit
non-goals (no crosswalk rows in v1 — SOX-638). DoD per ticket: house-style §6.

## 1. Scope & dependencies

### 1.1 Primary source citation

45 CFR Part 164, Subpart C, retrieved 2026-06-10 as point-in-time XML from the official eCFR
API (2026-06-09 snapshot): `https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C`.
Companion guide: NIST SP 800-66r2 (Final, 2024-02-14). NPRM 90 FR 898 (RIN 0945-AA22) —
**Proposed Rule only as of 2026-06-10, verified at the docket level**.

### 1.2 Structural inventory (counts)

From the fact sheet §0 (Tier 1, mechanical): 22 standards total — Administrative 9 (21 specs:
10 R / 11 A), Physical 4 (8: 2 R / 6 A), Technical 5 (7: 2 R / 5 A), Organizational 2,
Policies/documentation 2 (3 R specs). Appendix A matrix: 18 standards, 36 titled specs
(14 R / 22 A); 42-entry convention = 20 R / 22 A. 17 definitions in §164.304. Both counting
conventions must be labeled wherever a count appears.

### 1.3 Persona

**BOTH** (per ticket). Auditor side: OCR-readiness assessment, evidence expectations, finding
language. Auditee side: risk analysis, addressable-spec dispositions, BAA checklist,
right-sizing via §164.306(b)(2) flexibility factors.

### 1.4 Effort estimate

**M** (per ticket). 8 chunks, 4 industries, 3 UCs, 35+ tests. One build PR.

### 1.5 Dependencies

- Day 0 fact sheet (done, committed `a741ff2`).
- nist-800-53-rmf: HIPAA crosswalk completion is **SOX-638**, gated on CPRT extraction — not
  this build.
- nist-csf-2 healthcare industry view: cross-reference only (no shared data files).
- Registry: new citations (CFR-45-164-Subpart-C, HIPAA-Security-NPRM-2025, NIST-SP-800-66r2,
  HHS-SRA-Tool, PL-116-321) go to `data/registry/citations.json` FIRST.

### 1.6 Out-of-scope (explicit non-goals)

- Privacy Rule (Subpart E) and Breach Notification Rule (Subpart D) mechanics — touchpoints
  only (§164.314(a)(2)(i)(C) → §164.410; encryption safe-harbor pointer to §164.402
  "unsecured PHI" definition without reproducing Subpart D).
- NPRM content presented as anything other than PROPOSED.
- Crosswalk rows (CSF/800-53) — none in v1; chunks point to CPRT/OLIR (SOX-638).
- State law preemption, 42 CFR Part 2, FTC HBNR, OCR audit protocol line items.
- Penalty amounts beyond the pinned 2025-adjustment table with as-of date.

## 2. Chunk architecture (8 chunks)

| # | File | Contents (all facts from fact sheet) | Est. lines |
|---|------|--------------------------------------|-----------|
| 01 | 01-scope-and-general-rules.md | Subpart C map; CE/BA applicability (§164.302, BA direct liability); ePHI-only scope; §164.306(a) 4 general requirements; (b) flexibility factors; (d) required-vs-addressable decision logic; counting conventions + rendering artifacts | 180 |
| 02 | 02-risk-analysis-and-management.md | §164.308(a)(1) all 4 R specs; risk analysis as the anchor control; SP 800-66r2 cyclical approach; SRA Tool; recognized security practices (PL 116-321, mitigation-not-immunity); house-convention risk scales labeled | 190 |
| 03 | 03-administrative-safeguards.md | §164.308(a)(2)–(a)(8) + (b): each standard, its specs with exact (R)/(A), key activities, evidence examples | 195 |
| 04 | 04-physical-safeguards.md | §164.310 all 4 standards + 8 specs; facility/workstation/device-media; disposal & media re-use (R) emphasis | 160 |
| 05 | 05-technical-safeguards.md | §164.312 all 5 standards + 7 specs; encryption is Addressable as written but the de facto expectation (documented-decision pattern); audit controls vs ISAR distinction | 180 |
| 06 | 06-organizational-and-documentation.md | §164.314 BAA required provisions (a)(2)(i)(A)–(C), subcontractor flow-down, group health plans; §164.316 policies + 3 R documentation specs (6-year retention) | 170 |
| 07 | 07-addressable-decisions-and-evidence.md | The addressable-disposition workflow (assess→implement / document-why-not + equivalent alternative); disposition record template (house convention, labeled); evidence catalog per safeguard family; auditee prep | 185 |
| 08 | 08-enforcement-audit-and-nprm.md | Penalty tiers (2025-adjusted, as-of-dated, pointer to 45 CFR 102.3); 2019 NED caps labeled enforcement-posture; OCR audit readiness; **2025 NPRM — every item flagged PROPOSED**; re-verify instruction | 190 |

### 2.9 Why 8 chunks

Three safeguard families (admin is too big to share a chunk), risk analysis is the #1 OCR
finding and the anchor UC (own chunk), organizational+documentation pair naturally, the
addressable workflow is the skill's signature consumer value (own chunk), enforcement/NPRM
isolates the volatile content for cheap re-verification. 7 would merge 06+07 past 200 lines;
9 would split NPRM into a stub chunk.

## 3. Industry angles (4)

| Industry | Angle |
|----------|-------|
| healthcare.md | Hospital/provider CE: 6k-staff scale, medical devices/legacy systems vs §164.312, workforce churn vs §164.308(a)(3), OCR readiness |
| saas-technology.md | Health-tech SaaS BA: direct liability, BAA flow-down to subprocessors (§164.308(b)(2)), shared-responsibility vs cloud provider, SOC 2 evidence reuse (labeled: overlap, not equivalence) |
| financial-services.md | Group health plan sponsors (§164.314(b)), insurers as CEs, plan-document amendment specs |
| public-sector.md | State Medicaid/health agencies as hybrid entities, public-records vs 6-year retention, state breach overlays (pointer only) |

`_index.md` table mirrors SKILL.md routing exactly (consistency tests).

## 4. Use cases (3 — per ticket B28/B29/B30)

UC contracts below are the build's spine: **seed + oracle are designed here, docs are written
to the tested fixture** (process v3 rule 2). All oracles are derivability-based (no echo).

### 4.1 UC-01 — BA risk analysis & addressable dispositions (ticket B28)

Health-tech SaaS BA ("CareSync Relay", ~40 staff, AWS-hosted, ePHI for 12 provider customers).
Seed: `uc-01-input.json` (org profile, system inventory with ePHI flows), `uc-01-risks.json`
(15 risk records: asset, threat, vulnerability, likelihood 1–3, impact 1–3),
`uc-01-addressable-register.json` (**all 22 addressable specs** from the fact sheet, each with
environment facts; 12 of them flagged `decision_required: true` for the engagement — matching
ticket's "12 addressable specs w/ rationale").
Output: risk register rollup + disposition record per addressable spec
(`implement | alternative_measure | not_reasonable_documented`) + encryption-at-rest decision
(= `implement`, derived from seed facts: cloud-hosted, PHI volume, no compensating control).
Oracle (derivability): risk score = likelihood×impact (house convention, labeled in doc AND
stub docstring); counts by band recomputed independently; every addressable spec in the seed
has exactly one disposition; `alternative_measure` requires non-empty `alternative` field;
encryption-at-rest disposition == `implement`; no spec ID outside the fact-sheet 22.

### 4.2 UC-02 — Hospital CE OCR-readiness assessment (ticket B29)

Hospital CE ("Bellbrook Regional Health", 6k staff). Seed: `uc-02-control-inventory.json`
(per-standard implementation status across **all 22 standards**: status ∈
`implemented | partial | missing`, evidence_ref placeholder per engagement),
`uc-02-documentation-register.json` (policy docs with last-review dates).
Output: readiness matrix (22 rows), gap list with priority (house heuristic: missing R-spec
standard → High; partial R → Medium; addressable undocumented → Medium; else Low — labeled),
documentation-currency flags (>6y → finding), NPRM pre-read section every row tagged
`PROPOSED`.
Oracle (derivability): matrix has exactly 22 rows = fact-sheet standards; gap totals foot to
status counts; priority assignment recomputed independently; zero NPRM-derived rows in the
current-law gap list; documentation flags derivable from dates in seed (no wall-clock calls —
`as_of_date` is a seed field).

### 4.3 UC-03 — Solo consultant BAA + right-sized safeguard checklist (ticket B30)

Solo HIT consultant BA (1 person, laptop + SaaS EHR access). Seed: `uc-03-input.json`
(engagement profile, services, systems), `uc-03-baa-terms.json` (proposed BAA clause list, 2
required provisions intentionally missing).
Output: BAA completeness check against §164.314(a)(2)(i)(A)–(C) + §164.308(b)(3); right-sized
safeguard checklist derived via §164.306(b)(2) factors (size/complexity factor documented per
item); explicitly NOT a "small entities are exempt" claim (no such exemption exists).
Oracle (derivability): missing-provision list == exactly the 2 seeded omissions; every
checklist item carries a CFR cite that exists in the fact-sheet identifier list; flexibility
rationale present for every `scaled_down: true` item.

### 4.4 UC selection rationale

Ticket-specified (B28/B29/B30); covers BOTH personas (B28/B30 auditee, B29 auditor-readiness),
all three safeguard families, the addressable workflow (the skill's core consumer value), and
org sizes 1 / 40 / 6,000 (flexibility-of-approach demonstrated, not just asserted).

## 5. Test architecture

| File | Specific cases | Count |
|------|----------------|-------|
| test_hipaa_security_rule_lint.py | linter exit 0 | 1 |
| test_hipaa_security_rule_oracle.py | UC-01/02/03 derivability oracles (independent recompute + footing), expected-seed agreement | 5 |
| test_hipaa_security_rule_grounding.py | citations resolve to manifest; manifest bidirectional; registry label+URL match | 4 |
| test_hipaa_security_rule_trace.py | UC procedures cite real SKILL.md sections; chunks exist in routing | 3 |
| test_hipaa_security_rule_metamorphic.py | risk-record order invariance (UC-01); status relabel consistency (UC-02); BAA clause order invariance (UC-03) | 3 |
| test_hipaa_security_rule_adversarial.py | empty addressable register; all-implemented inventory (zero gaps); BAA with zero omissions; unknown spec ID rejected; NPRM item injected into current-law seed → excluded | 5 |
| test_hipaa_security_rule_telemetry.py | schema validates; instrument emits; enums | 5 |
| test_hipaa_security_rule_consistency.py | routing ↔ chunks; industry/UC index sync; fact-sheet counts == chunk-stated counts (inventory-diff in CI) | 5 |
| test_hipaa_security_rule_chunks.py | per-chunk frontmatter, ≤200 lines, in routing | 8 |
| **Total target** | | **39** |

**Inventory-diff as a CI test:** `test_..._consistency.py` parses the fact sheet §0 YAML and
asserts every count and spec ID stated in chunks matches it. The fact sheet is in-repo, so
this is a standing Tier 1 gate, not a one-time check.

### 5.11 Source-of-truth verification plan (REQUIRED)

| Fact | Source | Retrieved | Verified by |
|------|--------|-----------|-------------|
| 9/4/5 standards per safeguard family; 21/8/7 titled specs; R/A splits 10-11 / 2-6 / 2-5 | eCFR API XML 2026-06-09 snapshot | 2026-06-10 | dispatcher (mechanical transcription) |
| Appendix A: 18 standards, 36 titled specs (14R/22A); 42-entry convention 20R/22A | same + artifact notes (fact sheet §2) | 2026-06-10 | dispatcher |
| §164.306(d)(3) addressable logic verbatim | same | 2026-06-10 | dispatcher |
| NPRM 90 FR 898 is Proposed-only; no final rule under RIN 0945-AA22 | Federal Register API docket query | 2026-06-10 | dispatcher |
| SP 800-66r2 Final 2024-02-14, supersedes Rev 1; mappings moved to CPRT; CSF mapping is v1.1 "intentionally broad" | csrc.nist.gov + PDF pp. 105 | 2026-06-10 | dispatcher |
| PL 116-321 approved Jan 5, 2021 (NOT 2020 — 800-66r2 fn.9 error documented) | govinfo statute text | 2026-06-10 | dispatcher |
| Penalty tiers, 2025-adjusted amounts | eCFR Part 102 §102.3 table | 2026-06-10 | dispatcher |
| 6-year retention (§164.316(b)(2)(i)); 17 definitions (§164.304) | eCFR XML | 2026-06-10 | dispatcher |

G4 §5.11 pass re-verifies: NPRM status (live, every pass — this is the volatile claim),
all chunk-stated counts vs fact sheet, anti-hallucination/limits sections FIRST, currency of
SP 800-66r2, house-convention labeling (risk scale, gap-priority heuristic).

## 6. PoV analyses — 5 lenses

- **Framework fidelity:** the (R)/(A) designation per spec is the #1 fidelity risk — the
  consistency test diffs every designation against the fact sheet. "Addressable ≠ optional"
  language must be verbatim-derived from §164.306(d)(3).
- **Completeness:** all 22 standards reachable from routing; both personas served per UC;
  org-size range 1→6k.
- **Usability:** disposition record template + evidence catalog are copy-paste usable; every
  chunk's "what the auditor asks" mirrors SP 800-66r2 sample-question style without
  reproducing them verbatim.
- **Spine conventions:** ≤300-line router, ≤200-line chunks, §1–§11 contract, telemetry files,
  house-style §6 DoD per ticket.
- **Cross-skill alignment:** healthcare views in nist-csf-2/aicpa-soc-reporting reference
  HIPAA — cross-references must point at this skill's chunks, not restate facts (drift risk).

## 7. PoV analyses — 5 practitioner personas

- **FedRAMP 3PAO:** will ask where 800-53 mappings are — chunk 01/05 must state the CPRT
  pointer + SOX-638 deferral explicitly, not silently omit.
- **Big 4 SOX partner:** will probe penalty/enforcement claims — all as-of-dated, NED labeled
  posture-not-law.
- **SaaS compliance lead:** wants the addressable-disposition record + SOC 2 evidence-reuse
  honesty (overlap, not equivalence).
- **Healthcare CISO:** will test encryption guidance — Addressable-as-written vs de facto
  expectation + breach safe-harbor pointer, no overclaim.
- **State gov IT audit director:** hybrid-entity and public-records angles in
  public-sector.md; no state-law advice.

## 8. Cross-skill alignment table

| Other skill | Touchpoint | Shape |
|-------------|-----------|-------|
| nist-csf-2 | healthcare.md HIPAA rows (§164.308/310/312/408) | one-way reference INTO hipaa-security-rule chunks; no new facts there |
| nist-800-53-rmf | HIPAA crosswalk (SOX-638, deferred) | placeholder pointer only |
| aicpa-soc-reporting | SOC 2 evidence reuse for BAs | hipaa chunk 07 references soc skill; labeled overlap-not-equivalence |
| audit-workpapers | evidence/documentation standards | citation-style reference only |
| coso-internal-controls | none (no touchpoint) | — |

Cross-skill refs use the consistency library's existing shape (`skills/<slug>/...` paths).

## 9. Data & synthetic content

- `data/seeds/`: uc-01-input/risks/addressable-register/expected; uc-02-control-inventory/
  documentation-register/expected; uc-03-input/baa-terms/expected. All org names fictional
  (CareSync Relay, Bellbrook Regional Health, "Meridian HIT Consulting"); `as_of_date` seed
  field everywhere a date computation exists (no wall-clock in stub/tests).
- `data/generators/`: `gen_addressable_register.py --seed` (emits the 22-spec register from a
  vendored copy of the fact-sheet spec list), `gen_control_inventory.py --seed` (22-standard
  inventory with status mix).
- `data/crosswalks/`: **empty in v1** — README stub explaining CPRT/OLIR + SOX-638.
- PHI redaction: seeds contain zero PHI (org-level facts only); telemetry/redaction.md states
  ePHI must never enter telemetry events.

## 10. Telemetry & docs

Standard Spine set (schema.json, instrument.py, redaction.md, baseline.md with nulls until
first instrumented run). Docs: architecture.md, limits-and-disclaimers.md (NPRM-PROPOSED
banner, no-legal-advice, penalty as-of-date, addressable≠optional), changelog.md,
acceptance-gate.md seeded from the fact sheet's verification rows (≥20 rows, every row with
verbatim quote + retrieval date — born-vetted, not retrofitted). persona-review.md created by
the G4.5 pass inside this build PR.

## 11. Risk register (top items per category)

1. **Fidelity:** an agent restates a spec as (R) when it's (A) → inventory-diff CI test.
2. **Fidelity:** NPRM content drifts into current-law sections → adversarial test + grep gate
   for "NPRM|proposed" outside chunk 08 / flagged blocks.
3. **Completeness:** group health plan (§164.314(b)) forgotten because no UC uses it →
   chunk 06 + financial-services.md cover it; consistency test asserts the standard list.
4. **Usability:** disposition template too abstract → UC-01 doc walks all 12 decision-required
   specs end-to-end.
5. **Convention:** penalty numbers restated in multiple chunks → stated ONCE in chunk 08;
   grep test forbids amounts elsewhere.
6. **Cross-skill:** nist-csf-2 healthcare HIPAA rows contradict this skill → alignment check
   in G4 (grep both skills for §164 cites; one-way reference rule).

## 12. Build sequence

- Day 1: registry citations + scaffold from TEMPLATE + SKILL.md router + chunk 01.
- Day 2: chunks 02–05 (safeguard families) — from fact sheet only.
- Day 3: chunks 06–08; industries.
- Day 4: seeds + generators + stub + oracle/metamorphic/adversarial tests (contract first);
  UC docs written TO the passing fixtures.
- Day 5: remaining tests green; lint; consistency.
- Day 5.5 (§5.11): live-source verification pass (NPRM re-check mandatory) + fix pass +
  re-verify.
- Day 6: 5-lens + persona vetting (G4.5) inside the PR; smokes; acceptance-gate.md complete.
- Day 7: PR, CI, merge; Linear close; execution-plan update.

## 13. File-by-file plan

`skills/hipaa-security-rule/`: SKILL.md, README.md; chunks/01–08 (per §2); industries/_index +
4 files (per §3); use-cases/_index + uc-01-ba-risk-analysis.md, uc-02-ocr-readiness.md,
uc-03-baa-and-checklist.md; data/ per §9; tests/ 9 files + stub + conftest (per §5);
telemetry/ 4 files; docs/ 4 files + persona-review.md (G4.5 output); assets/ none v1.

## 14. Open questions for review

1. Should chunk 08's NPRM section enumerate proposal details or stay at headline level?
   **Decision: headline level only** — detail rots fastest; the FR doc is one click away.
2. Risk scale 1–3 vs 1–5 for UC-01? **Decision: 1–3** (house convention, labeled; smaller
   surface to defend).
3. Encryption-at-rest disposition hard-coded expectation? **Decision: derived from seed facts,
   not hard-coded** — the oracle asserts the derivation, the doc shows the reasoning.

## 15. Requirements parameters checklist

- [x] §1 scope/deps/out-of-scope; [x] §2 8 chunks ≤200 lines rationale; [x] §3 4 industries;
- [x] §4 3 UCs with seed+oracle contracts BEFORE docs; [x] §5 test architecture, 39 target,
  §5.11 plan with 8 fact rows; [x] §6 5 lenses; [x] §7 5 personas; [x] §8 cross-skill table;
- [x] §9 data plan (no PHI, no wall-clock); [x] §10 telemetry/docs; [x] §11 risk register;
- [x] §12 day plan; [x] §13 file plan; [x] §14 open questions resolved; [x] §15 this checklist.

## 16. Sign-off

- Designer: Claude (Fable 5) dispatcher, 2026-06-10.
- Fact-sheet gate: PASS (`tools/check_fact_sheet.py`, 2026-06-10).
- Ready for G3 build: **yes** — build agents receive the fact sheet + this design; the UC
  seed/oracle contracts in §4 are binding.
