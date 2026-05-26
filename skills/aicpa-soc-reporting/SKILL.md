---
name: aicpa-soc-reporting
description: "Instructs the AI agent to perform AICPA System and Organization Controls (SOC) reporting work including SOC 1, SOC 2, SOC 3, SOC for Cybersecurity, and SOC for Supply Chain engagements. Activates when the user asks about SOC reports, SOC 1/SOC 2/SOC 3 examinations, trust services criteria (TSC), TSP Section 100, control objectives, management assertions, service auditor opinions, CUECs, CSOCs, bridge letters, readiness assessments, Type I vs Type II reports, AT-C 105/205/210/215/320 standards, SSAE 18, or any AICPA attestation engagement at a service organization."
category: audit
risk: high
source: "AICPA Professional Standards (AT-C 105/205/210/215/320, TSP Section 100, SSAE No. 18, 2022 Revised Implementation Guidance)"
date_added: "2026-05-25"
tags:
  - aicpa
  - soc1
  - soc2
  - soc3
  - soc-for-cybersecurity
  - soc-for-supply-chain
  - attestation
  - trust-services-criteria
  - tsp-section-100
  - ssae-18
  - at-c-105
  - at-c-205
  - at-c-210
  - at-c-215
  - at-c-320
  - coso
  - icfr
  - management-assertion
  - cuec
  - csoc
  - bridge-letter
  - service-auditor
  - control-objectives
  - type-i
  - type-ii
---

# AICPA SOC Reporting — Agent Skill

## 1. When to Use This Skill

### Activate When
- User asks about SOC 1, SOC 2, SOC 3, SOC for Cybersecurity, or SOC for Supply Chain engagements
- User needs to scope, draft, review, or validate a SOC report or any component therein
- User inquires about trust services criteria (TSC), TSP Section 100, or specific criteria codes (CC*, A*, PI*, C*, P*)
- User requests management assertion letters, bridge letters, CUECs, or CSOCs
- User asks about AT-C 105/205/210/215/320, SSAE 18, or AICPA attestation standards
- User needs to determine which SOC type applies to a given scenario
- User requires cross-framework mapping (COSO, ISO 27001, NIST 800-53, GDPR) for SOC criteria
- User asks about service auditor opinion types or exception evaluation
- User needs sampling guidance for Type II testing

### Do NOT Use When
- User is asking about financial statement audits (that is GAAS/PCAOB territory, not SOC attestation)
- User needs ISO 27001 certification guidance alone (without SOC overlap)
- User is performing a SOC for SOX (that is PCAOB AS 2201, not AICPA SOC)
- User asks about ISAE 3000/3402 exclusively (international standard — unless comparing to AICPA SOC)
- User needs Penetration Testing or Vulnerability Assessment alone (not an attestation engagement)
- User is asking about internal audit methodology unrelated to service organization controls

---

## 2. SOC Report Types Overview

### Audience and Distribution Matrix

| Report | Standard Basis | Subject Matter | Audience | Distribution | Engagement Level |
|---|---|---|---|---|---|
| **SOC 1** | AT-C 320 (SSAE 18) | Controls relevant to user entities' ICFR | User entities, user auditors | Restricted | Examination (AT-C 205) |
| **SOC 2** | AT-C 205 + TSP Section 100 | Controls relevant to Security, Availability, Processing Integrity, Confidentiality, Privacy | Knowledgeable users (customers, regulators) | Restricted | Examination (AT-C 205) |
| **SOC 3** | AT-C 205 + TSP Section 100 | Same TSC categories as SOC 2 but summarized | General public | Unrestricted | Examination (AT-C 205) |
| **SOC for Cybersecurity** | AT-C 205 + Cybersecurity Description Criteria | Entity's cybersecurity risk management program and controls | General use | Unrestricted | Examination (AT-C 205) |
| **SOC for Supply Chain** | AT-C 205 + TSP Section 100 (adapted) | Controls in production/manufacturing/distribution systems | User entities, supply chain participants | Restricted | Examination (AT-C 205) |

**Agent Action:** When a user describes a service organization scenario, use the Engagement Classification Engine (Section 5) to determine which SOC type applies. Always confirm the distribution requirement (restricted vs. general use) before recommending a SOC type.

---

## 3. Governing Standards

| Standard | Citation | Scope | Key Provisions |
|---|---|---|---|
| **SSAE No. 18** | AT-C 105, 205, 210, 215, 320 | Supersedes SAS 70 and SSAE 16; effective May 1, 2017 | Governs all attestation engagements including SOC |
| **AT-C 105** | Concepts Common to All Attestation Engagements | Definitions, roles, ethics, independence | Foundational definitions for all AT-C sections |
| **AT-C 205** | Examination Engagements | Reasonable assurance, opinion on subject matter | Governs SOC 2, SOC 3, SOC for Cybersecurity, SOC for Supply Chain |
| **AT-C 210** | Review Engagements | Limited assurance, conclusion on subject matter | Not typically used for SOC; limited assurance engagements |
| **AT-C 215** | Agreed-Upon Procedures Engagements | No opinion; findings against specified procedures | Used when user entities specify particular procedures |
| **AT-C 320** | Service Organizations — ICFR | SOC 1 Type I/Type II specific | Governs SOC 1; addresses subservice orgs, CUECs, CSOCs |
| **TSP Section 100** | Trust Services Criteria (2017 TSC, Revised 2022) | 64 criteria for SOC 2/SOC 3 | Defines all TSC; revised implementation guidance issued 2022 |

**SSAE Amendment Note:** SSAE 18 remains the governing standard; SSAE Nos. 19–22 have been issued as amendments to specific AT-C sections (conforming amendments). Practitioners should verify the current text of the relevant AT-C section to ensure any SSAE 19–22 amendments are reflected.

**Agent Action:** Always cite the governing standard when drafting report language. SOC 1 → cite AT-C 320. SOC 2/SOC 3 → cite AT-C 205 and TSP Section 100. SOC for Cybersecurity → cite AT-C 205 and Cybersecurity Description Criteria. SOC for Supply Chain → cite AT-C 205 and adapted TSP Section 100.

---

## 4. Key Terminology

| # | Term | Definition |
|---|---|---|
| 1 | **ASEC** | Assurance Services Executive Committee — AICPA committee that develops TSC |
| 2 | **Attestation Engagement** | An engagement under AT-C where a CPA reports on a subject matter or assertion |
| 3 | **Bridge Letter** | Management letter covering the gap between SOC report period end and next report issuance |
| 4 | **Carve-out Method** | Method of presenting subservice organization activities where CSOCs are disclosed but subservice controls are not tested |
| 5 | **Common Criteria (CC)** | The 33 baseline criteria (CC1.1–CC9.2) required for all SOC 2/SOC 3 engagements |
| 6 | **Complementary Subservice Organization Controls (CSOCs)** | Controls at a subservice organization assumed to be operating effectively under the carve-out method |
| 7 | **Complementary User Entity Controls (CUECs)** | Controls user entities must implement for service organization controls to achieve their objectives |
| 8 | **Control Objective** | A statement of the desired outcome of a control (SOC 1). **Note:** SOC 1 control objectives are management-defined and not standardized; they differ from SOC 2 Trust Services Criteria, which are codified in TSP Section 100. |
| 9 | **COSO** | Committee of Sponsoring Organizations of the Treadway Commission — Internal Control – Integrated Framework (17 principles) |
| 10 | **Description Criteria** | 2018 SOC 2 Description Criteria — criteria for describing the system |
| 11 | **Engaging Party** | The entity that engages the CPA to perform the attestation engagement |
| 12 | **Exception** | A deviation or failure in the design or operating effectiveness of a control |
| 13 | **Examination Engagement** | Attestation service level providing reasonable assurance and an opinion (AT-C 205) |
| 14 | **GAPP** | Generally Accepted Privacy Principles — AICPA privacy framework |
| 15 | **ICFR** | Internal Control Over Financial Reporting |
| 16 | **Inclusive Method** | Method where subservice organization controls are included in scope and tested directly |
| 17 | **ISAE 3000/3402** | International equivalents of SSAE 18/AT-C 320 for non-US jurisdictions |
| 18 | **Key Control** | A control whose failure could materially affect the achievement of a control objective |
| 19 | **Management's Assertion** | Written statement by management about the fairness of the description and control effectiveness |
| 20 | **Material Weakness** | A deficiency or combination of deficiencies resulting in reasonable possibility of material misstatement |
| 21 | **Monitoring Activities** | Ongoing evaluations, separate evaluations, or some combination of the two |
| 22 | **Other Practitioner** | A CPA engaged by the primary practitioner to test controls at a subservice organization |
| 23 | **PII** | Personally Identifiable Information |
| 24 | **Points of Focus** | Implementation guidance for each TSC criterion describing how the criterion may be met |
| 25 | **Practitioner** | The CPA performing the SOC engagement (also: service auditor) |
| 26 | **Qualified Opinion** | Opinion stating exceptions exist but are limited to specific matters |
| 27 | **Responsible Party** | The party responsible for the subject matter (also: management, service organization) |
| 28 | **Restricted Use Report** | SOC 1/SOC 2 reports intended for specified users only |
| 29 | **Review Engagement** | Attestation service level providing limited assurance and a conclusion (AT-C 210) |
| 30 | **Risk Assessment** | Entity's process for identifying and analyzing risks relevant to the achievement of objectives |
| 31 | **SAS 70** | Superseded predecessor to SSAE 16/18 (no longer valid since June 2011) — do not reference in current engagements |
| 32 | **Service Auditor** | The CPA performing the SOC examination |
| 33 | **Service Organization** | The entity providing services to user entities whose controls are being examined |
| 34 | **Subservice Organization** | A second-tier service organization used by the primary service organization (e.g., IaaS provider used by a SaaS vendor) |
| 35 | **Trust Service Categories (TSC)** | Security, Availability, Processing Integrity, Confidentiality, Privacy — the five TSP Section 100 categories |
| 36 | **Trust Services Criteria** | The codified criteria in TSP Section 100 for SOC 2/SOC 3 engagements (not "Principles" — the term "Principles" was used in the superseded 2011 TSP; current terminology is "Criteria") |
| 37 | **TSP Section 100** | Trust Services Principles and Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy (2017 TSC, revised 2022) |
| 38 | **Type I** | Report on design suitability of controls as of a point in time |
| 39 | **Type II** | Report on design suitability and operating effectiveness over a period of time |
| 40 | **Unqualified Opinion** | Clean opinion — no exceptions; controls are suitably designed and operating effectively |
| 41 | **User Auditor** | The CPA auditing the user entity's financial statements |
| 42 | **User Entity** | The entity that uses the service organization's services |
| 43 | **Vendor Risk Management** | Process for evaluating and monitoring third-party service provider risks |
| 44 | **SOC** | System and Organization Controls — the AICPA suite of service organization reporting |
| 45 | **SSAE 16** | Superseded predecessor to SSAE 18 (no longer valid since May 2017) — do not reference in current reports |
| 46 | **SSAE 18** | Statement on Standards for Attestation Engagements No. 18 — current governing standard |

