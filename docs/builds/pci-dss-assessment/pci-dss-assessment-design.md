# Design — pci-dss-assessment (SOX-568)

> 15-section design per `docs/skill-design-template.md`. Built on the Day-0 fact sheet
> (`docs/pci-dss-assessment-fact-sheet.md`) and the mechanical inventory
> (`docs/builds/sox-568/pci-dss-inventory.json`) — **no build agent writes from recall.**
> Born-vetted (process v3/v3.1): G4.5 + the eval lane ship inside the build PR. Licence class
> = PCI "Read and Copy" (machine-verifiable against the local PDF; repo stores IDs/paraphrase
> + short attributed excerpts only).

## 0. Why this design doc exists

Second born-vetted skill, and M5 cycle 1. The design pins the chunk map, the three UC
contracts (ticket B19/B20/B21), the §5.11 plan, and the explicit non-goals (brand-defined
levels, sibling PCI standards). The defining design tension is **routing**: PCI's value to a
consumer is "which validation path applies to me and what must I actually do," so the SAQ
selector and the defined-vs-customized decision are the skill's spine, not the 249-requirement
catalog.

## 1. Scope & dependencies

### 1.1 Primary source citation

PCI DSS v4.0.1 (June 2024), acquired 2026-06-11 via PCI SSC document library under the Read
and Copy License; local oracle at `~/Standards-licensed/PCI/PCI-DSS-v4_0_1.pdf`. SAQ catalog
from the authoritative `doc_library.json`. Crosswalk anchor: OLIR PCI-DSS-4.0.1-to-CSF-v2.0.

### 1.2 Structural inventory (counts)

From the fact sheet §0 (mechanical): 6 goals; 12 principal requirements; 63 sections
(5/3/7/2/4/5/3/6/5/7/6/10 across Req 1–12); 249 main-body defined requirements (205 at depth-3,
44 at depth-4); 30 appendix-A requirements (A1 multi-tenant / A2 SSL-early-TLS / A3 DESV);
33 future-dated markers (ALL in force since 2025-03-31); 10 SAQ types; appendices A–G.

### 1.3 Persona

**IT** (per ticket), spanning both an auditee path (merchant/SP scoping, SAQ selection,
self-assessment) and an assessor path (QSA workflow, ROC vs AOC, compensating-control and
customized-approach validation). Both are served; the auditee path is the funnel entry.

### 1.4 Effort estimate

**M** (per ticket). 8 chunks, 4 industries, 3 UCs, 35+ tests + eval cases. One build PR.

### 1.5 Dependencies

- Day-0 fact sheet + inventory artifact (done).
- nist-csf-2 / nist-800-53-rmf: PCI↔CSF/800-53 crosswalk is a one-way reference; OLIR
  extraction deferred to a later structural ticket (not this build) to keep scope at M.
- Registry: new citations (PCI-SSC-Document-Library, PCI-SSC-Blog-v401) go to the registry
  FIRST. NIST-CSF-Informative-References / NIST-OLIR already exist.

### 1.6 Out-of-scope (explicit non-goals)

- **Merchant/service-provider validation levels** — brand-and-acquirer-defined, NOT in the
  standard; the skill names them only as brand-specific/variable, never as SSC thresholds.
- Card-brand compliance programs, fines, penalty amounts — pointer only.
- Sibling PCI standards (PTS, P2PE program internals, SSF beyond the Appendix F pointer, PIN
  security) — out of scope.
- Bulk standard text in the repo (licence: internal use only) — paraphrase + short excerpts.
- PCI↔CSF/800-53 crosswalk ROWS — none in v1 (OLIR extraction is a later ticket).

## 2. Chunk architecture (8 chunks)

