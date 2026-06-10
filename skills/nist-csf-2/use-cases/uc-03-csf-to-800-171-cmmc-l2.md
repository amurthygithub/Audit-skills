---
uc_id: UC-03
title: "Mid-market DoD supplier maps 14 lagging CSF 2.0 Subcategories to 800-171 Rev 2 (the CMMC L2 control set) for certification readiness"
industries: [manufacturing]
frameworks: [NIST-CSF-2.0, CMMC-L2, NIST-SP-800-171, 32-CFR-Part-170, NIST-SP-800-82-Rev3]
procedure:
  - "chunks/04-target-profile-and-gap.md §3 — Identify the 14 lagging Subcategories (Current status Not/Partially Implemented)"
  - "chunks/08-informative-references-crosswalk.md §3 — CSF → 800-171 orientation. CRITICAL: CMMC L2 assesses 800-171 REV 2 (110 requirements, 14 families, 3.x.y IDs) per 32 CFR 170.14(c)(3) — not Rev 3"
  - "industries/manufacturing.md — CMMC affirming-official reality and IT/OT convergence considerations"
  - "chunks/07-implementation-playbook.md §3 — 12-month readiness sizing (FTE + tool spend)"
expected_outputs:
  gap_subcategories: 14 rows (the seed's lagging Subcategories)
  crosswalk: 14 rows (subcategory_id, primary_800_171_control [Rev 2, 3.x.y], practice_domain = the control's actual Rev 2 family, secondary_controls, evidence_gap)
  cmmc_l2_readiness: 4 rows — the 4 Rev 2 families Apex targets first (Access Control, Identification & Authentication, Configuration Management, Incident Response)
  roadmap_12mo: 6 deliverables with FTE/cost sizing
  classification: CSF_TO_800-171_L2_READINESS
oracle:
  - "len(gap_subcategories) == 14 and len(crosswalk) == 14"
  - "all 14 crosswalk rows have a non-empty primary_800_171_control in Rev 2 format (3.x.y — NOT Rev 3's 03.xx.yy)"
  - "cmmc_l2_readiness covers the 4 targeted Rev 2 families; per-family counts cannot exceed the family's actual Rev 2 control count (IR has 3)"
  - "roadmap_12mo has at least 6 deliverables"
data_refs: [data/seeds/uc-03-input.json]
tests:
  - tests/test_nist_csf_2_oracle.py::test_uc_03_oracle
  - tests/test_nist_csf_2_oracle.py::test_uc_03_gap_size
  - tests/test_nist_csf_2_oracle.py::test_uc_03_crosswalk_size
  - tests/test_nist_csf_2_oracle.py::test_uc_03_800_171_control_format
  - tests/test_nist_csf_2_oracle.py::test_uc_03_cmmc_l2_domains
status: active
---

# UC-03 — CSF 2.0 → 800-171 Rev 2 crosswalk for CMMC L2 readiness (Apex Manufacturing)

## §1 Context and persona

**Apex Manufacturing** is a fictional 240-FTE precision-machining aerospace supplier (turbine blades, structural fittings; customers are DoD primes) with 2 facilities and a small OT estate (3 CNC cells, metrology lab, ERP). It holds CMMC Level 1 self-assessment status and is preparing for **CMMC Level 2 certification** with a target assessment date of 2026-09-30 (per the seed at `data/seeds/uc-03-input.json` — the tested fixture). A CSF 2.0 Current Profile identified **14 lagging Subcategories**; this use case maps them to the CMMC L2 control set and produces the readiness plan.

**The revision fact this UC exists to get right:** CMMC Level 2 assesses against **NIST SP 800-171 Rev 2** — 110 requirements across 14 families, IDs `3.x.y`. 32 CFR 170.14(c)(3) (verified eCFR, 2026-06-10): *"The security requirements in CMMC Level 2 are identical to the requirements in NIST SP 800-171 R2."* Rev 3 (May 2024; 97 requirements, 17 families, `03.xx.yy` IDs) is the current NIST publication but is **not** the CMMC L2 set — building a readiness plan on Rev 3 fails at scoping.

## §2 The 14 lagging Subcategories (from the seed)

PR.AA-01, PR.AA-03, PR.AA-05, PR.DS-01, PR.PS-01, PR.PS-02, PR.IR-01, DE.CM-01, DE.CM-03, RS.MA-01, RS.AN-03, RS.CO-02, RC.RP-01, RC.RP-03 — concentrated in PROTECT (the OT estate lags IT) plus detection, response, and recovery. Each carries an evidence-gap note in the seed (e.g., PR.AA-03: "MFA on IT systems but not on OT HMI terminals").

## §3 The crosswalk (Rev 2 controls; practice_domain = the control's actual Rev 2 family)

Representative rows from the seed (all 14 are in the fixture). Mapping choices are grounded in verified Rev 2 requirement texts; the `practice_domain` column names the control's real family — earlier versions of this UC mislabeled SC/AU/RA/MP controls as "Configuration Management".

| subcategory_id | primary (Rev 2) | family | rationale |
|----------------|-----------------|--------|-----------|
| PR.AA-01 (identities/credentials managed) | 3.1.1 | Access Control | "Limit system access to authorized users, processes..., and devices" — account management; I&A controls (3.5.x) secondary |
| PR.AA-03 (users/services/hardware authenticated) | 3.5.3 | Identification & Authentication | "Use multifactor authentication for local and network access to privileged accounts and for network access to non-privileged accounts" — the OT HMI gap |
| PR.AA-05 (least privilege) | 3.1.5 | Access Control | "Employ the principle of least privilege, including for specific security functions and privileged accounts" |
| PR.DS-01 (data-at-rest protected) | 3.13.16 | System & Communications Protection | "Protect the confidentiality of CUI at rest"; 3.13.8 (in-transit crypto) secondary |
| PR.PS-01 (config baselines) | 3.4.1 | Configuration Management | "Establish and maintain baseline configurations and inventories of organizational systems" |
| PR.PS-02 (software maintained; vuln scanning) | 3.11.1 | Risk Assessment | Periodic risk assessment; 3.11.2/3.11.3 (scan + remediate) secondary |
| PR.IR-01 (networks protected) | 3.13.1 | System & Communications Protection | "Monitor, control, and protect communications at the external boundaries and key internal boundaries" — the IT/OT segmentation gap |
| DE.CM-01 (networks monitored) | 3.14.6 | System & Information Integrity | "Monitor organizational systems, including inbound and outbound communications traffic, to detect attacks" |
| RS.MA-01 / RS.AN-03 / RS.CO-02 | 3.6.1 / 3.6.1 / 3.6.2 | Incident Response | 3.6.1 = handling capability incl. detection/analysis/containment/recovery; 3.6.2 = "Track, document, and report incidents to designated officials and/or authorities" |
| RC.RP-01 / RC.RP-03 (recovery) | 3.8.9 | Media Protection | **Honesty note:** 800-171 Rev 2 has NO contingency-planning family. 3.8.9 (protect backup CUI) is the nearest hook; recovery planning is largely OUTSIDE the CMMC L2 control set — plan it anyway (CSF demands it), but don't claim a Rev 2 control covers it |

## §4 CMMC L2 readiness scorecard (the 4 targeted families)

Apex targets 4 of the 14 Rev 2 families first. Verified Rev 2 family sizes cap the counts (AC=22, I&A=11, CM=9, IR=3):

| family | controls in family (Rev 2) | assessed so far | satisfied | gap |
|--------|---------------------------|-----------------|-----------|-----|
| Access Control | 22 | 8 | 4 | 4 |
| Identification & Authentication | 11 | 6 | 3 | 3 |
| Configuration Management | 9 | 9 | 5 | 4 |
| Incident Response | 3 | 3 | 1 | 2 |

The crosswalk in §3 also touches SC, SI, AU, RA, and MP controls — those families enter the wave-2 assessment (months 7-12). All 14 families are in scope for the C3PAO assessment; the 4-family focus is sequencing, not scoping.

## §5 The 12-month readiness roadmap

| deliverable | months | FTE | cost | notes |
|------------|--------|-----|------|-------|
| Affirming Official designation + governance charter | 1 | 0.25 | $5K | 32 CFR 170 affirmation duties; False Claims Act exposure — counsel review |
| 800-171 **Rev 2** self-assessment (110 requirements, per 800-171A objectives) | 1-3 | 0.75 | $35K | Output: 110-row SSP with per-control status |
| POA&M creation + resource allocation | 3-4 | 0.5 | $15K | The 14 §2 Subcategories are the top POA&M items |
| C3PAO pre-assessment (advisory) | 4-6 | 0.25 | $50K | Validates the self-assessment |
| Gap remediation (4 priority families + OT compensating controls) | 4-10 | 1.5 | $150-250K | OT MFA per IEC 62443 compensating-control pattern; segmentation; IR plan + tabletop; baselines; scanning |
| Evidence compilation + formal C3PAO scheduling | 10-12 | 0.5 | $25K | Certification assessment (~$75-120K) lands after month 12 |

Total 12-month readiness: ~$280-380K (excl. the certification assessment) — within the typical mid-market CMMC L2 range per `industries/manufacturing.md` (practitioner heuristic).

## §6 Anti-hallucination

- **Apex Manufacturing is a fictional archetype**; the seed is the tested fixture (an earlier version of this UC described a different company with a different gap list — they now match).
- **CMMC L2 = 800-171 Rev 2** (110 requirements, 14 families, `3.x.y` IDs) per 32 CFR 170.14(c)(3), assessed under 800-171A. Rev 3 (`03.xx.yy`, 97 requirements, 17 families) is NOT the CMMC L2 set; track DoD rulemaking before switching revisions.
- **The NIST IR spreadsheet's 800-171 column maps to Rev 3** — useful orientation, but translate to Rev 2 for CMMC work; this UC's mappings are grounded in verified Rev 2 requirement texts and must be re-verified against the SSP scoping for a real engagement.
- **Recovery planning is largely outside Rev 2's scope** (no CP family) — do not fabricate a control hook; plan recovery because CSF (and operational reality) demands it.
- **CMMC Levels are not CSF Tiers** — independent constructs on different axes; do not equate them.
- **The affirming official's SPRS affirmation carries False Claims Act exposure** (31 U.S.C. 3729-3733) — this UC is not legal advice.
