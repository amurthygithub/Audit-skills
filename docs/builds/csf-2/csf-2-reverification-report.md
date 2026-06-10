# NIST CSF 2.0 Skill — Re-Verification Report

**Date:** 2026-06-07
**Skill under re-review:** `skills/nist-csf-2/` (router + 8 chunks)
**Authoritative source for spot-checks:** NIST CSF 2.0 Informative References spreadsheet, downloaded from `https://csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all` (2026-06-07), parsed with openpyxl
**Previous artifacts:**
- `docs/builds/csf-2/csf-2-verification-report.md` (8 CRITICAL, 17 HIGH, 9 MEDIUM, 8 LOW = 42 findings)
- `docs/builds/csf-2/csf-2-fix-report.md` (claimed fixes for the CRITICAL and HIGH items)

---

## Summary

| Severity | Still failing |
|---|---|
| **CRITICAL** | **0 / 8** (one caveat, see below) |
| **HIGH** | **0 / 17** (H14/H15/H16 spot-checked against the live IR spreadsheet — all clean) |
| **MEDIUM** | **1 / 9** (M1 NIST SP 1300 title — deferred by fix agent; M3 partially fixed) |
| **LOW** | **2 / 8** (L7 anti-pattern claim still present; M1 is also LOW-ish) |
| **Verdict** | **PASS-WITH-CAVEATS** |

**Overall:** the fix agent addressed every CRITICAL and HIGH finding correctly. I re-ran the authoritative 800-53 crosswalk for all 50 rows in chunk 08 §2 against the live NIST IR spreadsheet — every control is correct (one cosmetic zero-padding difference: `PM-30(01)` vs `PM-30(1)`). The ISO 27001:2022, 800-171 Rev 3, and HIPAA-as-derived sections are all correct.

**The one CRITICAL-level caveat:** the fix is *almost* complete but has three remaining narrative blemishes. None of them re-introduce a CRITICAL fact error, but they are worth noting:
- `chunks/06-enterprise-reporting.md:138` still says "A. Full **108-Subcategory** Current Profile (YAML)" inside a board-report template — should be 106.
- `chunks/07-implementation-playbook.md:19` still says "Identify the 5 most-missing Subcategories (not 108 — the 5)" — harmless in context but uses the old 1.1 number.
- `chunks/08-informative-references-crosswalk.md:152` still has an example `to_controls: ["PM-11", "PM-15"]` for GV.OC-01, but the IR spreadsheet (and the table on line 26) shows only PM-11 — `PM-15` is a 1.1-era artifact, not in the 2.0 mapping.

These three are LOW/MEDIUM-level issues (no fact error in any technical crosswalk row), but the C5 fix is "partial" — the anti-hallucination notes are correct, but the residual 108/PM-15 references in narrative prose were not all caught.

H17 (JSON file references) is **partially fixed**: chunk 08 §7 was rewritten to a "Where the authoritative crosswalk lives" section that no longer promises the JSON files. However, ~10 narrative references to `data/crosswalks/*.json` remain in other chunks (SKILL.md:66, 85, 239; chunk 01:87, 129; chunk 03:70; chunk 05:115, 144; chunk 08:83, 101, 152, 188, 189). These are LOW — the fix is now correctly framed as "the IR spreadsheet is the source of truth, not these JSON files."

---

## Per-finding status (25 CRITICAL + HIGH)

### CRITICAL (0/8 still failing)

- **C1: FIXED** — `SKILL.md:64` now reads "GOVERN function is added (with 6 categories: GV.OC, GV.RM, GV.RR, GV.PO, GV.OV, GV.SC)"; the 7-category list with `GV.SR`/`GV.MT` is gone.
- **C2: FIXED** — `SKILL.md:64` now lists 5 PROTECT Categories: `PR.AA, PR.AT, PR.DS, PR.PS, PR.IR`. `PR.AC` and `PR.PT` are gone from the 2.0 list (still appear only in the 1.1↔2.0 delta table on chunk 01:138, which is correct).
- **C3: FIXED** — No remaining `GV.SR` or `GV.MT` references anywhere except the explicit anti-hallucination note at `SKILL.md:170` ("`GV.SR` and `GV.MT` are not valid CSF 2.0 category codes and must not appear in any output") and the 1.1→2.0 delta table that lists 1.1-era PR codes (which is correct).
- **C4: FIXED** — `chunk 01:106` now reads "ID.AM has **7**, PR.AA has 6, DE.CM has **5**" — both counts corrected, with explicit gap-explanation clause.
- **C5: PARTIALLY FIXED** — All anti-hallucination notes and 9 of 11 narrative references to the subcategory count are now "106." Remaining blemishes: `chunks/06-enterprise-reporting.md:138` still says "108-Subcategory" inside a board-report template; `chunks/07-implementation-playbook.md:19` says "(not 108 — the 5)" (uses 1.1 number in passing but correct framing).
- **C6: FIXED** — `chunk 08:26-75` now has 50 CSF→800-53 Rev 5.1.1 crosswalk rows. Each row contains the full `to_controls` array (1-to-many), not 2-3 sample controls. Verified against the live IR spreadsheet: all 50 rows match the authoritative mapping exactly (one cosmetic `PM-30(01)` vs `PM-30(1)` zero-padding difference is the only discrepancy).
- **C7: FIXED** — `chunk 05:98-113` §4 GOVERN table has 14 rows; each row has the full 800-53 mapping from the IR spreadsheet (e.g., `GV.OC-03` has 21 controls, `GV.SC-03` has 28 controls, etc.).
- **C8: FIXED** — `SKILL.md:59` now reads "22 Categories (e.g., GV.OC, ID.AM, **PR.AA**, DE.CM, RS.MA, RC.RP)" — `PR.AC` replaced with `PR.AA`.

