# Design — pci-dss-assessment (SOX-568)

> 15-section design per `docs/skill-design-template.md`, built on the Day-0 fact sheet
> (`docs/pci-dss-assessment-fact-sheet.md`, gate PASS 2026-06-11) and the mechanical inventory
> (`docs/builds/sox-568/pci-dss-inventory.json`). Born-vetted under process v3.1: eval cases
> ship with the build; G4.5 runs inside the build PR; the local v4.0.1 PDF
> (`~/Standards-licensed/PCI/`) is the machine-checkable verification oracle (read-and-copy
> licence — agents may verify against it; bulk text never enters the repo).

## 0. Why this design doc exists

M5 cycle 1. Second born-vetted skill; first under the read-and-copy licence class (machine
verification permitted, paraphrase-only publication). The design pins the chunk map, the three
UC contracts (seed + derivability oracle before docs), the eval-lane plan, and the licence
guardrails the build agents must obey.

## 1. Scope & dependencies

### 1.1 Primary source citation

PCI DSS v4.0.1 (June 2024), acquired 2026-06-11 via authorized document-library licence
acceptance; local oracle outside the repo. Companion machine-readable source: the PCI SSC
doc-library JSON (SAQ/ROC/AOC catalog). Public anchor for crosswalks: NIST OLIR
"PCI-DSS-4.0.1-to-CSF-v2.0" (final, 2025-12-23, PCI SSC-submitted).

### 1.2 Structural inventory (counts)

From the fact sheet §0 (mechanical): 6 goals; 12 principal requirements; 63 sections
(5/3/7/2/4/5/3/6/5/7/6/10 across Reqs 1→12); 249 main-body defined requirements (205 at x.y.z
+ 44 at x.y.z.w; testing procedures excluded by convention); 30 appendix requirements in 8
sections (A1/A2/A3); 33 future-dated markers — ALL IN FORCE since 2025-03-31; 10 SAQ types;
7 lettered appendices (B/C compensating controls coexist with D/E customized approach).

### 1.3 Persona

**IT** (per ticket), with a strong auditee lean: the funnel pull is merchants/SaaS picking a
validation pathway and preparing evidence; the QSA-support angle (UC-03) serves the assessor
side.

### 1.4 Effort estimate

**M** (per ticket). 8 chunks, 4 industries, 3 UCs, ~40 tests + eval cases. One build PR.

### 1.5 Dependencies

- Fact sheet + inventory artifact (committed `4a49f94`).
- Local PDF oracle for G3 verification agents and §5.11 (machine-checkable).
- SAQ eligibility criteria: the SAQ Instructions/individual SAQ PDFs are separate doc-library
  downloads (same licence flow) — acquire SAQ A, A-EP, D-Merchant + Instructions at G3 Day-1,
  record in `source-texts/manifest.json`.
- OLIR extraction method (proven, SOX-638) for the CSF 2.0 crosswalk rows at G3.
- Registry: new citations (PCI-SSC-Document-Library, PCI-SSC-Blog-v401, NIST-OLIR) go to
  `data/registry/citations.json` FIRST. NIST-CSF-Informative-References exists already.

### 1.6 Out-of-scope (explicit non-goals)

- Re-teaching all 249 requirements — the skill is an ASSESSMENT-WORKFLOW skill (scoping →
  pathway → approach → evidence → reporting), with requirement anchors, not a standard
  reproduction (licence + value both forbid it).
- Merchant/SP level thresholds as facts — brand-defined, labeled as such, never asserted.
- PTS, P2PE-standard internals, Software Security Framework beyond the Appendix F pointer,
  PIN security, card-brand fine schedules.
- Bulk standard text in the repo (read-and-copy licence) — paraphrase + ID + short attributed
  excerpts only.
- Crosswalks beyond the OLIR CSF 2.0 set in v1.

## 2. Chunk architecture (8 chunks)

| # | File | Contents (facts from fact sheet/inventory; paraphrase-only) | Est. lines |
|---|------|------------------------------------------------------------|-----------|
| 01 | 01-scope-and-account-data.md | Account data = CHD + SAD taxonomy; CDE definition; scoping principles and the annual scope-confirmation duty; segmentation as scope-reduction (not requirement-waiver); brand-vs-SSC role split (levels are brand-defined — the honesty anchor) | 180 |
| 02 | 02-structure-and-currency.md | 6 goals → 12 reqs → 63 sections map; defined-requirement counting conventions (the 249 + appendix 30); future-dated markers ALL IN FORCE since 2025-03-31 (the #1 currency trap); v4.0→v4.0.1 nature; re-verify instruction | 170 |
| 03 | 03-validation-pathways.md | The 10-SAQ catalog with eligibility logic (paraphrased criteria; verify against SAQ Instructions at G4); ROC vs AOC vs SAQ artifacts; QSA/ISA roles; pathway-selection decision tree (the UC-01 spine) | 195 |
| 04 | 04-defined-vs-customized.md | Both approaches; requ