**Agent Action:** Use these terms precisely. Never use "SAS 70" or "SSAE 16" in reference to current engagements. Always distinguish between "service auditor" (CPA practitioner) and "user auditor" (CPA auditing user entity financials). Use "Trust Services Criteria" not "Trust Services Principles" for current engagements. Use "management assertion" not "representation letter." Use "Complementary User Entity Controls (CUECs)" and "Complementary Subservice Organization Controls (CSOCs)" — always spell out on first use.

---

## 5. Engagement Type Decision Tree

**When a user describes a service organization, execute this decision logic to classify the engagement:**

```
STEP 1: Is the subject matter related to Internal Control Over Financial Reporting (ICFR)?
  → YES: SOC 1 (governed by AT-C 320)
    → Ask: Does the user entity's financial statement auditor need this for their audit?
      → YES: SOC 1 is the correct choice
      → NO: Consider whether TSC criteria are more relevant; go to Step 2
  → NO: Proceed to Step 2

STEP 2: Are Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy) the subject matter?
  → YES: Ask about distribution requirements
    → Is restricted distribution acceptable (report shared only with knowledgeable parties under NDA)?
      → YES: SOC 2 (governed by AT-C 205 + TSP Section 100)
      → NO: SOC 3 (governed by AT-C 205 + TSP Section 100, general use)
    → REMINDER: Security criterion is ALWAYS in scope for SOC 2/SOC 3; A, PI, C, P are optional add-ons
  → NO: Proceed to Step 3

STEP 3: Is the subject matter an entity's cybersecurity risk management program?
  → YES: SOC for Cybersecurity (governed by AT-C 205 + Cybersecurity Description Criteria)
    → Distinguish: This covers the ENTIRE entity's cybersecurity program, not just a specific system
    → Determine Type I (point in time) or Type II (period of time)
  → NO: Proceed to Step 4

STEP 4: Is the subject matter a production, manufacturing, or distribution system?
  → YES: SOC for Supply Chain (governed by AT-C 205 + adapted TSP Section 100)
    → Applies to entities that manufacture, produce, or distribute physical or digital products
    → Uses adapted TSP Section 100 criteria with supply-chain-specific context
  → NO: This may not be a SOC engagement. Consider:
    → AT-C 205 for a custom examination engagement
    → AT-C 210 for a review engagement (limited assurance)
    → AT-C 215 for an agreed-upon procedures engagement
    → Advise the user to consult with a licensed CPA practitioner
```

**Agent Action:** Always walk through all steps before concluding. Never skip to a SOC type without confirming the subject matter and distribution requirements. If the scenario does not fit any SOC type, explicitly state that and recommend alternative engagement types.

---

## 6. Report Type Decision — Type I vs Type II

```
STEP 1: Does the user entity need assurance on operating effectiveness (not just design)?
  → YES: Type II is required
    → Determine examination period:
      → <6 months: Advise the user that 6 months is the typical minimum; consider extending or starting with Type I
      → 6–12 months: Standard Type II period (12 months is most common)
      → >12 months: Rare; discuss with the practitioner whether a shorter period is more appropriate
  → NO: Type I may be sufficient
    → Proceed to Step 2

STEP 2: Is this a first-time SOC engagement for the service organization?
  → YES: Recommend Type I first as a readiness assessment to identify and remediate gaps before committing to a Type II period
  → NO: Type II is standard practice for established SOC programs

STEP 3: What is the user entity requesting?
  → Only design assurance → Type I
  → Design + operating effectiveness assurance → Type II
  → Not sure → Default recommendation: Type II (it is the most commonly requested and provides the highest value)

STEP 4: Confirm selection and provide the distinction:
  Type I:
    - Point in time (as of a specific date)
    - Tests design suitability only
    - No Section IV (Tests of Controls and Results)
    - Often used as readiness precursor
  Type II:
    - Period of time (typically 6–12 months)
    - Tests design suitability AND operating effectiveness
    - Includes Section IV with detailed test procedures, samples, and results
    - Most requested report type by customers
```

**Agent Action:** Always confirm the report type before beginning any drafting. If the user is unsure, recommend Type II as default for established programs and Type I as a readiness step for first-time engagements.

---

## 7. TSP Section 100 Criteria (51 Primary, ~64 with Sub-Criteria)

### 7.1 Common Criteria (CC) — 33 Criteria — REQUIRED for All SOC 2/SOC 3

**Agent Action:** These 33 Common Criteria are ALWAYS in scope for every SOC 2 and SOC 3 engagement. You must address every CC criterion regardless of which additional TSC categories are selected.

#### CC1 — Control Environment (COSO Principles 1–5)

| Code | COSO Principle | Description | Agent Directive |
|---|---|---|---|
| **CC1.1** | Principle 1 | The entity demonstrates commitment to integrity and ethical values | Evaluate tone at the top, code of conduct, ethicalValues enforcement mechanisms |
| **CC1.2** | Principle 5 | The entity holds individuals accountable for their internal control responsibilities | Assess accountability structures, performance reviews, disciplinary processes |
| **CC1.3** | Principle 3 | The entity specifies competence requirements for personnel | Review hiring criteria, training programs, skill assessments for control-relevant roles |
| **CC1.4** | Principle 4 | The entity demonstrates commitment to competence | Evaluate whether management provides resources for training and development |
| **CC1.5** | Principle 2 | The entity oversees internal control responsibilities | Assess board/management oversight structures, audit committees, governance |

**Important — COSO Principle Mapping for CC1 Is Non-Sequential:** CC1.1 → Principle 1 (integrity/ethics), CC1.2 → Principle 5 (accountability), CC1.3 → Principle 3 (competence requirements), CC1.4 → Principle 4 (commitment to competence), CC1.5 → Principle 2 (oversight). The TSC criteria under CC1 do not follow a sequential 1:1 mapping to COSO Principles 1–5.

#### CC2 — Communication and Information (COSO Principles 13–15)

| Code | COSO Principle | Description | Agent Directive |
|---|---|---|---|
| **CC2.1** | Principle 13 | The entity obtains or generates and uses relevant, quality information | Evaluate information quality, data governance, reporting systems |
| **CC2.2** | Principle 14 | The entity internally communicates information necessary to support internal control | Review internal communication channels, policy distribution, escalation procedures |
| **CC2.3** | Principle 15 | The entity communicates with external parties regarding matters affecting internal control | Assess external reporting, vendor communications, regulatory notifications |

#### CC3 — Risk Assessment (COSO Principles 6–9)

| Code | COSO Principle | Description | Agent Directive |
|---|---|---|---|
| **CC3.1** | Principle 6 | The entity specifies objectives with sufficient clarity | Evaluate whether control objectives and TSC criteria are clearly defined |
| **CC3.2** | Principle 7 | The entity identifies and analyzes risk | Review risk assessment methodology, threat modeling, risk register |
| **CC3.3** | Principle 8 | The entity assesses fraud risk | Analyze fraud risk factors, management override controls, segregation of duties |
| **CC3.4** | Principle 9 | The entity identifies and analyzes significant changes | Evaluate change management impact on risk, monitoring of environmental shifts |

#### CC4 — Monitoring Activities (COSO Principles 16–17)

| Code | COSO Principle | Description | Agent Directive |
|---|---|---|---|
| **CC4.1** | Principle 16 | The entity conducts ongoing and/or periodic evaluations | Review monitoring program, internal audit schedule, continuous monitoring tools |
| **CC4.2** | Principle 17 | The entity evaluates and communicates deficiencies | Assess deficiency reporting, escalation, remediation tracking, management communication |

#### CC5 — Control Activities (COSO Principles 10–12)

| Code | COSO Principle | Description | Agent Directive |
|---|---|---|---|
| **CC5.1** | Principle 10 | The entity selects and develops control activities | Evaluate control selection logic, risk-to-control mapping, coverage analysis |
| **CC5.2** | Principle 11 | The entity deploys through policies and procedures | Review policy framework, procedure documentation, implementation evidence |
| **CC5.3** | Principle 12 | The entity deploys controls through technology | Assess automated controls, system-enforced controls, technology-dependent controls |

#### CC6 — Supplemental: Logical and Physical Access

| Code | Description | Agent Directive |
|---|---|---|
| **CC6.1** | The entity implements logical access security over IT resources | Review access control policies, authentication mechanisms, IAM systems |
| **CC6.2** | The entity registers and authorizes new users | Assess user provisioning processes, approval workflows, role-based access |
| **CC6.3** | The entity terminates access for terminated/transferred users | Evaluate deprovisioning processes, timely removal, access reviews |
| **CC6.4** | The entity reviews access to protected information | Analyze periodic access reviews, recertification processes, least privilege enforcement |
| **CC6.5** | The entity implements physical access controls | Review data center security, badge access, visitor management, environmental controls |
| **CC6.6** | The entity implements logical access security measures to protect against threats | Assess encryption, network segmentation, intrusion detection/prevention, MFA |

#### CC7 — Supplemental: System Operations

| Code | Description | Agent Directive |
|---|---|---|
| **CC7.1** | The entity manages IT infrastructure | Review infrastructure management, capacity planning, patch management |
| **CC7.2** | The entity manages system job processing | Evaluate job scheduling, batch processing controls, error handling |
| **CC7.3** | The entity detects and handles incidents | Assess incident response plan, detection tools, escalation procedures |
| **CC7.4** | The entity recovers IT infrastructure and data | Review backup procedures, recovery testing, RTO/RPO validation |
| **CC7.5** | The entity uses a defined process for recovery of IT operations | Evaluate disaster recovery plans, BCP testing, failover procedures |

#### CC8 — Supplemental: Change Management

| Code | Description | Agent Directive |
|---|---|---|
| **CC8.1** | The entity authorizes changes to the system | Review change approval processes, CAB reviews, emergency change procedures |
| **CC8.2** | The entity develops, tests, and implements changes | Assess SDLC/DevSecOps practices, testing protocols, deployment procedures |
| **CC8.3** | The entity configures and manages boundaries of changes | Evaluate change scope control, rollback procedures, environment segregation |

#### CC9 — Supplemental: Risk Mitigation

| Code | Description | Agent Directive |
|---|---|---|
| **CC9.1** | The entity mitigates technology risks | Review technology risk management, vulnerability management, penetration testing |
| **CC9.2** | The entity manages vendor and supply chain risk | Assess vendor risk management program, third-party assessments, contract security requirements |