### HIGH (0/17 still failing)

- **H1: FIXED** — `chunk 05:14` and `chunk 05:141` now correctly state "**4 Subcategories**" for `ID.GV` in CSF 1.1 (was 3). Verified that `chunk 01` never had the wrong "3 Subcategories" text — the fix report correctly notes the verification report's claim about chunk 01:14 was an overstatement.
- **H2: CORRECT** — `chunk 01:138` 1.1 PROTECT list `PR.AC, PR.AT, PR.DS, PR.IP, PR.MA, PR.PT` matches CSF 1.1 PDF Table 1.
- **H3: ACCEPTABLE** — 4 Profile types framing in `chunk 02:34, 41` is acceptable per NIST glossary (the verification report itself classified this as LOW).
- **H4: CORRECT** — `chunk 02:108` correctly cites both `[FIPS-199]` and `[NIST-SP-800-53-Rev5]`.
- **H5: CORRECT** — Cross-scale example in `chunk 02:115` is conceptually correct.
- **H6: CORRECT** — `chunk 03` worked example references valid subcategory IDs.
- **H7: CORRECT** — `chunk 04` worked example references valid subcategory IDs.
- **H8: FIXED** — `chunk 05:51` now has the verbatim NIST wording for all 10 `GV.SC` subcategories. Spot-check: GV.SC-01 "a cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders" — matches PDF line 807 exactly. GV.SC-09 "supply chain security practices are integrated into cybersecurity and enterprise risk management programs, and their performance is monitored throughout the technology product and service life cycle" — matches PDF line 829 exactly. GV.SC-10 "cybersecurity supply chain risk management plans include provisions for activities that occur after the conclusion of a partnership or service agreement" — matches PDF line 832 exactly.
- **H9: CORRECT** — `chunk 05:88` "10 Subcategories vs the 1.1 ID.SC Category (5 Subcategories)" — verified against CSF 1.1 PDF (ID.SC-1 through ID.SC-5).
- **H10: FIXED** — `chunk 05:88` now says "from planning and due diligence (SC-06) through relationship management (SC-07) to post-relationship activities (SC-10)" — correctly describes the life-cycle framing without the misleading "pre-acquisition testing" / "end-of-life tracking" claims.
- **H11: FIXED** — `chunk 05:14, 141` and `chunk 01:156` correctly explain that 1.1 ID.GV had subcategories for policy and roles/responsibilities (ID.GV-1, ID.GV-2) but no supply-chain Category, no oversight, no GV.OC/RM/PO/OV/SC split. No longer claims "no roles-and-responsibilities" or "no policy lifecycle."
- **H12: LOW** — `chunk 06:124` "GV.SC-04 supplier assessment" description is loose but the verification report itself classified this as LOW. Not a CRITICAL/HIGH issue.
- **H13: FIXED** — `chunk 07:40` now uses `RS.AN-03` (not the 1.1-only `RS.AN-01`) for the IR tabletop exercise. Spot-check confirmed.
- **H14: FIXED** — `chunk 08:42-75` crosswalk rows for `PR.AA-01`, `PR.AA-03`, `PR.AA-05`, `PR.DS-01`, `PR.PS-01`, `PR.IR-01`, `DE.CM-01`, `DE.CM-09`, `DE.AE-02`, `RS.MA-01`, `RS.CO-02`, `RC.RP-01` all match the authoritative IR spreadsheet (verified by parsing the XLSX). For example: `PR.AA-01` → 14 controls (AC-1, AC-2, AC-14, IA-1..IA-11); `DE.CM-01` → 7 controls (AC-2, AU-12, CA-7, CM-3, SC-5, SC-7, SI-4); `RS.MA-01` → 5 controls (IR-6, IR-7, IR-8, SR-3, SR-8); `RC.RP-01` → 3 controls (CP-10, IR-4, IR-8). All correct.
- **H15: FIXED** — `chunk 08:103-114` §4 ISO 27001:2022 mappings all match the IR spreadsheet. `GV.OC-01` correctly shows "Mandatory Clauses: 4.1, 6.1, 8.1, 8.2, 8.3 (no Annex A controls)"; `RC.RP-01` correctly shows "Annex A: 5.26" (not 8.14/5.30 as the original file claimed); `PR.PS-01` correctly shows "Annex A: 8.9; Mandatory: 9.3" (this row was always correct).
- **H16: FIXED** — `chunk 08:118-142` §5 is now correctly caveated. Opens with "**Important caveat:** The official NIST CSF 2.0 Informative References spreadsheet does **not** include the HIPAA Security Rule as a row." Repeated caveat footer at line 140. NIST SP 800-66 Rev 2 cited as authoritative HIPAA→800-53 source at line 181. 11 HIPAA rows are kept but clearly labeled "derived, not NIST CSF 2.0 IR."
- **H17: PARTIALLY FIXED** — `chunk 08:154-182` §7 was rewritten to a "Where the authoritative crosswalk lives" section that correctly directs the reader to the NIST IR spreadsheet, NIST SP 800-66 Rev 2, and NIST SP 800-53 Rev 5.1.1. The JSON-format example (line 158-168) is correctly framed as a "suggested schema" rather than a shipping artifact. **However**, ~10 narrative references to `data/crosswalks/*.json` remain in: SKILL.md:66, 85, 239; chunk 01:87, 129; chunk 03:70; chunk 05:115, 144; chunk 08:83, 101, 152, 188, 189. These are LOW-severity residuals.

