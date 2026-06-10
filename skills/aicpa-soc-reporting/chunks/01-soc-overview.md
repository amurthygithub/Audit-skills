---
chunk_id: 01-soc-overview
parent_skill: aicpa-soc-reporting
topic: "SOC Report Types Overview, Governing Standards, and Key Terminology"
load_when: "user asks about SOC report types, SOC 1/2/3 differences, governing standards (AT-C, SSAE 21), or key AICPA terminology"
---

# Chunk 01 -- SOC Overview: Types, Standards, Terminology

## SOC Report Types -- Audience and Distribution Matrix

| Report | Standard Basis | Subject Matter | Audience | Distribution | Engagement Level |
|--------|---------------|----------------|----------|--------------|-----------------|
| SOC 1 | AT-C 320 (SSAE 18, as amended) | Controls relevant to user entities' ICFR | User entities, user auditors | Restricted | Examination (AT-C 205) |
| SOC 2 | AT-C 105/205 + TSP Section 100 | Controls relevant to Security, Availability, Processing Integrity, Confidentiality, Privacy | Knowledgeable users (customers, regulators) | Restricted | Examination (AT-C 205) |
| SOC 3 | AT-C 105/205 + TSP Section 100 | Same TSC categories as SOC 2 but summarized | General public | Unrestricted | Examination (AT-C 205) |
| SOC for Cybersecurity | AT-C 105/205 + Cybersecurity Description Criteria | Entity's cybersecurity risk management program and controls | General use | Unrestricted | Examination (AT-C 205) |
| SOC for Supply Chain | AT-C 105/205 + TSP Section 100 (adapted) | Controls in production/manufacturing/distribution systems | User entities, supply chain participants | Restricted | Examination (AT-C 205) |

When a user describes a service organization scenario, use the Engagement Classification Engine (see chunk 02) to determine which SOC type applies. Always confirm the distribution requirement before recommending a SOC type.

## Governing Standards

| Standard | Citation | Scope | Key Provisions |
|----------|----------|-------|----------------|
| SSAE No. 18 | AT-C codification | Attestation Standards: Clarification and Recodification — remains current AS AMENDED by SSAE 19-22 | The codification all SOC engagements operate under |
| AT-C 105 | Concepts Common to All Attestation Engagements | Definitions, roles, ethics, independence (SSAE 18, amended by 19/21) | Foundational for all AT-C sections |
| AT-C 205 | Assertion-Based Examination Engagements (renamed by SSAE 21) | Reasonable assurance, opinion on subject matter | Governs SOC 2, SOC 3, SOC for Cybersecurity, SOC for Supply Chain |
| AT-C 206 | Direct Examination Engagements (NEW in SSAE 21, eff. June 15 2022) | Direct opinion without an assertion | Not used for classic SOC reports |
| AT-C 210 | Review Engagements (SSAE 22) | Limited assurance, conclusion on subject matter | Not typically used for SOC |
| AT-C 215 | Agreed-Upon Procedures Engagements (SSAE 19) | No opinion; findings against specified procedures | Used when user entities specify particular procedures |
| AT-C 320 | Examination of Controls at a Service Organization Relevant to User Entities' ICFR (SSAE 18) | SOC 1 Type I/Type II | Governs SOC 1; addresses subservice orgs, CUECs, CSOCs |
| TSP Section 100 | Trust Services Criteria (2017 TSC, Revised PoF 2022) | 61 criteria (33 CC + 28 category-specific), ~200 points of focus | Defines all TSC |

SSAE 18 remains the AT-C codification, as amended (SSAE 21 did NOT supersede it; SSAE 21 added AT-C 206 and renamed AT-C 205, effective for reports dated on or after June 15, 2022). "AT-C 100/200/300" are series GROUPINGS, never citable sections.

Always cite the governing standard when drafting report language. SOC 1 -> cite AT-C 320. SOC 2/SOC 3 -> cite AT-C 105 + AT-C 205 and TSP Section 100. SOC for Cybersecurity -> cite AT-C 105 + AT-C 205 and the Cybersecurity Description Criteria. SOC for Supply Chain -> cite AT-C 105 + AT-C 205 and adapted TSP Section 100.