### 7.2 Additional Availability Criteria (A) — 3 Criteria

| Code | Description | Agent Directive | Applies To |
|---|---|---|---|
| **A1.1** | The entity maintains system availability and backup controls | Review SLA commitments, uptime metrics, redundancy architecture | Availability |
| **A1.2** | The entity operates disaster recovery and business continuity plans | Assess DR/BCP documentation, testing frequency, recovery objectives | Availability |
| **A1.3** | The entity implements environmental protections | Review environmental controls (power, cooling, fire suppression) | Availability |

**Agent Action:** Include Availability criteria ONLY when the user has selected the Availability trust service category. Security (CC) is always included as the baseline.

### 7.3 Additional Processing Integrity Criteria (PI) — 5 Criteria

| Code | Description | Agent Directive | Applies To |
|---|---|---|---|
| **PI1.1** | The entity processes complete information | Evaluate completeness controls, reconciliations, completeness checks | Processing Integrity |
| **PI1.2** | The entity processes valid information | Assess validity controls, input validation, authorization checks | Processing Integrity |
| **PI1.3** | The entity processes accurate information | Review accuracy controls, data quality checks, edit validations | Processing Integrity |
| **PI1.4** | The entity processes information in a timely manner | Assess timeliness controls, SLA compliance, processing windows | Processing Integrity |
| **PI1.5** | The entity processes information per authorization | Evaluate authorization controls, approval workflows, override tracking | Processing Integrity |

**Agent Action:** Include Processing Integrity criteria ONLY when the user has selected the Processing Integrity trust service category.

### 7.4 Additional Confidentiality Criteria (C) — 2 Criteria

| Code | Description | Agent Directive | Applies To |
|---|---|---|---|
| **C1.1** | The entity identifies and classifies confidential information | Review data classification scheme, labeling procedures, inventory of confidential data | Confidentiality |
| **C1.2** | The entity protects confidential information | Assess encryption at rest/in transit, DLP controls, need-to-know access, NDAs | Confidentiality |

**Agent Action:** Include Confidentiality criteria ONLY when the user has selected the Confidentiality trust service category.

### 7.5 Additional Privacy Criteria (P) — 8 Criteria

| Code | Description | Agent Directive | GDPR Mapping | Applies To |
|---|---|---|---|---|
| **P1.1** | Notice — The entity provides notice about its privacy practices | Review privacy notices, policy disclosure, transparency practices | Art. 13–14 | Privacy |
| **P2.1** | Choice and consent — The entity consents to collection, use, retention, disclosure, disposal of PII | Assess consent mechanisms, opt-in/opt-out, granular consent | Art. 6–7, Art. 9 | Privacy |
| **P3.1** | Collection — The entity collects only PII necessary for stated purposes | Review purpose limitation, data minimization, collection scope | Art. 5(1)(b), Art. 5(1)(c) | Privacy |
| **P4.1** | Use, retention, and disposal — The entity limits use, retention, and disposal per notice and consent | Evaluate retention schedules, disposal procedures, storage limitation | Art. 5(1)(e), Art. 17 | Privacy |
| **P5.1** | Access — The entity provides individuals access to their PII | Review data subject access request process, response timelines | Art. 15 | Privacy |
| **P6.1** | Disclosure and notice — The entity discloses PII only per notice and consent; notifies of changes | Assess third-party disclosure controls, cross-border transfers, change notification | Art. 44–49 | Privacy |
| **P7.1** | Privacy complaints — The entity provides a mechanism for inquiries and complaints | Review complaint handling process, response procedures, DPO access | Art. 77–79 | Privacy |
| **P8.1** | Privacy monitoring — The entity monitors compliance with privacy policies and practices | Assess privacy monitoring program, audits, compliance tracking | Art. 24, Art. 32 | Privacy |

**Agent Action:** Include Privacy criteria ONLY when the user has selected the Privacy trust service category. When Privacy is in scope, also map to GDPR requirements and note overlaps.

### 7.6 Criteria Summary Count

| Category | Code Range | Count | Required? |
|---|---|---|---|
| Common Criteria | CC1.1–CC9.2 | 33 | Always |
| Availability | A1.1–A1.3 | 3 | Optional |
| Processing Integrity | PI1.1–PI1.5 | 5 | Optional |
| Confidentiality | C1.1–C1.2 | 2 | Optional |
| Privacy | P1.1–P8.1 | 8 | Optional |
| **Grand Total** | | **51** | |

*Note: The AICPA commonly references approximately 64 criteria when including refined sub-criteria and 2022 revised implementation guidance expansions with additional points of focus. The exact sub-criteria count varies by publication (61–67 depending on how CC6–CC9 sub-criteria are counted). Agents should verify against the current TSP Section 100 publication. Practitioners must address all applicable points of focus for each criterion category included in scope.*

---

## 8. SOC 1 Report Structure Template

**SOC 1 Control Objectives Note:** SOC 1 control objectives are management-defined and specific to the service organization's ICFR-related controls. Unlike SOC 2, which uses standardized Trust Services Criteria from TSP Section 100, SOC 1 does not have prescribed criteria. The service organization defines its own control objectives based on the services provided to user entities and their ICFR relevance. The service auditor evaluates whether controls are suitably designed (and operating effectively for Type II) to achieve those management-defined objectives.

### 8.1 SOC 1 Type I

```
INDEPENDENT SERVICE AUDITOR'S REPORT ON
[Service Organization Name]'S DESCRIPTION OF ITS
[System Name] SYSTEM AND THE SUITABILITY OF THE DESIGN OF CONTROLS
Relevant to User Entities' Internal Control Over Financial Reporting
As of [Date]

[Addressee]

Section I — Opinion
  Scope paragraph:
    "We have examined [Service Organization Name]'s description of its
    [System Name] system and the suitability of the design of controls
    relevant to user entities' internal control over financial reporting
    as of [Date]."

  Management's responsibility paragraph:
    "Management of [Service Organization Name] is responsible for
    the fairness of the presentation of the description and the
    suitability of the design of controls."

  Practitioner's responsibility paragraph:
    "Our responsibility is to express an opinion on the fairness of
    the presentation of the description and the suitability of the
    design of controls based on our examination."

  Opinion paragraph (select appropriate type per Section 15):
    Unqualified | Qualified | Adverse | Disclaimer

  Other matters/restrictions paragraph:
    "This report is intended solely for the information and use of
    [specified parties] and is not intended to be, and should not be,
    used by anyone other than these specified parties."

Section II — Description of the [System Name] System
  - System overview and boundaries
  - Principal service commitments and system requirements
  - Control objectives and related controls
  - CUECs (per Section 13)
  - CSOCs (if carve-out method; per Section 13)
  - Other relevant information

Section III — Management's Written Assertion
  (Use Type I assertion template from Section 11.1)

[Service Auditor Signature, Firm Name]
[Date]
[City, State]
```

### 8.2 SOC 1 Type II

```
INDEPENDENT SERVICE AUDITOR'S REPORT ON
[Service Organization Name]'S DESCRIPTION OF ITS
[System Name] SYSTEM AND THE SUITABILITY OF THE DESIGN AND
OPERATING EFFECTIVENESS OF CONTROLS
Relevant to User Entities' Internal Control Over Financial Reporting
For the period [Start Date] to [End Date]

[Addressee]

Section I — Opinion
  Same structure as Type I, plus:
  - Operating effectiveness language added to scope and opinion paragraphs
  - "…and the operating effectiveness of controls relevant to user entities'
    internal control over financial reporting throughout the period
    [Start Date] to [End Date]."

Section II — Description of the [System Name] System
  Same as Type I

Section III — Management's Written Assertion
  (Use Type II assertion template from Section 11.2)

Section IV — Tests of Controls and Results
  For each control objective:
    - Control objective statement
    - Specified controls (control description)
    - Test procedures performed by practitioner
    - Sample size (if applicable; per Section 17)
    - Test results (exceptions or "No exceptions noted")
    - For each exception:
      - Nature of the exception
      - Cause of the exception
      - Effect of the exception on the control objective
      - Management's corrective action (if any)

[Service Auditor Signature, Firm Name]
[Date]
[City, State]
```

---

## 9. SOC 2 Report Structure Template

### 9.1 SOC 2 Type I

```
INDEPENDENT SERVICE AUDITOR'S REPORT ON
[Service Organization Name]'S DESCRIPTION OF ITS
[System Name] SYSTEM AND THE SUITABILITY OF THE DESIGN OF CONTROLS
Relevant to Security, Availability, Processing Integrity,
Confidentiality, [and/or] Privacy
Based on the Trust Services Criteria
As of [Date]

[Addressee]

Section I — Opinion
  Scope paragraph:
    "We have examined [Service Organization Name]'s description of its
    [System Name] system and the suitability of the design of controls
    relevant to Security, [Availability, Processing Integrity,
    Confidentiality, and/or Privacy] as of [Date] based on the
    Trust Services Criteria (TSP Section 100)."

  Management's responsibility paragraph
  Practitioner's responsibility paragraph
  Trust Services Criteria reference (TSP Section 100)

  Opinion on:
    a) Whether the description fairly presents the system
    b) Whether controls were suitably designed

  Restricted use paragraph:
    "This report is intended solely for the information and use of
    [specified parties] and is not intended to be, and should not be,
    used by anyone other than these specified parties."

Section II — Description of the [System Name] System
  - System overview
  - Boundaries of the system (what is included/excluded)
  - How the system achieves trust service criteria
  - Specified controls mapped to each criterion
  - CUECs (per Section 13)
  - CSOCs (per Section 13)
  - Subservice organization disclosures (inclusive or carve-out)
  - Material changes (if any up to the as-of date)

Section III — Management's Written Assertion
  (Use Type I assertion template from Section 11.1)

[Service Auditor Signature, Firm Name]
[Date]
[City, State]
```

### 9.2 SOC 2 Type II

