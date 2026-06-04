---
chunk_id: 06-observation-and-lifecycle
parent_skill: isaca-audit-methodology
topic: "5-Part Audit Observation Format and Audit Engagement Lifecycle"
load_when: "user asks about audit observations, 5-part format, finding format, audit lifecycle, engagement phases, or audit reporting"
---

# Chunk 06 - Observation Format and Engagement Lifecycle

## 5-Part Audit Observation Format

Use this format for EVERY audit finding. No exceptions.

### Part 1: Condition (What Is)

Factual description of the current state observed. Must be objective, verifiable, specific (names, dates, numbers, systems). Avoid blame language.

Example: "The organization does not perform periodic access recertification for 3 of 5 critical applications reviewed (SAP ERP, Oracle Financials, Salesforce CRM)."

### Part 2: Criteria (What Should Be)

The standard, policy, regulation, or best practice against which the condition is measured. Must cite the source: ISACA Standard, COBIT Objective, regulatory requirement, company policy.

Example: "ISACA Standard S17 and company policy ISP-003 require quarterly access recertification for all critical applications."

### Part 3: Cause (Why the Condition Exists)

Root cause analysis. Categorize: People, Process, Technology, or Management. Use root cause methodology (5-Whys, fishbone/Ishikawa, fault tree). Address the cause, not the symptom.

Example: "The IT security team lacks automated recertification tooling. (Root Cause: Technology - lack of automation)."

### Part 4: Effect (So What / Impact)

Actual or potential impact. Quantify where possible: financial loss, regulatory penalty, operational disruption. Differentiate actual vs potential impact. Map to COBIT information criteria affected.

Example: "12% of terminated employees retained active access for an average of 45 days. Potential regulatory penalties under GDPR Article 32. COBIT criteria affected: Confidentiality, Integrity, Compliance."

### Part 5: Recommendation (What Should Be Done)

Specific, actionable, risk-ranked. Address root cause. Provide 3 levels: primary recommendation, compensating control, long-term improvement. Each: action, owner, target date, priority.

## Complete Observation Template

```yaml
finding:
  id: "ACC-2026-001"
  title: "Inadequate Access Recertification"
  severity: "High"
  status: "Open"
  condition: "No recertification for 3 of 5 critical applications"
  criteria: "ISACA S17; ISP-003 Section 4.2; COBIT APO13.02"
  cause:
    description: "Lack of automated tooling; insufficient staff"
    root_cause_category: "Technology"
  effect:
    actual: "12% of terminated employees had active access avg 45 days"
    potential: "Unauthorized data access; data breach"
    financial_exposure: "$500K-$5M per incident"
    cobit_criteria_affected: ["Confidentiality", "Integrity", "Compliance"]
  recommendations:
    - type: "Primary"
      action: "Implement automated recertification tool"
      owner: "CISO"
      target: "Q3 2026"
      priority: "90 Days"
    - type: "Compensating"
      action: "Manual recertification monthly until tool deployed"
      priority: "Immediate"
  management_response:
    agreed: true
    action_plan: "Evaluate and procure IGA tool"
    target_date: "2026-09-30"
```

## Complete IT Audit Engagement Lifecycle

### Phase 1: PLANNING

| Step | Action | Standard |
|------|--------|----------|
| 1.1 | Receive engagement request / select from audit plan | S5 |
| 1.2 | Perform preliminary risk assessment | S17 |
| 1.3 | Define audit scope, objectives, constraints | S5 |
| 1.4 | Identify relevant controls and control objectives | S5 |
| 1.5 | Determine audit approach (controls-based, substantive, hybrid) | S5 |
| 1.6 | Develop audit program (test procedures, evidence requirements) | S5 |
| 1.7 | Allocate resources (team, budget, timeline) | S3 |
| 1.8 | Conduct entrance conference | S7 |

### Phase 2: FIELDWORK / EXECUTION

| Step | Action | Standard |
|------|--------|----------|
| 2.1 | Gather and evaluate audit evidence | S13 |
| 2.2 | Test ITGC (access, change, operations, SDLC) | S6 |
| 2.3 | Test ITAC (input, processing, output, data integrity) | S6 |
| 2.4 | Perform walkthrough testing | S6 |
| 2.5 | Perform sampling-based testing | S14 |
| 2.6 | Use CAATs for data analytics | S11 |
| 2.7 | Evaluate control design and operating effectiveness | S6 |
| 2.8 | Document test results and working papers | S15 |
| 2.9 | Notify management of significant findings | S7 |

### Phase 3: REPORTING

| Step | Action | Standard |
|------|--------|----------|
| 3.1 | Classify findings by risk severity | S7 |
| 3.2 | Draft audit observations (5-part format) | S7 |
| 3.3 | Compile executive summary and detailed findings | S7 |
| 3.4 | Conduct exit conference with auditee | S7 |
| 3.5 | Obtain management responses | S7 |
| 3.6 | Finalize audit report | S7 |
| 3.7 | Distribute report per audit charter authority | S7 |

### Phase 4: FOLLOW-UP

| Step | Action | Standard |
|------|--------|----------|
| 4.1 | Track management action plans | S8 |
| 4.2 | Perform follow-up testing on remediated findings | S8 |
| 4.3 | Verify effectiveness of corrective actions | S8 |
| 4.4 | Escalate overdue/unresolved findings | S8 |
| 4.5 | Update risk assessment based on audit results | S17 |
| 4.6 | Close findings when remediation confirmed | S8 |

## Audit Approach Decision Logic

```
IF ITGC_effective == TRUE THEN
    audit_approach = "controls-based"
    substantive_testing = REDUCED
ELSE IF ITGC_effective == FALSE THEN
    audit_approach = "substantive"
    substantive_testing = INCREASED
ELSE IF ITGC_effective == PARTIAL THEN
    audit_approach = "hybrid"
END IF
```

## Follow-Up Decision Rules

- Action plan completed and effective -> Close finding.
- Action plan completed but not effective -> Reopen, escalate.
- Action plan overdue >30 days past target -> Escalate to audit committee.
- Management accepts risk -> Document risk acceptance, monitor periodically.

## CAATs Guidance

| CAAT Type | Use | Examples |
|-----------|-----|----------|
| Data Extraction | Large populations; full-population testing | ACL, IDEA, Python |
| Data Analysis | Trend, anomaly detection, calculations | Benford's law, duplicate detection |
| Exception Testing | Control violation identification | Access violations, policy exceptions |
| Re-performance | Calculation verification | Re-run payroll, interest calculations |
| Continuous Auditing | Ongoing monitoring | Automated exception alerts, CCM |


## Cross-Reference: ISACA 5-Part Format and Audit-Workpapers C-C-C-E-R

The ISACA 5-part observation format (Condition, Criteria, Cause, Effect, Recommendation) is the same concept as the audit-workpapers skill's C-C-C-E-R finding format. The labels differ by framework convention -- ISACA uses the 5-part terminology from CISA-CRM-28E while PCAOB-aligned workpapers use C-C-C-E-R from AS 1215/AU-C 230. The underlying structure and five elements are identical and map element-for-element. See `audit-workpapers/chunks/05-finding-and-workflow.md` for the C-C-C-E-R equivalent.

## Citations

5-part format from `[CISA-CRM-28E]`. Lifecycle phases from `[ITAF]` standards S5-S8, S13-S15, S17. See SKILL.md S10.