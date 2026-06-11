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

## §2 — Subscription / package options (extension, retrieved live 2026-06-11)

Buyer profile for the comparison: solo practitioner, US, ~5–7 ISO documents over ~a year;
baseline = à-la-carte EVS DRM PDFs (~€20–25/doc, ~€130–200 total, owned files, current editions).

| option | provider | model | published price (verbatim) | scope | access form | users | notes | URL |
|---|---|---|---|---|---|---|---|---|
| BSOL / BSI Knowledge | BSI (UK) | annual subscription, 54 modules incl. Digital/ICT (27000 family confirmed) | Quote-only ("tailored"); secondary indications: BSOL Select "from £3,254/yr per site for 2 modules" (undated price list); Jisc education £220/yr (institutions only) | 140,000+ standards | online reading | organisational; no solo tier advertised | no external sharing/redistribution | bsigroup.com/.../bsi-knowledge-subscription/ |
| NEN Connect "Informatiebeveiliging" | NEN (NL) | annual subscription (smallest infosec package) | **€513/yr (1–2 users)**; €641/yr w/ compliance tool | ISO/IEC 27000, 27001, 27002, 27003 only (no 27701/42001/22301) | **online reading only** — "no PDF… cannot download or save" (verbatim, translated) | 1–2 | view-only DRM; nothing owned | connect.nen.nl/.../Informatiebeveiliging |
| Accuris per-doc (ex-Techstreet) | Accuris (US) | per-document | $254.00 for 27001:2022 PDF (search-snippet grade; store bot-walled, Cloudflare 403) | full ISO catalogue | PDF download | 1 | ~10× EVS for identical text | store.accuristech.com |
| Accuris Engineering Workbench | Accuris | enterprise subscription | Quote-only (nothing published) | multi-SDO | platform | org | corporate/university product | store.accuristech.com |
| DS cyber package | Dansk Standard (DK) | ONE-TIME package (not a subscription) | "4.395,00 kr" (~€590; price API-gated — partially UNVERIFIED; package contents + single-user PDF licence confirmed via page metadata) | 27001, 27002, 27005 + related (710 pp) | PDF download, single-user | 1 | 25% off DS à-la-carte; DS single 27001 ≈ 779 kr ≈ €104 — still 4–5× EVS | webshop.ds.dk |
| SFS Online | SFS (FI) | annual subscription, browse/print tiers | Quote-only | custom collection | browser reading | sized per org | advertises a paid tier for systems use — still within ISO licence limits | sfs.fi |
| EVS browsing service | EVS (EE) | pay-per-view | **€2 / 30 min; €3 / 24 h (excl VAT)** — the €2.48 = €2 + Estonian VAT; ONE standard per purchase | any single standard | browser view only | 1 session | pre-purchase check, not an access strategy | evs.ee/en/browsing-service |
| EVS online reading service | EVS | annual subscription | Quote-only (up to 5 users incl.) | 47,000+ EVS/EN adoptions (pure ISO originals excluded) | online reading, no print/save | ≤5 | requires Estonian ID/Smart-ID — practical blocker for a US buyer | evs.ee/en/online-reading-service |
| EVS e-shop "Pakett 12" (IT security) | EVS | one-time package | **€180.79 incl VAT** | 27000/27001:**2017**/27002:**2017**/27003:2011/27005:2019/27033/27035 | DRM PDF | 1 | **TRAP: pre-2022 editions — do not buy** | evs.ee/et/standardite-pakett-12 |
| ISO direct bundle PUB200270 | ISO | one-time bundle (no end-user subscription exists; OBP subs are codes/T&D collections only) | ~CHF 546 (search-snippet grade; page bot-walled). À-la-carte sum CHF 607 → ~10% discount | 27000+27001+27002+27005 | watermarked PDF / OBP view | 1 (name-watermarked) | full ISO licence incl. AI/ML prohibition | iso.org/publication/PUB200270.html |
| Library route | e.g., Linda Hall Library (Kansas City); academic Techstreet subs (USC, MIT) | library access | free (on-site) | 150,000+ standards (Linda Hall) | on-site consultation; academic remote access is affiliate-only | — | viable for reading sessions, never for owned PDFs; no remote public-library ISO access found | libguides.lindahall.org/standards_specifications |

### §2 verdict

1. **No subscription beats à-la-carte EVS for this buyer.** Cheapest verified subscription
   (NEN Connect €513/yr, 1–2 users) costs 2.5–4× the entire multi-year baseline, covers only
   4 standards, is read-only (nothing owned), and recurs annually.
2. BSOL, SFS, EVS-reading, Accuris Workbench: quote-only, organisation-oriented; no solo tier.
3. One-time bundles (DS ~€590; ISO ~CHF 546) carry 27002/27005 at 3–4× the EVS cost of the
   same titles; EVS's own €180.79 infosec package is a trap (2017 editions).
4. The €2.48 EVS "browse" = 30 minutes of viewing one standard (€2 + VAT) — pre-purchase
   check only.
5. **The ISO AI/ML licence prohibition applies identically under every option above** — no
   subscription buys extra usage rights. Recommendation unchanged: à-la-carte EVS, one
   purchase per skill at its Day-0. Revisit only at ~10+ docs/year cadence.