## Key Terminology

| # | Term | Definition |
|---|------|-----------|
| 1 | ASEC | Assurance Services Executive Committee -- AICPA committee that develops TSC |
| 2 | Attestation Engagement | An engagement under AT-C where a CPA reports on a subject matter or assertion |
| 3 | Bridge Letter | Management letter covering the gap between SOC report period end and next report issuance |
| 4 | Carve-out Method | Method where subservice activities are disclosed but subservice controls are not tested |
| 5 | Common Criteria (CC) | The 33 baseline criteria (CC1.1-CC9.2) required for all SOC 2/SOC 3 engagements |
| 6 | CSOCs | Complementary Subservice Organization Controls -- assumed to be operating effectively under carve-out |
| 7 | CUECs | Complementary User Entity Controls -- controls user entities must implement |
| 8 | Control Objective | Desired outcome of a control (SOC 1). Management-defined; not standardized. Differs from SOC 2 TSC |
| 9 | COSO | Committee of Sponsoring Organizations -- Internal Control Integrated Framework (17 principles) |
| 10 | Description Criteria | 2018 SOC 2 Description Criteria -- criteria for describing the system |
| 11 | Exception | A deviation or failure in the design or operating effectiveness of a control |
| 12 | Inclusive Method | Subservice organization controls are included in scope and tested directly |
| 13 | ISAE 3000/3402 | International equivalents: ISAE 3402 maps to SOC 1 (ICFR); ISAE 3000 maps to SOC 2 |
| 14 | Management Assertion | Written statement by management about fairness of description and control effectiveness |
| 15 | Material Weakness | A deficiency resulting in reasonable possibility of material misstatement |
| 16 | Points of Focus | Implementation guidance for each TSC criterion describing how it may be met |
| 17 | Practitioner | The CPA performing the SOC engagement (also: service auditor) |
| 18 | Qualified Opinion | Opinion stating exceptions exist but are limited to specific matters |
| 19 | Responsible Party | The party responsible for the subject matter (also: management, service organization) |
| 20 | Restricted Use Report | SOC 1/SOC 2 reports intended for specified users only |
| 21 | SAS 70 | Superseded predecessor to SSAE 16/18 (no longer valid since June 2011) -- do not reference |
| 22 | Service Auditor | The CPA performing the SOC examination |
| 23 | Service Organization | The entity providing services to user entities whose controls are being examined |
| 24 | Subservice Organization | A second-tier service organization used by the primary service org (e.g., IaaS provider) |
| 25 | TSC | Trust Services Criteria -- Security, Availability, Processing Integrity, Confidentiality, Privacy |
| 26 | TSP Section 100 | Trust Services Principles and Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (2017 TSC, revised 2022) |
| 27 | Type I | Report on design suitability of controls as of a point in time |
| 28 | Type II | Report on design suitability and operating effectiveness over a period of time |
| 29 | Unqualified Opinion | Clean opinion -- no exceptions; controls suitably designed and operating effectively |
| 30 | User Auditor | The CPA auditing the user entity's financial statements |
| 31 | User Entity | The entity that uses the service organization's services |
| 32 | SOC | System and Organization Controls -- the AICPA suite of service organization reporting |
| 33 | SSAE 16 | Superseded predecessor to SSAE 21 (no longer valid since May 2017) -- do not reference |
| 34 | SSAE 21 | Statement on Standards for Attestation Engagements No. 21 -- current governing standard |

Use these terms precisely. Never use "SAS 70" or "SSAE 16" in reference to current engagements. Always distinguish "service auditor" (CPA practitioner) from "user auditor" (CPA auditing user entity financials). Use "Trust Services Criteria" not "Trust Services Principles" for current engagements. Use "management assertion" not "representation letter."

## Citations in this chunk

- [AT-C-105] -- foundational definitions
- [AT-C-205] -- examination engagements
- [AT-C-320] -- SOC 1
- [TSP-Section-100] -- trust services criteria
- [SSAE-21] -- current governing standard (superseded SSAE 18)

See SKILL.md Section 10 for the full citation manifest.
