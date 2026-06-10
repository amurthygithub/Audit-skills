---
chunk_id: 03-tsp-criteria
parent_skill: aicpa-soc-reporting
topic: "TSP Section 100 Criteria -- All 61 Criteria (33 CC + 28 category) with COSO Mapping and Cross-Framework Maps"
load_when: "user needs TSC criteria listings, CC1.1-CC9.2, A/PI/C/P criteria, COSO mapping, or cross-framework mappings"
---

# Chunk 03 -- TSP Section 100 Criteria

Criteria inventory verified verbatim against the 2017 TSC (With Revised Points of Focus -- 2022), retrieved 2026-06-10. The 2017 TSC has **33 common criteria and 61 total criteria**. "Sub-criteria" is not a TSC concept -- the supporting items are **points of focus**, which are not required to be individually addressed.

## Common Criteria (CC) -- 33 Criteria -- REQUIRED for every SOC 2

### CC1 Control Environment (COSO Principles 1-5, mapped SEQUENTIALLY)
| Code | COSO Principle | Description |
|------|---------------|-------------|
| CC1.1 | P1 | Demonstrates commitment to integrity and ethical values |
| CC1.2 | P2 | Board demonstrates independence from management and exercises oversight |
| CC1.3 | P3 | Management establishes, with board oversight, structures, reporting lines, authorities, and responsibilities |
| CC1.4 | P4 | Demonstrates commitment to attract, develop, and retain competent individuals |
| CC1.5 | P5 | Holds individuals accountable for their internal control responsibilities |

CC1.1-CC1.5 are labeled COSO Principles 1-5 in the TSC itself, in order. (An earlier version of this chunk claimed the mapping was "non-sequential" -- that was wrong.)

### CC2 Communication and Information (COSO P13-15)
| Code | COSO Principle | Description |
|------|---------------|-------------|
| CC2.1 | P13 | Obtains/generates and uses relevant, quality information |
| CC2.2 | P14 | Internally communicates information supporting internal control |
| CC2.3 | P15 | Communicates with external parties on matters affecting internal control |

### CC3 Risk Assessment (COSO P6-9)
| Code | COSO Principle | Description |
|------|---------------|-------------|
| CC3.1 | P6 | Specifies objectives with sufficient clarity |
| CC3.2 | P7 | Identifies and analyzes risk |
| CC3.3 | P8 | Assesses fraud risk |
| CC3.4 | P9 | Identifies and analyzes significant changes |

### CC4 Monitoring Activities (COSO P16-17)
| Code | COSO Principle | Description |
|------|---------------|-------------|
| CC4.1 | P16 | Conducts ongoing and/or periodic evaluations |
| CC4.2 | P17 | Evaluates and communicates deficiencies |

### CC5 Control Activities (COSO P10-12)
| Code | COSO Principle | Description |
|------|---------------|-------------|
| CC5.1 | P10 | Selects and develops control activities |
| CC5.2 | P11 | Selects and develops general controls over technology |
| CC5.3 | P12 | Deploys through policies and procedures |

### CC6 Logical and Physical Access Controls (supplemental series)
| Code | Description |
|------|-------------|
| CC6.1 | Implements logical access security software, infrastructure, and architectures over protected information assets |
| CC6.2 | Registers and authorizes new internal and external users before issuing credentials; removes credentials when no longer authorized |
| CC6.3 | Authorizes, modifies, or removes access based on roles and responsibilities, considering segregation of duties |
| CC6.4 | Restricts PHYSICAL access to facilities and protected information assets (data centers, backup media, sensitive locations) to authorized personnel |
| CC6.5 | Discontinues logical and physical protections over physical assets only after data/software recovery ability has been diminished (disposal/sanitization) |
| CC6.6 | Implements logical access security measures against threats from sources outside the system boundary |
| CC6.7 | Restricts the transmission, movement, and removal of information; uses encryption and protection during transmission/movement/removal |
| CC6.8 | Implements controls to prevent or detect and act upon the introduction of unauthorized or malicious software |

### CC7 System Operations (supplemental series)
| Code | Description |
|------|-------------|
| CC7.1 | Uses detection and monitoring procedures to identify (1) configuration changes introducing new vulnerabilities and (2) susceptibilities to newly discovered vulnerabilities |
| CC7.2 | Monitors system components for anomalies indicative of malicious acts, natural disasters, and errors; analyzes anomalies as potential security events |
| CC7.3 | Evaluates security events to determine failures to meet objectives (security incidents) and acts to prevent/address them |
| CC7.4 | Responds to identified security incidents via a defined incident response program |
| CC7.5 | Identifies, develops, and implements activities to recover from identified security incidents |

### CC8 Change Management (supplemental series -- ONE criterion)
| Code | Description |
|------|-------------|
| CC8.1 | Authorizes, designs, develops or acquires, configures, documents, tests, approves, and implements changes to infrastructure, data, software, and procedures |

(The 2017 TSC contains no CC8.2 or CC8.3 -- an earlier version of this chunk invented them.)

### CC9 Risk Mitigation (supplemental series)
| Code | Description |
|------|-------------|
| CC9.1 | Identifies, selects, and develops risk mitigation activities for risks from potential business disruptions |
| CC9.2 | Assesses and manages risks associated with vendors and business partners |