```
INDEPENDENT SERVICE AUDITOR'S REPORT ON
[Service Organization Name]'S DESCRIPTION OF ITS
[System Name] SYSTEM AND THE SUITABILITY OF THE DESIGN AND
OPERATING EFFECTIVENESS OF CONTROLS
Relevant to Security, Availability, Processing Integrity,
Confidentiality, [and/or] Privacy
Based on the Trust Services Criteria
For the period [Start Date] to [End Date]

[Addressee]

Section I — Opinion
  Scope paragraph:
    "We have examined [Service Organization Name]'s description of its
    [System Name] system and the suitability of the design and operating
    effectiveness of controls relevant to Security, [Availability,
    Processing Integrity, Confidentiality, and/or Privacy] throughout
    the period [Start Date] to [End Date] based on the Trust Services
    Criteria (TSP Section 100)."

  Management's responsibility paragraph
  Practitioner's responsibility paragraph
  Trust Services Criteria reference (TSP Section 100)

  Opinion on:
    a) Whether the description fairly presents the system
    b) Whether controls were suitably designed AND operated effectively

  Restricted use paragraph:
    "This report is intended solely for the information and use of
    [specified parties] and is not intended to be, and should not be,
    used by anyone other than these specified parties."

Section II — Description of the [System Name] System
  - System overview
  - Boundaries of the system (what is included/excluded)
  - How the system achieves trust service criteria
  - Control objectives and controls
  - CUECs (per Section 13)
  - CSOCs (per Section 13)
  - Subservice organization disclosures (inclusive or carve-out)
  - Material changes (if any during the period)
  - Incidents (if any during the period)

Section III — Management's Written Assertion
  (Use Type II assertion template from Section 11.2)

Section IV — Tests of Controls and Results
  Organized by Trust Service Category (Security first, then A, PI, C, P as applicable)
  For each criterion:
    - Criterion reference (e.g., CC6.1)
    - Control description
    - Test of design suitability
    - Test of operating effectiveness
    - Sample size
    - Test results
    - Exceptions (if any; include nature, cause, effect)

[Service Auditor Signature, Firm Name]
[Date]
[City, State]
```

---

## 10. SOC 3 Report Structure Template

```
INDEPENDENT SERVICE AUDITOR'S REPORT ON
[Service Organization Name]'S DESCRIPTION OF ITS
[System Name] SYSTEM AND THE SUITABILITY OF THE DESIGN AND
OPERATING EFFECTIVENESS OF CONTROLS
Relevant to Security, Availability, Processing Integrity,
Confidentiality, [and/or] Privacy
Based on the Trust Services Criteria
For the period [Start Date] to [End Date]

- Opinion paragraph (abbreviated but same opinion structure as SOC 2)
- Summary description of the system (high-level; no detailed boundary descriptions)
- Management's assertion (abbreviated)
- NO detailed tests of controls and results
- NO detailed CUECs or CSOCs
- NO restricted use paragraph (general use permitted)

[Service Auditor Signature, Firm Name]
[Date]
[City, State]
```

**Type I/Type II Optionality Note:** The template above shows a Type II SOC 3 (period of time, design + operating effectiveness). SOC 3 may also be issued as Type I (point in time, design suitability only). For a SOC 3 Type I, replace "For the period [Start Date] to [End Date]" with "As of [Date]" and remove operating effectiveness language, consistent with the Type I vs Type II distinctions in Section 6. Most SOC 3 reports are Type II given the general-use audience's expectation of operating effectiveness assurance, but Type I is permitted.

**Agent Action:** SOC 3 is significantly abbreviated vs. SOC 2. Never include detailed test results, CUECs, or CSOCs in a SOC 3. The purpose of SOC 3 is public-facing trust signaling, not detailed assurance for user auditors.

---

## 11. Management Assertion Letter Templates

### 11.1 Type I Assertion

```
[Service Organization Letterhead]
[Date]

To: [CPA Firm Name / Practitioner Name]

RE: Management's Assertion — [System Name]
    [SOC 1 / SOC 2 / SOC for Cybersecurity / SOC for Supply Chain]
    Type I

We assert that:

1. The description of the [System Name] system in Section II of the
   report fairly presents the [System Name] system as it relates to
   the [Description Criteria / Trust Services Criteria / Cybersecurity
   Description Criteria]. The criteria we used to prepare the
   description were [specify criteria reference].

2. The controls described in the system description were suitably
   designed to provide reasonable assurance that the [control
   objectives / trust service criteria] would be achieved if the
   controls operated effectively as of [Date].

Sincerely,

[Management Representative Name]
[Title]
[Service Organization Name]
```

### 11.2 Type II Assertion

```
[Service Organization Letterhead]
[Date]

To: [CPA Firm Name / Practitioner Name]

RE: Management's Assertion — [System Name]
    [SOC 1 / SOC 2 / SOC for Cybersecurity / SOC for Supply Chain]
    Type II

We assert that:

1. The description of the [System Name] system in Section II of the
   report fairly presents the [System Name] system as it relates to
   the [Description Criteria / Trust Services Criteria / Cybersecurity
   Description Criteria]. The criteria we used to prepare the
   description were [specify criteria reference].

2. The controls described in the system description were suitably
   designed to provide reasonable assurance that the [control
   objectives / trust service criteria] would be achieved if the
   controls operated effectively throughout the period from
   [Start Date] to [End Date].

3. The controls described in the system description operated
   effectively throughout the period from [Start Date] to [End Date]
   to provide reasonable assurance that the [control objectives /
   trust service criteria] were achieved.

Sincerely,

[Management Representative Name]
[Title]
[Service Organization Name]
```

**Agent Action:**
- Type I assertion has 2 paragraphs: fair presentation + design suitability
- Type II assertion has 3 paragraphs: fair presentation + design suitability + operating effectiveness
- If management refuses to provide the assertion, the practitioner MUST withdraw per AT-C 205. Flag this immediately if encountered.
- Always ensure the assertion is signed and dated.

---

## 12. Bridge Letter Template

```
[Service Organization Letterhead]
[Date]

RE: Bridge Letter — [System Name] SOC 2 Type II Report
Period Covered: [Report End Date] to [Current Date / Expected Next Report Date]

Dear [User Entity / Relevant Party]:

This letter is provided to supplement the SOC 2 Type II report issued by
[CPA Firm Name] dated [Report Date], covering the period [Start Date] to
[End Date].

During the period from [Report End Date] to [Current Date]:

1. There [have / have not] been material changes to the system description
   that was included in the SOC 2 Type II report.
   [If changes exist: Describe each material change, its nature, and timing.]

2. There [have / have not] been material changes to the design of controls
   described in the SOC 2 Type II report.
   [If changes exist: Describe each change and its impact on control objectives.]

3. There [have / have not] been exceptions in the operating effectiveness
   of controls described in the SOC 2 Type II report.
   [If exceptions exist: Describe each exception, its nature, cause, and
   any corrective action taken.]

4. The complementary user entity controls (CUECs) and complementary
   subservice organization controls (CSOCs) disclosed in the SOC 2
   Type II report [remain / do not remain] appropriate.
   [If not appropriate: Describe changes and updated controls.]

This letter is a management representation only and does not provide
auditor assurance. It is not a substitute for a SOC 2 Type II report
and should not be relied upon as such.

Sincerely,

[Management Representative Name]
[Title]
[Service Organization Name]
```

**Agent Action:**
- Bridge letters are issued by MANAGEMENT, not the CPA
- They provide NO auditor assurance — the letter must explicitly state this
- They cover the gap period (typically 3–6 months) between SOC report end date and current/next report date
- Always include the disclaimer that it is not a SOC report
- Commonly requested during vendor due diligence reviews
- Typical gap: SOC 2 report covers Jan 1–Dec 31; bridge letter covers Jan 1–June 30 while next report is being prepared

---

## 13. CUEC and CSOC Identification Guidance

### 13.1 Complementary User Entity Controls (CUECs)

**Definition:** Controls that user entities (customers of the service organization) are expected to have in place for the service organization's controls to achieve their stated objectives.

**How to Identify CUECs:**

```
STEP 1: For each control objective or TSC criterion, ask:
  "Does this control depend on actions taken by the user entity
   for it to function as designed?"

STEP 2: If YES, document the CUEC:
  - State the specific action the user entity must take
  - Explain why it is necessary (link to the control objective/criterion)
  - Describe the consequence if the user entity does not implement the CUEC

STEP 3: Common CUEC categories:
  - User access provisioning and maintenance (adding/removing users on the service org's system)
  - Data input validation before submission to the service org
  - Segregation of duties at the user entity level
  - Review and approval of transactions processed by the service org
  - Physical security of endpoints accessing the service org's system
  - Customer-managed encryption key management
  - Incident notification to the service org
  - Business continuity planning at the user entity level
  - Privacy notice and consent management at the user entity level

STEP 4: CUECs must be disclosed in:
  - Section II of the SOC 1 report
  - Section II of the SOC 2 report
  - NOT required in SOC 3 (abridged report)

STEP 5: Service auditor has NO responsibility to evaluate the
  suitability of CUECs. This must be stated in the report.
```

### 13.2 Complementary Subservice Organization Controls (CSOCs)

**Definition:** Controls at a subservice organization that management assumes are operating effectively under the carve-out method.

**How to Identify CSOCs:**

```
STEP 1: Identify all subservice organizations used by the service
  organization (e.g., IaaS provider, payment processor, email service)

STEP 2: Determine presentation method (see Section 14):
  → If CARVE-OUT method: Proceed to identify CSOCs
  → If INCLUSIVE method: Subservice controls are tested directly; CSOCs not needed

STEP 3: For carve-out, document CSOCs:
  - Identify the subservice organization by name
  - Describe the services provided by the subservice organization
  - List the controls at the subservice organization that management
    assumes are operating effectively
  - Explain how these CSOCs relate to the service organization's
    control objectives/criteria

STEP 4: CSOCs must be disclosed in:
  - Section II of the SOC 1 report (if carve-out method used)
  - Section II of the SOC 2 report (if carve-out method used)

STEP 5: Service auditor tests ONLY the service organization's controls,
  NOT CSOCs. Exceptions in CSOCs may affect the opinion.

STEP 6: Common CSOC categories:
  - Infrastructure access controls at the IaaS provider
  - Data center physical security (subservice data center)
  - Network security controls operated by the cloud provider
  - Payment processing security controls
  - Encryption and key management at the subservice level
```

---

## 14. Inclusive vs Carve-out Method Decision Logic

```
STEP 1: Does the service organization use subservice organizations?
  → NO: This decision is not applicable. No CSOCs needed.
  → YES: Proceed to Step 2.

STEP 2: Can the practitioner obtain sufficient evidence about the
  subservice organization's controls?
  → YES: Consider the INCLUSIVE method
    - Advantages: More comprehensive opinion, no CSOC gap
    - Requirements: Subservice org must be willing to be examined,
      description included in scope, controls tested directly
    - Best when: Subservice org already has its own SOC report or
      is willing to cooperate with the examination

  → NO: Use the CARVE-OUT method
    - Advantages: Practical when subservice org is uncooperative or
      examination is infeasible
    - Requirements: Must disclose CSOCs; management assumes subservice
      controls are effective
    - Limitations: Practitioner does NOT test subservice controls;
      exceptions in CSOCs may affect the opinion
    - Best when: Subservice org has its own SOC report the user
      entity can review separately

STEP 3: Document the decision in the system description:
  → INCLUSIVE: State that subservice organization controls are included
    in the system description and were examined
  → CARVE-OUT: State that the carve-out method was used, identify the
    subservice organizations, and disclose CSOCs

STEP 4: Impact on the practitioner's report:
  → INCLUSIVE: Opinion covers subservice organization controls
  → CARVE-OUT: Opinion excludes subservice organization controls;
    CSOCs are assumed but not tested
```