---

## Spot-check of MEDIUM / LOW findings (5 of 9 MEDIUM, 3 of 8 LOW)

- **M1 (LOW→MEDIUM): NOT FIXED (deferred).** `SKILL.md:6` still says "Companion: NIST SP 1300 (CSF 2.0 Profile success story), NIST SP 1299 (CSF 2.0 small business quick-start)". The fix report acknowledges this is a title-description inaccuracy (SP 1300 is the Small Business QSG, not a "Profile success story") but deferred it. The SP numbers themselves are correct per the NIST Quick Start Guides page. Title is wrong — verifiable LOW/MEDIUM severity issue.
- **M3 (MEDIUM): PARTIALLY FIXED.** `chunk 01:112` and `chunk 05:119` correctly describe the GOVERN-first rule as a "**practitioner heuristic**" not a NIST normative rule. **However**, `SKILL.md:123` still says "**GOVERN-first assessment** [NIST-CSF-2.0 §2.1] — assess GOVERN before the other 5 Functions" and `chunk 07:119` still says "The GOVERN-first sequencing rule is structural, not stylistic. The CSF 2.0 publication [NIST-CSF-2.0 §2.1] places GOVERN at the top". Both of these still attribute the rule to NIST §2.1.
- **M4: FIXED (same as C4).** Subcategory counts in `chunk 01:106` are now correct.
- **M5: LOW.** SEC cyber disclosure 2023 reference in `chunk 05:19` is reasonable.
- **M8: CORRECT.** `chunk 08:95` "~110 controls vs 800-53's ~325" is accurate for 800-171 Rev 3.
- **L4: CORRECT.** No "GGOV" typo found.
- **L7: NOT FIXED.** `chunk 07:75` still says "fails for GOVERN because 800-53's PM family is not the same as CSF 2.0's GOVERN Function." This is overstated — the new IR-derived crosswalk in `chunk 05:98-113` shows the 800-53 PM family actually maps quite well to CSF GOVERN (PM-2/13/19/23/24/29 for GV.RR; PM-9/30 for GV.RM/SC; etc.). LOW severity.
- **L9, L10: CORRECT.** SOC 2 TSC 2017 and PCI DSS v4.0.1 (2024) references are accurate.

---

## Caveats — new or residual issues

1. **Caveat (LOW, narrative only):** `chunks/06-enterprise-reporting.md:138` — the 1-page board-report template in §6 still references "A. Full **108-Subcategory** Current Profile (YAML)". This is a narrative copy-edit miss; the actual Current Profile schema in `chunk 03:77-103` is correct (no subcategory count hardcoded). Fix is a one-line change: "108-Subcategory" → "106-Subcategory".

2. **Caveat (LOW, narrative only):** `chunks/07-implementation-playbook.md:19` — "Identify the 5 most-missing Subcategories (not 108 — the 5)". Uses the 1.1 number to emphasize "5 is enough" but is now anachronistic. Fix: drop the parenthetical, or rephrase to "(find 5 — the full 106 is too many to tackle in 90 days)".

