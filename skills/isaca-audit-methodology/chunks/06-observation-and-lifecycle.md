---
chunk_id: 06-observation-and-lifecycle
parent_skill: isaca-audit-methodology
topic: "5-Part Audit Observation Format and Audit Engagement Lifecycle"
load_when: "user asks about audit observations, 5-part format, finding format, audit lifecycle, engagement phases, or audit reporting"
---

# Chunk 06 - Observation Format and Engagement Lifecycle

## 5-Part Audit Observation Format

Use this format for every audit finding in ISACA-methodology engagements. (GAGAS engagements: the Yellow Book defines four elements -- criteria, condition, cause, effect -- developed as needed for the objectives; recommendation is reported separately. See the cross-reference at the end of this chunk.)

### Part 1: Condition (What Is)

Factual description of the current state observed. Must be objective, verifiable, specific (names, dates, numbers, systems). Avoid blame language.

Example: "The organization does not perform periodic access recertification for 3 of 5 critical applications reviewed (SAP ERP, Oracle Financials, Salesforce CRM)."

### Part 2: Criteria (What Should Be)

The standard, policy, regulation, or framework practice against which the condition is measured. Must cite a real, verifiable source the AUDITEE is obligated to meet: company policy clause, regulation, contractual requirement, or COBIT management practice. **ITAF standards govern the auditor's work, not the auditee -- do not cite ITAF as finding criteria.** Never cite an identifier you cannot verify in the source publication.

Example: "Company policy ISP-003 Section 4.2 requires quarterly access recertification for all critical applications; COBIT 2019 DSS05.04 (Manage user identity and logical access) is the corresponding framework practice."

### Part 3: Cause (Why the Condition Exists)

Root cause analysis. Categorize: People, Process, Technology, or Management. Use root cause methodology (5-Whys, fishbone/Ishikawa, fault tree). Address the cause, not the symptom.

Example: "The IT security team lacks automated recertification tooling. (Root Cause: Technology - lack of automation)."

### Part 4: Effect (So What / Impact)

Actual or potential impact. Quantify where possible: financial loss, regulatory penalty, operational disruption. Differentiate actual vs potential impact. Map to COBIT information criteria affected.

Example: "12% of terminated employees retained active access for an average of 45 days. Potential regulatory exposure where GDPR applies: Article 32 infringements carry fines up to EUR 10M or 2% of worldwide turnover under Article 83(4) -- verify the applicable regime and tier before quantifying. Information attributes affected: Confidentiality, Integrity, Compliance." (The "COBIT information criteria" are a COBIT 4.1 construct -- COBIT 2019 uses the goals cascade; treat these tags as a house convention. See chunk 02.)

### Part 5: Recommendation (What Should Be Done)

Specific, actionable, risk-ranked. Address root cause. Provide 3 levels: primary recommendation, compensating control, long-term improvement. Each: action, owner, target date, priority.

## Complete Observation Template

Values marked EXAMPLE are template illustrations -- replace them with engagement facts; never
copy them into a deliverable as evidence. The result envelope wraps the finding (under the
envelope key `observation`) with a `classification` field equal to the severity. Include a
`sample_summary` whenever the finding comes from sample testing, and the documentation fields
(population, period, evidence refs, preparer/reviewer) that let an experienced auditor
reperform the work.

```yaml
classification: "High"
observation:
  id: "ACC-2026-001"
  title: "Inadequate Access Recertification"
  severity: "High"            # judgment call per chunks/05 SFinding Severity -- never a count
  status: "Open"
  condition: "No recertification for 3 of 5 critical applications"
  criteria: "<the auditee's obligation: company policy clause, regulation, or COBIT practice -- never ITAF>"
  cause:
    description: "Lack of automated tooling; insufficient staff"
    root_cause_category: "Technology"
  effect:
    actual: "12% of terminated employees had active access avg 45 days"
    potential: "Unauthorized data access; data breach"
    financial_exposure: "EXAMPLE -- estimate only with evidentiary basis, else omit"
    cobit_criteria_affected: ["Confidentiality", "Integrity", "Compliance"]  # information-attribute tags; see note below
  sample_summary:
    total_applications: 5
    non_compliant: 3
    compliance_rate_pct: 40.0
  documentation:               # AS 1215-style reperformability fields
    population: "All critical financial applications (N=5)"
    selection_method: "100% of population"
    testing_period: "2026-01-01 to 2026-03-31"
    evidence_refs: ["WP-ACC-010", "WP-ACC-011"]
    preparer: "<name, date>"
    reviewer: "<name, date>"
  recommendations:
    - type: "Primary"
      action: "Implement automated recertification tool"
      owner: "CISO"
      target: "Q3 2026"
      priority: "90 Days"
    - type: "Compensating"
      action: "Manual recertification monthly until tool deployed"
      priority: "Immediate"
  management_response:          # EXAMPLE -- populate from the auditee's actual written response
    agreed: true
    action_plan: "Evaluate and procure IGA tool"
    target_date: "2026-09-30"
```

