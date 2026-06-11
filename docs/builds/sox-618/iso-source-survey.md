# SOX-618 — ISO/IEC 27001 source-ecosystem survey

> All rows verified live 2026-06-11 by a webfetch research agent (83 fetches; bot-walls and
> dead links documented in §c). Feeds the build decision for iso-27001-isms (SOX-567).

## Source table

| # | source | paid/free | price (verbatim) | unlocks | store in open repo? | URL | retrieved |
|---|--------|-----------|------------------|---------|---------------------|-----|-----------|
| 1 | ISO/IEC 27000:2018 official full text (PAS) | Free | CHF 0 (click-through licence) | Full official PDF: ISMS family overview + all 77 definitions (3.1–3.77). Download verified end-to-end. Product page: "Expected to be replaced by ISO/IEC 27000 within the coming months" — re-check at build time | No — ISO Customer Licence (no redistribution). Link only | standards.iso.org/ittf/PubliclyAvailableStandards/c073906_ISO_IEC_27000_2018_E.zip ; iso.org/standard/73906.html | 2026-06-11 |
| 2a | ISO OBP preview, 27001:2022 | Free | — | Verbatim Foreword, Intro (0.1–0.2), Scope, Cl. 2, Cl. 3 (defers to 27000), Bibliography. Clauses 4–10 and Annex A (incl. titles) NOT shown | Short cited excerpts only | iso.org/obp/ui/en/#!iso:std:82875:en | 2026-06-11 |
| 2b | ISO OBP preview, 27002:2022 | Free | — | Foreword, Intro 0.1–0.7, Scope, Cl. 2–3, Bibliography. No control titles or text | Same | iso.org/obp/ui/en/#!iso:std:75652:en | 2026-06-11 |
| 3 | Edition status + Amd 1:2024 | Free (info) | Amd 1: CHF 0 | 27001:2022 = Ed. 3, current (60.60); 2013 Withdrawn. Amd 1:2024 "Climate action changes" exists, sold separately at CHF 0; NO consolidated 2022+Amd1 product on iso.org | Link only | iso.org/standard/82875.html | 2026-06-11 |
| 4 | NIST OLIR/CPRT mappings | Free | — | BOTH target the 2022 edition: (a) ISO/IEC-27001:2022-to-CSFv2.0 v1.0.0 (OLIR referenceId=154); (b) SP 800-53 Rev 5 → 27001:2022 mapping xlsx (live, 155 KB, last-mod 2025-05-07). Control-ID-level crosswalks incl. ISO identifiers — the cleanest legal anchor for the 93-control inventory | Link; extract IDs/titles (US-gov artifact) | nist.gov/cyberframework/informative-references ; csrc.nist.gov/.../sp800-53r5-to-iso-27001-mapping-2022-OLIR-2023-10-12-UPDATED.xlsx | 2026-06-11 |
| 5 | IAF MD 26:2023 (Issue 2) | Free | — | Full PDF; verbatim transition deadline "31 October 2025" confirmed; cites 27006:2015 7.1.2.1.3; 27006-1:2024 replaces 27006:2015 (Mar 2024) | Link (check IAF copyright note) | iaf.nu/iaf_system/uploads/documents/IAF_MD26_Issue_2_15012023.pdf | 2026-06-11 |
| 6 | Public 93-control title listings | Free | — | No major CB page lists all 93 titles. Complete listing found at a consultancy (High Table; 4 spot-checks correct). CB/AB pages corroborate structure (114→93; 11 new/58 updated/24 merged) | Secondary corroboration; link only | hightable.io/iso-27001-annex-a-controls-reference-guide/ ; dnv.com (structure) | 2026-06-11 |
| 7 | ISO Survey (cert statistics) | Free (login) | CHF 0 | 27001: 48,671 certs (2023 survey). From 2025 hosted on IAF CertSearch (login) | Stats facts OK | iso.org/the-iso-survey.html | 2026-06-11 |
| 8 | ISO store direct | Paid | 27001:2022 CHF 155; Amd 1 CHF 0; 27002:2022 CHF 227; 27005:2022 CHF 225 | Full requirements + guidance text — offline human verification ONLY (see row 12) | NO | iso.org/standard/82875.html etc. | 2026-06-11 |
| 9 | ANSI Webstore (INCITS adoption) | Paid | UNVERIFIED (hard Cloudflare wall on all routes) | Identical-text US adoption | No | webstore.ansi.org/standards/incits/incitsisoiec2700120222023 | 2026-06-11 (blocked) |
| 10 | Estonian EVS | Paid | EVS-EN 27001:2023 PDF 19.84 € incl tax; **consolidated +A1:2024 PDF 24.80 €**; A1 alone 0.00 € | Identical-text EN adoption — cheapest legal full text. DRM-locked PDF: no text copy, 2 prints, device-bound | NO | evs.ee/en/evs-en-iso-iec-27001-2023-a1-2024-consolidated | 2026-06-11 |
| 11 | NEN (Netherlands) | Paid | €192.00 excl VAT | Same text, ~8× EVS price | No | nen.nl/en/nen-en-iso-iec-27001-2023-en-313608 | 2026-06-11 |
| 12 | Licence terms (the binding constraint) | — | — | ISO End Customer Licence: no reproduction/distribution/third-party disclosure; no incorporation into products, databases, or structured datasets; **explicit AI/ML clause** — no training, fine-tuning, embedding, prompting, querying, structured extraction, or automated knowledge extraction; ISO opts out of the EU TDM exception (Art. 4, Directive 2019/790). No quotation permission granted (statutory quotation right only). EVS adds DRM no-copy | — | iso.org/terms-conditions-licence-agreement.html | 2026-06-11 |

