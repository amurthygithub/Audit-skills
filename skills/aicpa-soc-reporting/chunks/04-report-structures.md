---
chunk_id: 04-report-structures
parent_skill: aicpa-soc-reporting
topic: "SOC 1, SOC 2, SOC 3, SOC for Cybersecurity, and SOC for Supply Chain Report Structure Templates"
load_when: "user needs to draft a SOC report, asks about SOC 1/2/3 report structure, or needs report section templates"
---

# Chunk 04 -- Report Structure Templates

## SOC 1 Report Structure

SOC 1 control objectives are management-defined, not standardized. Unlike SOC 2 TSC, there are no prescribed criteria. The service organization defines its own control objectives based on the services provided and their ICFR relevance.

### SOC 1 Type I
Section I -- Independent Service Auditor's Opinion:
- Scope paragraph describing system and design suitability.
- Management's responsibility paragraph.
- Practitioner's responsibility paragraph.
- Opinion paragraph (Unqualified / Qualified / Adverse / Disclaimer).
- Restricted use paragraph: intended solely for specified parties.

Section II -- Description of the System:
- System overview and boundaries.
- Principal service commitments and system requirements.
- Management-defined control objectives and related controls.
- CUECs (per chunk 06).
- CSOCs if carve-out method (per chunk 06).

Section III -- Management's Written Assertion (2-paragraph Type I format, per chunk 05).

### SOC 1 Type II
Same as Type I, plus:
- Operating effectiveness language in Scope and Opinion paragraphs.
- Section IV -- Tests of Controls and Results: for each control objective, list control description, test procedures, sample size, test results, and exceptions with nature/cause/effect.

## SOC 2 Report Structure

### SOC 2 Type I
Section I -- Opinion:
- Scope: "We have examined [Org]'s description of its [System] and the suitability of the design of controls relevant to Security, [Availability, Processing Integrity, Confidentiality, and/or Privacy] as of [Date] based on TSP Section 100."
- Opinion on: (a) fair presentation of description, (b) suitable design of controls.
- Restricted use paragraph.

Section II -- Description of the System:
- System overview, boundaries, how system achieves TSC.
- Specified controls mapped to each criterion.
- CUECs, CSOCs, subservice disclosures.

Section III -- Management's Written Assertion (2-paragraph Type I format).

### SOC 2 Type II
Same as Type I plus:
- Operating effectiveness language.
- Section IV -- Tests of Controls and Results: organized by TSC category. For each criterion: criterion reference, control description, test of design, test of operating effectiveness, sample size, results, exceptions.

## SOC 3 Report Structure

Abbreviated SOC 2 for general-public distribution:
- Opinion paragraph (abbreviated, same opinion structure).
- Summary description of system (high-level, no detailed boundaries).
- Management's assertion (abbreviated).
- NO detailed tests of controls and results.
- NO detailed CUECs or CSOCs.
- NO restricted use paragraph (general use permitted).

Most SOC 3 reports are Type II. Type I SOC 3 is permitted (point in time, design only) but rare.

## SOC for Cybersecurity Report Structure

Entity-level cybersecurity risk management program:
- Management's description: how entity identifies information assets and cybersecurity risks, key policies/processes/controls, governance structure, risk communication.
- Criteria: Description Criteria + TSC (Security + Availability + Confidentiality). Privacy and Processing Integrity optional.
- General use (unrestricted), unlike SOC 2.
- Scope is entity-level, not system-specific.

## SOC for Supply Chain Report Structure

For entities that manufacture, produce, or distribute products:
- Focuses on product/service integrity through the supply chain.
- Uses adapted TSP Section 100.
- Restricted distribution.
- Parallel structure to SOC 2 but with supply-chain-focused description.

## Report Validation Checklist (17 items)

Before finalizing any SOC report, verify:
1. Title includes "Independent"
2. Addressee specified
3. Engagement scope clearly described
4. Criteria referenced (AT-C 200, TSP Section 100, etc.)
5. Report period/dates specified
6. Management's responsibility paragraph
7. Practitioner's responsibility paragraph
8. Opinion paragraph with clear opinion type
9. System description covers required elements
10. CUECs identified and disclosed
11. CSOCs identified (carve-out method)
12. Management's written assertion (signed, dated)
13. Tests of controls section (Type II only)
14. For Type II: each control tested, sample size, results
15. Restricted use paragraph (SOC 1, SOC 2, SOC for Supply Chain)
16. NO restricted use paragraph (SOC 3, SOC for Cybersecurity)
17. Practitioner signature, date, location

## Citations
- [AT-C-200] [AT-C-300] [TSP-Section-100] [SOC-for-Cybersecurity] [SOC-for-Supply-Chain]
See SKILL.md Section 10.