| # | File | Contents (all from fact sheet / local PDF) | Est. lines |
|---|------|--------------------------------------------|-----------|
| 01 | 01-scope-and-applicability.md | What PCI DSS applies to; account data = CHD + SAD; the CDE; NSC terminology (not "firewalls"); the 6 goals → 12 requirements map; v4.0.1 currency + future-dated-now-in-force banner; brand-defined-levels caveat | 180 |
| 02 | 02-scoping-and-segmentation.md | CDE scoping; connected-to/security-impacting systems; segmentation to reduce scope; scoping as the highest-leverage decision; sampling for assessors | 175 |
| 03 | 03-saq-selection.md | The 10 SAQ types, eligibility conditions per type, the selection decision tree, SAQ vs full ROC, why most e-comm lands on A vs A-EP (client-side script reqs 6.4.3 / 11.6.1) | 190 |
| 04 | 04-requirements-1-6.md | Build/maintain secure networks (1–2) + protect account data (3–4) + vuln management (5–6): section-level (x.y) map with paraphrased intent, evidence examples; future-dated specifics flagged in-force | 195 |
| 05 | 05-requirements-7-12.md | Access control (7–9), monitoring/testing (10–11), policy/programs (12): same treatment; req 8 MFA + req 10 logging + req 11 scanning/pentest emphasis | 195 |
| 06 | 06-validation-roc-aoc.md | Assessment process; ROC vs AOC vs SAQ; QSA/ISA/QSA-support roles; assessor sampling; AOC parts; service-provider responsibility matrix | 180 |
| 07 | 07-approaches-and-compensating-controls.md | Defined vs customized approach (Appendix D/E; TRA); when customized has no option; compensating controls (Appendix B/C) — distinct from customized; legacy req-8 example; which to use when | 190 |
| 08 | 08-currency-and-program-context.md | v4.0.1 = only active; future-dated all mandatory 2025-03-31; no successor announced (re-verify each pass); brand programs/levels (pointer); appendix A1/A2/A3 applicability; relationship to CSF/800-53 (OLIR pointer, no rows) | 175 |

### 2.9 Why 8 chunks

Scope/segmentation and SAQ-selection are the consumer's first two questions and each carries
its own decision logic (own chunks). The 12 requirements split 1–6 / 7–12 to stay under 200
lines while keeping the goal groupings intact. Validation (ROC/AOC) and the
approaches/compensating-controls distinction are the assessor-side value and the single most
confused topic in v4 respectively (own chunks). Currency/program-context isolates the volatile
material for cheap re-verification (the chunk-08 pattern from hipaa).

## 3. Industry angles (4)

| Industry | Angle |
|----------|-------|
| saas-technology.md | E-commerce/SaaS merchant + service provider; client-side script requirements (6.4.3/11.6.1); SAQ A vs A-EP; cloud shared-responsibility and the SP responsibility matrix |
| retail-ecommerce.md | Card-present + e-comm retail; POS/POI; segmentation of store networks; SAQ B/B-IP/C/C-VT/P2PE paths; franchise multi-site |
| financial-services.md | Acquirers, processors, larger service providers; full ROC; DESV (Appendix A3); A1 multi-tenant for processors |
| healthcare.md | Providers taking card payments (often overlooked CDE); scope-minimization via outsourcing/P2PE; intersection with the HIPAA skill (different data, same vendor-management discipline) |

`_index.md` mirrors SKILL.md routing.

## 4. Use cases (3 — ticket B19/B20/B21)

UC seed + oracle contracts designed here; docs written to the tested fixtures (process v3
rule 2). Oracles are derivability-based — the stub computes selection/scoping outcomes from
seed facts; nothing echoed.

### 4.1 UC-01 — E-commerce SaaS: SAQ A-EP vs full ROC (ticket B19)

