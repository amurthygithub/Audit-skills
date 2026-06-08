# NIST CSF 2.0 Skill — Fact-Verification Report

**Date:** 2026-06-07
**Skill under review:** `skills/nist-csf-2/` (router + 8 chunks)
**Authoritative sources consulted:**
- NIST CSF 2.0 PDF (NIST CSWP 29, Feb 26, 2024) — `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`
- NIST CSF 1.1 PDF (NIST CSWP 04162018, Apr 16, 2018) — for 1.1↔2.0 delta verification
- NIST CSF 2.0 Informative References spreadsheet (downloaded from `csrc.nist.gov/extensions/nudp/services/json/csf/download?olirids=all`, May 2026 update)
- NIST CSF 2.0 web page — `https://www.nist.gov/cyberframework`

---

## Summary

| Severity | Count |
|---|---|
| **CRITICAL** (wrong structure, wrong IDs, wrong function/category lists) | **8** |
| **HIGH** (wrong crosswalk rows, wrong subcategory counts, wrong subcategory existence) | **17** |
| **MEDIUM** (wrong dates, wrong heuristic, mis-attribution) | **9** |
| **LOW** (typos, formatting, vague wording) | **8** |
| **Total claims checked** | **~75** |

**Overall verdict: FAIL.** The skill contains multiple fabricated Category IDs (`GV.SR`, `GV.MT`) that do not exist in CSF 2.0, wrong subcategory counts for ID.GV in 1.1, an inflated "108" subcategory figure for 2.0 (actual: 106), a fabricated 7th GOVERN category, and a very large number of incorrect CSF↔800-53 crosswalk rows that are not supported by the NIST Informative References spreadsheet. The skill cannot ship until the CRITICAL and HIGH items are corrected.

---

## CRITICAL findings (must fix)

### C1. SKILL.md:64 — Fabricated GOVERN Categories `GV.SR` and `GV.MT`; wrong category count
- **File says (line 64):** "the new **GOVERN** function is added (with 7 categories: GV.OC, GV.RM, GV.SC, GV.SR, GV.PO, GV.OV, GV.MT)"
- **NIST says (CSF 2.0 PDF, Table 1, lines 698–704):** GOVERN has **6** Categories: `GV.OC`, `GV.RM`, `GV.RR`, `GV.PO`, `GV.OV`, `GV.SC`. **`GV.SR` does not exist. `GV.MT` does not exist.**
- **Severity:** CRITICAL
- **Proposed fix:** Replace with: "the new **GOVERN** function is added (with 6 categories: GV.OC, GV.RM, GV.RR, GV.PO, GV.OV, GV.SC) and now sits across the top of the framework".

### C2. SKILL.md:64 — Fabricated PROTECT categories for CSF 2.0
- **File says (line 64):** "The **PROTECT** categories were renamed (PR.AA, PR.AC, PR.DS, PR.PS, PR.IR, PR.PT)"
- **NIST says (CSF 2.0 PDF, Table 1, lines 708–712):** PROTECT Categories in 2.0 are **5**: `PR.AA`, `PR.AT`, `PR.DS`, `PR.PS`, `PR.IR`. `PR.AC` and `PR.PT` are 1.1 categories, not 2.0.
- **Severity:** CRITICAL
- **Proposed fix:** "The **PROTECT** categories were renamed (PR.AA, PR.AT, PR.DS, PR.PS, PR.IR) — see `chunks/01-functions-categories.md` for the 1.1-to-2.0 delta".

### C3. SKILL.md:37, 151, 170, 219; chunks/05:134, 06:150, 07:43 — References to non-existent `GV.SR` and `GV.MT` Categories
- **File says (multiple lines):** References `GV.SR`, `GV.MT`, and the 7-category GOVERN list including them.
- **NIST says:** Neither `GV.SR` nor `GV.MT` exist anywhere in NIST CSF 2.0 (PDF, glossary, Appendix A, or Informative References spreadsheet).
- **Severity:** CRITICAL
- **Proposed fix:** Remove all references to `GV.SR` and `GV.MT` and replace with valid GOVERN Category codes. Affected lines:
  - SKILL.md lines 37, 64, 151, 170, 219 — remove `GV.SR`, `GV.MT` from lists
  - chunks/05-govern-function.md line 134: replace "GV.OV and GV.MT" with "GV.OV"
  - chunks/06-enterprise-reporting.md line 150: replace "GV.OV, GV.MT, GV.SC" with "GV.OV, GV.SC"
  - chunks/07-implementation-playbook.md line 43: replace "GV.OV-01, GV.MT-*" with "GV.OV-01"

### C4. chunks/01-functions-categories.md:106 — Wrong subcategory count for `ID.AM` and `DE.CM`
- **File says (line 106):** "Subcategories-per-Category counts are uneven: `GV.OC` has 5 Subcategories, `ID.AM` has 8, `PR.AA` has 6, `DE.CM` has 9, `RS.MA` has 5, etc."
- **NIST says (PDF Appendix A and counted from text):**
  - `ID.AM` has **7** subcategories (ID.AM-01, -02, -03, -04, -05, -07, -08 — gap at -06)
  - `DE.CM` has **5** subcategories (DE.CM-01, -02, -03, -06, -09 — gaps at -04, -05, -07, -08)
