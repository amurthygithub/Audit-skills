---
chunk_id: 04-itgc-itac
parent_skill: isaca-audit-methodology
topic: "IT General Controls and IT Application Controls"
load_when: "user asks about ITGC, ITAC, general controls, application controls, sampling, or IT audit testing"
---

# Chunk 04 - ITGC and ITAC

ITGC are pervasive controls across ALL IT systems. ITAC are controls embedded within specific business applications. You MUST assess both.

## ITGC Category 1: Access Controls / Logical Security

| Control | What to Verify | Test Procedure |
|---------|----------------|----------------|
| 1.1 User Access Provisioning | New user requests authorized, RBAC-aligned | Verify authorization and access levels for sampled users |
| 1.2 User Access Termination | Timely removal on termination (same-day for privileged) | Verify termination list and access removal timeliness |
| 1.3 Access Recertification | Periodic reviews by data/application owners | Verify completeness, timeliness, owner sign-off |
| 1.4 Privileged Access Management | Admin/root accounts controlled, monitored | Review privileged inventory; verify approval and monitoring |
| 1.5 Password Policy | Complexity, rotation, lockout, history | Test AD/IAM configuration; verify enforcement |
| 1.6 Authentication Controls | MFA for remote access, privileged accounts | Verify MFA enrollment and enforcement |
| 1.7 Segregation of Duties | SoD matrices defined and enforced | Review SoD conflict reports; verify compensating controls |

## ITGC Category 2: Change Management

| Control | What to Verify | Test Procedure |
|---------|----------------|----------------|
| 2.1 Change Request Authorization | All changes have documented authorization | Sample change requests; verify authorization |
| 2.2 Change Testing | Changes tested in non-production | Verify test evidence before deployment |
| 2.3 Change Approval (CAB) | CAB approval for standard changes | Verify CAB approval records |
| 2.4 Emergency Changes | Post-implementation review required | Review emergency changes; verify retrospective approval |
| 2.5 Change Implementation | Authorized personnel per approved procedures | Verify implementer authorization |
| 2.6 Rollback Plans | Backout procedures documented and tested | Verify rollback procedures and test evidence |
| 2.7 Post-Implementation Review | PIR for significant changes | Verify PIR documentation |

## ITGC Category 3: IT Operations

| Control | What to Verify | Test Procedure |
|---------|----------------|----------------|
| 3.1 Job Scheduling and Batch Processing | Batch jobs scheduled, monitored, exceptions handled | Review batch logs; verify completion |
| 3.2 Backup and Recovery | Backups per schedule, stored securely, tested | Review schedules and restoration test results |
| 3.3 Problem Management | Incidents tracked, root cause analysis | Review problem tickets; verify RCA |
| 3.4 Data Center Physical Security | Badges, CCTV, visitors, environmental | Verify physical access logs, CCTV coverage |
| 3.5 Environmental Controls | HVAC, fire suppression, power (UPS, generator) | Verify environmental control systems and testing |
| 3.6 System Monitoring | CPU, disk, memory, network monitoring | Review dashboards and alert thresholds |
| 3.7 Output Controls | Report distribution, output reconciliation | Review distribution logs and reconciliation evidence |

## ITGC Category 4: System Development / SDLC

| Control | What to Verify | Test Procedure |
|---------|----------------|----------------|
| 4.1 Requirements Definition | Business requirements documented and approved | Sample projects; verify phase approvals |
| 4.2 System Design | Design reviewed and approved by stakeholders | Verify design review and approval evidence |
| 4.3 Testing | Unit, integration, system, UAT completed | Review test plans and results |
| 4.4 Data Conversion | Migration controls (validation, reconciliation) | Review conversion plans; verify reconciliation |
| 4.5 Go-Live Authorization | Go-live approved by appropriate stakeholders | Verify go-live authorization evidence |
| 4.6 Post-Implementation Review | PIR assessing benefits and control effectiveness | Verify PIR documentation |

## ITAC Category 1: Input Controls

| Control | What to Verify | Test Procedure |
|---------|----------------|----------------|
| 1.1 Data Authorization | Input transactions authorized | Sample transactions; verify authorization |
| 1.2 Data Validation | Completeness, format, range, reasonableness | Boundary testing; invalid data rejection |
| 1.3 Duplicate Detection | Prevent duplicate processing | Submit duplicates; verify detection |
| 1.4 Error Handling | Errors detected, logged, corrected with audit trail | Review error logs; verify correction procedures |
| 1.5 Source Document Control | Source documents controlled, numbered, tracked | Trace source documents to processed transactions |