E-commerce SaaS, ~2M transactions, validating as a merchant. Seed: `uc-01-input.json`
(payment-page architecture: redirect/iframe vs direct-post/JS; transaction volume; service-
provider status). Output: SAQ-eligibility determination (A vs A-EP vs full ROC) WITH the
deciding factor, and the client-side-script requirement flags (6.4.3, 11.6.1) when applicable.
Oracle (derivability): the SAQ decision recomputed from the page-architecture facts in the
seed (redirect-only + outsourced → A-eligible; merchant JS on the page → A-EP; volume/SP →
ROC), the applicable-requirement list derived from the SAQ type, never a hardcoded verdict.

### 4.2 UC-02 — Retail manufacturer POS: full ROC + segmentation + customized approach (ticket B20)

L1 retail/manufacturer, ~8M transactions, full ROC. Seed: `uc-02-input.json` (14-system
inventory with CDE/connected-to/out-of-scope tags; one requirement (8.3.6 password length)
flagged for customized approach with a TRA). Output: CDE scope determination (in-scope count),
segmentation effect, and a defined-vs-customized routing per flagged requirement. Oracle:
in-scope system count recomputed from the seed tags; customized-approach rows require a TRA
field present; segmentation reduces the in-scope count deterministically.

### 4.3 UC-03 — Solo QSA-support: SAQ-D franchise + compensating-control worksheet (ticket B21)

Solo consultant supporting a 30-location franchise on SAQ D, with a legacy system unable to
meet a Req-8 control → compensating control. Seed: `uc-03-input.json` (franchise profile;
the legacy constraint; a proposed compensating control with its four worksheet elements).
Output: compensating-control worksheet completeness check (constraint / objective / risk /
controls-in-place per Appendix C) and the distinction from a customized approach. Oracle: the
worksheet is complete iff all four Appendix-C elements are present; the "is this a compensating
control or a customized approach?" classification derived from seed flags (existing-requirement
+ constraint → compensating; meet-intent-differently → customized).

### 4.4 UC selection rationale

Ticket-specified (B19/B20/B21); covers the SAQ path, the full-ROC+customized path, and the
compensating-control path — the three validation routes — across org sizes (2M / 8M / 30-site
franchise) and both personas (merchant self-assessment, assessor support).

## 5. Test architecture

| File | Cases | Count |
|------|-------|-------|
| test_pci_dss_assessment_lint.py | linter exit 0 | 1 |
| test_pci_dss_assessment_oracle.py | UC-01/02/03 derivability oracles + expected-seed agreement | 5 |
| test_pci_dss_assessment_grounding.py | citations resolve to manifest; manifest bidirectional; registry sync | 4 |
| test_pci_dss_assessment_trace.py | UC procedures cite real SKILL.md sections; chunks exist in routing | 3 |
| test_pci_dss_assessment_metamorphic.py | SAQ-input order invariance; segmentation monotonicity (more out-of-scope tags → in-scope count non-increasing); compensating-control element order | 3 |
| test_pci_dss_assessment_adversarial.py | SAQ with missing architecture fact → refuse/ask; empty system inventory; compensating control missing an element; brand-level question → "brand-defined" non-answer; future-dated req presented as optional → rejected | 5 |
| test_pci_dss_assessment_telemetry.py | schema validates; instrument emits; enums | 5 |
| test_pci_dss_assessment_consistency.py | routing ↔ chunks; industry/UC index sync; fact-sheet counts == chunk-stated counts (inventory-diff in CI) | 5 |
| test_pci_dss_assessment_chunks.py | per-chunk frontmatter, ≤200 lines, in routing | 8 |
| **Total target** | | **39** |

Eval lane (process v3.1): `evals/pci-dss-assessment/cases/` with the 3 UC substance cases +
1 idempotence invariant + the SAQ/scoping perturbation set (refusal contract), oracle-labeled
via the stub, CI-enforced from the build PR.

### 5.11 Source-of-truth verification plan