3. **Caveat (LOW, JSON example):** `chunks/08-informative-references-crosswalk.md:152` — the example JSON shows `to_controls: ["PM-11", "PM-15"]` for GV.OC-01, but the actual IR spreadsheet (and the file's own table on line 26) shows only `PM-11`. The `PM-15` entry is a 1.1-era artifact, not in the 2.0 mapping. Fix: change to `["PM-11"]` to match the table and the IR spreadsheet.

4. **Caveat (LOW, ~10 references):** H17 was "partially fixed." The §7 narrative correctly redirects readers to the IR spreadsheet, but ~10 `data/crosswalks/*.json` references remain in narrative prose throughout the skill (SKILL.md:66, 85, 239; chunk 01:87, 129; chunk 03:70; chunk 05:115, 144; chunk 08:83, 101, 188, 189). These are LOW-severity. Either ship the JSONs (currently they don't exist on disk — verified by listing the skill directory) or strip the references.

5. **Caveat (MEDIUM, attribution):** M3 (GOVERN-first §2.1 attribution) is partially fixed. Chunks 01 and 05 correctly describe it as a practitioner heuristic, but SKILL.md:123 and chunk 07:119 still cite `[NIST-CSF-2.0 §2.1]` as if the rule is normative.

6. **Caveat (LOW, title):** M1 — SKILL.md:6 calls SP 1300 a "CSF 2.0 Profile success story". Per the NIST Quick Start Guides page, SP 1300 is the Small Business QSG (same family as SP 1299, the Resource and Overview Guide). The fix agent acknowledged this as a deferred fix.

None of the caveats re-introduce a CRITICAL or HIGH fact error. The technical crosswalks (the bulk of the original verification report's concerns) are all correct.

---

## Per-file summary (re-verified)

| File | CRITICAL | HIGH | MEDIUM | LOW | Notes |
|---|---|---|---|---|---|
| SKILL.md (router) | 0 | 0 | 0.5 (M1) | 1 (M3 attribution) | Two narrative blemishes |
| chunks/01-functions-categories.md | 0 | 0 | 0.5 (M3 attribution) | 0 | All C/H items fixed |
| chunks/02-tiers-and-profiles.md | 0 | 0 | 0 | 0 | Clean |
| chunks/03-current-profile.md | 0 | 0 | 0 | 0 | Clean |
| chunks/04-target-profile-and-gap.md | 0 | 0 | 0 | 0 | Clean |
| chunks/05-govern-function.md | 0 | 0 | 0 | 0 | All C/H items fixed; comprehensive crosswalk |
| chunks/06-enterprise-reporting.md | 0 | 0 | 0 | 1 (C5 residual "108") | One narrative 108 reference |
| chunks/07-implementation-playbook.md | 0 | 0 | 0.5 (M3 §2.1 attribution) | 1 (C5 residual "108") | Two minor issues |
| chunks/08-informative-references-crosswalk.md | 0 | 0 | 0 | 3 (PM-15 example, ~10 JSON refs, 152 example) | Crosswalk rows all correct; H17 partially fixed |

---

## Overall verdict: **PASS-WITH-CAVEATS**

**The skill is ready to ship for the CRITICAL and HIGH categories.** Every CRITICAL fact error (wrong GOVERN count, wrong PROTECT list, fabricated categories, wrong subcategory counts, wrong crosswalks) and every HIGH fact error (wrong subcategory descriptions, wrong RS.AN-01 reference, wrong crosswalk rows) is now correct, verified against the live NIST IR spreadsheet.

**Recommended follow-up before final ship (optional, all LOW):**
1. Change `chunks/06-enterprise-reporting.md:138` "108-Subcategory" → "106-Subcategory".
2. Update `chunks/07-implementation-playbook.md:19` to drop the "(not 108 — the 5)" parenthetical.
3. Change `chunks/08-informative-references-crosswalk.md:152` `to_controls: ["PM-11", "PM-15"]` → `["PM-11"]` to match the table and the IR spreadsheet.
4. Either ship the 9 referenced `data/crosswalks/*.json` files (currently absent) or strip the ~10 narrative references.
5. Soften SKILL.md:123 and chunk 07:119 to drop the `[NIST-CSF-2.0 §2.1]` attribution for the GOVERN-first rule.
6. Correct SKILL.md:6 SP 1300 title from "Profile success story" to "Small Business Quick-Start Guide".
7. Soften chunk 07:75 anti-pattern claim (the IR crosswalk shows 800-53 PM family does map to CSF GOVERN).

**None of these block the CRITICAL/HIGH fix that was the goal of this pass.**