**Agent Action:** Always ask whether subservice organizations exist before drafting the system description. The inclusive vs. carve-out decision fundamentally shapes the scope and the opinion. If the user does not know, list common subservice organization types (cloud IaaS, payment processors, CDNs, email services, managed security services) and ask if any are used.

---

## 15. CPA Opinion Types and Determination Logic

### 15.1 Opinion Types

| Opinion Type | When Issued | Report Language | Implications |
|---|---|---|---|
| **Unqualified (Clean)** | Description fairly presented; controls suitably designed and operating effectively | "In our opinion, in all material respects…" | Full confidence; no exceptions |
| **Qualified** | Exceptions exist in design or operating effectiveness but are limited in scope | "Except for the matters described… in all other material respects…" | Exceptions noted; overall still positive |
| **Adverse** | Controls are not suitably designed or not operating effectively across the engagement scope | "In our opinion, the description does not fairly present… / controls are not suitably designed…" | Major deficiencies; users should not rely on controls |
| **Disclaimer** | Practitioner unable to obtain sufficient evidence | "We were unable to obtain sufficient appropriate evidence…" | No assurance; scope limitation |

### 15.2 Opinion Determination Decision Tree

```
STEP 1: Was sufficient appropriate evidence obtained to form an opinion?
  → YES: Proceed to Step 2
  → NO: Can additional evidence be obtained through extended procedures?
    → YES: Obtain additional evidence, then return to Step 1
    → NO: Issue DISCLAIMER OF OPINION
      - State the scope limitation
      - State that insufficient evidence was obtained
      - Do NOT express an opinion on design or operating effectiveness

STEP 2: Are there any exceptions in the FAIR PRESENTATION of the description?
  → YES, material misstatement affecting the entire description:
    → Issue ADVERSE OPINION on description fairness
  → YES, but limited to specific aspects:
    → Issue QUALIFIED OPINION — describe the specific aspects that
      are not fairly presented and their effects
  → NO: Proceed to Step 3

STEP 3: Are there any exceptions in DESIGN SUITABILITY of controls?
  → YES, controls are not suitably designed across ALL or most objectives:
    → Issue ADVERSE OPINION on design suitability
  → YES, but limited to specific controls or objectives:
    → Issue QUALIFIED OPINION — describe the specific controls that
      are not suitably designed and their effects
  → NO: Proceed to Step 4

STEP 4: (Type II only) Are there any exceptions in OPERATING EFFECTIVENESS?
  → YES, exceptions are pervasive and affect multiple control objectives:
    → Issue ADVERSE OPINION on operating effectiveness
  → YES, but limited to specific controls or periods:
    → Issue QUALIFIED OPINION — describe exceptions, their nature,
      cause, effect, and any compensating controls
  → NO: Issue UNQUALIFIED (CLEAN) OPINION

STEP 5: For QUALIFIED opinions, ensure the report:
  - Identifies each exception clearly
  - States the nature, cause, and effect of each exception
  - Notes whether management implemented compensating controls
  - Uses "except for" language in the opinion paragraph
  - Still expresses a positive opinion on controls not affected by exceptions

COMPOUND ISSUES NOTE: When multiple exceptions exist across different
criteria or control objectives, evaluate each exception independently
first, then assess their cumulative effect. Multiple qualified exceptions
may, in aggregate, rise to the level of an adverse opinion if they
collectively indicate pervasive control failure. Apply professional
judgment to determine whether the compound effect of individual exceptions
is limited (qualified) or pervasive (adverse). Document the rationale
for the aggregate assessment explicitly in the report.
```

**Agent Action:** When evaluating exceptions, always consider:
1. Is the exception isolated or systematic?
2. Does a compensating control exist that mitigates the risk?
3. Is the exception material to the control objective?
4. Was the exception corrected during the examination period?
5. What is the impact on user entities?
6. Do multiple exceptions, when viewed together, create a compound effect that elevates the opinion from qualified to adverse?

---

## 16. Complete Engagement Lifecycle

### Phase 1: Scoping and Readiness

```
1.1  Classify the engagement type (Section 5 decision tree)
1.2  Determine report type: Type I or Type II (Section 6 decision tree)
1.3  Define system boundaries:
     - What systems, services, and processes are in scope
     - What is explicitly excluded and why
1.4  Select trust service categories (SOC 2/SOC 3):
     - Security: ALWAYS required
     - Availability, Processing Integrity, Confidentiality, Privacy: Optional
     - Document rationale for each included/excluded category
1.5  Identify subservice organizations:
     - List all subservice organizations and services provided
     - Determine inclusive vs. carve-out method (Section 14)
1.6  Perform readiness assessment (gap analysis):
     - Map existing controls to all applicable TSC criteria
     - Identify gaps where criteria are not addressed by existing controls
     - Document severity and priority of each gap
1.7  Develop remediation plan:
     - Prioritize gaps by risk and control objective impact
     - Establish timelines for remediation
     - Assign ownership for each remediation action
1.8  Establish examination period (Type II):
     - Determine start date and end date
     - Minimum 6 months recommended; 12 months is standard
     - Ensure all remediated controls are operational before period start
1.9  Engage the CPA practitioner:
     - Confirm practitioner independence per AICPA Code of Professional Conduct
     - Confirm practitioner is licensed and enrolled in peer review program
     - Execute engagement letter
```

### Phase 2: Evidence Gathering and Examination

```
2.1  Management prepares the system description per Description Criteria:
     - System boundaries, purpose, types (infrastructure, software, people, procedures, data)
     - System processes (input, processing, output)
     - Relevant TSC categories and control objectives
     - Specified controls mapped to each criterion
     - CUECs for each control objective
     - CSOCs if carve-out method applies
     - Material changes and incidents

2.2  Management prepares the written assertion (Section 11 templates)

2.3  Practitioner obtains understanding of the system:
     - Conduct walkthroughs of key processes
     - Interview key personnel
     - Review documentation (policies, procedures, architectures)
     - Observe control operations

2.4  Practitioner tests design suitability (Type I and Type II):
     - Evaluate whether each control is appropriately designed
     - Assess whether controls, if operated as designed, would meet criteria
     - Document design testing procedures and conclusions

2.5  Practitioner tests operating effectiveness (Type II only):
     - Determine sample sizes per Section 17 guidance
     - Execute test procedures for each control over the examination period
     - Document all test procedures, samples, and results
     - Record exceptions and deviations
     - Evaluate management's corrective actions for exceptions
     - Assess whether compensating controls exist for deviations

2.6  Practitioner evaluates the system description:
     - Does it fairly present the system as it relates to the criteria?
     - Are all required Description Criteria elements present?
     - Is there any omitted or misrepresented information?

2.7  Practitioner evaluates management's assertion:
     - Is the assertion fairly stated in all material respects?
     - Does it cover all required elements (fair presentation, design, operating effectiveness)?

2.8  Practitioner evaluates CUECs and CSOCs:
     - Are CUECs appropriately identified and disclosed?
     - Are CSOCs appropriately identified and disclosed (carve-out)?
     - Does the practitioner have any responsibility to test CUECs or CSOCs? (No)
```

### Phase 3: Report Issuance

```
3.1  Draft the practitioner's report using the appropriate template:
     - SOC 1: Section 8 templates
     - SOC 2: Section 9 templates
     - SOC 3: Section 10 template
     - SOC for Cybersecurity: Section 18 template
     - SOC for Supply Chain: Section 19 template

3.2  Determine the opinion type using the decision tree (Section 15)

3.3  Verify all required report sections are present (Section 21 checklist)

3.4  Management review and sign-off:
     - Review and approve the system description
     - Sign and date the management assertion
     - Confirm all CUECs and CSOCs are accurately disclosed

3.5  Practitioner issues the final report:
     - Sign and date the report
     - Include firm name, city, and state
     - Deliver to the service organization

3.6  Issue bridge letter if applicable (Section 12):
     - Provided by management (not the CPA)
     - Covers gap between report end date and current/next report date
     - Used during vendor due diligence when new report is not yet available
```

### Phase 4: Ongoing Monitoring

```
4.1  Continuous monitoring of controls between examination periods:
     - Track control execution and exceptions
     - Monitor for material changes to the system
     - Maintain evidence repositories for next examination

4.2  Remediate exceptions identified in prior reports:
     - Document corrective actions
     - Test effectiveness of remediation before next examination period

4.3  Document material changes to the system:
     - New systems, services, or processes added
     - Controls added, modified, or removed
     - Subservice organization changes
     - Personnel or organizational changes affecting controls

4.4  Prepare for next examination:
     - Update system description
     - Reassess risk and controls
     - Adjust scope if TSC categories change
     - Establish new examination period
     - Issue bridge letter during gap periods
```

---

## 17. Sampling Guidance for Type II

**Agent Action:** When guiding Type II testing, use these minimum sample sizes based on control frequency. Adjust upward for higher-risk controls or when preliminary testing reveals deviations.

| Control Frequency | Minimum Sample Size | Notes |
|---|---|---|
| **Daily** | 25–40 items | Select across the entire examination period; ensure coverage of all months |
| **Weekly** | 10–20 items | Spread selections across the period |
| **Monthly** | 2–5 items | Select from different months |
| **Quarterly** | 1–2 items | Select from each quarter |
| **Annual** | 1–2 items | Test the single annual occurrence or a minimum of 1 |
| **Per occurrence** (triggered) | All occurrences or statistical sample | Depends on volume and risk; for low-volume triggered controls, test all |

### Deviation Rate Analysis

```
STEP 1: Calculate the actual deviation rate:
  Actual Deviation Rate = (Number of deviations / Sample size) × 100

STEP 2: Compare to the expected (tolerable) deviation rate:
  - Expected rate is established during engagement planning
  - Typically 0%–5% depending on control criticality

STEP 3: Evaluate results:
  → Actual rate ≤ Expected rate: Control is operating effectively
    (but consider whether to increase sample size for confirmation)

  → Actual rate > Expected rate but < Material threshold:
    - Document the deviation
    - Evaluate whether compensating controls exist
    - Consider impact on opinion (may require qualified opinion)

  → Actual rate ≥ Material threshold:
    - Control is not operating effectively
    - Evaluate impact on overall opinion
    - May result in qualified or adverse opinion

STEP 4: For each exception, document:
  - Nature: What happened?
  - Cause: Why did it happen?
  - Effect: What is the impact on the control objective?
  - Corrective action: What did management do to fix it?
  - Compensating controls: Are there any that mitigate the risk?
```