## Additional Availability Criteria (A) -- 3 Criteria
| Code | Description |
|------|-------------|
| A1.1 | Maintains, monitors, and evaluates current processing CAPACITY and use of system components to manage capacity demand |
| A1.2 | Authorizes, designs, operates, and monitors environmental protections, data backup processes, and recovery infrastructure |
| A1.3 | Tests recovery plan procedures supporting system recovery |

## Additional Processing Integrity Criteria (PI) -- 5 Criteria
| Code | Description |
|------|-------------|
| PI1.1 | Obtains/generates and communicates quality information regarding processing objectives and product/service specifications |
| PI1.2 | System inputs are complete and accurate; input events recorded completely and accurately |
| PI1.3 | System processing is complete, accurate, timely, and authorized |
| PI1.4 | System output is complete, accurate, distributed, and retained per specifications |
| PI1.5 | Stores inputs/items in process/outputs completely, accurately, and timely per specifications |

## Additional Confidentiality Criteria (C) -- 2 Criteria
| Code | Description |
|------|-------------|
| C1.1 | Identifies and maintains confidential information to meet confidentiality objectives |
| C1.2 | Disposes of confidential information to meet confidentiality objectives |

## Additional Privacy Criteria (P) -- 18 Criteria across 8 categories
| Code | Category | Description | GDPR Map |
|------|----------|-------------|----------|
| P1.1 | Notice | Provides notice about privacy practices | Art. 13-14 |
| P2.1 | Choice and Consent | Communicates choices and obtains consent | Art. 6-7, Art. 9 |
| P3.1 | Collection | Collects PII consistent with privacy objectives | Art. 5(1)(b)(c) |
| P3.2 | Collection | Obtains explicit consent when required for sensitive PII | Art. 9 |
| P4.1 | Use/Retention/Disposal | Limits use of PII to identified purposes | Art. 5(1)(b) |
| P4.2 | Use/Retention/Disposal | Retains PII only as long as needed | Art. 5(1)(e) |
| P4.3 | Use/Retention/Disposal | Securely disposes of PII | Art. 17 |
| P5.1 | Access | Grants identified/authenticated data subjects access to their PII | Art. 15 |
| P5.2 | Access | Corrects/amends PII or explains denial | Art. 16 |
| P6.1 | Disclosure & Notification | Discloses PII to third parties only with consent for identified purposes | Art. 44-49 |
| P6.2 | Disclosure & Notification | Creates and retains a record of authorized disclosures | Art. 30 |
| P6.3 | Disclosure & Notification | Creates and retains a record of unauthorized disclosures (breach record) | Art. 33(5) |
| P6.4 | Disclosure & Notification | Obtains third-party privacy commitments before sharing PII | Art. 28 |
| P6.5 | Disclosure & Notification | Obtains notification from third parties of unauthorized disclosures | Art. 33(2) |
| P6.6 | Disclosure & Notification | Provides breach notification to affected data subjects/regulators | Art. 33-34 |
| P6.7 | Disclosure & Notification | Accounts for disclosures of PII on data-subject request | Art. 15(1)(c) |
| P7.1 | Quality | Maintains accurate, complete, relevant PII | Art. 5(1)(d) |
| P8.1 | Monitoring & Enforcement | Implements a process for complaints, disputes, and compliance monitoring | Art. 77-79 |

## Criteria Count Summary (verified against TSP Section 100, 2022 PoF edition)
| Category | Count | Required? |
|----------|-------|-----------|
| Common Criteria (CC1.1-CC9.2) | 33 | Always |
| Availability (A1.1-A1.3) | 3 | Optional |
| Processing Integrity (PI1.1-PI1.5) | 5 | Optional |
| Confidentiality (C1.1-C1.2) | 2 | Optional |
| Privacy (P1.1-P8.1) | 18 | Optional |
| Grand Total | 61 | |

The criteria are supported by ~200 points of focus (revised 2022); points of focus guide evaluation and are NOT individually required criteria.

## Cross-Framework Map (category level -- starting points, not authoritative mappings)
### TSC -> NIST 800-53 Rev 5
- CC6 -> AC, PE, IA, SC | CC7 -> SI, AU, IR | CC8 -> CM, SA | CC9 -> SR (vendor risk) | CC3 -> RA | P1-P8 -> PT (Rev 5 integrated privacy; the Rev 4 Appendix J families AR/DI no longer exist)
### TSC -> ISO 27001:2022 Annex A
- Security (CC6) -> 5.15-5.18, 6.5-6.8, 7.1-7.9, 8.1-8.28
- Availability (A1) -> 5.29-5.30, 8.14-8.15
- PI -> 8.7-8.16 | C1 -> 5.12-5.13, 8.10-8.12 | P1-P8 -> 5.34, ISO 27701
### TSC -> COSO
CC1->P1-5 (sequential), CC2->P13-15, CC3->P6-9, CC4->P16-17, CC5->P10-12, CC6-9 (supplemental series)
### TSC -> COBIT 2019
CC1->EDM01-03, CC2->APO01-02, CC3->APO12-13, CC4->MEA01-03, CC6->DSS05-06, CC7->DSS01-04, CC8->BAI06-07, CC9->APO10/APO12

## Citations
- [TSP-Section-100] | [COSO-2013] | [NIST-SP-800-53-Rev5] | [ISO-27001-2022] | [GDPR]
See SKILL.md Section 10.
