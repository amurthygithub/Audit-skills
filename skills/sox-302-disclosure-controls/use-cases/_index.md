---
title: "Use cases for SOX §302 Disclosure Controls & Procedures (15 U.S.C. 7241; 17 CFR 240.13a-14/15; Reg S-K Items 307/308)"
parent_skill: sox-302-disclosure-controls
type: use-cases-index
last_verified: "2026-06-11"
---

# Use cases — SOX §302 Disclosure Controls & Procedures

Each use case is an end-to-end engagement: a persona + a scenario + seeded inputs + expected outputs + derivability-oracle assertions the test suite verifies. The three UCs span the three paths a SOX/SEC-reporting professional actually builds — the material-weakness interplay, the newly-public first-302 obligation/scope determination, and the multi-entity sub-certification cascade — and exercise both boundary concepts the skill exists to teach: **DC&P ≠ ICFR** and **§302 ≠ §404**.

## Available use cases

| UC | Title | Industry | Persona | Key output |
|---|---|---|---|---|
| [UC-01](uc-01-mw-interplay.md) | Material-weakness interplay and the sub-cert cascade — Crestline Financial Corp (accelerated filer, Q3 10-Q, unremediated ITGC logical-access material weakness) | financial-services | Controller / SEC-reporting manager | DC&P conclusion **not effective** (`DCP_NOT_EFFECTIVE`); cert ¶5 disclosure to auditors + audit committee required; 14-owner cascade rolls up **1 exception / 13 clean** (IT/ITGC); top-level cert NOT clean; 302-vs-404 interplay shown |
| [UC-02](uc-02-newly-public-first-302.md) | Newly-public first §302 and the obligation/scope split — Nimbus Cloud Inc (newly-public EGC, first periodic report) | saas-technology | Disclosure-committee chair / SEC-reporting manager | §302 required from the first periodic report (no exemption); §404(b) auditor attestation **exempt**; §404(a) management assessment required (first annual report); DC&P scope **7** items / ICFR scope **3**; cyber 8-K Item 1.05 in DC&P scope (`FIRST_302_404B_EXEMPT`) |
| [UC-03](uc-03-multientity-subcert.md) | Multi-entity §302 sub-certification cascade — Meridian Group (15 entities, parent Meridian Holdings Inc) | manufacturing | Big-4 SOX advisor / group controller | **14 covered / 1 gap** (Entity-14, `CASCADE_GAPS_1`); FPI evaluation-frequency split **12 domestic (quarterly) / 3 FPI (annual)**; cascade labeled house framework |

All 3 use cases are `status: active`: seeds exist in `data/seeds/`, the stub executor returns the expected output, and the oracle/metamorphic/adversarial tests pass.

## How to use a use case

1. Open the UC file for the persona/scenario you need and read the frontmatter first — `inputs`, `procedure`, `expected_outputs`, `oracle`, `data_refs`, `tests`, `status` are the fields the lint and test suite validate.
2. The `procedure` steps name specific chunk files (chunks/01–07) and SKILL.md §1–§11 — the procedure is a navigation map through the skill.
3. The seeds in `data_refs` are the tested fixture and the UC's source of truth; the doc describes exactly what the oracle derives from them.
4. The oracles are **derivability-based**: every expected number is recomputed independently from the seed files (no echo). If you change a seed, the oracle tells you what the new truth is.
5. House conventions (the sub-certification cascade in UC-01 and UC-03, the disclosure-committee charter in UC-02) are labeled everywhere they appear — they are recommended practice / house framework, not rule requirements.

## How the use cases map to the industries

- `financial-services.md` → UC-01 (Crestline Financial Corp, accelerated-filer MW interplay and large cascade).
- `saas-technology.md` → UC-02 (Nimbus Cloud Inc, newly-public first 302, disclosure committee, cyber scope, 404(b) exempt).
- `manufacturing.md` → UC-03 (Meridian Group, 15-entity cascade and the FPI annual-vs-quarterly nuance).
- `healthcare.md` → no dedicated seeded UC in v1; it reuses the UC-02 scope method with a health-tech disclosure inventory (HIPAA/clinical and privacy/cyber 8-K items as non-financial DC&P scope).

## Use cases NOT in scope

Valid engagement types not codified in v1 (candidates for a future release):

- **§404 ICFR assessment / auditor attestation mechanics** — owned by `coso-internal-controls`; this skill references the §302-vs-§404 boundary (UC-01 §6) and does not re-teach §404.
- **§906 criminal certification** (18 U.S.C. 1350) — named as the companion certification in chunk 01; no seeded fixture.
- **Cyber 8-K Item 1.05 incident-response workflow** — the 4-business-day clock is a DC&P touchpoint here (UC-02 §5); the incident-response process itself lives in `nist-csf-2` / `hipaa-security-rule`.
- **Restatement / Item 4.02 non-reliance 8-K** — a DC&P-adjacent timely-disclosure path not seeded in v1.