## ITAC Category 2: Processing Controls

| Control | What to Verify | Test Procedure |
|---------|----------------|----------------|
| 2.1 Batch Controls | Batch totals reconciled | Recalculate; compare to system totals |
| 2.2 Sequence Checks | Missing/duplicate items detected | Introduce missing/duplicate items |
| 2.3 Authorization of Processing | Processing steps authorized | Verify processing authorization |
| 2.4 Exception Handling | Exceptions identified, investigated, resolved | Review exception reports |
| 2.5 Automated Calculations | Interest, tax, discounts accuracy | Re-perform independently |
| 2.6 Run-to-Run Totals | Control totals carried forward | Trace processing stages |

## ITAC Category 3: Output Controls

| Control | What to Verify | Test Procedure |
|---------|----------------|----------------|
| 3.1 Output Accuracy | Output reconciled to input/processing | Reconcile output to input/processing totals |
| 3.2 Output Distribution | Reports to authorized recipients only | Verify distribution logs |
| 3.3 Output Review | Management review of key reports | Verify management sign-off |
| 3.4 Error Correction | Proper authorization and audit trail | Test error correction procedures |
| 3.5 Report Integrity | Reports from approved definitions | Verify report definitions are version-controlled |

## ITAC Category 4: Data Integrity Controls

| Control | What to Verify | Test Procedure |
|---------|----------------|----------------|
| 4.1 Database Integrity | Referential, entity, domain integrity | Attempt invalid data insertion |
| 4.2 Data Validation Rules | Business rules at database level | Review/test trigger and constraint config |
| 4.3 Audit Trail | Who, what, when for data changes | Review audit trail configuration |
| 4.4 Data Backup and Recovery | Application-level backup/recovery | Test restoration from backup |
| 4.5 Encryption at Rest | Field-level, database-level, volume-level encryption | Verify per data classification |

## Sampling Methodology

| Method | When to Use | Approach |
|--------|-------------|----------|
| Statistical - Attribute | Pass/fail control testing | n = (Z^2 x p x (1-p)) / P^2, where P = tolerable deviation rate - expected deviation rate. For finite populations, multiply by population factor. See `audit-workpapers/chunks/03-sampling.md` for complete attribute sampling tables. |
| Statistical - Variable | Monetary amounts; substantive | Based on confidence, variance, tolerable misstatement |
| Statistical - MUS | Large populations for overstatement | n = (CF x BV) / TM |
| Non-Statistical - Judgmental | Targeted testing by auditor judgment | Cannot project to population |
| Non-Statistical - Haphazard | Simple selection without structure | May not be representative |
| Non-Statistical - Random | Simple random selection | Cannot evaluate statistically |

## ITGC Assessment Procedure (10 Steps)

1. Understand IT environment. 2. Identify ITGC control objectives. 3. Obtain/review policies and procedures. 4. Perform walkthrough. 5. Design and execute tests. 6. Evaluate design effectiveness. 7. Evaluate operating effectiveness. 8. Document findings (5-part format). 9. Assess ITAC reliance impact. 10. Summarize and form overall opinion.

## ITAC Assessment Procedure (9 Steps)

1. Understand application and data flows. 2. Identify control objectives. 3. Obtain/review documentation. 4. Perform walkthrough. 5. Design and execute tests. 6. Use CAATs for automated testing. 7. Evaluate design and operating effectiveness. 8. Document findings (5-part format). 9. Summarize and form overall opinion.

## ITGC -> ITAC Dependency Decision Logic

```
IF ITGC_effective == TRUE THEN
    ITAC_reliance = TRUE; audit_approach = "controls-based"
ELSE IF ITGC_effective == FALSE THEN
    ITAC_reliance = FALSE; audit_approach = "substantive"
ELSE IF ITGC_effective == PARTIAL THEN
    audit_approach = "hybrid"
    // Controls-based where ITGC effective; substantive where not
END IF
```

## Output template (ITGC Summary)

```yaml
itgc_assessment:
  overall_effectiveness: "PARTIAL"
  categories:
    - name: "Access Controls"
      design: "EFFECTIVE"
      operating: "EFFECTIVE"
      findings: 0
    - name: "Change Management"
      design: "EFFECTIVE"
      operating: "PARTIAL"
      findings: 1
  itac_reliance: "hybrid"
  audit_approach: "hybrid"
```

## Citations

Control categories and procedures from `[CISA-CRM-28E]` and `[ITAF]`. See SKILL.md S10.