## Complete IT Audit Engagement Lifecycle

Standard references below use the official ITAF series (General 1001-1008, Performance 1201-1207, Reporting 1401-1402); see `chunks/03-itaf-and-maturity.md`.

### Phase 1: PLANNING

| Step | Action | ITAF Standard |
|------|--------|----------|
| 1.1 | Receive engagement request / select from audit plan | 1202 Audit Scheduling |
| 1.2 | Perform preliminary risk assessment | 1201 Risk Assessment in Planning |
| 1.3 | Define audit scope, objectives, constraints | 1203 Engagement Planning |
| 1.4 | Identify relevant controls and control objectives | 1203 Engagement Planning |
| 1.5 | Determine audit approach (controls-based, substantive, hybrid) | 1203 Engagement Planning |
| 1.6 | Develop audit program (test procedures, evidence requirements) | 1203 Engagement Planning |
| 1.7 | Allocate resources (team, budget, timeline) | 1203 / 1006 Proficiency |
| 1.8 | Conduct entrance conference | 1203 Engagement Planning |

### Phase 2: FIELDWORK / EXECUTION

| Step | Action | ITAF Standard |
|------|--------|----------|
| 2.1 | Gather and evaluate audit evidence | 1205 Evidence |
| 2.2 | Test ITGC (access, change, operations, SDLC) | 1204 Performance and Supervision |
| 2.3 | Test ITAC (input, processing, output, data integrity) | 1204 Performance and Supervision |
| 2.4 | Perform walkthrough testing | 1204 Performance and Supervision |
| 2.5 | Perform sampling-based testing | 1204 / 1205 |
| 2.6 | Use CAATs for data analytics | 1204 / 1205 |
| 2.7 | Evaluate control design and operating effectiveness | 1204 Performance and Supervision |
| 2.8 | Document test results and working papers | 1204 Performance and Supervision |
| 2.9 | Notify management of significant findings | 1401 Reporting |

### Phase 3: REPORTING

| Step | Action | ITAF Standard |
|------|--------|----------|
| 3.1 | Classify findings by risk severity | 1401 Reporting |
| 3.2 | Draft audit observations (5-part format) | 1401 Reporting |
| 3.3 | Compile executive summary and detailed findings | 1401 Reporting |
| 3.4 | Conduct exit conference with auditee | 1401 Reporting |
| 3.5 | Obtain management responses | 1401 Reporting |
| 3.6 | Finalize audit report | 1401 Reporting |
| 3.7 | Distribute report per audit charter authority | 1401 / 1001 Audit Charter |

### Phase 4: FOLLOW-UP

| Step | Action | ITAF Standard |
|------|--------|----------|
| 4.1 | Track management action plans | 1402 Follow-up Activities |
| 4.2 | Perform follow-up testing on remediated findings | 1402 Follow-up Activities |
| 4.3 | Verify effectiveness of corrective actions | 1402 Follow-up Activities |
| 4.4 | Escalate overdue/unresolved findings | 1402 Follow-up Activities |
| 4.5 | Update risk assessment based on audit results | 1201 Risk Assessment in Planning |
| 4.6 | Close findings when remediation confirmed | 1402 Follow-up Activities |

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

The ISACA 5-part observation format (Condition, Criteria, Cause, Effect, Recommendation) is the same concept as the audit-workpapers skill's C-C-C-E-R finding format. The element lineage is GAGAS/IIA: GAGAS 2024 defines the elements of a finding as criteria, condition, cause, and effect, developed as needed for the audit objectives (recommendation is not a GAGAS element -- the elements "provide a context for evaluating recommendations"). AS 1215 and AU-C 230 govern audit DOCUMENTATION (retention, reperformability), not the finding format. For government performance audits, note the 4-element-as-needed discipline differs from this skill's "always 5 parts" house rule. See `audit-workpapers/chunks/05-finding-and-workflow.md`.

## Citations

5-part observation convention as taught in `[CISA-CRM-28E]`; finding-element lineage per GAGAS 2024 ch. 8 (see audit-workpapers skill). Lifecycle standard references from `[ITAF]` (1000/1200/1400 series). See SKILL.md S10.