---

## 18. SOC for Cybersecurity Framework Components

### 18.1 Framework Structure

| Component | Description | Agent Directive |
|---|---|---|
| **Description Criteria** | Criteria for describing the entity's cybersecurity risk management program | Evaluate whether management's description covers all required description criteria elements |
| **Control Criteria** | Trust Services Criteria for Security, Availability, and Confidentiality | Use TSP Section 100 criteria (Security + Availability + Confidentiality); Privacy and Processing Integrity are optional |
| **Attestation Guide** | Reporting on an Entity's Cybersecurity Risk Management Program and Controls | Follow AICPA attestation guide for report structure and opinion language |

### 18.2 Report Structure

```
INDEPENDENT PRACTITIONER'S REPORT ON
[Entity Name]'S CYBERSECURITY RISK MANAGEMENT PROGRAM AND CONTROLS
Based on the AICPA Cybersecurity Description Criteria and
Trust Services Criteria
[As of Date / For the period Start Date to End Date]

1. Management's Description of the Cybersecurity Risk Management Program
   - How the entity identifies information assets and cybersecurity risks
   - Key security policies, processes, and controls
   - Risk management program scope and boundaries
   - Cybersecurity governance structure
   - Communication of cybersecurity risks

2. Management's Assertion
   - Fair presentation of description
   - Design suitability of controls
   - Operating effectiveness (Type II only)

3. Practitioner's Opinion
   - Opinion on description fairness
   - Opinion on control design suitability
   - Opinion on operating effectiveness (Type II only)
   - General use or restricted use paragraph

[Practitioner Signature, Firm Name]
[Date]
[City, State]
```

### 18.3 Key Distinctions from SOC 2

- **Scope:** Entity-level cybersecurity program, not just a specific system
- **Categories:** Security, Availability, Confidentiality (Privacy and PI optional)
- **Focus:** Cybersecurity risk management (broader than system controls)
- **Reporting levels:**
  - Entity level — for the entity's own stakeholders
  - Service provider level — for user entities' vendor risk management
  - Supply chain level — for supply chain risk management
- **Distribution:** General use (unrestricted), unlike SOC 2

**Agent Action:** If the user's scenario involves a cybersecurity risk management program at the entity level (not system-specific), recommend SOC for Cybersecurity. If the user needs system-specific TSC reporting, recommend SOC 2.

---

## 19. SOC for Supply Chain Key Distinctions

### 19.1 Full Title

*SOC for Supply Chain: Reporting on an Examination of Controls Relevant to Security, Availability, Processing Integrity, Confidentiality, or Privacy in a Production, Manufacturing, or Distribution System*

### 19.2 Key Differences from SOC 2

| Factor | SOC 2 | SOC for Supply Chain |
|---|---|---|
| **Applicable entities** | Service organizations (SaaS, IaaS, etc.) | Entities that manufacture, produce, or distribute physical or digital products |
| **System type** | IT service systems | Production, manufacturing, distribution systems |
| **Risk focus** | Data and system controls | Product/service integrity through the supply chain |
| **TSC criteria** | Standard TSP Section 100 | Adapted TSP Section 100 with supply-chain-specific context |
| **Report structure** | Standard SOC 2 structure | Parallel to SOC 2 but supply-chain-focused description |
| **Distribution** | Restricted | Restricted |

### 19.3 Report Structure

```
INDEPENDENT SERVICE AUDITOR'S REPORT ON
[Entity Name]'S DESCRIPTION OF ITS
[System Name] PRODUCTION/MANUFACTURING/DISTRIBUTION SYSTEM AND
THE SUITABILITY OF THE DESIGN AND OPERATING EFFECTIVENESS OF CONTROLS
Relevant to Security, Availability, Processing Integrity,
Confidentiality, [and/or] Privacy in a Production, Manufacturing,
or Distribution System
Based on the Trust Services Criteria
For the period [Start Date] to [End Date]

1. Practitioner's opinion
2. Management's description of the production/manufacturing/distribution system
3. Management's assertion
4. Tests of controls and results (Type II)

[Service Auditor Signature, Firm Name]
[Date]
[City, State]
```

**Agent Action:** Use SOC for Supply Chain when the entity manufactures, produces, or distributes products and the user needs assurance on supply chain controls. The description must focus on how the system ensures product/service integrity through the supply chain.

---

## 20. Cross-Reference Mappings

### 20.1 TSP Section 100 to COSO Internal Control — Integrated Framework

| TSC Category | COSO Principle(s) | Alignment |
|---|---|---|
| CC1.1 | Principle 1 (Integrity and ethical values) | Direct alignment |
| CC1.2 | Principle 5 (Accountability) | **Note: Non-sequential mapping** — CC1.2 maps to P5, not P2 |
| CC1.3 | Principle 3 (Competence requirements) | Direct alignment |
| CC1.4 | Principle 4 (Commitment to competence) | Direct alignment |
| CC1.5 | Principle 2 (Oversight) | **Note: Non-sequential mapping** — CC1.5 maps to P2, not P5 |
| CC2.1–CC2.3 | Principles 13–15 (Information & Communication) | Direct alignment |
| CC3.1–CC3.4 | Principles 6–9 (Risk Assessment) | Direct alignment |
| CC4.1–CC4.2 | Principles 16–17 (Monitoring Activities) | Direct alignment |
| CC5.1–CC5.3 | Principles 10–12 (Control Activities) | Direct alignment |
| CC6.1–CC6.6 | Principle 12 (supplemental) | Supplemental: logical/physical access controls |
| CC7.1–CC7.5 | Principle 12 (supplemental) | Supplemental: system operations |
| CC8.1–CC8.3 | Principle 12 (supplemental) | Supplemental: change management |
| CC9.1–CC9.2 | Principle 12 (supplemental) | Supplemental: risk mitigation |

**Agent Note:** The 2017 TSC was explicitly modeled on COSO 2013. The criteria under CC1–CC5 correspond to COSO's 17 principles, but the mapping for CC1 is non-sequential: CC1.2 (accountability) maps to COSO Principle 5, and CC1.5 (oversight) maps to COSO Principle 2. CC6–CC9 supplement COSO Principle 12 with IT-specific controls.

**Cross-Skill Note:** The COSO Internal Controls skill's Section 22 contains a TSC↔COSO reverse mapping table. If discrepancies exist between that mapping and this section, the mapping in this Section 20.1 is authoritative per AICPA TSP Section 100.

### 20.2 TSP Section 100 to ISO/IEC 27001:2022

**Note:** The cross-references below use ISO/IEC 27001:2022 Annex A numbering (4 themes: Organizational, People, Physical, Technological; 93 controls). For engagements referencing the superseded ISO 27001:2013 edition, key equivalents are noted in parentheses (A.6–A.18).

| TSC Category | ISO 27001:2022 Annex A | 2013 Equivalent | Mapping Notes |
|---|---|---|---|
| Security (CC6) | 5.15–5.18 (Organizational), 6.5–6.8 (People), 7.1–7.9 (Physical), 8.1–8.28 (Technological) | A.6–A.13 | Access control, cryptography, physical security, operations security |
| Availability (A1) | 5.29–5.30 (Organizational), 8.14–8.15 (Technological) | A.17 | Information security aspects of business continuity, redundancy |
| Processing Integrity (PI1) | 8.7–8.16 (Technological) | A.12 | Operations security — protection against malware, backup, logging, capacity |
| Confidentiality (C1) | 5.12–5.13 (Organizational), 8.10–8.12 (Technological) | A.8 | Asset management — classification, media handling, data masking |
| Privacy (P1–P8) | ISO 27701:2019 / 5.34 (Organizational), 7.4 (Physical) | ISO 27701:2019 / A.18 | Privacy extension; PII processing; GDPR alignment |
| Risk Assessment (CC3) | Clause 6 + 5.1–5.5 (Organizational) | Clause 6 + A.6 | Context of the organization, risk assessment, risk treatment |
| Change Management (CC8) | 8.31–8.33 (Technological) | A.14 | System acquisition, development, and maintenance |
| Monitoring (CC4) | Clause 9 + 5.35–5.36 (Organizational) | Clause 9 + A.18 | Performance evaluation, measurement, compliance review |

**Key Distinction:** ISO 27001 is a certifiable standard with fixed Annex A controls (93 controls in the 2022 edition, 114 in the 2013 edition). SOC 2 uses criteria-based evaluation with flexibility in controls implemented. ISO certification covers the entire ISMS; SOC 2 can be scoped to specific systems and TSC categories.

### 20.3 TSP Section 100 to NIST SP 800-53 Rev 5

| TSC Category | NIST 800-53 Rev 5 Control Family | Example Controls |
|---|---|---|
| CC6 (Logical/Physical Access) | AC, PE, IA | AC-1–AC-25 (Access Control), PE-1–PE-20 (Physical/Environmental), IA-1–IA-11 (Identification/Authentication) |
| CC7 (System Operations) | AU, SI, CP | AU-1–AU-16 (Audit), SI-1–SI-16 (System Integrity), CP-1–CP-10 (Contingency Planning) |
| CC8 (Change Management) | CM, SA | CM-1–CM-11 (Configuration Management), SA-1–SA-14 (System Acquisition) |
| CC9 (Risk Mitigation) | RA, SR | RA-1–RA-6 (Risk Assessment), SR-1–SR-12 (Supply Chain Risk) |
| Privacy (P1–P8) | PT, AR, DI | PT-1–PT-8 (Privacy Transparency), AR-1–AR-8 (Individual Participation), DI-1–DI-16 (Data Quality) |

**Note:** All NIST 800-53 control references in this section are based on NIST SP 800-53 Rev 5. For engagements referencing Rev 4, note that Rev 5 reorganized several control families (e.g., Privacy controls PT/AR/DI were added in Rev 5; supply chain risk controls SR were separated from SA). Verify the applicable revision with the user.

### 20.4 TSP Section 100 Privacy Criteria to GDPR

| TSC Criterion | GDPR Article(s) | Mapping |
|---|---|---|
| P1.1 (Notice) | Art. 13–14 | Information to be provided at data collection |
| P2.1 (Choice/Consent) | Art. 6–7, Art. 9 | Lawfulness of processing, conditions for consent |
| P3.1 (Collection) | Art. 5(1)(b), Art. 5(1)(c) | Purpose limitation (Art. 5(1)(b)), data minimization (Art. 5(1)(c)) |
| P4.1 (Use/Retention/Disposal) | Art. 5(1)(e), Art. 17 | Storage limitation, right to erasure |
| P5.1 (Access) | Art. 15 | Right of access by the data subject |
| P6.1 (Disclosure) | Art. 44–49 | Transfers of personal data to third countries |
| P7.1 (Complaints) | Art. 77–79 | Right to lodge a complaint, right to judicial remedy |
| P8.1 (Monitoring) | Art. 24, Art. 32 | Responsibility of the controller, security of processing |

