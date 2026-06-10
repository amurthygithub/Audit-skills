# Persona Review — aicpa-soc-reporting (G4.5 consumer-ready gate)

Run 2026-06-10 per `prompts/persona-vetting.md` (process v2): 5 LLM persona agents + 4
clean-session smoke tests. Every CRITICAL/HIGH verified BEFORE fixing — Tier 1 (on-disk
greps, count tallies) or Tier 2 (live sources with verbatim quotes: the 2017 TSC PDF
text-extracted with a full 61-ID inventory transcription, AICPA AT-C codification
"Sources of Sections" PDF, AICPA SOC 2 FAQ, 45 CFR 164.308/.312, HITRUST v11 sample
reports + assessor publications, SP 800-53 Rev 5 family table).
**LLM-vetted — a filter, not a certification.**

Resolution key: **FIXED** (PR `fix/SOX-636-vet-aicpa`) · **TICKETED — SOX-642** · **ACCEPTED**.

## CRITICAL

| persona | finding | verification | resolution |
|---|---|---|---|
| Partner, 3PAO, CISO | **Fabricated TSC criteria**: CC8.2 and CC8.3 do not exist (CC8 = CC8.1 only); CC count inflated to 35; Privacy listed as 8 criteria vs the actual 18; "53 primary / ~66 with sub-criteria" — "sub-criteria" isn't a TSC concept. Four mutually contradicting counts shipped (33/35/51/53). | Tier 2 — full ID extraction from the TSC PDF: 33 CC + 3 A + 2 C + 5 PI + 18 P = 61 | **FIXED** — chunk 03 rebuilt from the verified inventory (full 18-criterion P-series with GDPR maps); every count statement across SKILL.md/README/limits synced to 33/61 |
| Partner, State Dir | **Fabricated standards citations**: "AT-C 100/200/300" cited as the governing sections (they're series groupings; the citable sections are AT-C 105/205/210/215/320); "SSAE 21 superseded SSAE 18 effective December 2020" — false (SSAE 21 amended the codification, added AT-C 206, renamed AT-C 205, eff. June 15 2022). The anti-hallucination section itself taught the wrong citation. | Tier 2 — AICPA "Sources of Sections in Current Text" PDF + SSAEs-currently-effective page | **FIXED** — codification corrected everywhere (SKILL.md tables/frontmatter/§9, chunk 01 table rebuilt, chunk 02 tree, manifest rows, citation-registry labels renamed AT-C-105/205/320) |
| 3PAO, CISO | **Invented "non-sequential" CC1→COSO mapping** (CC1.2→P5, CC1.5→P2) presented as insider knowledge — the TSC labels CC1.1–CC1.5 with COSO Principles 1–5 IN ORDER (CC1.2 = board oversight). | Tier 2 — CC1.2/CC1.5 verbatim from the TSC | **FIXED** — sequential mapping restored in chunk 03 + SKILL.md §3.4; UC-02's SoD CUEC remapped CC1.2→CC6.3 |
| SaaS | Path 2 stub returns canned demo output for any input; "Unqualified" echoed to a first-timer reads as a predicted audit outcome. | Tier 1 (executed) | **ACCEPTED** (deterministic reference executor, labeled since PR #30; harness = Epic 6) + first-timer affordances **TICKETED — SOX-642** |

## HIGH

| persona | finding | resolution |
|---|---|---|
| Partner, 3PAO, CISO, State Dir | Wrong criterion descriptions: CC6.4/CC6.5 swapped semantics (physical access vs disposal), CC7.1/CC7.2 ("manages IT infrastructure"/"job processing" vs vulnerability/anomaly monitoring), A1.1 missing capacity. Propagated into UC-02's CSOC mappings. | **FIXED** — descriptions rebuilt from verbatim criterion texts; UC-02 mappings corrected (CC6.5→CC6.4 etc.) |
| Partner, SaaS | "Type II minimum 6 months" stated as a rule — the AICPA prescribes NO minimum (SOC 2 FAQ §.05 verbatim); "Type I as readiness assessment" conflates an attestation with non-attest consulting. | **FIXED** — chunk 02/07 + SKILL.md: no-minimum language with evidence-sufficiency caution; readiness assessment distinguished from Type I |
| Partner, 3PAO, State Dir | Carve-out/inclusive logic self-contradictory (both branches "best when subservice has its own SOC report"); inclusive method's hard requirement (subservice management's written assertion) omitted; framed as the practitioner's evidence call instead of management's presentation election; "auditor has NO responsibility to evaluate CUEC suitability" overstated. | **FIXED** — chunk 06 decision tree rebuilt; UC-02 rationale corrected; CUEC relevance/completeness evaluation restored |
| 3PAO | 800-53 crosswalk cited Rev-4 ghost families (AR, DI) and mapped RA→CC9. | **FIXED** — Rev 5 verified family list (PT for privacy; CC3→RA; CC9→SR) |
| 3PAO, CISO | tsc-to-hipaa.json: off-by-one spec cites (unique user ID, emergency access, automatic logoff), CC8.1 mapped to malware (that's CC6.8), CC7.3 to log-in monitoring (incident procedures is 164.308(a)(6)). | **FIXED** — 5 rows corrected per verified CFR text, Required/Addressable flags added |
| 3PAO, CISO | tsc-to-hitrust.json: 5 of 7 distinct domain labels wrong vs HITRUST v11's 19 assessment domains (3≠Risk Mgmt, 7≠Access Control, 10≠Comms&Ops, 17≠Privacy). Repeated in healthcare.md. | **FIXED** — all 13 rows remapped to the verified domain list; healthcare table synced |
| Partner, State Dir | Bridge letter conventions: sample dated June 15 attesting through June 30 (future attestation); "no exceptions" asserted without testing; 3-6 month gap stated as typical (convention ≤3). | **FIXED** — date discipline + "nothing has come to our attention" guidance in chunk 05; UC-03 sample re-dated; gap guidance corrected |
| CISO | Break-glass mapped to CC6.3 (role changes) instead of CC6.1 + 164.312(a)(2)(ii) Required spec; "vendor CUEC reports evidence BAA compliance" — backwards (CUECs are YOUR obligations). | **FIXED** — healthcare.md corrected; UC-04 §3 reframed as user-entity vendor review with the directionality warning |
| Partner | Opinion tree routed any evidence insufficiency straight to disclaimer — materiality/pervasiveness axis absent. | **FIXED** — chunk 07 Step 1 now applies the qualified-vs-disclaimer ladder (AT-C 205) |
| State Dir | No AU-C 402 user-auditor track; SOC 1 name-checked without depth (no control objectives, no SOC 1 UC); public-sector view is vendor-side only; consumer-side UC missing (also CISO). | **TICKETED — SOX-642** |
| SaaS | UC-04 promises a per-criterion evidence checklist that doesn't exist; no timeline/cost/auditor-selection playbook; criteria-vs-controls never explained; README verify block said "1 passed" (actual 25). | README/UC count fixes **FIXED**; first-timer content **TICKETED — SOX-642** |

## MEDIUM/LOW (summary)

UC-01 "Privacy adds → 46" → 56 — **FIXED**. UC-02 PI-mappings outside declared scope — **FIXED**.
data/README phantom tsc-to-nist-800-53-mod.json — **FIXED** (marked planned). README inventory
(7→8 chunks, 51→61 criteria, test counts) — **FIXED**. Report-section ordering (assertion before
description), DC 200 as description criteria, inherent-limitations checklist item, "Type I SOC 3"
removal, SOC-for-Cybersecurity depth — **TICKETED — SOX-642**.

## Smoke tests

4/4 PASS-WITH-NOTES. Two agents independently flagged the 33-vs-35 count contradiction unprompted
and reported per the UC oracle (38) — correct behavior. UC-03's letter inherited the template's
future-dating flaw (now fixed). The "consistently wrong" pattern repeats: clean routing and
internally-coherent outputs built on a partly fabricated criteria catalog.

## Verdict

4 CRITICAL / 12 HIGH verified findings: all FIXED, TICKETED (SOX-642), or ACCEPTED. Headline:
**the criteria catalog — the single most load-bearing artifact in a SOC skill — contained invented
criteria, and the anti-hallucination section taught fabricated citations.** The full 61-criterion
inventory is now transcribed verbatim from the TSC with a retrieval date, and the AT-C codification
matches the AICPA's own sources-of-sections table.
