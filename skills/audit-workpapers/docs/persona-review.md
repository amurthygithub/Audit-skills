# Persona Review — audit-workpapers (G4.5 consumer-ready gate)

Run 2026-06-09 per `prompts/persona-vetting.md` (process v2): 5 LLM persona agents in
parallel; every CRITICAL/HIGH finding verified BEFORE fixing — Tier 1 (recomputed: Poisson
RF factors, binomial attribute sizes, stub execution) or Tier 2 (live sources with verbatim
quotes: GAO 2024 Yellow Book, PCAOB AS 1215 + Release 2024-004, AS 2315, AICPA MUS
methodology, 45 CFR 164.312). **LLM-vetted — a filter, not a practitioner certification.**

One persona claim was **REFUTED** during verification and dropped: "chunk 09 absent from the
§11 routing table" — SKILL.md routes to chunk 09 at three §11 entries (verified by grep).
Findings are hypotheses; this is why the dispatcher verifies.

Resolution key: **FIXED** (PR `fix/SOX-636-vet-audit-workpapers`) · **TICKETED** · **ACCEPTED**.

## CRITICAL

| persona | finding | verification | resolution |
|---|---|---|---|
| Partner | ULM formula omitted tainting and projected misstatement entirely (`ULM = BP + sum((RF_i−RF_{i−1})×SI)`) — a $1 and a $150K misstatement produced identical ULM; tainting was defined then never used | Tier 1 (internal contradiction) + Tier 2 (AICPA MUS methodology quote) | **FIXED** — full BP + PM + IA form with descending taintings and top-stratum actual-misstatement rule |
| Partner | RF table wrong in the anti-conservative direction: 20% column k=1..3 read 2.95/4.17/5.32 (correct 3.00/4.28/5.52), 15% k=3 read 5.98 (correct 6.02) | Tier 1 — recomputed via Poisson solver | **FIXED** — 4 cells corrected |
| Partner, 3PAO | Stub concluded "ULM >= TM — consider expanded sample" on its own clean golden case (BP=500,001 > TM=500,000 from SI display rounding + strict `<`), and the oracle blessed it by substring-matching "ULM" | Tier 1 — executed the stub | **FIXED** — BP = RF × unrounded SI = TM exactly; accept rule `ULM <= TM`; oracle now asserts the conclusion, not a substring |
| Partner | Any RIA ≠ 5% silently got the 10% factor (2.31): RIA=1% produced n=57 instead of ~116 — lowering acceptable risk SHRANK the sample | Tier 1 — executed at RIA=1% | **FIXED** — RF table lookup keyed on RIA {1,5,10,15,20}%, hard `ValueError` on unsupported parameters |
| 3PAO, CISO, State Dir | Discovery-sampling formula divides by zero at its own "typical" parameter (d=0) | Tier 1 — trivial | **FIXED** — closed form `n ≥ ln(1−D)/ln(1−p)` with worked example |
| State Dir | "All five elements are mandatory" + attribution to GAO: GAGAS 2024 defines FOUR elements (criteria/condition/cause/effect) "to the extent necessary"; recommendation is report content (¶6.53) | Tier 2 — GAO-24-106786 verbatim ¶6.17/¶8.57/¶6.53 | **FIXED** — chunk 05 states the GAGAS taxonomy accurately; 5-part template kept as documentation default |
| SaaS | UC-02 is a stub that can't teach a non-auditor to WRITE a finding; the executor returns canned XYZ Corp text for any input with no warning | Tier 1 (read/executed) | **TICKETED — SOX-640** (company-side walk-through, full prose example, management-response template); stub honesty covered by README "deterministic reference executor" labeling (PR #30) — **ACCEPTED** for the executor itself (harness = Epic 6) |

## HIGH

| persona | finding | resolution |
|---|---|---|
| Partner, 3PAO | Attribute table didn't tie to AICPA Table A-1 (150/60/90/45/30 vs 149/59/93/42/29; the 90-vs-93 row under-sampled) | **FIXED** — Tier-1 recomputed exact values; tie-out note added |
| 3PAO | Attribute evaluation compared raw sample deviation rate to tolerable rate — no sampling-risk allowance; silently passes failed controls | **FIXED** — achieved upper-deviation-limit evaluation in the procedure line |
| Partner | TD re-mapped to a different "RIA" scale, double-counting conservatism — AS 2315 defines TD AS the allowable risk of incorrect acceptance | **FIXED** (Tier-2 AS 2315 quote) — chunk 04 table, stub, UC-03, oracle test all use TD = RIA |
| Partner | UC-02 criteria cited ASC 606 (revenue) for an AP cutoff finding | **FIXED** — accrual-basis liability/expense recognition wording in UC, stub, oracle |
| State Dir | Management response only "recommended" — GAGAS requires views of responsible officials (¶6.58) | **FIXED** — GAGAS-required note in chunk 05; full government findings/report formats **TICKETED — SOX-640** |
| Partner | 14-day vs 45-day AS 1215 documentation-completion confusion | **FIXED** — Release 2024-004 staged effective dates stated (Tier-2 verified, incl. the release-number correction from 2024-005) |
| 3PAO (cross-skill) | Severity master table attributed a Low/Mod/High/Critical scale to "NIST SP 800-53A Rev 5" — 800-53A produces only S/OTS; the scale is FedRAMP's POA&M layer | **FIXED** — column re-labeled, attribution corrected (FedRAMP POA&M template carries "Critical" in original risk ratings — Tier-2 verified) |
| CISO | healthcare.md unreachable (README table + _index "(planned)"); encryption misstated as unconditional "must" (it's addressable); covered-entity vs auditor retention conflated | **FIXED** — routed in README + _index; addressable wording (Tier-2: 45 CFR quote); retention regimes split. PHI-in-evidence procedures + patient-AR variant **TICKETED — SOX-640** |
| 3PAO, CISO | No ITGC/access-review or frequency-based control-population sampling guidance anywhere; ">500 → statistical" bright line fabricated | Bright line **FIXED** (real decision factors); ITGC/frequency sampling section **TICKETED — SOX-640** |
| State Dir | No questioned-costs/Uniform-Guidance severity branch; PCAOB-only retention guidance | **TICKETED — SOX-640** |
| Partner, SaaS, CISO, 3PAO | README inventory false: "4 tests" (42), "184-line router" (196), "7 chunks" (9), phantom test files, missing chunks 08/09 + healthcare in trees, fictitious UC test refs | **FIXED** — all inventories regenerated from disk |

## MEDIUM/LOW (summary)

ITAF 4th→5th in limits doc — **FIXED**. AS 1215.06A phantom cite — **FIXED** (.06). Jargon
wall (RIA/TM/ULM undefined in README), glossary gaps, plain-language routing triggers,
OpenAI-key prerequisites, FS-overlay depth (CECL/confirmations), controls-assessor evidence
crosswalk (AS 1105 ↔ 800-53A) — **FIXED 2026-06-11 (SOX-640 slice)**: orientation crosswalk + explicit not-for-FedRAMP scope boundary in chunk 07. SaaS view auditor-vs-company framing
— **TICKETED — SOX-640**.

## Verdict

6 CRITICAL / 12 HIGH verified findings (1 persona claim refuted and dropped): all FIXED,
TICKETED (SOX-640), or ACCEPTED with rationale. The headline: **the sampling math at the
skill's core failed reperformance** — wrong RF cells, an ULM formula missing its central
term, and a stub whose golden case concluded the wrong way, all previously blessed by a
substring-matching oracle. Every number now ties to recomputation, and the oracle asserts
conclusions, not substrings.