**ISO 27701:2019 Alignment Note:** The Privacy TSC criteria (P1–P8) also map to ISO 27701:2019 (Privacy Information Management System extension to ISO 27001). For dual ISO 27001 + ISO 27701:2019 certified organizations, the P1–P8 criteria provide a direct bridge between SOC 2 Privacy and the ISO privacy management framework.

**Agent Action:** When the Privacy TSC category is in scope, provide GDPR cross-references to help the user understand regulatory alignment. This is particularly useful for service organizations with EU data subjects.

### 20.5 SOC Reporting ↔ ISACA/COBIT Cross-Reference

| SOC Area | ISACA/COBIT Equivalent | Relationship | Notes |
|---|---|---|---|
| SOC 2 Trust Services Criteria | COBIT 2019 Management Objectives | Overlapping governance | TSC focuses on system-level controls; COBIT addresses enterprise IT governance broadly |
| CC1 Control Environment | EDM01–EDM03 (Evaluate, Direct, Monitor) | Strong alignment | COSO Principle 1–5 map to COBIT EDM governance practices |
| CC2 Communication & Information | APO01–APO02 (Manage Framework, Strategy) | Partial alignment | COBIT APO covers IT strategy/communication governance |
| CC3 Risk Assessment | APO12 (Manage Risk), APO13 (Manage Security) | Direct alignment | Risk assessment is core to both; COBIT uses risk-based approach |
| CC4 Monitoring Activities | MEA01–MEA03 (Monitor, Evaluate, Assess) | Direct alignment | Both require ongoing/periodic evaluation and deficiency communication |
| CC5 Control Activities | BAI02–BAI07 (Manage Projects, Changes) | Partial alignment | COBIT BAI covers internal controls and change management |
| CC6 Logical/Physical Access | DSS05 (Manage Security Services), DSS06 (Manage Business Process Controls) | Strong alignment | Access management controls map between both |
| CC7 System Operations | DSS01–DSS04 (Manage Operations, Service Requests, Problems, Continuity) | Strong alignment | Operations and continuity management overlap |
| CC8 Change Management | BAI06 (Manage Changes), BAI07 (Manage Change Acceptance) | Direct alignment | Change control processes are closely aligned |
| CC9 Risk Mitigation | APO12 (Manage Risk), APO10 (Manage Vendors) | Direct alignment | Vendor and risk management overlap significantly |
| Privacy (P1–P8) | APO13 (Manage Security), COBIT Privacy Objective | Partial alignment | COBIT has a dedicated privacy management objective |
| SOC 1 Control Objectives | COBIT Application Controls (ITAC) | Conceptual alignment | SOC 1 control objectives are management-defined; COBIT ITAC provides standardized application control framework |
| Service Auditor Role | IS Audit per ITAF | Overlapping profession | Both require independence, due professional care, sufficiency of evidence |
| Sampling for Type II | ISACA Sampling Methodology (CISA CRM) | Shared methodology | Both use attribute sampling for tests of operating effectiveness |
| Exception Evaluation | ISACA 5-Part Observation (Condition, Criteria, Cause, Effect, Recommendation) | Conceptual alignment | SOC report exceptions document nature, cause, effect; ISACA format adds explicit criteria and recommendation structure |

---

## 21. Report Validation Checklist

**Agent Action:** Before finalizing any SOC report, verify ALL of the following items. A report that fails any mandatory item is incomplete and must be corrected before issuance.

| # | Validation Item | Mandatory? | Applies To |
|---|---|---|---|
| 1 | Title includes "Independent" | YES | All SOC reports |
| 2 | Addressee specified | YES | All SOC reports |
| 3 | Engagement scope clearly described (engagement type, criteria, period) | YES | All SOC reports |
| 4 | Criteria referenced (AT-C 205, TSP Section 100, AT-C 320, etc.) | YES | All SOC reports |
| 5 | Report period/dates specified (as-of date for Type I; start/end dates for Type II) | YES | All SOC reports |
| 6 | Management's responsibility paragraph included | YES | All SOC reports |
| 7 | Practitioner's responsibility paragraph included | YES | All SOC reports |
| 8 | Opinion paragraph with clear opinion type (unqualified/qualified/adverse/disclaimer) | YES | All SOC reports |
| 9 | System description covers all required Description Criteria elements | YES | SOC 1, SOC 2 |
| 10 | CUECs identified and disclosed | YES | SOC 1, SOC 2 |
| 11 | CSOCs identified and disclosed (if carve-out method used) | YES | SOC 1, SOC 2 (carve-out) |
| 12 | Management's written assertion included (signed and dated) | YES | All SOC reports |
| 13 | Tests of controls and results section included (Type II only) | YES | SOC 1 Type II, SOC 2 Type II |
| 14 | For Type II: Each control tested, sample size, and results documented | YES | SOC 1 Type II, SOC 2 Type II |
| 15 | Restricted use paragraph included | YES | SOC 1, SOC 2, SOC for Supply Chain |
| 16 | NO restricted use paragraph (general use permitted) | YES | SOC 3, SOC for Cybersecurity |
| 17 | Practitioner signature, date, and location (city, state) | YES | All SOC reports |

**Agent Action:** If any mandatory item is missing, flag it immediately with the specific item number and description. Do not proceed with issuance until all items are satisfied.

---

## 22. Quality Gates — Before Producing Any Output, Verify:

- [ ] **QG1:** Are all SOC report sections present and correctly numbered per the applicable template (Sections 8–10, 18–19)?
- [ ] **QG2:** Does the opinion type match the evidence evaluation per the decision tree in Section 15?
- [ ] **QG3:** Are all 33 Common Criteria addressed when SOC 2/SOC 3 is in scope?
- [ ] **QG4:** Is the management assertion in the correct format (2-paragraph for Type I, 3-paragraph for Type II)?
- [ ] **QG5:** Are CUECs and CSOCs identified, disclosed, and linked to specific control objectives or TSC criteria?
- [ ] **QG6:** Are all COSO principle mappings correct (especially CC1.2 → Principle 5, CC1.5 → Principle 2)?
- [ ] **QG7:** Is the terminology enforced per Section 24 (service auditor not auditor, Trust Services Criteria not Principles, etc.)?
- [ ] **QG8:** Are cross-references to other frameworks accurate and using current edition numbering (ISO 27001:2022, NIST 800-53 Rev 5)?
- [ ] **QG9:** For Type II, are sample sizes and deviation rates documented per Section 17?
- [ ] **QG10:** Does the output maintain professional objectivity and avoid providing audit opinions without sufficient evidence?

## 23. Mandatory Formats

- **SOC report structure:** ALWAYS use the templates in Sections 8–10, 18–19. No exceptions.
- **Management assertions:** ALWAYS use the 2-paragraph (Type I) or 3-paragraph (Type II) format from Section 11. No alternatives.
- **Bridge letters:** ALWAYS use the 4-attestation format from Section 12. No alternatives.
- **CUEC/CSOC disclosures:** ALWAYS link each CUEC/CSOC to a specific control objective or TSC criterion. No orphan disclosures.
- **Opinion language:** ALWAYS use the exact opinion types defined in Section 15.1 (Unqualified, Qualified, Adverse, Disclaimer). No other opinion types.
- **CUEC/CSOC acronyms:** ALWAYS spell out "Complementary User Entity Controls" and "Complementary Subservice Organization Controls" on first use in any document section.
- **Finding severity:** ALWAYS classify exceptions by their impact on the opinion (material vs. limited). No arbitrary severity scales.

## 24. Terminology Enforcement

- Use "service auditor" not "auditor" when referring to the CPA performing the SOC examination
- Use "management assertion" not "representation letter" when referring to management's written assertion in a SOC report
- Use "Complementary User Entity Controls (CUECs)" and "Complementary Subservice Organization Controls (CSOCs)" — always spell out on first use
- Use "Trust Services Criteria" not "Trust Services Principles" for current engagements — "Principles" was used in the superseded 2011 TSP; current terminology is "Criteria"
- Never say "SAS 70" or "SSAE 16" for current engagements — both are superseded (SAS 70 since June 2011, SSAE 16 since May 2017); current standard is SSAE 18
- Use "user auditor" not "user entity auditor" when referring to the CPA auditing the user entity's financial statements
- Use "control objective" for SOC 1 (management-defined) vs. "trust service criterion" for SOC 2 (codified in TSP Section 100)
- Use "carve-out method" not "carve-out approach" or "exclusion method"
- Use "inclusive method" not "inclusive approach" or "inclusion method"
- Use "description criteria" not "reporting criteria" for SOC 2 system description standards
- Use "points of focus" not "implementation guidance" or "application guidance" when referring to TSP Section 100 implementation support
- Use "exception" not "deficiency" or "finding" in the context of SOC report test results

---

## 25. Behavioral Requirements

**The agent MUST be able to perform the following 15 capabilities:**

1. **Classify** a given service organization scenario into the correct SOC engagement type using the decision tree in Section 5. Present the classification with supporting rationale.

2. **Scope** a SOC engagement by identifying applicable TSC categories and all 33 Common Criteria plus selected additional criteria. Document the scope with explicit in/out boundaries.

3. **Generate** a complete system description per the Description Criteria elements in Section 16 (Phase 2, step 2.1). Include system boundaries, purpose, types, processes, controls, CUECs, and CSOCs.

4. **Generate** management assertion letters for Type I (2-paragraph) and Type II (3-paragraph) using the templates in Section 11. Ensure all required elements are present and the assertion is signed and dated.

5. **Generate** CUEC disclosures by working through the identification steps in Section 13.1. Link each CUEC to the specific control objective or TSC criterion it supports.

6. **Generate** CSOC disclosures by working through the identification steps in Section 13.2. Identify subservice organizations, describe services, list assumed controls, and explain their relevance.

7. **Generate** bridge letters using the template in Section 12. Cover all four required attestations (system description changes, control design changes, operating effectiveness exceptions, CUEC/CSOC appropriateness).

8. **Map** TSC criteria to ISO 27001:2022 Annex A, NIST 800-53 Rev 5 control families, COSO principles, and GDPR articles using the cross-reference tables in Section 20. Present mappings in tabular format.

9. **Evaluate** evidence sufficiency for Type II testing by applying the sampling guidance in Section 17. Determine sample sizes based on control frequency, assess deviation rates, and identify exceptions.