## Mix tiers and what stays unverifiable

| Tier | Cost | Verifiable | Remains UNVERIFIABLE |
|---|---|---|---|
| A — free only | €0 | 77 definitions (verbatim, official); scope/intro verbatim; 93 control IDs+titles (via NIST OLIR artifact); edition/amendment status; certification/transition process; cert statistics; CSF/800-53 crosswalks | Clause 4–10 normative ("shall") text; Annex A control statements; Amd 1 inserted text; all 27002 guidance; 27005 |
| B — free + EVS 27001 consolidated | **€24.80** | Tier A + clause 4–10 and Annex A requirement semantics, HUMAN-verified against the licensed copy | 27002 guidance/purpose/attribute taxonomy; 27005 detail; 27006-1 audit tables |
| C — Tier B + EVS 27002 | ~€50 total | Tier B + control purpose/guidance/attributes for chunk depth | 27005, 27003/27004, 27006-1 annexes |

## Process implication (binding for the iso-27001 build)

The ISO AI/ML licence clause means **no licensed text may enter the repo, a prompt, a build
pipeline, or any agent context — under any tier.** Two standing consequences:

1. **§5.11 exception class — "licensed-source row":** acceptance-gate rows for clause-text facts
   carry a clause pointer + `verified_by: human (licensed copy, EVS-EN ISO/IEC 27001:2023+A1)` +
   date — NO verbatim quote (the only §5.11 row type exempt from the quote rule, and only for
   ISO-licensed sources). Machine verification (webfetch agents) covers the free layer only.
2. **The skill ships paraphrase + pointer, never standard text.** Every requirement claim is
   labeled with its clause cite and the instruction to verify against a licensed copy.

## Recommendation

**Tier B now (€24.80, EVS consolidated 27001:2023+A1 PDF), Tier C deferred** until chunk-depth
work demands 27002 guidance. Human verification labor (the licence's practical cost): expect
~60–100 fact-sheet rows to check manually against the DRM PDF during G1 and again at G4 —
budget 2–3 hours of reviewer time across the build. Build order unaffected: pci-dss (free
source) can open M5 while the purchase + human-verification scheduling happens.