- **Severity:** CRITICAL (the file's anti-hallucination note elsewhere is correct that gaps in numbering are deliberate, but the file contradicts itself by giving wrong counts)
- **Proposed fix:** "Subcategories-per-Category counts are uneven: `GV.OC` has 5 Subcategories, `ID.AM` has 7, `PR.AA` has 6, `DE.CM` has 5, `RS.MA` has 5, etc. (Gaps in subcategory numbers — e.g., DE.CM-04, DE.CM-05 — are deliberate and indicate CSF 1.1 subcategories that were relocated in 2.0; see CSF 2.0 PDF p.15.)"

### C5. chunks/01-functions-categories.md:85, 154, 169 (SKILL.md), and other places — Wrong "~108" subcategory count for CSF 2.0
- **File says (multiple lines, including the anti-hallucination note):** "Subcategory count is ~108 in CSF 2.0; the precise count varies between 106 and 108 depending on whether sub-letter items are counted."
- **NIST says:** CSF 2.0 has exactly **106 Subcategories** (counted from the PDF Appendix A: 31 GV + 21 ID + 22 PR + 11 DE + 13 RS + 8 RC = 106). There are no "sub-letter items" in 2.0; gaps in numbering (e.g., DE.CM-04 missing) are deliberate to indicate 1.1 subcategories that were relocated (PDF p.15 line 695: "gaps in numbering indicate CSF 1.1 Subcategories that were relocated in CSF 2.0"). The "108" figure is the count for **CSF 1.1**, not 2.0.
- **Severity:** CRITICAL (the file's own anti-hallucination note is wrong; the user is told to cite a count that doesn't match the official PDF)
- **Proposed fix:** Replace "**~108 Subcategories**" with "**106 Subcategories**" in all places. Update the anti-hallucination note in chunk 01 line 154 to: "Subcategory count is 106 in CSF 2.0. The number 108 is the count for CSF 1.1, not 2.0. Gaps in numbering (e.g., DE.CM-04 absent) are deliberate and indicate relocated 1.1 subcategories — see CSF 2.0 PDF p.15." Same change in SKILL.md line 60, 169, 170 and in the descriptions of all chunks.

### C6. chunks/08-informative-references-crosswalk.md:35, 36, 38, 40, 43, 44 — Multiple incorrect 800-53 mappings
- **File claims (rows in §2 table):**
  - `GV.OC-01` → `PM-11`, `PM-15`
  - `GV.OC-03` → `PM-9`, `RA-1`
  - `GV.RM-02` → `PM-9`, `PM-8`
  - `GV.SC-01` → `SR-1`, `SR-3`
  - `GV.SC-05` → `SR-8`, `IR-4`
  - `GV.OV-01` → `CA-7`, `PM-6`
  - `GV.RR-01` → `PM-2`, `PM-3`
- **NIST Informative References spreadsheet (actual authoritative source) says:**
  - `GV.OC-01` → `PM-11` only (PM-15 NOT in mapping)
  - `GV.OC-03` → AC-01, AT-01, AU-01, CA-01, CM-01, CP-01, IA-01, IR-01, MA-01, MP-01, PE-01, PL-01, PM-01, PS-01, PT-01, RA-01, SA-01, SC-01, SI-01, SR-01, PM-28 (PM-9 and RA-1 NOT in mapping)
  - `GV.RM-02` → `PM-9` only (PM-8 NOT in mapping)
  - `GV.SC-01` → `PM-30`, `SR-2`, `SR-3` (SR-1 NOT in mapping; SR-2 is the actual first SR control)
  - `GV.SC-05` → `SA-4`, `SA-9`, `SR-3`, `SR-5`, `SR-6`, `SR-10` (SR-8 and IR-4 NOT in mapping)
  - `GV.OV-01` → AC-01..SR-01 (all -1 controls), PM-09, PM-18, PM-30, PM-31, RA-07, SR-06 (CA-7 and PM-6 NOT in mapping)
  - `GV.RR-01` → PM-2, PM-19, PM-23, PM-24, PM-29 (PM-3 NOT in mapping)
- **Severity:** CRITICAL (crosswalk rows are the primary deliverable of chunk 08; ~10+ wrong rows means the skill publishes incorrect cross-references)
- **Proposed fix:** Replace the §2 crosswalk table in chunk 08 with mappings derived from the authoritative Informative References spreadsheet. For each row, include the complete `to_controls` array (the 1-to-many shape), not just 2 controls. The spreadsheet is the source of truth at `https://www.nist.gov/cyberframework/informative-references`.

### C7. chunks/05-govern-function.md:99-114 — Wrong 800-53 mappings in GOVERN table
- **File claims (rows in §4 table):**
  - `GV.OC-01` → PM-11, PM-15
  - `GV.OC-03` → PM-9, RA-1
  - `GV.RM-02` → PM-9, PM-8
  - `GV.SC-01` → SR-1, SR-3
  - `GV.SC-05` → SR-8, IR-4
  - `GV.OV-01` → CA-7, PM-6
  - `GV.OV-03` → CA-2, CA-7
  - `GV.RR-01` → PM-2, PM-3
  - `GV.RR-03` → PM-3, PM-4
- **NIST Informative References spreadsheet says:** (same as C6 above) — most of these are wrong or incomplete.
- **Severity:** CRITICAL (chunk 05 publishes the same wrong crosswalk as chunk 08, doubling the bad-claims surface)
- **Proposed fix:** Replace the §4 table with mappings derived from the Informative References spreadsheet.

### C8. SKILL.md:59 — Lists `PR.AC` as a 2.0 Category
- **File says (line 59):** "22 Categories (e.g., GV.OC, ID.AM, PR.AC, DE.CM, RS.MA, RC.RP)"
- **NIST says (CSF 2.0 Table 1):** `PR.AC` is a **1.1** Category, not 2.0. The 2.0 equivalent is `PR.AA`.
- **Severity:** CRITICAL (the example list given in the router is itself wrong)
- **Proposed fix:** "22 Categories (e.g., GV.OC, ID.AM, PR.AA, DE.CM, RS.MA, RC.RP)"

---

## HIGH findings (must fix)

### H1. chunks/01-functions-categories.md:14, 154; chunks/05-govern-function.md:14 — Wrong `ID.GV` subcategory count in CSF 1.1
- **File says:** "There was a partial governance Category under Identify (`ID.GV` — "Governance") but it was under-developed: 3 Subcategories" (chunk 01 line 14); and "3 Subcategories, no supply chain, no roles-and-responsibilities, no oversight, no policy lifecycle" (chunk 05 line 14).
- **NIST says (CSF 1.1 PDF, lines 1309-1348):** `ID.GV` had **4 Subcategories** (ID.GV-1, ID.GV-2, ID.GV-3, ID.GV-4), not 3. They covered policy (ID.GV-1), roles/responsibilities (ID.GV-2), legal/regulatory (ID.GV-3), and governance/risk management processes (ID.GV-4). The claim that 1.1 had "no roles-and-responsibilities" or "no policy lifecycle" is misleading — those existed as Subcategories within ID.GV.
- **Severity:** HIGH
- **Proposed fix:** "There was a partial governance Category under Identify (`ID.GV` — 'Governance') with 4 Subcategories (policy, roles/responsibilities, legal/regulatory, risk management processes). It was under-developed relative to 2.0 GOVERN."

### H2. chunks/01-functions-categories.md:138 — Wrong 1.1 PROTECT category codes
- **File says (line 138):** "PR.AC, PR.AT, PR.DS, PR.IP, PR.MA, PR.PT"
- **NIST says (CSF 1.1 PDF Table 1, lines 1215-1220):** `PR.AC`, `PR.AT`, `PR.DS`, `PR.IP`, `PR.MA`, `PR.PT` ✓ MATCH
- **Status:** CORRECT (this is the only 1.1 PROTECT list that matches)

### H3. chunks/02-tiers-and-profiles.md:34, 41 — "4 Profile types" framing
- **File says (lines 34, 41):** "CSF 2.0 formalized 4 Profile types — in 1.1, only 'Current' and 'Target' were named" and the table has 4 rows (Current, Target, Organizational, Community).
- **NIST says (CSF 2.0 PDF, §3.1, glossary):** NIST defines 4 named profile-related terms: "CSF Community Profile", "CSF Current Profile", "CSF Organizational Profile", "CSF Target Profile". The body of the document says "Every Organizational Profile includes one or both of the following: A Current Profile… A Target Profile…" (line 355-362). So "Organizational Profile" is the umbrella; "Current" and "Target" are the contents; "Community Profile" is a separate thing.
- **Status:** ACCEPTABLE — the "4 Profile types" framing is consistent with how the NIST glossary enumerates them. NIST CSF 1.1 only defined Current Profile and Target Profile, so the "in 1.1 only Current and Target were named" is correct.
- **Severity:** LOW (acceptable as written, but the user should be aware that "Organizational Profile" is the umbrella and Current/Target are parts of it)

### H4. chunks/02-tiers-and-profiles.md:108 — References "NIST-SP-800-53-Rev5" for FIPS 199 baseline
- **File says (line 108):** "800-53 baseline (FIPS 199 impact) | Low / Moderate / High | [FIPS-199] [NIST-SP-800-53-Rev5]"
- **NIST says:** FIPS 199 impact levels (Low/Moderate/High) are defined in FIPS 199; 800-53 Rev 5 (and now Rev 5.1.1 and 5.2.0) provides control baselines that correspond to FIPS 199 impact. The reference is correct.
- **Status:** CORRECT

### H5. chunks/02-tiers-and-profiles.md:114-115 — Cross-scale example
- **File says (line 115):** "An org with FIPS 199 **High** systems can be CSF **Tier 1** (Partial) — the systems are sensitive but the org has not built the maturity scaffolding."
- **Status:** CONCEPTUALLY CORRECT (the two scales are independent)

### H6. chunks/03-current-profile.md:115-139 — Worked example references the correct subcategories
- **Status:** CORRECT for the specific subcategory IDs cited (GV.OC-01, GV.SC-01, GV.RR-01, ID.AM-01, ID.RA-01, PR.AA-01, PR.DS-01, DE.CM-01, DE.CM-09, RS.MA-01, RC.RP-01 — all match the NIST PDF text).

### H7. chunks/04-target-profile-and-gap.md:170-178 — Worked example references correct subcategory IDs
- **Status:** CORRECT for the cited subcategories (GV.SC-01, PR.AA-03, DE.CM-09, GV.RR-01, RS.MA-01, DE.CM-01).

### H8. chunks/05-govern-function.md:51 — Lists GV.SC subcategories
- **File says (line 51):** "`GV.SC-01` (supply chain risk management program established), `GV.SC-02` (suppliers prioritized by criticality), `GV.SC-03` (contracts include cybersecurity requirements), `GV.SC-04` (suppliers routinely assessed), `GV.SC-05` (supplier incident response plans coordinated), `GV.SC-06` (supplier disruptions planned for), `GV.SC-07` (supply chain risks identified and managed throughout life cycle), `GV.SC-08` (suppliers included in incident response planning), `GV.SC-09` (supplier products/services tested prior to acquisition), `GV.SC-10` (components tracked through life cycle)."
- **NIST says (CSF 2.0 PDF lines 806-837):** All 10 subcategories exist (GV.SC-01 to GV.SC-10), but the file's paraphrased descriptions are imprecise. Actual:
  - GV.SC-01: "A cybersecurity supply chain risk management program, strategy, objectives, policies, and processes are established and agreed to by organizational stakeholders"
  - GV.SC-02: "Cybersecurity roles and responsibilities for suppliers, customers, and partners are established, communicated, and coordinated internally and externally" (NOT "suppliers prioritized by criticality" — that's GV.SC-04)
  - GV.SC-03: "Cybersecurity supply chain risk management is integrated into cybersecurity and enterprise risk management, risk assessment, and improvement processes" (NOT "contracts" — that's GV.SC-05)
  - GV.SC-04: "Suppliers are known and prioritized by criticality" (file is right here)
  - GV.SC-05: "Requirements to address cybersecurity risks in supply chains are established, prioritized, and integrated into contracts and other types of agreements with suppliers and other relevant third parties" (this is contracts, not "supplier incident response plans")
  - GV.SC-06: "Planning and due diligence are performed to reduce risks before entering into formal supplier or other third-party relationships"
  - GV.SC-07: "The risks posed by a supplier, their products and services, and other third parties are understood, recorded, prioritized, assessed, responded to, and monitored over the course of the relationship"
  - GV.SC-08: "Relevant suppliers and other third parties are included in incident planning, response, and recovery activities" (file has this right)
  - GV.SC-09: "Supply chain security practices are integrated into cybersecurity and enterprise risk management programs, and their performance is monitored throughout the technology product and service life cycle" (NOT "products tested prior to acquisition")
  - GV.SC-10: "Cybersecurity supply chain risk management plans include provisions for activities that occur after the conclusion of a partnership or service agreement" (NOT "components tracked through life cycle")
- **Severity:** HIGH — multiple GV.SC subcategory descriptions are incorrectly mapped (e.g., "suppliers prioritized by criticality" is GV.SC-04, not GV.SC-02; "contracts" is GV.SC-05, not GV.SC-03; "supplier products tested prior to acquisition" is not GV.SC-09 in 2.0).
- **Proposed fix:** Use the exact NIST wording for each GV.SC subcategory. Replace the parenthetical descriptions with the official text.

### H9. chunks/05-govern-function.md:88 — Wrong 1.1 ID.SC subcategory count
- **File says (line 88):** "10 Subcategories vs the 1.1 `ID.SC` Category (5 Subcategories)"
- **NIST says:** ID.SC in 1.1 had 5 subcategories (ID.SC-1 to ID.SC-5) ✓ MATCH
- **Status:** CORRECT

### H10. chunks/05-govern-function.md:88 — Wrong claim about GV.SC subcategory count
- **File says (line 88):** "10 Subcategories vs the 1.1 `ID.SC` Category (5 Subcategories). The new Subcategories cover the **full supplier life cycle** — from pre-acquisition testing (SC-09) to end-of-life tracking (SC-10)"
- **NIST says (GV.SC-09):** "Supply chain security practices are integrated into cybersecurity and enterprise risk management programs, and their performance is monitored throughout the technology product and service life cycle" — this is NOT "pre-acquisition testing" in the way the file describes.
- **NIST says (GV.SC-10):** "Cybersecurity supply chain risk management plans include provisions for activities that occur after the conclusion of a partnership or service agreement" — this is post-relationship/end-of-contract, NOT "end-of-life tracking of components" as the file says.
- **Severity:** HIGH (descriptive inaccuracy about the SC-09 and SC-10 subcategories)
- **Proposed fix:** "The new Subcategories cover the **full supplier life cycle** — from planning/due-diligence (SC-06) through relationship management (SC-07) to post-relationship activities (SC-10)."

### H11. chunks/05-govern-function.md:14 — "no supply chain, no roles-and-responsibilities, no oversight, no policy lifecycle" in 1.1 ID.GV
- **NIST says:** ID.GV in 1.1 had subcategories for policy (ID.GV-1) and roles/responsibilities (ID.GV-2). The claim that 1.1 had "no policy lifecycle" and "no roles-and-responsibilities" is misleading.
- **Severity:** HIGH
- **Proposed fix:** "There was a partial governance Category under Identify (`ID.GV` — 'Governance') with 4 Subcategories (policy, roles/responsibilities, legal/regulatory, risk management processes), but no supply chain (which was a separate `ID.SC` Category), no distinct oversight Subcategory, and no GV.OC/RM/PO/OV/SC split."

### H12. chunks/06-enterprise-reporting.md:124-126 — Top 3 priority gaps sample
- **File says (line 124):** "[e.g., GV.SC-04 supplier assessment]"
- **NIST says:** GV.SC-04 is "Suppliers are known and prioritized by criticality" (not "supplier assessment" — that's more like GV.SC-07)
- **Status:** LOW (the example is illustrative but the description is loose)
- **Severity:** LOW

### H13. chunks/07-implementation-playbook.md — Quick wins list references correct subcategories
- The 90-day quick wins reference subcategories like GV.OV-01, GV.PO-01, PR.AA-03, RS.MA-01, ID.AM-01, ID.AM-08, GV.RR-04, ID.RA-01, DE.CM-01, RS.AN-01, GV.SC-01, RS.MA-01, RS.AN-03, GV.OV-02, GV.OV-03, GV.SC-04, DE.AE-02.
- **NIST verification:**
  - GV.OV-01 ✓ exists
  - GV.PO-01 ✓ exists
  - PR.AA-03 ✓ exists (Users, services, and hardware are authenticated)
  - RS.MA-01 ✓ exists
  - ID.AM-01 ✓ exists
  - ID.AM-08 ✓ exists
  - **GV.RR-04** ✓ exists (Cybersecurity is included in human resources practices)
  - ID.RA-01 ✓ exists
  - DE.CM-01 ✓ exists
  - **RS.AN-01** — **DOES NOT EXIST** in CSF 2.0! (RS.AN-03 is the lowest in 2.0; RS.AN-01 and -02 existed in 1.1 only)
  - GV.SC-01 ✓ exists
  - **RS.AN-03** ✓ exists
  - GV.OV-02 ✓ exists
  - GV.OV-03 ✓ exists
  - GV.SC-04 ✓ exists
  - DE.AE-02 ✓ exists
- **Severity:** HIGH (chunk 07 line 40 cites `RS.AN-01` which is a 1.1 subcategory, not 2.0)
- **Proposed fix (chunk 07 line 40):** Change "Run the first IR tabletop exercise (covers `RS.MA-01`, `RS.AN-01`)" to "covers `RS.MA-01`, `RS.AN-03`" (the first RS.AN subcategory in 2.0 is RS.AN-03).

### H14. chunks/08-informative-references-crosswalk.md:42, 44, 51-58 — Incomplete/inaccurate 800-53 mappings
- **File says (line 42):** "`PR.AA-01` (identity mgmt) | `IA-2`, `IA-5`, `AC-2`"
- **NIST xlsx says:** PR.AA-01 → AC-1, AC-2, AC-14, IA-1, IA-2, IA-3, IA-4, IA-5, IA-6, IA-7, IA-8, IA-9, IA-10, IA-11 (14 controls)
- **File says (line 47):** "`PR.AA-03` (MFA) | `IA-2(1)`, `IA-2(2)`, `AC-6(9)`"
- **NIST xlsx says:** PR.AA-03 → AC-7, AC-12, IA-2, IA-3, IA-5, IA-7, IA-8, IA-9, IA-10, IA-11 (the enhancements IA-2(1), IA-2(2), AC-6(9) are NOT in the authoritative mapping)
- **File says (line 49):** "`PR.AA-05` (access permissions) | `AC-2`, `AC-3`, `AC-5`, `AC-6`"
- **NIST xlsx says:** PR.AA-05 → AC-1, AC-2, AC-3, AC-5, AC-6, AC-10, AC-16, AC-17, AC-18, AC-19, AC-24, IA-13 (12 controls; missing 8)
- **File says (line 50):** "`PR.DS-01` (data-at-rest) | `SC-28`, `SC-28(1)`"
- **NIST xlsx says:** PR.DS-01 → CA-3, CP-9, MP-8, SC-4, SC-7, SC-12, SC-13, SC-28, SC-32, SC-39, SC-43, SI-3, SI-4, SI-7 (14 controls)
- **File says (line 51):** "`PR.PS-01` (configuration mgmt) | `CM-2`, `CM-6`, `CM-7`"
- **NIST xlsx says:** PR.PS-01 → CM-1 through CM-11 (all 11 CM controls)
- **File says (line 52):** "`PR.IR-01` (network segmentation) | `SC-7`, `SC-32`"
- **NIST xlsx says:** PR.IR-01 → AC-3, AC-4, SC-4, SC-5, SC-7 (5 controls; SC-32 is not in this mapping for IR-01)
- **File says (line 53):** "`DE.CM-01` (network monitoring) | `SI-4`, `AU-2`"
- **NIST xlsx says:** DE.CM-01 → AC-2, AU-12, CA-7, CM-3, SC-5, SC-7, SI-4 (7 controls; AU-2 is wrong — should be AU-12)
- **File says (line 54):** "`DE.CM-09` (compute monitoring) | `SI-4`, `SI-4(2)`"
- **NIST xlsx says:** DE.CM-09 → AC-4, AC-9, AU-12, CA-7, CM-3, CM-6, CM-10, CM-11, SC-34, SC-35, SI-4, SI-7 (12 controls; SI-4(2) not in mapping)
- **File says (line 55):** "`DE.AE-02` (event correlation) | `AU-6`, `SI-4(2)`"
- **NIST xlsx says:** DE.AE-02 → AU-6, CA-7, IR-4, SI-4 (4 controls; SI-4(2) not in mapping but IR-4 is)
- **File says (line 56):** "`RS.MA-01` (IR plan executed) | `IR-4`, `IR-5`, `IR-6`"
- **NIST xlsx says:** RS.MA-01 → IR-6, IR-7, IR-8, SR-3, SR-8 (5 controls; IR-4 and IR-5 absent; IR-7, IR-8, SR-3, SR-8 missing)
- **File says (line 57):** "`RS.CO-02` (regulator notification) | `IR-6`"
- **NIST xlsx says:** RS.CO-02 → IR-4, IR-6, IR-7, SR-3, SR-8 (5 controls)
- **File says (line 58):** "`RC.RP-01` (recovery executed) | `CP-2`, `CP-10`, `IR-4`"
- **NIST xlsx says:** RC.RP-01 → CP-10, IR-4, IR-8 (3 controls; CP-2 wrong, IR-8 missing)
- **Severity:** HIGH (many specific crosswalk rows are wrong or missing controls)
- **Proposed fix:** Replace the §2 table with mappings derived from the authoritative Informative References spreadsheet. Include the full `to_controls` array for each row, not just 2-3 sample controls.

### H15. chunks/08-informative-references-crosswalk.md:88-97 — Inaccurate ISO 27001:2022 mappings
- **File claims (rows in §4 table):**
  - `GV.OC-01` (mission) → A.5.1 (Policies), A.5.2 (Information security roles)
  - `PR.PS-01` (configuration mgmt) → A.8.9 (Configuration management)
  - `RC.RP-01` (recovery executed) → A.8.14 (Backup), A.5.30 (ICT readiness)
- **NIST Informative References spreadsheet says (for ISO/IEC 27001:2022):**
  - `GV.OC-01` → Mandatory Clauses 4.1, 6.1, 8.1, 8.2, 8.3; Annex A Controls: (none listed). The file's claim of A.5.1 and A.5.2 is **not** in the official mapping.
  - `PR.PS-01` → Annex A Controls: 8.9 ✓ (this one is correct)
  - `RC.RP-01` → Annex A Controls: 5.26 (not 8.14 and not 5.30) ✗
- **Severity:** HIGH
- **Proposed fix:** Replace ISO 27001:2022 rows with the official mapping from the Informative References spreadsheet.

### H16. chunks/08-informative-references-crosswalk.md:108-119 — Inaccurate HIPAA mappings
- **File claims (rows in §5 table):**
  - `ID.AM-01` (asset inventory) → §164.308(a)(1)(ii)(A)
  - `PR.AA-01` (identity mgmt) → §164.308(a)(4), §164.312(a)(1), §164.312(d)
  - `PR.DS-01` (data-at-rest) → §164.312(a)(2)(iv)
  - `RS.MA-01` (IR plan) → §164.308(a)(6)
- **NIST Informative References spreadsheet (CSF 2.0 IR) says:** The official CSF 2.0 Informative References spreadsheet does NOT include HIPAA Security Rule as a row (it's not a published NIST informative reference). HIPAA mappings must be derived from NIST SP 800-66 Rev 2 (the HIPAA Security Rule → 800-53 crosswalk).
- **Severity:** HIGH (the file claims these are the "CSF → HIPAA" mappings, but they are not from the authoritative NIST source; they appear to be the file author's interpretation. The file's own anti-hallucination note in line 103 acknowledges this: "NIST 800-66 Rev 2 is the authoritative HIPAA → 800-53 mapping; the CSF → HIPAA mapping in this skill is derived from 800-66's reverse direction." But the user is still shown specific §164.x references without source citations.)
- **Proposed fix:** Either (a) cite NIST SP 800-66 Rev 2 as the source and mark these as derived mappings requiring verification, or (b) provide a machine-readable cross-reference to 800-66 and let the user derive HIPAA mappings. Remove the "the full mapping ships in `data/crosswalks/csf-to-hipaa.json`" claim unless the file actually exists with this content.

### H17. chunks/08-informative-references-crosswalk.md:160-169 — References JSON files that don't exist
- **File says (line 160-169):** Lists `data/crosswalks/csf-to-800-53-mod.json`, `csf-to-800-53-high.json`, `csf-to-800-171-r3.json`, `csf-to-iso27001-2022.json`, `csf-to-hipaa.json`, `csf-to-soc2-tsc-2017.json`, `csf-to-pci-dss-4.0.1.json`, `csf-to-cobit-2019.json`, `csf-2-0-subcategories.json` as if they exist.
- **Status:** These are referenced multiple times throughout the chunks (e.g., chunk 01 line 87, chunk 05 line 115, chunk 08 throughout) but the skill ships **only the markdown** — there is no `data/crosswalks/` directory.
- **Severity:** HIGH (the file repeatedly promises JSON deliverables that don't exist)
- **Proposed fix:** Either ship the JSON files or remove the references and replace with "the canonical list lives in the NIST CSF 2.0 PDF Appendix A and the Informative References spreadsheet at https://www.nist.gov/cyberframework/informative-references".

---

## MEDIUM findings (should fix)

### M1. SKILL.md:6 — References NIST SP 1300, NIST SP 1299
- **File says (line 6):** "Companion: NIST SP 1300 (CSF 2.0 Profile success story), NIST SP 1299 (CSF 2.0 small business quick-start)"
- **Status:** NIST did publish a "CSF 2.0 Small Business Quick-Start Guide" (NIST SP 1300 is a different doc). The actual small business QSG is `NIST SP 1300` (per the NIST CSF 2.0 page on 2026-02-24 update: "The final version of *NIST Cybersecurity Framework 2.0: Cybersecurity, Enterprise Risk Management, and Workforce Management Quick-Start Guide* (SP 1308)"). The numbering in the file is likely wrong (the file claims 1299 and 1300, but the actual CSF 2.0 QSGs are SP 1300, 1301, 1302, 1303, 1308 etc., depending on topic).
- **Severity:** MEDIUM (unverified)
- **Proposed fix:** Verify the SP numbers against the actual NIST CSF 2.0 Quick Start Guides page (https://www.nist.gov/cyberframework/quick-start-guides) and correct.

### M2. SKILL.md:184-205 — Manifest labels and dates
- **File claims (line 184):** "NIST-CSF-2.0 | 2.0 (Feb 26, 2024)" — **NIST PDF says Feb 26, 2024** ✓ MATCH
- **File claims (line 185):** "NIST-SP-800-53-Rev5 | Sept 2020" — should verify (800-53 Rev 5 was Sept 2020; Rev 5.1.1 is the current version with the Informative References mappings shown above) ✓ APPROXIMATELY CORRECT
- **File claims (line 196):** "OMB-A-130 | July 28, 2016" — should verify
- **Status:** MEDIUM severity (mostly correct but worth verifying)

### M3. chunks/01-functions-categories.md:108-116 — "GOVERN-first sequencing rule" attribution
- **File says (line 108):** "The GOVERN-first sequencing rule [NIST-CSF-2.0 §2.1]"
- **NIST says (CSF 2.0 PDF line 301-307):** "Figure 2 shows the CSF Functions as a wheel because all of the Functions relate to one another… GOVERN is in the center of the wheel because it informs how an organization will implement the other five Functions."
- **NIST does not explicitly mandate a "GOVERN-first" assessment rule.** The PDF says "The order of Functions, Categories, and Subcategories of the Core is not alphabetical; it is intended to resonate most with those charged with operationalizing risk management within an organization" (line 693-695) and "The Functions should be addressed concurrently" (line 321).
- **Severity:** MEDIUM (the file claims GOVERN-first is a NIST §2.1 rule, but NIST describes the wheel/concurrent model; "GOVERN-first" is a practitioner heuristic, not a NIST rule)
- **Proposed fix:** Soften the language. "The GOVERN-first sequencing rule is a **practitioner heuristic** supported by NIST's structural placement of GOVERN in the center of the Functions wheel (Figure 2 of the CSF 2.0 PDF), but NIST does not mandate it as a normative rule."

### M4. chunks/01-functions-categories.md:106 — Same "unequal counts" example
- Same as C4; the specific counts (ID.AM=8, DE.CM=9) are wrong.

### M5. chunks/05-govern-function.md:18-20 — "SEC cyber disclosure rules 2023" attribution
- **File says (line 19):** "Regulatory expectations (SEC cyber disclosure rules 2023, NY DFS 500 §500.04 board reporting, EU DORA)"
- **Status:** These are real regulatory items but the SEC cyber disclosure rules were adopted July 2023 and became effective December 2023 (for large filers). The file's reference is reasonable but not directly relevant to the GOVERN elevation in CSF 2.0 (which is dated Feb 2024, before some of these rules took effect).
- **Severity:** LOW (reasonable narrative but timing is slightly off)

### M6. chunks/06-enterprise-reporting.md — Tier 1 = "Tiers are per Function" but the radar shows tiers 2.0/2.5/3.0
- The radar uses fractional tiers (2.5, 3.5) which is a practical convention. NIST Tiers are 1, 2, 3, 4. The file acknowledges this ("the empirical Tier may be 2.0 not 2.5" in chunk 02).
- **Severity:** LOW (the skill documents this as a heuristic)

### M7. chunks/06-enterprise-reporting.md:35 — "Mermaid radar" Mermaid block
- The Mermaid syntax may not be valid (radar charts in Mermaid are not standard). The radar chart type was added to Mermaid in version 10+, but the syntax may not work in all renderers.
- **Severity:** LOW (functional issue, not a factual error)

### M8. chunks/08-informative-references-crosswalk.md:78 — "800-171 is a strict subset of 800-53 Moderate (~110 controls vs 800-53's ~325)"
- **NIST says:** 800-171 Rev 3 has 14 control families and approximately 110+ controls (varies by counting method); 800-53 Rev 5 Moderate baseline has ~325 controls.
- **Status:** CORRECT
- **Severity:** NONE

### M9. chunks/05-govern-function.md:91 — "GV.SC" cross-Function dependencies
- **File says (line 91):** "GV.SC Subcategories cross-reference ID.AM (supplier inventory), PR.PS (supplier product security), DE.CM (supplier monitoring), RS.MA (supplier incident coordination)"
- **Status:** CONCEPTUALLY CORRECT but not directly from NIST text.

---

## LOW findings (typos, formatting, vagueness)

### L1. chunks/01-functions-categories.md:114 — "Cybersecurity Supply Chain Risk Management | Third-party / supplier / vendor cyber risk (elevated in 2.0)" — NIST calls it "Cybersecurity Supply Chain Risk Management" but uses "Cyber supply chain risk management" in the body. The label is correct.

### L2. chunks/01-functions-categories.md:25 — "Good Identities Protect, Detect, Respond, Recover" mnemonic — Heuristic, not NIST.

### L3. chunks/02-tiers-and-profiles.md:22-28 — Practical heuristic for selecting a target Tier — Heuristic, not NIST.

### L4. chunks/02-tiers-and-profiles.md:46 — "GGOV" → "GOVERN" (no actual typo found, just stylistic)

### L5. chunks/06-enterprise-reporting.md:99 — "GOVERN is usually the lowest Tier (because GOVERN is the new Function in 2.0 and most orgs under-invest in it)" — Practitioner observation, not NIST.

### L6. chunks/07-implementation-playbook.md — FTE estimates and cost ranges are heuristics, clearly marked as such. Not NIST claims.

### L7. chunks/07-implementation-playbook.md:75 — "For orgs already subject to 800-53 (federal, DoD), the temptation is to use the 800-53 implementation as the substrate and derive the CSF profile from it. This works for the controls side… but fails for GOVERN because 800-53's PM family is not the same as CSF 2.0's GOVERN Function." — This is a practitioner observation. The 800-53 PM family actually does map closely to CSF GOVERN (e.g., PM-9, PM-11 are referenced in the GV.OC-01, GV.RM-02 mappings). The "fails for GOVERN" claim is overstated.

### L8. SKILL.md:50, 167, 175-176 — Multiple "this skill encodes knowledge, not judgment" disclaimers. Standard pattern, not an error.

### L9. SKILL.md:198 — "SOC-2-TSC-2017 | Trust Services Criteria | AICPA | 2017 (TSP §100, 2022 revised points of focus)" — accurate.

### L10. SKILL.md:200 — "PCI-DSS-4.0.1 | Payment Card Industry Data Security Standard | PCI SSC | v4.0.1 (2024)" — accurate (PCI DSS v4.0.1 was published June 2024).

---

## Per-file summary

| File | CRITICAL | HIGH | MEDIUM | LOW |
|---|---|---|---|---|
| SKILL.md (router) | 4 (C1, C2, C3, C8) | 0 | 1 (M2) | 2 |
| chunks/01-functions-categories.md | 2 (C4, C5) | 2 (H1, H11) | 1 (M3) | 2 |
| chunks/02-tiers-and-profiles.md | 0 | 0 | 0 | 0 |
| chunks/03-current-profile.md | 0 | 0 | 0 | 0 |
| chunks/04-target-profile-and-gap.md | 0 | 0 | 0 | 0 |
| chunks/05-govern-function.md | 1 (C7) | 3 (H8, H10, H11) | 1 (M9) | 1 |
| chunks/06-enterprise-reporting.md | 0 | 0 | 0 | 1 |
| chunks/07-implementation-playbook.md | 0 | 1 (H13) | 0 | 1 |
| chunks/08-informative-references-crosswalk.md | 1 (C6) | 3 (H14, H15, H16) | 0 | 1 |

Note: H11 appears in both chunks/01 and chunks/05 because the same wrong claim is made in both files.

---

## Overall verdict: FAIL

The skill cannot ship in its current form. The minimum set of fixes before shipping:

### Must-fix (blocking)

1. **Remove all references to `GV.SR` and `GV.MT`** (these are fabricated Category codes). Affects SKILL.md (5 lines), chunks/05 (1 line), chunks/06 (1 line), chunks/07 (1 line).
2. **Fix the GOVERN Category count** from "7" to "6" everywhere, and use the correct list: GV.OC, GV.RM, GV.RR, GV.PO, GV.OV, GV.SC.
3. **Fix the PROTECT Category list in SKILL.md line 64** to remove the 1.1 codes (PR.AC, PR.PT) that don't exist in 2.0.
4. **Fix the subcategory count** from "~108" to "106" in all 9 files. Update the anti-hallucination note in chunk 01 to acknowledge that "108" was the 1.1 count and 2.0 has 106.
5. **Fix the ID.AM (8→7) and DE.CM (9→5) subcategory counts** in chunk 01 line 106.
6. **Fix the ID.GV-1.1 subcategory count** from "3" to "4" in chunks 01 line 14 and 05 line 14.
7. **Replace the crosswalk tables in chunks 05 (§4) and 08 (§2-5)** with mappings derived from the authoritative NIST Informative References spreadsheet. The current crosswalk rows have ~10+ wrong or incomplete mappings.
8. **Fix the RS.AN-01 reference in chunk 07 line 40** to RS.AN-03 (RS.AN-01 is 1.1 only).
9. **Fix the GV.SC subcategory descriptions in chunk 05 line 51** — multiple are incorrectly mapped to the wrong GV.SC-XX code (e.g., "suppliers prioritized by criticality" is GV.SC-04 not GV.SC-02).

### Should-fix (recommended)

10. Soften the "GOVERN-first sequencing rule [NIST-CSF-2.0 §2.1]" attribution to a practitioner heuristic.
11. Either ship the `data/crosswalks/*.json` files referenced throughout or remove the references.
12. Verify NIST SP 1300/1299/QSG numbers in SKILL.md line 6 against the actual NIST Quick Start Guides.
13. Add a section in chunk 08 explicitly stating that HIPAA mappings are derived (not from a published NIST Informative Reference) and should be verified against NIST SP 800-66 Rev 2.

### Out-of-scope (already correct)

The Tier definitions (4 tiers: Partial, Risk Informed, Repeatable, Adaptive) are correct and match the NIST PDF Appendix B. The Tier names match between 1.1 and 2.0. The 4 Profile types (Current, Target, Organizational, Community) framing is acceptable per the NIST glossary. The publication date (Feb 26, 2024) is correct. The function ordering (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) is correct. The worked examples in chunks 03, 04, 06 reference valid subcategory IDs. The 90-day quick wins and FTE estimates in chunk 07 are clearly marked as heuristics, not NIST claims.