10. **Determine** opinion type (unqualified/qualified/adverse/disclaimer) by applying the decision tree in Section 15. Walk through each step, document the basis for the opinion, and generate the appropriate opinion language.

11. **Generate** complete report structures for SOC 1 (Section 8), SOC 2 (Section 9), SOC 3 (Section 10), SOC for Cybersecurity (Section 18), and SOC for Supply Chain (Section 19). Use exact section numbering and required language.

12. **Track** examination period dates and bridge letter requirements. Calculate bridge periods, identify when bridge letters are needed, and flag approaching report expiration dates.

13. **Validate** that a SOC report meets all 17 required elements using the checklist in Section 21. Flag any missing items with specific item numbers and remediation guidance.

14. **Identify** whether the inclusive or carve-out method is appropriate for subservice organizations by applying the decision logic in Section 14. Present the recommendation with pros, cons, and impact on the opinion scope.

15. **Explain** the relationship between SOC reporting and other frameworks (COBIT, ISO 27001, NIST 800-53 Rev 5, GDPR) using the cross-reference mappings in Section 20. Highlight key distinctions and overlapping requirements.

---

## 26. Examples — Realistic SOC Engagement Scenarios

### Example 1: SaaS Company First SOC 2

**Scenario:** CloudStack SaaS Inc. provides a cloud-based project management platform. Their customers (user entities) are asking for a SOC 2 report. This is CloudStack's first SOC engagement. They use AWS as their IaaS provider.

**Agent Execution:**

1. **Classify:** Subject matter is Trust Services Criteria → SOC 2 (restricted distribution acceptable for customers under NDA)
2. **Report type:** First engagement → Recommend Type I as readiness assessment, then Type II after 6-month period
3. **TSC categories:** Security (mandatory) + Availability (SLA commitments to customers) + Confidentiality (customer data protected)
4. **Subservice org:** AWS (IaaS provider) → Recommend carve-out method (AWS has its own SOC 2 report; no need to test directly)
5. **Scope:** 33 Common Criteria + 3 Availability + 2 Confidentiality = 38 criteria
6. **CUECs to identify:** User access provisioning, data input validation, customer-managed encryption keys, incident notification
7. **CSOCs to identify:** AWS infrastructure access controls, data center physical security, network security, encryption at rest
8. **Readiness gaps:** Likely gaps in CC3.3 (fraud risk), CC9.2 (vendor risk management for AWS), C1.1 (data classification)

### Example 2: Payroll Processor SOC 1

**Scenario:** PayRight Inc. processes payroll for 500+ companies. User entity auditors need assurance on controls relevant to ICFR for their financial statement audits.

**Agent Execution:**

1. **Classify:** Subject matter is ICFR → SOC 1 (governed by AT-C 320)
2. **Report type:** User auditors need operating effectiveness → Type II
3. **Examination period:** January 1 – December 31 (annual, aligned with user entity fiscal years)
4. **Control objectives:** Payroll processing accuracy, completeness, authorization, timeliness (management-defined, not standardized TSC)
5. **CUECs:** User entity employee data submission, payroll approval at user entity, segregation of duties for payroll changes
6. **Subservice org:** Bank for direct deposits → Carve-out method; CSOC: Bank ACH processing controls

### Example 3: Multi-TSC SOC 2 with Privacy

**Scenario:** HealthData Corp. provides a healthcare analytics platform that processes protected health information (PHI). They need a SOC 2 covering all five TSC categories.

**Agent Execution:**

1. **Classify:** Trust Services Criteria → SOC 2
2. **Report type:** Type II (established program, 12-month period)
3. **TSC categories:** Security + Availability + Processing Integrity + Confidentiality + Privacy (all five)
4. **Total criteria:** 33 CC + 3 A + 5 PI + 2 C + 8 P = 51 criteria
5. **Privacy-GDPR alignment:** Review P1.1–P8.1 against GDPR Art. 6–79; identify gaps for EU data subjects
6. **Key focus areas:** P2.1 (HIPAA consent + GDPR consent), P3.1 (minimum necessary standard + data minimization), C1.2 (PHI encryption at rest/in transit), CC6.6 (MFA, intrusion detection)

### Example 4: Bridge Letter After SOC 2 Report

**Scenario:** CloudStack SaaS Inc. received their SOC 2 Type II report covering January 1 – December 31, 2025. A customer requests assurance for the period through May 2026, but the next report won't be ready until August 2026.

**Agent Execution:**

1. **Gap period:** January 1, 2026 – May 31, 2026 (5 months)
2. **Generate bridge letter** per Section 12 template covering:
   - No material changes to system description
   - No material changes to control design
   - No exceptions in operating effectiveness
   - CUECs and CSOCs remain appropriate
3. **Disclaimer:** Bridge letter is management representation only; no auditor assurance
4. **Recommendation:** Advise customer to request CloudStack's next SOC 2 report when issued

### Example 5: Opinion Determination with Exceptions

**Scenario:** During a SOC 2 Type II examination, the practitioner found that 3 out of 30 sampled user access reviews (CC6.4) were performed late during Q3. No compensating controls were identified. All other controls tested had no exceptions.

**Agent Execution:**

1. **Deviation rate:** 3/30 = 10% (exceeds typical tolerable rate of 5%)
2. **Scope of exception:** Limited to CC6.4 during Q3; does not affect all control objectives
3. **No compensating controls:** Increases significance of the exception
4. **Opinion determination per Section 15:**
   - Description is fairly presented → No adverse on description
   - Design is suitable → Exception is in operating effectiveness, not design
   - Operating effectiveness exception is NOT pervasive across all objectives → QUALIFIED OPINION
5. **Opinion language:** "Except for the matter described in the following paragraph, in all other material respects…"
6. **Exception description:** Nature (late access reviews), Cause (resource constraints in Q3), Effect (potential unauthorized access during review gap), Corrective action (hired additional staff, implemented automated review reminders)

### Example 6: Compound Exception Evaluation

**Scenario:** During a SOC 2 Type II examination, the practitioner found exceptions in three separate areas: (a) CC6.4 — 3 of 30 access reviews were late, (b) CC7.3 — incident response SLA was missed 4 times out of 12, and (c) CC8.2 — 2 of 20 changes were deployed without complete testing documentation.

**Agent Execution:**

1. **Evaluate each exception individually:**
   - CC6.4: 10% deviation rate; no compensating controls → qualified exception
   - CC7.3: 33% deviation rate; no compensating controls → qualified exception
   - CC8.2: 10% deviation rate; compensating control (emergency change procedure) partially mitigates → qualified exception
2. **Assess compound effect per Section 15, Step 5 Compound Issues Note:**
   - Do the three exceptions collectively indicate pervasive control failure?
   - Individually, each is limited to a specific criterion → qualified
   - Collectively, they span access, operations, and change management — but each is limited in scope and does not affect the overall description fairness or design suitability
   - Compound assessment: Still QUALIFIED OPINION, not adverse
3. **Opinion language:** Single qualified opinion paragraph covering all three exceptions with "except for the matters described…"
4. **Document the compound evaluation rationale** explicitly in work papers

---

## 27. Current Updates and Compliance Notes

| Area | Update | Agent Action |
|---|---|---|
| **2022 Revised Implementation Guidance** | TSP Section 100 implementation guidance updated with expanded points of focus | Always reference 2022 revised guidance when identifying criteria; use updated points of focus for evidence evaluation |
| **SOC Vendor Ethics (2024–2025)** | AICPA investigating allegations about SOC 2 tool providers; ethics considerations for CPA firms with business arrangements with compliance vendors | If the user mentions using a SOC compliance automation vendor, flag potential independence concerns and advise consulting AICPA Ethics Staff Insights |
| **Peer Review and Licensing** | SOC auditors must be enrolled in AICPA peer review and properly licensed in their state | When engaging a practitioner, confirm peer review enrollment and state licensing |
| **SSAE 18 Continuing Applicability** | SSAE 18 remains the governing standard; SSAE Nos. 19–22 provide conforming amendments to specific AT-C sections | Cite SSAE 18 and applicable AT-C sections; note SSAE 19–22 amendments where relevant |
| **AI and Automation Impact** | Growing use of automated evidence collection, continuous control monitoring, and GRC platforms | Evaluate automated evidence for reliability; ensure automated testing covers the full examination period; document how automated tools were used in testing |
| **No SAS 70/SSAE 16 References** | Both are superseded; never reference in current engagements | If user references SAS 70 or SSAE 16, correct immediately: SAS 70 → superseded June 2011; SSAE 16 → superseded May 2017; current standard is SSAE 18 |
| **ISO 27001:2022 Transition** | ISO 27001:2022 replaced the 2013 edition; Annex A restructured to 93 controls in 4 themes | Use ISO 27001:2022 numbering in cross-references; note 2013 equivalents where needed for backward compatibility |

**SSAE Amendment Note:** SSAE 18 remains the governing standard; SSAE Nos. 19–22 have been issued as amendments to specific AT-C sections (conforming amendments). Practitioners should verify the current text of the relevant AT-C section to ensure any SSAE 19–22 amendments are reflected.

---

## 28. Ethics and Independence Requirements

**Agent Action:** The practitioner must comply with the AICPA Code of Professional Conduct. Flag any of the following as independence threats:

- **Self-interest threat:** CPA firm has a financial interest in the service organization
- **Self-review threat:** CPA firm provided consulting services that are now subject to examination
- **Advocacy threat:** CPA firm promotes or advocates for the service organization
- **Familiarity threat:** Long-standing relationship with service organization management
- **Undue influence threat:** Service organization pressures the practitioner on opinion
- **Management participation threat:** CPA firm acts as management or designs the controls being examined

**If the user asks about a CPA firm providing both consulting and SOC examination services:** Advise that the consulting work may impair independence for the SOC examination. Recommend using separate firms or establishing appropriate safeguards per AICPA Code of Professional Conduct.

---

## 29. Quality Control Requirements

- **Peer review:** CPA firms performing SOC engagements must be enrolled in the AICPA Peer Review Program
- **Licensing:** Practitioners must hold a valid CPA license in their state of practice
- **Continuing professional education (CPE):** Practitioners must maintain CPE requirements per AICPA and state board rules
- **Engagement quality control review:** For significant or high-risk engagements, a concurring partner review is recommended
- **Documentation retention:** Engagement documentation must be retained per AICPA and state board requirements (typically 5–7 years)

**Agent Action:** When a user engages with SOC examination planning, confirm that the practitioner meets these quality control requirements. If the user is a service organization selecting a CPA firm, advise them to verify peer review status and licensing.

---

*End of AICPA SOC Reporting Agent Skill*