# Acceptance gate — NIST CSF 2.0 skill

This gate was fully re-verified on 2026-06-10 during the G4.5 consumer-ready vetting run. The
previous version of this file contained an unresolved recount ("hmm = 27, need recount")
marked as ✓-verified, a false "24 categories" caveat, and a backwards ID.AM-06 claim — all
replaced below with values verified against the official CSRC CSF 2.0 reference data and the
CSWP 29 PDF. Evidence: `docs/persona-review.md`.

## §5.11 verification table (re-verified 2026-06-10)

| # | Fact | Source | Verifier | Status |
|---|---|---|---|---|
| 1 | CSF 2.0 published Feb 26, 2024 (CSWP 29) | nvlpubs CSWP 29 PDF | webfetch | ✓ verified |
| 2 | 6 Functions: GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER | CSWP 29 §2.1 | webfetch | ✓ verified |
| 3 | 22 Categories = 6 GV + 3 ID + 5 PR + 2 DE + 4 RS + 2 RC | CSRC CSF 2.0 JSON export (withdrawn 1.1 elements excluded) + CSWP 29 App. A | webfetch | ✓ verified |
| 4 | 106 Subcategories = 31 GV + 21 ID + 22 PR + 11 DE + 13 RS + 8 RC | CSRC CSF 2.0 JSON export | webfetch | ✓ verified |
| 5 | GOVERN Categories: GV.OC, GV.RM, GV.RR, GV.PO, GV.OV, GV.SC (6) | CSWP 29 | webfetch | ✓ verified |
| 6 | Tiers 1-4: Partial, Risk Informed, Repeatable, Adaptive; applied to Organizational Profiles; NOT maturity levels | CSWP 29 §3.2/App. B; NIST 1.1-era FAQ carries the verbatim "not intended to be maturity levels" | webfetch | ✓ verified |
| 7 | No official implementation-status scale (SP 1301's Profile example is notional/free-format) | SP 1301 PDF | webfetch | ✓ verified |
| 8 | GV.PO = {-01, -02} only; PR.AT = {-01, -02} only; RS.AN = {-03, -06, -07, -08}; ID.AM has no -06 (withdrawn from 1.1); DE.CM = {-01, -02, -03, -06, -09} | CSRC CSF 2.0 JSON export | webfetch | ✓ verified |
| 9 | QSGs: SP 1299 Resource & Overview; SP 1300 Small Business; SP 1301 Org Profiles; SP 1302 Tiers; SP 1303 ERM; SP 1305 C-SCRM (no per-Function series; no "Profile success story" SP) | csrc.nist.gov pub pages | webfetch | ✓ verified |
| 10 | GV.OC-01 → 800-53 PM-11 (PM-15 not in the mapping) | NIST IR spreadsheet | webfetch | ✓ verified (Subcategory-level, not Category-level) |
| 11 | 800-171 Rev 2: 110 requirements, 14 families, 3.x.y IDs (Feb 2020) | nvlpubs 800-171r2 PDF (counted) | webfetch | ✓ verified |
| 12 | 800-171 Rev 3: 97 requirements, 17 families, 03.xx.yy IDs, published May 2024 | nvlpubs 800-171r3 PDF (counted; 130 headings − 33 withdrawn) | webfetch | ✓ verified |
| 13 | CMMC L2 assesses 800-171 REV 2 — "identical to the requirements in NIST SP 800-171 R2" | 32 CFR 170.14(c)(3) via eCFR | webfetch | ✓ verified |
| 14 | FFIEC CAT sunset effective Aug 31, 2025 (statement Aug 2024); May 2017 was the final version; no "v2" ever existed; Domain 4 = External Dependency Management; no FFIEC MTTD target exists | FFIEC sunset statement PDF; CAT May 2017 PDF | webfetch | ✓ verified |
| 15 | CISA CPG 2.0 published Dec 11, 2025: ~34 goals, IDs 1.A-6.A under the six CSF Functions; title has never contained "ICS"; v1.0.1 (Mar 2023) had 38 goals | cisa.gov CPG pages | webfetch | ✓ verified |
| 16 | FedRAMP: no statutory authorization duration (44 USC 3607-3616); JAB replaced by the FedRAMP Board (2024) | govinfo USC text; fedramp.gov | webfetch | ✓ verified |
| 17 | HIPAA breach notification: §164.404 = individuals, §164.406 = media, §164.408 = the Secretary (regulator) | 45 CFR via LII mirror | webfetch | ✓ verified |
| 18 | SEC 8-K Item 1.05: 4 business days from the registrant's MATERIALITY DETERMINATION (not occurrence) | sec.gov Form 8-K | webfetch | ✓ verified |
| 19 | ISO 27001:2022: 93 Annex A controls; clauses 4-10; A.5.26 = Response to information security incidents; A.5.30 = ICT readiness for business continuity | reputable mirrors (iso.org paywalled) | webfetch | ✓ verified |
| 20 | CJIS Security Policy current = v6.0 (Dec 27, 2024) | le.fbi.gov PDF | webfetch | ✓ verified |
| 21 | EO 13800: agency heads SHALL use the Framework | 82 FR 22391 via govinfo | webfetch | ✓ verified |
| 22 | TX Gov Code: §2054.0593 = TX-RAMP; §2054.515 = biennial assessment; 44 USC §3554 = agency-head duties | statutes.capitol.texas.gov (archive); govinfo | webfetch | ✓ verified |

## G4.5 consumer-ready gate (SOX-636)

| check | result | date | verifier |
|---|---|---|---|
| Persona vetting (5 personas) | 9 CRITICAL clusters / ~15 HIGH verified findings; all FIXED/TICKETED/ACCEPTED (see persona-review.md) | 2026-06-10 | claude (LLM-vetted — a filter, not a certification) |
| §5.11 live re-verification | Table above — 22 facts re-verified with verbatim quotes via 2 Tier-2 agents | 2026-06-10 | claude + verification agents |
| smoke-test uc-01 | PASS-WITH-NOTES (notes — UC-doc/seed contradictions, phantom sections — fixed: UC rebuilt to seed truth, stub emits all 6 Functions) | 2026-06-10 | clean-session agent |
| smoke-test uc-02 | PASS-WITH-NOTES (notes — seed/doc described different banks; fabricated trend — fixed: UC rebuilt to Pinecrest seed, baseline-note replaces trend) | 2026-06-10 | clean-session agent |
| smoke-test uc-03 | PASS-WITH-NOTES (notes — Rev 2/Rev 3 split, domain mislabels — fixed: UC + seed rebuilt on Rev 2/CMMC truth, family labels corrected) | 2026-06-10 | clean-session agent |

N=1 clean-session runs are an existence proof, not a reliability claim — that requires the Epic 6 harness (N>=20, >=2 models).

## Sign-off

The §5.11 gate and the G4.5 vetting pass are complete as of 2026-06-10: every CRITICAL/HIGH
persona finding is FIXED, TICKETED (SOX-645), or ACCEPTED with rationale. The skill remains
`status: draft` v0.1.0 pending Epic 6 reliability measurement.
