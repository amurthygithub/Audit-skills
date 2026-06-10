# Persona Review — nist-csf-2 (G4.5 consumer-ready gate)

Run 2026-06-10 per `prompts/persona-vetting.md` (process v2): 5 LLM persona agents + 3
clean-session smoke tests in parallel; every CRITICAL/HIGH verified BEFORE fixing — Tier 1
(on-disk greps, seed/stub execution, math checks) or Tier 2 (live sources with verbatim
quotes: CSWP 29 PDF + the official CSRC CSF 2.0 JSON export (full 106-subcategory inventory
parsed), SP 1299-1305 pub pages, SP 800-171 r2/r3 PDFs (requirements counted), 32 CFR 170
via eCFR, cisa.gov CPG pages, FFIEC sunset statement + CAT May 2017 PDF, 44 USC via govinfo,
fedramp.gov, 45 CFR breach rule, SEC Form 8-K, ISO mirrors, le.fbi.gov CJIS v6.0, EO 13800,
TX statutes). **LLM-vetted — a filter, not a certification.**

Resolution key: **FIXED** (PR `fix/SOX-636-vet-nist-csf-2`) · **TICKETED — SOX-645** · **ACCEPTED**.

> **Findings-are-hypotheses, round three:** Tier-2 verification refuted the persona consensus
> twice more. (1) All five personas treated "CISA CPG 2.0" as fabricated — CISA published CPG
> 2.0 on Dec 11, 2025 (after most model knowledge): ~34 goals, IDs 1.A-6.A under the six CSF
> Functions. The skill's "8-element" claim and its CPG 1-8 table were still fabricated, but
> "no CPG 2.0 exists" was wrong. (2) The "Tiers are not maturity levels" sentence personas
> placed in CSF 2.0 §3/App. B exists verbatim only in NIST's 1.1-era FAQ — the position is
> NIST's, the citation was not. Concurrence is not verification.

## CRITICAL

