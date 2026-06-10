# Persona Review — nist-800-53-rmf (G4.5 consumer-ready gate)

Run 2026-06-09 per `prompts/persona-vetting.md`: 5 LLM persona agents in parallel
(FedRAMP 3PAO Lead Assessor, Big 4 SOX 404 Audit Partner, SaaS Head of Compliance,
Healthcare CISO, State Gov IT Audit Director). Every CRITICAL/HIGH finding below was
independently verified against the repo (and live sources where external) before
resolution. **This is an LLM-vetted review — a filter, not a practitioner certification**
(see AGENTS.md §3 and the SOX-633 DoD).

Resolution key: **FIXED** (PR `feat/SOX-636-vet-nist-800-53-rmf`) ·
**TICKETED** (SOX number) · **ACCEPTED** (with rationale).

## CRITICAL

| persona | finding | verification | resolution |
|---|---|---|---|
| 3PAO, SaaS | SC-8(1) called "Cryptographic Protection for Wireless" and SCOPED OUT for "no wireless" in chunks/03, uc-01 (3 places), README. SC-8(1) is transmission cryptographic protection (mandatory for cloud); wireless is AC-18. An SSP scoping out SC-8(1) is auto-rejected. | Verified on disk; control semantics confirmed | **FIXED** — scoping example replaced with AC-18 across all 4 files + uc-01-expected.json; explicit "SC-8 is never scopable" warning added |
| 3PAO | Fabricated FedRAMP SLAs: "Critical: remediate within 48 hours; report to FedRAMP PMO within 24 hours" (chunks/05:36,47; SKILL.md:230). FedRAMP POA&M uses High/Mod/Low with 30/90/180-day ConMon clocks; incident reporting is a separate IR process. | Verified on disk; FedRAMP ConMon timeframes confirmed | **FIXED** — replaced with 30-day High treatment + AO escalation/IR separation in all 3 locations |
| 3PAO, SaaS | OMB M-22-15 mis-cited as both "FedRAMP OMB Memo" (frontmatter) and "Delivering a Digital-First Public Experience" (§10 manifest). FedRAMP modernization memo is M-24-15 (July 2024). The anti-hallucination manifest itself was wrong. | Verified on disk; M-24-15 PDF URL live-checked (HTTP 200) | **FIXED** — SKILL.md frontmatter/§3/§10, public-sector.md, limits doc, and data/registry/citations.json all updated to OMB-M-24-15 |
| 3PAO, Partner, SaaS | "SOC 2 TSC map 1:1 onto CC1-CC9, which derive from 800-53 AC/AU/CM families" (SKILL.md:80) — TSC aligns to COSO 2013 (CC1-CC5 mirror the 17 principles); mapping is many-to-many. Also "CMMC L2 ≈ 800-53 Moderate" — L2 is the 110 SP 800-171 requirements. | Verified on disk; lineage facts confirmed | **FIXED** — both lines rewritten (SKILL.md §3) |
| Partner, SaaS | UC-03 headline (231 mapped / 71% overlap / 94 gaps) is not derivable from the shipped crosswalk (33 rows, ~27-39 unique controls ≈ 8%); stub hardcodes the headline; oracle asserts the hardcoded constants (circular); gap list has 93 records vs stated 94; 12 controls appear as both mapped and gap. | Verified: gap list = 93 records (counted); chunk 09 admits ~8% | **TICKETED — SOX-637** (UC-03 data coherence + derivable crosswalk). Interim: chunk 09 now labels the crosswalk "a representative sample, not a complete mapping" |
| CISO | HIPAA crosswalk seed has 12 mappings vs ~50+ Subpart C specs; 164.308(a)(5)(ii)(C) (log-in monitoring) wrongly mapped to AT-2 as "exact"; all of 164.310 physical safeguards absent; no break-glass row. | Verified row count + the AT-2 row on disk | **TICKETED — SOX-638** (HIPAA crosswalk completion + healthcare UC) |
| State Dir | "Public sector" industry view covers only federal contexts; SKILL.md:40 promises "state-RMF" support that no content backs; authorization model assumes federal AO/CFACTS/FedRAMP machinery with no state/local or non-federal translation. | Verified on disk | **TICKETED — SOX-639** (non-federal adoption paths: state/local view, GAGAS finding format, resource-constrained scoping, non-federal authorization model) |
| SaaS | No working LLM executor: Path 1 sends only the router (chunks unreachable over a bare API call); Path 2 stub returns canned fixtures for any input. | Verified (by design) | **ACCEPTED** — documented limitation (README status line; stub labeled "deterministic reference executor" since PR #30). Real executor = ARGUS/SOX-611 Phase 2; real reliability testing = Epic 6 harness (SOX-600) |

## HIGH

| persona | finding | resolution |
|---|---|---|
| 3PAO, Partner, State Dir | UC-02 fixtures contradicted each other: UC file said {H:4, M:8, L:10} + "(10 Low, 4 Moderate)" composition + input examples not in the seed; seed/stub/README say {H:3, M:11, L:8}. | **FIXED** — UC file fully synced to the tested seed (5 prose locations + 2 YAML tables + input block regenerated from seed) |
| 3PAO | Agency ATO duration "typically 1 year" — agency ATOs run up to 3 years or ongoing per OMB A-130 ISCM. | **FIXED** — chunks/06 rewritten (3-year/ongoing presented; UC-02's 1-year labeled a conservative worked-example choice) |
| 3PAO | Baseline counts presented as NIST but approximating FedRAMP; SP 800-53B (the actual baseline source) uncited. | **FIXED (interim)** — limits doc now distinguishes SP 800-53B vs FedRAMP baseline workbook without asserting unverified counts; adding SP-800-53B to manifest+registry folded into SOX-637 |
| 3PAO, SaaS, Partner | README: wrong chunk filenames in file tree, "23 tests" vs actual 22, RMF step numbers inconsistent with SKILL.md (Categorize labeled Step 1 vs Step 2), fictitious test paths in UC frontmatter (tests/test_oracle.py). | **FIXED** — file tree, counts, step numbers, and all 3 UCs' test refs corrected to real paths |
| 3PAO, SaaS | uc-01 AC-2 "inherited" from AWS contradicts its own expected output ("hybrid") and shared-responsibility reality; AC-2(8) scoped with a shared-accounts rationale (wrong enhancement). | **FIXED** — AC-2 → hybrid in frontmatter + expected.json; AC-2(8) row removed (AC-18 example replaces it) |
| Partner, SaaS, CISO, State Dir | Rev 4→Rev 5 find/replace corruption destroyed the revision-selection guidance ("Rev 5 vs Rev 5", "Rev Rev 5") in limits doc, README, uc-03. | **FIXED** — Rev 4 vs Rev 5 text restored in all 3 files (PT/SR delta noted) |
| Partner, SaaS | UC walk-throughs cite SKILL.md sections that don't exist (§3.6, §5.1, §4.6, §5.7…). | **FIXED** — dangling §refs replaced with real chunk references (uc-01, uc-03) |
| Partner, CISO | chunks/09 procedure references nonexistent data/crosswalks/800-53-default.json. | **FIXED** — points at the real soc2-to-800-53-mod.json, labeled as a curated sample |
| 3PAO | UC-02 finding cites AC-2(4) "Automated Audit Actions" for a missed account review (correct element: AC-2j) with invented 800-53A criteria text; no 800-53A objective data shipped. | **TICKETED — SOX-637** (seed+stub+test cascade; ship/link OSCAL assessment objectives) |
| State Dir | IRS Pub 1075 in manifest but unused; MARS-E/SSA overlays absent for the benefits-eligibility scenario; assessment procedure offers no risk-based scoping for small shops. | **TICKETED — SOX-639** |
| CISO | UC-01's "Availability: LOW because manual workaround" pattern is unsafe if copied for clinical systems; no PHI/patient-safety categorization guidance; no healthcare UC (industries/healthcare.md says "Planned UC-04"). | **TICKETED — SOX-638** |
| SaaS | Procedures end at "document in SSP §2/§8/§9/§10" with no SSP template shipped or linked; no sponsorship/3PAO/before-you-start path. | **TICKETED — SOX-639** (consumer affordances) |

## MEDIUM / LOW (disposition summary)

- saas-technology.md §3 Owns/Inherits table was inverted (hyperscaler shown owning nothing) — **FIXED**.
- "overlap_pct [68,75] industry-typical" uncited; "~64 criteria with points of focus" — **TICKETED — SOX-637**.
- financial-services.md "no native cloud inheritance" contradicts UC-03's AWS scenario — **TICKETED — SOX-637**.
- Board-legible output template absent (CISO); PHI/BAA warning absent from quickstart (CISO) — **TICKETED — SOX-639**.
- fin-svcs/public-sector views judged substantially real practitioner content (not pasted-in) by their personas — no action.

## Verdict

8 CRITICAL / 12 HIGH / 8 MEDIUM-LOW findings. After this fix pass: **0 unresolved CRITICAL/HIGH**
(every one is FIXED, TICKETED with a SOX number, or ACCEPTED with rationale above).
The headline lesson: this skill passed 22 tests, 3 §5.11 verification rounds, and the linter
while carrying 8 CRITICALs — structural gates do not catch domain falsehoods. Persona vetting
goes to the front of the G4.5 gate for the remaining 5 skills.
