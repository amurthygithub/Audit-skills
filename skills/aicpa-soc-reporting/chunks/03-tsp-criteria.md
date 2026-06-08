---
chunk_id: 03-tsp-criteria
parent_skill: aicpa-soc-reporting
topic: "TSP Section 100 Criteria -- Full 53 Primary Criteria with COSO Mapping and Agent Directives"
load_when: "user needs TSC criteria listings, CC1.1-CC9.2, A/PI/C/P criteria, COSO mapping, or cross-framework mappings"
---

# Chunk 03 -- TSP Section 100 Criteria

## Common Criteria (CC) -- 35 Common Criteria -- REQUIRED

### CC1 Control Environment (COSO Principles 1-5)
| Code | COSO Principle | Description |
|------|---------------|-------------|
| CC1.1 | P1 | Commitment to integrity and ethical values |
| CC1.2 | P5 | Holds individuals accountable for internal control responsibilities |
| CC1.3 | P3 | Specifies competence requirements for personnel |
| CC1.4 | P4 | Commitment to competence |
| CC1.5 | P2 | Oversees internal control responsibilities |

Important: CC1 mapping to COSO is non-sequential. CC1.2->P5 (accountability), CC1.5->P2 (oversight).

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
| CC5.2 | P11 | Deploys through policies and procedures |
| CC5.3 | P12 | Deploys controls through technology |

### CC6 Logical and Physical Access (Supplemental to P12)
| Code | Description |
|------|-------------|
| CC6.1 | Implements logical access security over IT resources |
| CC6.2 | Registers and authorizes new users |
| CC6.3 | Terminates access for terminated/transferred users |
| CC6.4 | Reviews access to protected information |
| CC6.5 | Implements physical access controls |
| CC6.6 | Implements logical access security measures against threats |
| CC6.7 | Implements encryption and data masking controls |
| CC6.8 | Implements anti-malware and endpoint protection |

### CC7 System Operations (Supplemental to P12)
| Code | Description |
|------|-------------|
| CC7.1 | Manages IT infrastructure |
| CC7.2 | Manages system job processing |
| CC7.3 | Detects and handles incidents |
| CC7.4 | Recovers IT infrastructure and data |
| CC7.5 | Uses a defined process for recovery of IT operations |

### CC8 Change Management (Supplemental to P12)
| Code | Description |
|------|-------------|
| CC8.1 | Authorizes changes to the system |
| CC8.2 | Develops, tests, and implements changes |
| CC8.3 | Configures and manages boundaries of changes |

### CC9 Risk Mitigation (Supplemental to P12)
| Code | Description |
|------|-------------|
| CC9.1 | Mitigates technology risks |
| CC9.2 | Manages vendor and supply chain risk |

## Additional Availability Criteria (A) -- 3 Criteria
| Code | Description |
|------|-------------|
| A1.1 | Maintains system availability and backup controls |
| A1.2 | Operates disaster recovery and business continuity plans |
| A1.3 | Implements environmental protections |

## Additional Processing Integrity Criteria (PI) -- 5 Criteria
| Code | Description |
|------|-------------|
| PI1.1 | Processes complete information |
| PI1.2 | Processes valid information |
| PI1.3 | Processes accurate information |
| PI1.4 | Processes information in a timely manner |
| PI1.5 | Processes information per authorization |

## Additional Confidentiality Criteria (C) -- 2 Criteria
| Code | Description |
|------|-------------|
| C1.1 | Identifies and classifies confidential information |
| C1.2 | Protects confidential information |

## Additional Privacy Criteria (P) -- 8 Criteria
| Code | Description | GDPR Map |
|------|-------------|----------|
| P1.1 | Notice -- provides notice about privacy practices | Art. 13-14 |
| P2.1 | Choice and consent | Art. 6-7, Art. 9 |
| P3.1 | Collection -- collects only PII necessary for stated purposes | Art. 5(1)(b)(c) |
| P4.1 | Use, retention, and disposal | Art. 5(1)(e), Art. 17 |
| P5.1 | Access -- provides individuals access to their PII | Art. 15 |
| P6.1 | Disclosure and notice | Art. 44-49 |
| P7.1 | Privacy complaints mechanism | Art. 77-79 |
| P8.1 | Privacy monitoring | Art. 24, Art. 32 |

## Criteria Count Summary
| Category | Count | Required? |
|----------|-------|-----------|
| Common Criteria (CC1.1-CC9.2) | 35 | Always |
| Availability (A1.1-A1.3) | 3 | Optional |
| Processing Integrity (PI1.1-PI1.5) | 5 | Optional |
| Confidentiality (C1.1-C1.2) | 2 | Optional |
| Privacy (P1.1-P8.1) | 8 | Optional |
| Grand Total | 53 | |

Note: AICPA commonly references ~66 criteria with sub-criteria and 2022 revised points of focus. Exact sub-criteria count varies by publication (63-69). Verify against current TSP Section 100.

## Cross-Framework Map
### TSC -> NIST 800-53 Rev 5
- CC6 -> AC, PE, IA | CC7 -> AU, SI, CP | CC8 -> CM, SA | CC9 -> RA, SR | P1-P8 -> PT, AR, DI
### TSC -> ISO 27001:2022 Annex A
- Security (CC6) -> 5.15-5.18, 6.5-6.8, 7.1-7.9, 8.1-8.28
- Availability (A1) -> 5.29-5.30, 8.14-8.15
- PI -> 8.7-8.16 | C1 -> 5.12-5.13, 8.10-8.12 | P1-P8 -> 5.34, ISO 27701
### TSC -> COSO
CC1->P1-5 (non-sequential), CC2->P13-15, CC3->P6-9, CC4->P16-17, CC5->P10-12, CC6-9->P12 (supplemental)
### TSC -> COBIT 2019
CC1->EDM01-03, CC2->APO01-02, CC3->APO12-13, CC4->MEA01-03, CC6->DSS05-06, CC7->DSS01-04, CC8->BAI06-07, CC9->APO10/APO12

## Citations
- [TSP-Section-100] | [COSO-2013] | [NIST-SP-800-53-Rev5] | [ISO-27001-2022] | [GDPR]
See SKILL.md Section 10.
