---
chunk_id: 05-requirements-7-12
parent_skill: pci-dss-assessment
topic: "Requirements 7-12: access control (7-9), monitoring/testing (10-11), policy and programs (12) — section-level map with paraphrased intent; MFA, logging, scanning/pentest emphasis"
load_when: "user asks about Requirement 7-12, access control, authentication/MFA, physical access, logging and monitoring, vulnerability scanning, penetration testing, or security policies/programs"
---

# Chunk 05 — Requirements 7-12

Section-level map (x.y) with **paraphrased intent** and evidence examples; requirement bodies and testing procedures live in the licensed standard. Items once "best practice until 31 March 2025" are flagged **[in force now]** — mandatory since 2025-03-31, never optional.

## Req 7 — Restrict Access to System Components and Cardholder Data by Business Need to Know (3 sections)

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 7.1 | Governance of access-control processes | access-control policy |
| 7.2 | Access assigned by role/job function on least-privilege, need-to-know | role definitions; access matrix |
| 7.3 | Access enforced via an access-control system with default-deny | system config; deny-by-default proof |

## Req 8 — Identify Users and Authenticate Access to System Components (6 sections)

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 8.1 | Governance of identification/authentication processes | IAM policy |
| 8.2 | Unique IDs; manage the user-account lifecycle; no shared/generic accounts where attributable action is needed | account inventory; joiner/mover/leaver |
| 8.3 | Strong authentication factors; password/passphrase strength | auth-policy config |
| 8.4 | **MFA for all access into the CDE** and for remote network access **[in force now for the broadened CDE coverage]** | MFA enrollment/config |
| 8.5 | MFA systems implemented to resist bypass/replay | MFA hardening review |
| 8.6 | Manage application/system accounts and their authentication factors **[in force now]** | service-account inventory |

## Req 9 — Restrict Physical Access to Cardholder Data (5 sections)

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 9.1 | Governance of physical-security processes | physical-security policy |
| 9.2 | Facility entry controls; restrict/monitor physical access to the CDE | badge logs; CCTV |
| 9.3 | Authorize and manage physical access for personnel and visitors | visitor logs |
| 9.4 | Securely store, distribute, and destroy media containing account data | media-handling/destruction records |
| 9.5 | Protect POI devices from tampering and substitution; periodic inspections **[in force now for the inspection cadence]** | POI inspection log |

## Req 10 — Log and Monitor All Access to System Components and Cardholder Data (7 sections)

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 10.1 | Governance of logging/monitoring processes | logging policy |
| 10.2 | Audit logs capture defined events for all in-scope components | log-field config |
| 10.3 | Protect audit logs from alteration/loss | log-integrity controls |
| 10.4 | Review logs (automated mechanisms for daily review) **[in force now]** | SIEM review records |
| 10.5 | Retain audit-log history (e.g., 12 months, 3 months readily available) | retention config |
| 10.6 | Time-synchronization across systems | NTP config |
| 10.7 | Detect, alert, and respond to failures of critical security control systems **[in force now]** | control-failure alerting |

## Req 11 — Test Security of Systems and Networks Regularly (6 sections)

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 11.1 | Governance of security-testing processes | testing policy |
| 11.2 | Manage/inventory wireless access points; detect rogue wireless | wireless scan results |
| 11.3 | Internal and external **vulnerability scans** (external by an ASV); remediate and rescan | scan reports; ASV attestations |
| 11.4 | Internal and external **penetration testing**; test **segmentation** controls (11.4.5; service providers more often, 11.4.6) | pentest reports |
| 11.5 | Detect intrusions and unexpected file changes | IDS/FIM config |
| 11.6 | **11.6.1** change-and-tamper detection on payment-page headers/content **[in force now]** | page-tamper alerting |

## Req 12 — Support Information Security with Organizational Policies and Programs (10 sections)

| Section | Paraphrased intent | Evidence example |
|---------|--------------------|------------------|
| 12.1 | Overall information-security policy and program | InfoSec policy |
| 12.2 | Acceptable-use policies for end-user technologies | AUP |
| 12.3 | **Targeted Risk Analyses (TRA)** for flexible/periodic activities and the customized approach **[in force now]** | TRA records (see `chunks/07`) |
| 12.4 | PCI DSS compliance management (service-provider responsibility) | governance charter |
| 12.5 | Maintain scope: inventory and **annual scope confirmation** | inventory; scope-confirmation memo |
| 12.6 | Security-awareness program | training records |
| 12.7 | Personnel screening | screening records |
| 12.8 | Manage third-party service-provider (TPSP) risk and responsibilities | TPSP list; responsibility matrix |
| 12.9 | TPSP acknowledgment of responsibility (service-provider side) | written acknowledgments |
| 12.10 | Incident-response plan and readiness | IR plan; test records |

## Cross-references
**12.3** anchors the **Targeted Risk Analysis** used by the customized approach (`chunks/07`). **11.4.5** segmentation testing supports scope reduction (`chunks/02`). **11.6.1** pairs with **6.4.3** (`chunks/04`) for A-EP/ROC e-commerce (`chunks/03`).