| Fact | Source | Verified by |
|------|--------|-------------|
| 6 goals / 12 reqs / 63 sections / 249 main-body reqs / 30 appendix reqs | local PDF mechanical census (inventory artifact) | dispatcher; G4 re-diff |
| 33 future-dated markers, all in force 2025-03-31 | local PDF + PCI SSC blog | dispatcher |
| 10 SAQ types + versions | doc_library.json | dispatcher |
| Req titles (esp. Req 1 NSC, Req 3 "account data") | local PDF | dispatcher |
| Defined vs customized; compensating ≠ customized | local PDF Appendices B/C/D/E §8 | dispatcher (machine-checkable) |
| v4.0.1 only active; no successor | PCI SSC site/blog (live, every G4) | dispatcher |
| Levels are brand-defined | absence-in-standard + brand docs | dispatcher |

PCI is machine-verifiable (Read-and-Copy licence) — §5.11 agent diffs claims against the local
PDF; no human-licensed-row exception needed (that is the ISO path). Anti-hallucination/limits
sections verified FIRST.

## 6. PoV analyses — 5 lenses

- **Framework fidelity:** future-dated-as-optional is the #1 risk (33 markers) → adversarial
  test + chunk-08 banner. Req 1 "firewall" anachronism and Req 3 "cardholder" (vs account)
  data are fidelity traps → terminology rows.
- **Completeness:** all 12 reqs reachable; all 10 SAQs in the selector; both personas.
- **Usability:** the SAQ decision tree and the scope-minimization guidance are the copy-paste
  consumer value; the compensating-control worksheet is assessor-ready.
- **Spine conventions:** ≤300-line router, ≤200-line chunks, §1–§11, telemetry, house-style §6.
- **Cross-skill alignment:** healthcare.md references the HIPAA skill (vendor-management
  discipline); CSF/800-53 pointer is one-way (no rows).

## 7. PoV analyses — 5 personas

- **QSA lead assessor:** will probe ROC/AOC accuracy, sampling, customized-approach TRA
  rigor, and compensating-vs-customized — chunk 06/07 must be precise.
- **E-comm SaaS compliance lead (B19):** SAQ A vs A-EP and the client-side script reqs are
  the live 2026 question; must be exactly right.
- **Retail security manager (B20):** segmentation as scope reduction; POS realities.
- **Solo consultant (B21):** the compensating-control worksheet without over-claiming a QSA
  role; SAQ D mechanics.
- **Acquirer/brand risk analyst:** will check that the skill does NOT assert brand levels as
  SSC facts — the boundary must be explicit.

## 8. Cross-skill alignment table

| Other skill | Touchpoint | Shape |
|-------------|-----------|-------|
| hipaa-security-rule | healthcare merchants; vendor-management discipline | one-way reference from healthcare.md |
| nist-csf-2 | PCI↔CSF mapping | pointer only (OLIR); no rows in v1 |
| nist-800-53-rmf | PCI↔800-53 mapping | pointer only; no rows in v1 |
| aicpa-soc-reporting | SaaS providing a SOC 2 + PCI AOC | reference in saas-technology.md |
| coso/isaca/workpapers | none material | — |

## 9. Data & synthetic content

- `data/seeds/`: uc-01-input/expected (payment-page architecture), uc-02-input/expected
  (14-system inventory + customized-approach flag), uc-03-input/expected (franchise +
  compensating-control worksheet). Fictional orgs; zero real PAN/CHD (the skill must model
  that PAN never appears in examples — a teaching point, not just hygiene); `as_of_date` field
  where any date logic exists.
- `data/generators/`: `gen_system_inventory.py --seed` (UC-02 CDE-tagged inventory) and
  `gen_saq_cases.py --seed` (architecture→SAQ boundary cases for the eval sampler).
- `data/crosswalks/`: empty in v1 (README: OLIR pointer; deferred).
- Redaction: telemetry/redaction.md states PAN/CHD/SAD never enter telemetry; seeds carry none.

## 10. Telemetry & docs