| persona | finding | verification | resolution |
|---|---|---|---|
| all 5 (+acceptance gate itself) | **The verification gate was false assurance**: a ✓-verified row containing the literal text "= 22, hmm = 27, need recount"; a caveat asserting "the actual count is 24 (not 22)"; a ✓-verified claim that ID.AM-06 is "new in 2.0" (it was withdrawn FROM 1.1); sign-off declaring "all 21 facts verified" | Tier 2 — CSRC JSON export: 22 categories (6/3/5/2/4/2), 106 subcategories (31/21/22/11/13/8); ID.AM has no -06 | **FIXED** — gate fully rewritten with the verified 22-fact table |
| Partner, 3PAO, CISO, State Dir | **Invented subcategories**: GV.PO-03/-04 (GV.PO has exactly 2) in the flagship GOVERN chunk; PR.AT-03 (PR.AT has exactly 2) in the CPG table; RS.AN-01 used in 2.0 contexts (2.0 = RS.AN-03/-06/-07/-08); multiple wrong glosses (PR.AA-02/-04/-05, PR.IR-01, RS.MA-03, GV.RR-03, GV.SC-04/05) | Tier 2 — full ID inventory + verbatim texts from the CSRC export | **FIXED** — IDs/glosses corrected everywhere from verified texts |
| all 5 | **All three UC documents described different companies than their seeds** (Meridian vs Pinecrest; Apex Defense vs Apex Manufacturing; DataRelay narrative contradicting its own seed on MFA), with different gap lists, radar values, and dollar totals — the tests certified fixtures the docs didn't describe | Tier 1 — seed/doc diffs | **FIXED** — all three UCs rebuilt to seed truth; UC-02's fabricated 2-quarter trend replaced with the baseline-note rule its own chunk mandates |
| 3PAO, SaaS | **CMMC L2 mislabeled as 800-171 Rev 3** across UC-03/seed/manufacturing.md (with Rev 2 numbers — "110 across 14 families" — labeled Rev 3, and a test enforcing Rev 2 ID format while calling it Rev 3) | Tier 2 — 32 CFR 170.14(c)(3) verbatim ("identical to ... NIST SP 800-171 R2"); r2=110/14 and r3=97/17 counted from the PDFs | **FIXED** — Rev 2 framing skill-wide; UC-03 renamed and rebuilt; seed family labels + key mappings corrected; honest no-CP-family note for recovery rows |
| Partner, CISO, State Dir | **Tiers sold as maturity** (router §3.3 "Tiers 1-4 (maturity)", "per Function" as framework fact) plus invented aggregation math (fractional tiers, "average CSF Tier of 1.8" that didn't even match its own radar, %-gap table contradicting its own formula) | Tier 2 — CSWP 29 ("applied to Organizational Profiles"); 1.1-era FAQ verbatim; Tier-1 math checks | **FIXED** — rigor-not-maturity framing skill-wide; per-Function/fractional tiers labeled house conventions; %-gap cells corrected; "no Tier averages without methodology label" rule in UC-02 |
| 3PAO, State Dir | **Fabricated federal facts in "anti-hallucination" sections**: "FedRAMP ATO duration: 12 months under PL 117-263" (no statutory duration exists); "annual ATOs"; "800-53 Tiers = FIPS 199 impact" / "Tier 3 system means 800-53 Moderate" (no such construct); stale JAB | Tier 2 — 44 USC 3607-3616 full-text grep; fedramp.gov JAB→Board | **FIXED** — all replaced with verified statements |
| Partner, SaaS, CISO | **Fabricated regulatory benchmarks in the board exemplar**: "21-day FFIEC supervisory target" for MTTD (no such thing); "FFIEC CAT v2.x (2024)" of a tool sunset Aug 31, 2025; "FFIEC CAT Domain 7" (CAT has 5 domains; D4 = External Dependency Management); Heightened Standards items marked "regulatory-mandated" for a bank under the >$50B threshold | Tier 2 — FFIEC sunset statement + CAT 2017 PDF (domain list); absence search for the MTTD target | **FIXED** — benchmarks removed; CAT marked sunset with migration framing; mandate-honesty rule (mandated / supervisory expectation / discretionary) added |
| SaaS, 3PAO, CISO, State Dir | **Phantom deliverables**: `data/crosswalks/` JSONs cited as "ships/added in Wave 2" in SKILL.md and chunks 01/03/05 while chunk 08 said no JSON ships and the directory doesn't exist | Tier 1 — `ls` | **FIXED** — no-derivative-JSON stance consistent skill-wide; data/README rewritten |
| 3PAO, CISO | HIPAA crosswalk: RS.CO-02 regulator notification cited to §164.404 (that's INDIVIDUALS; the Secretary is §164.408); §164.310 physical safeguards absent; GV.SC-04 mislabeled as the BAA hook; MFA implied as a Security Rule requirement | Tier 2 — 45 CFR verbatim | **FIXED** — rows corrected; PR.AA-06→§164.310 row added; MFA-not-required + emergency-access note |

## HIGH (summary — all verified before action)

CPG content rebuilt on the real CPG 2.0 (Dec 11, 2025: ~34 goals, 1.A-6.A; the "8-element CPG
2.0" and the CPG 1-8 table were fabricated; v1.0.1 had 38 goals; "ICS" was never in the title) —
**FIXED**. QSG numbering corrected (SP 1300 = Small Business; SP 1299 = Resource & Overview; no
per-Function QSG series; no "Profile success story" SP) — **FIXED**. Status scale relabeled as a
house convention (no official NIST scale; SP 1301 notional) and UC-01's "official NIST scale"
claim removed — **FIXED**. Stub conflation softened (Largely no longer ⇒ T3; all 6 Functions
emitted; RECOVER default documented; UC-03 fallback no longer invents AC mappings) — **FIXED**.
DFS Table 3 / SOX Table 4 subcategory IDs re-derived from verified texts (PR.AA-03 for MFA,
RS.CO-02 for 72-hour notice, RS.AN-03, PR.AA-06 physical, GV.SC-05/06 for 500.11) — **FIXED**.
ISO row fix (A.5.30 ICT readiness; A.5.26 is incident response) — **FIXED**. MA restored to the
20-family 800-53 list; GV.OC-01-vs-Category PM-11 wording; pseudo-precise "PDF lines 738-906"
cites; chunk 06 §-numbering used by UC-02; mixed-format control IDs noted — **FIXED**. CJIS
v6.0; TX §2054.515 vs §2054.0593; 44 USC §3554; EO 13800 mandate; BOD 22-01/23-01 currency;
state/SLTT reality (NASCIO/StateRAMP/MS-ISAC/CIS IG1) — **FIXED**. README/SKILL frontmatter
contradictions (status/risk/date/budget), "9 test files" (7 exist), broken links, [VERIFY] tags
in active UCs, unsourced statistics (60% CAIQ, half-tier/quarter, "most orgs...") hedged or
removed — **FIXED**. Manufacturing corrupted sentence repaired — **FIXED**.

**TICKETED — SOX-645**: healthcare view (HPH CPGs, 405(d) HICP, 800-66r2, IoMT) + consumer-side
affordances; GAGAS/legislative reporting variant + state/local UC; per-CPG-goal mapping table
from the published CPG 2.0 checklist; telemetry baseline; deeper FS rebuild against post-CAT
examiner guidance; stub `governance` key → `govern` (cosmetic contract change).
**ACCEPTED**: stub remains a canned reference executor (labeled; Epic 6 = real reliability).

## Smoke tests

3/3 PASS-WITH-NOTES pre-fix — the notes were the seed/doc contradictions and phantom references
documented above, all addressed in the fix pass (acceptance-gate rows updated). The library
pattern held for the sixth time: green tests + internally-coherent outputs sitting on fabricated
or stale external facts that only live-source verification catches.

## Verdict

9 CRITICAL clusters / ~15 HIGH verified findings: all FIXED, TICKETED (SOX-645), or ACCEPTED.
Headline: **the skill's own acceptance gate contained an unresolved recount marked ✓-verified,
and its "anti-hallucination" sections carried fabricated statutes, sunset tools cited as
current, invented subcategories, and a wrong CMMC revision** — now all corrected against a
22-fact live-source verification table, with all three worked examples rebuilt to match their
tested fixtures.
