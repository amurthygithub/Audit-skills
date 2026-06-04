---
chunk_id: 07-outputs-and-cross-refs
parent_skill: isaca-audit-methodology
topic: "Output Templates and Cross-Reference Tables"
load_when: "user asks about audit report template, output format, cross-reference, framework mapping, or terminology glossary"
---

# Chunk 07 - Output Templates and Cross-References

## Audit Report Structure

```markdown
# AUDIT REPORT: [Engagement Title]

## Executive Summary
- Audit objectives and scope
- Overall audit opinion / rating
- Summary of critical and high findings
- Key recommendations

## Background
- Auditable entity description
- Audit engagement context
- Audit period

## Scope and Objectives
- Systems, processes, and locations in scope
- Audit objectives per ISACA standards
- Scope limitations and exclusions

## Audit Approach and Methodology
- Audit approach (controls-based, substantive, hybrid)
- Sampling methodology
- Testing period and coverage
- Standards applied (ITAF, COBIT, regulatory)

## Detailed Findings
### Finding [ID]: [Title] - [Severity]
- Condition, Criteria, Cause, Effect, Recommendation
- Management Response

## ITGC Assessment Summary
| Category | Control Objective | Design | Operating | Findings |
|----------|-------------------|--------|-----------|----------|

## ITAC Assessment Summary
| Category | Control Objective | Design | Operating | Findings |
|----------|-------------------|--------|-----------|----------|

## Appendix
- A: Audit program
- B: Sampling details
- C: Evidence inventory
```

## Audit Observation Template (Expanded)

```markdown
## Finding [ID]: [Title]
**Severity:** [Critical | High | Medium | Low]
**Status:** [Open | Remediated | Accepted Risk | Escalated]

### Condition
[What is - factual, objective, specific]

### Criteria
[What should be - standard, policy, regulation]
- Source: [ISACA Standard X / COBIT Y / Company Policy Z]

### Cause
[Why the condition exists]
- Root Cause Category: [People | Process | Technology | Management]

### Effect
- Actual Impact: [Description]
- Potential Impact: [Description]
- Financial Exposure: [Estimate]
- Regulatory Risk: [Penalties]

### Recommendation
1. [Primary - address root cause]
2. [Compensating - interim mitigation]
3. [Long-term - continuous enhancement]
**Responsible Party:** [Role]
**Target Date:** [Date]
**Priority:** [Immediate | 30 Days | 90 Days | Next Quarter]

### Management Response
**Agree/Disagree:** [Disposition]
**Action Plan:** [Description]
**Target Date:** [Date]
**Owner:** [Role]
```

## ISACA to COSO Mapping

| ISACA/COBIT | COSO Component | Mapping |
|-------------|---------------|---------|
| COBIT EDM objectives | Board governance / Internal Environment | Map governance practices to COSO board oversight |
| COBIT APO objectives | Control Activities | Map IT-specific controls to COSO control activity principles |
| COBIT EDM03 (Risk) | Risk Assessment | Align IT risk assessment with COSO enterprise risk assessment |
| COBIT MEA objectives | Monitoring Activities | Map IT monitoring to COSO ongoing and separate evaluations |
| ITGC controls | Control Environment + Control Activities | Map to COSO control environment principles and control activities |

## ISACA to AICPA/SOC Mapping

| ISACA/COBIT | AICPA Trust Services Criteria | Mapping |
|-------------|-------------------------------|---------|
| ITGC testing | SOC 1/SOC 2 TSC | ITGC results support TSC |
| COBIT DSS05 | SOC 2 Security | Map security services to Security criteria |
| COBIT DSS04 | SOC 2 Availability | Map continuity to Availability criteria |
| COBIT BAI/DSS | SOC 2 Processing Integrity | Map change mgmt and ops to PI |
| COBIT APO13/DSS05 | SOC 2 Confidentiality | Map security to Confidentiality |
| ISACA audit procedures | AT-C 105/205/320 (SOC 1) | IS audit procedures support Type I/II |

## ISACA to NIST CSF 2.0 Mapping

| ISACA/COBIT | NIST CSF 2.0 | Mapping |
|-------------|-------------|---------|
| COBIT EDM | Govern | Map governance to NIST Govern function |
| COBIT APO | Identify | Map planning to NIST Identify function |
| COBIT DSS05/DSS06 | Protect | Map security/process controls to Protect |
| COBIT MEA | Detect | Map monitoring to NIST Detect |
| COBIT DSS02/DSS03 | Respond | Map incident/problem to Respond |
| COBIT DSS04 | Recover | Map continuity to Recover |

## ISACA to ISO 27001/27002 Mapping

| ISACA/COBIT | ISO 27001/27002 | Mapping |
|-------------|---------------|---------|
| COBIT APO13 + DSS05 | ISO 27001 Annex A | Map Managed Security and Security Services to Annex A controls |
| COBIT governance | ISO 27001 ISMS | COBIT governance supports ISMS implementation |
| COBIT management practices | ISO 27002 Controls | Map detailed practices to ISO 27002 control guidance |

## ISACA to ITIL Mapping

| ISACA/COBIT | ITIL | Mapping |
|-------------|------|---------|
| APO02, APO05 | Service Strategy | Map strategy and portfolio management |
| APO03, BAI | Service Design | Map architecture and build/acquire |
| BAI06, BAI07 | Service Transition | Map change management and acceptance |
| DSS01, DSS02 | Service Operation | Map operations and incident management |
| MEA01, MEA02, MEA03 | Continual Service Improvement | Map monitoring and assessment |

## Key Terminology

| Term | Definition |
|------|-----------|
| Audit Charter | Document establishing audit function purpose, authority, responsibility |
| Audit Universe | Complete inventory of all auditable entities |
| Audit Risk | AR = Inherent Risk x Control Risk x Detection Risk |
| Inherent Risk | Susceptibility before considering controls |
| Control Risk | Risk that controls will not prevent/detect misstatement |
| Detection Risk | Risk that auditor procedures will not detect misstatement |
| Materiality | Threshold above which deficiencies are significant |
| CAATs | Computer-Assisted Audit Techniques |
| Walkthrough | Tracing a single transaction through entire process |
| Substantive Testing | Tests verifying accuracy/validity/completeness of balances/transactions |
| Compliance Testing | Tests verifying controls operate as designed |
| Compensating Control | Alternative control mitigating missing/weak primary control |
| Preventive Control | Prevents errors before they occur (e.g., access controls) |
| Detective Control | Detects errors after occurrence (e.g., reconciliation, monitoring) |
| Corrective Control | Corrects errors after detection (e.g., patching, IR) |
| RBAC | Role-Based Access Control |
| SoD | Segregation of Duties |
| MFA | Multi-Factor Authentication |
| CAB | Change Advisory Board |
| BIA | Business Impact Analysis |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| SOC 1 | Service Org Control Report (ICFR controls). Can be Type I (design only) or Type II (design + operating effectiveness) |
| SOC 2 | Service Org Control Report (TSC-based). Can be Type I (design only) or Type II (design + operating effectiveness) |
| ICFR | Internal Controls over Financial Reporting |

## Citations

Output formats from `[CISA-CRM-28E]`. Cross-references from `[COBIT-2019]`, `[NIST-CSF-2.0]`, `[ISO-27001-2022]`, `[COSO-2013]`, `[AICPA-TSC-2017]`. See SKILL.md S10.