Standard Spine set (schema.json, instrument.py, redaction.md, baseline.md nulls). Docs:
architecture.md, limits-and-disclaimers.md (future-dated-in-force banner; brand-levels caveat;
not-a-QSA-engagement; no PAN in examples; licence note), changelog.md, acceptance-gate.md
(seeded from the fact-sheet verification rows, ≥20). persona-review.md created by G4.5.

## 11. Risk register (top per category)

1. **Fidelity:** a future-dated requirement taught as optional → adversarial test + grep gate
   for "future-dated|best practice until" outside chunk 08 / flagged blocks.
2. **Fidelity:** SAQ eligibility stated as a fixed verdict rather than derived from page
   architecture → oracle derives it; adversarial missing-fact → refuse.
3. **Completeness:** a SAQ type dropped from the selector → consistency test asserts all 10.
4. **Usability:** compensating-control vs customized-approach blurred → chunk 07 + UC-03
   explicitly contrast; oracle classifies.
5. **Convention:** brand levels asserted as SSC facts → limits banner + adversarial non-answer.
6. **Cross-skill:** a fabricated CSF/800-53 row → none encoded; pointer only; grep gate.

## 12. Build sequence

- Day 1: registry citations + scaffold + SKILL.md router + chunk 01.
- Day 2: chunks 02–05.
- Day 3: chunks 06–08; industries.
- Day 4: seeds + generators + stub + oracle/metamorphic/adversarial tests (contract first);
  UC docs to the passing fixtures; eval cases.
- Day 5: remaining tests; lint; consistency; calibration eval sweep (N=2 Haiku).
- Day 5.5 (§5.11): verification vs local PDF + fix pass + re-verify.
- Day 6: 5-lens + persona vetting (G4.5) in-PR; smokes; acceptance-gate.
- Day 7: PR, CI, merge; Linear; plan update.

## 13. File-by-file plan

`skills/pci-dss-assessment/`: SKILL.md, README.md; chunks/01–08; industries/_index + 4;
use-cases/_index + uc-01-saq-selection.md, uc-02-roc-segmentation.md,
uc-03-compensating-control.md; data/ per §9; tests/ 9 files + stub + conftest; telemetry/ 4;
docs/ 4 + persona-review.md (G4.5); evals/pci-dss-assessment/cases/.

## 14. Open questions for review

1. Encode the full 249-requirement catalog, or section-level (63) with paraphrased intent?
   **Decision: section-level (x.y) with intent paraphrase** — the 249 live in the inventory
   artifact and the local PDF; reproducing them is licence-grey and low-value vs the decision
   logic. Chunks teach the structure and route to requirements, not transcribe them.
2. SAQ eligibility — encode all 10 decision trees or the common merchant ones?
   **Decision: all 10 in the selector chunk; oracle covers the B19 A/A-EP/ROC path in depth**,
   others at routing depth.
3. Crosswalk rows now or deferred? **Deferred** (keeps scope at M; OLIR extraction is its own
   ticket, method already proven).

## 15. Requirements parameters checklist

- [x] §1 scope/deps/out-of-scope; [x] §2 8 chunks ≤200 rationale; [x] §3 4 industries;
- [x] §4 3 UCs with seed+oracle contracts before docs; [x] §5 test arch (39 target) + §5.11
  plan; [x] §6 5 lenses; [x] §7 5 personas; [x] §8 cross-skill; [x] §9 data (no PAN/CHD);
- [x] §10 telemetry/docs; [x] §11 risk register; [x] §12 day plan; [x] §13 file plan;
- [x] §14 open questions resolved; [x] §15 this checklist.

## 16. Sign-off

- Designer: Claude (Fable 5) dispatcher, 2026-06-11.
- Fact-sheet gate: PASS. Inventory artifact: present. Licence class: Read-and-Copy (machine-
  verifiable).
- Ready for G3: **yes** — build agents receive the fact sheet + inventory + this design; the
  UC seed/oracle contracts in §4 are binding; bulk standard text stays out of the repo.
