---
name: coso-internal-controls
description: >
  Perform COSO-based internal control assessments including ICIF 2013 principle evaluation,
  SOX 404 management/auditor ICFR work, PCAOB AS 2201 top-down audit approach, deficiency
  classification (deficiency/significant deficiency/material weakness), walkthrough procedures,
  Risk and Control Matrix documentation, entity-level and process-level control assessment,
  COSO 2017 ERM integration, and emerging technology controls (RPA, GenAI, ICSR). Activate
  for any task involving COSO framework application, ICFR assessment, SOX 404 compliance,
  internal control deficiency evaluation, or PCAOB AS 2201 audit procedures.
category: audit
risk: high
source: COSO 2013 ICIF, COSO 2017 ERM, SOX 404, PCAOB AS 2201, SEC Reg S-K Item 308
date_added: 2026-05-25
tags:
  - coso
  - icifr
  - sox404
  - pcaob
  - as2201
  - internal-controls
  - material-weakness
  - significant-deficiency
  - deficiency-classification
  - walkthrough
  - entity-level-controls
  - risk-and-control-matrix
  - erm
  - icif-2013
  - fraud-risk
  - audit-committee
  - compensating-controls
  - rpa-controls
  - genai-controls
  - icsr
---

# COSO Internal Controls — Agent Skill

You are an expert agent performing COSO-based internal control assessment work. Follow every instruction below precisely. Use official COSO/PCAOB terminology exclusively. When producing outputs, use the templates provided. When classifying deficiencies, apply the decision tree as executable logic without deviation.

---

## 1. When to Use / Not Use This Skill

### Use This Skill When:
- Assessing ICFR effectiveness under COSO 2013 ICIF for SOX 404 compliance
- Evaluating any of the 17 COSO principles for presence and functioning
- Performing a PCAOB AS 2201 integrated ICFR audit using the top-down approach
- Designing or executing walkthrough procedures for significant processes
- Classifying control deficiencies (deficiency, significant deficiency, material weakness)
- Documenting a Risk and Control Matrix (RcM) for SOX scoping
- Evaluating entity-level controls vs process-level controls
- Preparing or reviewing Management's Report on ICFR or Auditor's Report on ICFR
- Assessing compensating controls for deficiency mitigation
- Applying COSO 2017 ERM framework for enterprise risk management contexts
- Evaluating internal controls over emerging technologies (RPA, GenAI, ICSR/sustainability)
- Performing monitoring control assessments per COSO 2009 guidance
- Cross-referencing COSO to AICPA, ISACA/COBIT, NIST, ISO 31000, or PCAOB standards
- Drafting deficiency communications to audit committees or management

### Do NOT Use This Skill When:
- The task involves SOC 1/SOC 2 reporting (use AICPA SOC skill instead)
- The task is purely financial statement audit without ICFR (use GAAS/audit skill)
- The task involves IT audit only without COSO mapping (use IT audit skill, then map with this skill)
- The task is a forensic investigation (use forensic accounting skill, then assess COSO implications)
- The entity is non-US and not subject to SOX/PCAOB (use local regulatory framework, adapt COSO principles)

---

## 2. COSO 2013 Internal Control — Integrated Framework (ICIF)

### 2.1 Definition of Internal Control

> Internal control is a process, effected by an entity's board of directors, management, and other personnel, designed to provide reasonable assurance regarding the achievement of objectives relating to operations, reporting, and compliance.

### 2.2 Three Categories of Objectives

| Category | Description |
|----------|-------------|
| **Operations** | Effectiveness and efficiency of the entity's operations |
| **Reporting** | Reliability of external and internal financial and non-financial reporting |
| **Compliance** | Adherence to applicable laws, regulations, and rules |

### 2.3 Definition of Effective Internal Control

Internal control is **effective** when BOTH conditions are met:
1. **Present and Functioning**: Each of the five components and relevant principles is present and functioning.
2. **Operating in Integrated Manner**: The five components are operating together in an integrated manner.

A principle is **present** when the components and relevant principles associated with it exist in the design and implementation of the system of internal control. A principle is **functioning** when it continues to exist and operate as designed.

When evaluating effectiveness, the agent MUST assess both conditions for each component and principle.

### 2.4 Reasonable Assurance Standard

Internal control provides **reasonable assurance**, not absolute assurance. Limitations inherent to any system of internal control include:
- Human judgment in decision-making can be faulty
- Breakdowns can occur from human error (mistakes, fatigue)
- Collusion among individuals can circumvent controls
- Management can override controls
- Cost-benefit constraints limit control design

The agent MUST communicate these limitations in any ICFR assessment conclusion.

### 2.5 Component 1: Control Environment

**5 Principles, 21 Points of Focus**

**Principle 1**: The organization demonstrates a commitment to integrity and ethical values.

Points of Focus — The agent SHALL evaluate whether the entity:
- Sets tone at the top — Senior leadership embodies integrity and ethical values through actions and communications
- Establishes standards of conduct — Codified in policies (code of conduct, ethics policies)
- Evaluates adherence to standards — Monitoring mechanisms exist (hotlines, surveys, disciplinary actions)
- Addresses deviations in a timely manner — Consistent enforcement regardless of position

**Principle 2**: The board of directors demonstrates independence from management and exercises oversight of the development and performance of internal control.

Points of Focus — The agent SHALL evaluate whether the entity:
- Establishes oversight responsibilities — Board/audit committee charter documents ICFR oversight
- Applies relevant expertise — Board members have financial reporting and internal control expertise
- Operates independently from management — No undue management influence on board decisions
- Provides oversight for the external auditor and internal audit — Direct reporting lines exist

**Principle 3**: The organization establishes, with board oversight, structures, reporting lines, and appropriate authorities and responsibilities in the pursuit of objectives.

Points of Focus — The agent SHALL evaluate whether the entity:
- Considers structures and reporting lines — Organization charts and reporting hierarchies are defined and current
- Defines, assigns, and limits authorities and responsibilities — Delegation of authority matrices exist
- Specifies competencies needed — Job descriptions and competency frameworks are documented
- Addresses reporting lines and hierarchies — Cross-functional and dotted-line relationships are clear

**Principle 4**: The organization demonstrates a commitment to attract, develop, and retain competent individuals in alignment with objectives.

Points of Focus — The agent SHALL evaluate whether the entity:
- Develops expectations of competence — Competency models are defined for key roles
- Attracts, develops, and retains individuals — Recruitment, training, and retention programs exist
- Plans and prepares for succession — Succession plans exist for key positions
- Evaluates competence and addresses shortcomings — Performance evaluations address competence gaps

**Principle 5**: The organization holds individuals accountable for their internal control responsibilities in the pursuit of objectives.

Points of Focus — The agent SHALL evaluate whether the entity:
- Enforces accountability through policies and procedures — Accountability is codified in policy
- Establishes performance measures, incentives, and rewards — Compensation and incentive structures are defined
- Evaluates performance measures, incentives, and rewards for possible unintended consequences — Incentive review is performed
- Considers excessive pressures — Pressure assessment is conducted (unrealistic targets, resource constraints)
- Evaluates performance and rewards/actions for alignment with internal control standards of conduct — Consistency between incentives and ethical standards is monitored

### 2.6 Component 2: Risk Assessment

**4 Principles, 16 Points of Focus**

**Principle 6**: The organization specifies objectives with sufficient clarity to enable the identification and assessment of risks relating to objectives.

Points of Focus — The agent SHALL evaluate whether the entity has defined:
- Operations objectives — Measurable targets for operational effectiveness and efficiency
- External financial reporting objectives — Conformity with applicable GAAP/IFRS frameworks
- External non-financial reporting objectives — Regulatory, statutory, and stakeholder requirements
- Internal reporting objectives — Management reporting needs for decision-making
- Compliance objectives — Adherence to applicable laws and regulations

**Principle 7**: The organization identifies and analyzes risk as a basis for determining how risk should be managed.

Points of Focus — The agent SHALL evaluate whether the entity:
- Identifies and assesses risk that impacts objectives — Risk inventory and risk assessment process exists
- Assesses fraud risk — Fraud risk assessment is performed considering incentives/pressures, opportunities, and attitudes/rationalizations (see also Principle 8)
- Identifies and assesses significant change — Environmental, process, and organizational changes are evaluated for risk impact

**Principle 8**: The organization considers the potential for fraud in assessing risks to the achievement of objectives.

Points of Focus — The agent SHALL evaluate whether the entity considers:
- Incentives and pressures — Financial targets, compensation structure, personal pressures
- Opportunities — Weak controls, management override capability, related-party transactions
- Attitudes and rationalizations — Ethical environment, justification culture, historical issues
- Management override — Explicit assessment of risk that management can circumvent controls

**Principle 9**: The organization identifies and assesses changes that could significantly impact the system of internal control.

Points of Focus — The agent SHALL evaluate whether the entity identifies and assesses:
- Changes in external environment — Regulatory, economic, competitive, market
- Changes in business model — Mergers, acquisitions, divestitures, new business lines
- Changes in leadership — C-suite, board, key management turnover
- Changes in systems, processes, and technology — ERP implementations, system migrations, process redesign, RPA/AI deployment

### 2.7 Component 3: Control Activities

**3 Principles, 13 Points of Focus**

**Principle 10**: The organization selects and develops control activities that contribute to the mitigation of risks to the achievement of objectives to acceptable levels.

Points of Focus — The agent SHALL evaluate whether the entity:
- Integrates with risk assessment — Control activities are linked to assessed risks
- Considers mix of control types — Preventive and detective controls; manual and automated controls are appropriately mixed
- Considers at what level activities are applied — Entity-wide, process-level, and transaction-level controls are applied appropriately
- Addresses segregation of duties — Incompatible duties are separated; mitigating controls exist where separation is impractical
- Evaluates design effectiveness — Controls are designed to meet control objectives
- Evaluates operating effectiveness — Controls operate as designed by competent personnel

**Principle 11**: The organization selects and develops general control activities over technology.

Points of Focus — The agent SHALL evaluate whether the entity has controls over:
- Technology infrastructure — Data centers, network operations, cloud infrastructure
- Security management — Logical access (user provisioning, authentication, authorization) and physical access
- Technology acquisition, development, and maintenance — SDLC, system implementation, vendor management
- Technology change management — Program change controls, emergency change procedures, change approval

**Principle 12**: The organization deploys control activities through policies and procedures.

Points of Focus — The agent SHALL evaluate whether the entity:
- Establishes policies — Documented policies define what is expected
- Establishes procedures — Documented procedures define how policies are executed
- Deploys through policies and procedures — Policies and procedures are communicated, trained, and enforced

### 2.8 Component 4: Information and Communication

**3 Principles, 13 Points of Focus**

**Principle 13**: The organization obtains or generates and uses relevant, quality information to support the functioning of internal control.

Points of Focus — The agent SHALL evaluate whether the entity:
- Identifies information requirements — Defines data needed for each component and objective
- Captures/obtains internal and external data — Sources are defined and reliable
- Processes data into quality information — Data transformation produces accurate, complete, timely information
- Evaluates sufficiency and currency — Information is reviewed for continuing relevance and timeliness

**Principle 14**: The organization internally communicates information, including objectives and responsibilities, necessary to support the functioning of internal control.

Points of Focus — The agent SHALL evaluate whether the entity:
- Communicates throughout the organization — Downward, upward, and cross-functional communication exists
- Provides separate communication lines — Whistleblower hotlines, fraud reporting, bypass channels exist
- Communicates with the board — Regular board reporting on ICFR, risk, and compliance
- Communicates with the audit committee — Direct reporting on internal control matters

**Principle 15**: The organization communicates with external parties regarding matters affecting the functioning of internal control.

Points of Focus — The agent SHALL evaluate whether the entity:
- Communicates with external parties — Customers, suppliers, partners receive relevant information
- Receives and considers input from external parties — Feedback mechanisms exist and are acted upon
- Communicates with regulators — Regulatory correspondence and reporting is timely and complete
- Provides information to customers and suppliers — Contractual and regulatory information sharing
- Communicates to shareholders and stakeholders — Investor relations, annual reports, ICFR disclosures

### 2.9 Component 5: Monitoring Activities

**2 Principles, 8 Points of Focus**

**Principle 16**: The organization selects, develops, and performs ongoing or separate evaluations to ascertain whether each of the five components of internal control is present and functioning.

Points of Focus — The agent SHALL evaluate whether the entity:
- Considers mix of ongoing and separate evaluations — Combines continuous monitoring with periodic assessments
- Considers rate of change — Evaluation frequency matches pace of organizational and environmental change
- Evaluates internal control components for presence and functioning — All 5 components are assessed
- Evaluates through self-assessments, internal audit, and external audit — Multiple evaluation methods are used

**Principle 17**: The organization evaluates and communicates internal control deficiencies in a timely manner to those parties responsible for taking corrective action, including senior management and the board of directors, as appropriate.

Points of Focus — The agent SHALL evaluate whether the entity:
- Assesses results of evaluations — Findings are evaluated for severity (see Section 8: Deficiency Classification)
- Determines severity of deficiencies — Classifies as deficiency, significant deficiency, or material weakness
- Communicates deficiencies to management and board — Reporting follows severity requirements (see Section 8)
- Takes timely corrective action — Remediation plans are documented and tracked

**TOTAL ICIF 2013: 5 Components, 17 Principles, 71 Points of Focus (listed). COSO references 81 including additional PoFs not enumerated above — consult COSO 2013 publication for the complete set.**

---

## 3. COSO 2017 Enterprise Risk Management — Integrating with Strategy and Performance

### 3.1 Four Categories of Objectives

| Category | Description |
|----------|-------------|
| **Strategic** | High-level goals aligned with and supporting the entity's mission |
| **Operations** | Effective and efficient use of the entity's resources |
| **Reporting** | Reliability of the entity's reporting (internal and external) |
| **Compliance** | Compliance with applicable laws and regulations |

### 3.2 Component 1: Governance and Culture (5 Principles)

| Principle | Title |
|-----------|-------|
| P1 | The organization demonstrates commitment to integrity and ethical values |
| P2 | The board of directors provides oversight of enterprise risk management |
| P3 | Management establishes organizational structures, reporting lines, and appropriate authorities and responsibilities in the pursuit of objectives |
| P4 | The organization demonstrates a commitment to attract, develop, and retain competent individuals in alignment with objectives |
| P5 | The organization holds individuals accountable for their enterprise risk management responsibilities |

### 3.3 Component 2: Strategy and Objective-Setting (4 Principles)

| Principle | Title |
|-----------|-------|
| P6 | The organization defines its desired culture, which supports enterprise risk management |
| P7 | The organization identifies, assesses, and manages risk that may impact the achievement of strategy and business objectives |
| P8 | The organization considers the potential for business disruption while determining strategy and business objectives |
| P9 | The organization identifies and assesses risk that may impact the achievement of **strategy and business objectives** _(Editorial note: Strategy-level risk — risks that could alter or undermine the entity's strategic choices and direction)_ |

### 3.4 Component 3: Performance (5 Principles)

| Principle | Title |
|-----------|-------|
| P10 | The organization identifies and assesses risk that may impact the achievement of strategy and business objectives **at the performance level** _(Editorial note: Execution-level risk — risks arising from day-to-day operations, processes, and performance targets)_ |
| P11 | The organization identifies and assesses risk in the entity's portfolio view |
| P12 | The organization analyzes risk in the context of the entity's portfolio |
| P13 | The organization assesses severity of risk |
| P14 | The organization responds to risk based on severity |

### 3.5 Component 4: Review and Revision (3 Principles)

| Principle | Title |
|-----------|-------|
| P15 | The organization identifies and assesses substantial change that may impact strategy and business objectives |
| P16 | The organization reviews the performance of enterprise risk management |
| P17 | The organization pursues improvement in enterprise risk management |

### 3.6 Component 5: Information, Communication, and Reporting (3 Principles)

| Principle | Title |
|-----------|-------|
| P18 | The organization leverages information systems to support enterprise risk management |
| P19 | The organization communicates risk information across the entity |
| P20 | The organization reports on enterprise risk management |

**TOTAL ERM 2017: 5 Components, 20 Principles**

### 3.7 Framework Selection Guidance

When the agent is asked to perform an assessment, determine which framework applies:
- **ICIF 2013**: Use when the objective is ICFR assessment (SOX 404, financial reporting controls), or when evaluating internal controls over operations, reporting, or compliance specifically.
- **ERM 2017**: Use when the objective is enterprise risk management, strategy-risk integration, or when the entity needs a broader risk management framework beyond ICFR.
- Both frameworks may be used together when an entity needs both ICFR compliance and ERM maturity.

---

## 4. SOX Section 404 Requirements

### 4.1 Section 404(a) — Management Assessment

The agent MUST ensure the following management responsibilities are addressed:

1. **Establish and Maintain**: Management is responsible for establishing and maintaining adequate ICFR.
2. **Assess Effectiveness**: Management must assess the effectiveness of ICFR as of the end of the most recent fiscal year.
3. **Identify Framework**: Management must identify the framework used to evaluate effectiveness. COSO 2013 ICIF is the de facto standard and must be named explicitly.
4. **Include in Annual Report**: Management's assessment must be included in the annual report (Form 10-K for SEC registrants).
5. **Disclose Material Weaknesses**: Any material weaknesses identified must be disclosed.
6. **State Auditor Attestation**: Management must state that the registered public accounting firm has issued an attestation report on management's assessment.

When preparing management's assessment, the agent MUST follow the template in Section 12.

### 4.2 Section 404(b) — Auditor Attestation

The agent MUST ensure the following auditor requirements are addressed:

1. **Attest to Management's Assessment**: The company's registered public accounting firm must attest to, and report on, management's assessment of ICFR.
2. **Not a Separate Engagement**: The auditor's attestation cannot be the subject of a separate engagement — it must be integrated with the financial statement audit.
3. **Express Opinion**: The auditor must express an opinion on whether the company maintained, in all material respects, effective ICFR as of the specified date.
4. **Integrated Audit**: The ICFR audit must be integrated with the audit of financial statements per PCAOB AS 2201.

When preparing the auditor's report, the agent MUST follow the template in Section 13.

### 4.3 Section 302 — Disclosure Controls Certification

While SOX 302 addresses disclosure controls and procedures (not ICFR specifically), the agent SHOULD consider:
- CEO and CFO must certify the design and effectiveness of disclosure controls
- Disclosure controls encompass ICFR but are broader (include non-financial information)
- Deficiencies in ICFR may also affect disclosure controls certification

### 4.4 JOBS Act Exemptions

The agent MUST be aware of the following exemptions:
- **Emerging Growth Companies (EGCs)**: Exempt from SOX 404(b) auditor attestation for up to 5 years after IPO (or until revenue exceeds $1.235B, or until classified as a large accelerated filer)
- **Smaller Reporting Companies**: Exempt from SOX 404(b) auditor attestation
- **Non-Accelerated Filers**: Exempt from SOX 404(b) auditor attestation
- **All companies**, regardless of size, remain subject to SOX 404(a) management assessment

---

## 5. PCAOB AS 2201 — Top-Down Approach Methodology

The agent MUST apply the top-down approach when performing or guiding an ICFR audit. Follow the exact sequence below, referencing AS 2201 paragraph numbers.

### 5.1 Planning the Audit (AS 2201.09-.20)

The agent SHALL:
1. **Evaluate entity risk** (AS 2201.10-.12): Consider the company's size, complexity, organizational structure, business units, and risk of misstatement
2. **Address fraud risk** (AS 2201.14-.15): Incorporate fraud risk factors into the ICFR audit plan
3. **Use the work of others** (AS 2201.16-.19): Evaluate the competence and objectivity of internal audit and others whose work may be used; determine the extent to which the auditor can use the work of others
4. **Determine materiality** (AS 2201.20): Apply the same materiality considerations as the financial statement audit
5. **Scale the audit** (AS 2201.13): Adjust the nature, timing, and extent of procedures based on the entity's size and complexity

### 5.2 Top-Down Approach Sequence (AS 2201.21-.41)

The agent MUST follow this exact sequence:

**Step 1 — Financial Statement Level** (AS 2201.21):
Start at the financial statement level. Identify the company's financial statements and the overall risk context.

**Step 2 — Entity-Level Controls** (AS 2201.22-.27):
Identify and evaluate entity-level controls. Classify each ELC by precision:
- **Indirect effect on ICFR** (AS 2201.23): Control environment controls that have a pervasive but indirect effect. These alone do NOT reduce testing of lower-level controls.
- **Operating as monitoring controls** (AS 2201.24-.25): Controls that monitor other controls' effectiveness. May reduce but do not eliminate testing of the controls being monitored.
- **Precise enough to prevent/detect misstatements** (AS 2201.26): Controls designed to operate at a level of precision to prevent or detect misstatements in significant accounts. These MAY eliminate the need for additional testing at the process level.

The agent MUST specifically evaluate controls over the period-end financial reporting process (AS 2201.26-.27):
- Procedures to enter transaction totals into the general ledger
- Procedures for selecting and applying accounting policies
- Procedures to initiate, authorize, record, and process journal entries
- Procedures for recurring and nonrecurring adjustments
- Procedures for preparing financial statements and disclosures

**Step 3 — Significant Accounts and Disclosures** (AS 2201.28-.33):
Identify significant accounts and disclosures. An account or disclosure is significant if there is a reasonable possibility that it could contain a misstatement that, individually or when aggregated with others, would cause the financial statements to be materially misstated.

Consider:
- Size and composition of the account
- Susceptibility to misstatement due to errors or fraud
- Volume of activity, complexity, and homogeneity
- Nature of the account (related parties, significant estimates, etc.)
- Accounting and reporting complexity

**Step 4 — Relevant Assertions** (AS 2201.28-.33):
For each significant account or disclosure, identify the relevant assertions. A relevant assertion is one that has a reasonable possibility of containing a misstatement that would cause the financial statements to be materially misstated.

The five financial statement assertions:
1. **Existence or Occurrence**: Assets/liabilities exist; transactions have occurred
2. **Completeness**: All transactions and events that should have been recorded have been recorded
3. **Valuation or Allocation**: Amounts are recorded at appropriate amounts
4. **Rights and Obligations**: Entity holds rights to assets; obligations are obligations of the entity
5. **Presentation and Disclosure**: Items are appropriately classified, described, and disclosed

**Step 5 — Understanding Likely Sources of Misstatement** (AS 2201.34-.38):
For each relevant assertion, understand the likely sources of misstatement by understanding the flow of transactions. This is accomplished through walkthroughs.

**Step 6 — Select Controls to Test** (AS 2201.39-.41):
Select those controls that are important to the auditor's conclusion about whether the company's controls sufficiently address the assessed risk of misstatement to each relevant assertion. The agent MUST test only key controls — those that address the risk of misstatement to relevant assertions.

### 5.3 Testing Design Effectiveness (AS 2201.42-.43)

The agent SHALL evaluate whether:
- A control, if operated as prescribed by persons possessing the necessary authority and competence, satisfies the company's control objectives
- The control is designed to prevent or detect misstatements that could result in material misstatement

Methods to test design effectiveness:
- Inquiry of personnel
- Inspection of control documentation
- Walkthrough of a transaction (also tests design AND provides understanding)
- Observation of control execution

### 5.4 Testing Operating Effectiveness (AS 2201.44-.61)

The agent SHALL evaluate whether:
- The control is operating as designed
- The person performing the control possesses the necessary authority and competence to perform the control effectively

Testing considerations the agent MUST address:
- **Nature of the test** (AS 2201.44-.46): Inquiry alone is NEVER sufficient; combine with observation, inspection, or re-performance
- **Timing of the test** (AS 2201.48-.50): Test controls over the period being audited; consider interim testing and roll-forward
- **Extent of the test** (AS 2201.51-.52): Sufficient samples to provide enough evidence; consider the frequency of the control and the period being audited
- **Use the work of others** (AS 2201.53-.61): Internal audit, third-party auditors; evaluate competence and objectivity

### 5.5 Forming an Opinion (AS 2201.71-.74)

The agent SHALL form an opinion on the effectiveness of ICFR based on:
1. All evidence obtained from testing design and operating effectiveness
2. Results of walkthroughs
3. Evaluation of identified deficiencies
4. Evaluation of management's assessment process

---

## 6. Walkthrough Procedures

### 6.1 Definition and Purpose (AS 2201.37-.38)

A walkthrough **follows a transaction from origination through the company's processes** including information systems, until it is reflected in the company's financial records, using the **same documents and IT that company personnel use**.

The agent MUST perform walkthroughs for each **major class of transactions** in each significant process.

### 6.2 Required Walkthrough Procedures

At each important processing point, the agent SHALL perform ALL of the following:

1. **Inquiry**: Ask appropriate personnel about their understanding of prescribed procedures and controls. Ask:
   - What is required by the company's prescribed procedures and controls?
   - How are exceptions handled?
   - What happens when an error is identified?
   - How are different types of significant transactions handled?

2. **Observation**: Observe the company's operations and processes in action to verify that procedures are actually performed as described.

3. **Inspection**: Inspect relevant documentation at each processing point, including:
   - Transaction initiation documents (purchase orders, sales orders, etc.)
   - System input screens and outputs
   - Approval signatures and electronic approvals
   - Reconciliation documents
   - Exception reports

4. **Re-performance**: Re-perform selected controls to verify they function as designed (e.g., re-calculate an automated three-way match, re-perform a reconciliation).

### 6.3 Walkthrough Documentation

The agent MUST document the following for each walkthrough:

- Process name and sub-process
- Transaction type followed
- Transaction initiated by (role/person)
- Each processing point traversed
- At each point: inquiry responses, observations, documents inspected, controls re-performed
- IT systems traversed (application names, modules)
- Journal entries and general ledger posting
- Control points where misstatements could arise
- Controls present at key processing points
- Identified gaps (missing or ineffective controls)
- Assessment: Does the walkthrough confirm the design of internal control?

### 6.4 Probing Questions Template

At each key processing point, the agent SHALL ask and document answers to:

| Question | Purpose |
|----------|---------|
| What does the prescribed procedure require? | Verify understanding vs. documented policy |
| Who performs this step? | Confirm segregation of duties and competence |
| What happens when an exception is identified? | Verify error handling and escalation |
| How are errors corrected? | Verify correction controls and re-submission |
| What happens when volumes spike? | Verify scalability and stress controls |
| How does this process interact with IT systems? | Verify IT application and general controls |
| What reports are produced? | Verify detective monitoring controls |
| Who reviews the output? | Verify review and approval controls |

---

## 7. Entity-Level vs Process-Level Controls Classification

### 7.1 Entity-Level Controls (ELC) — AS 2201.22-.27

The agent MUST identify and evaluate the following categories of entity-level controls:

| ELC Category | Examples | Precision | Effect on Process-Level Testing |
|--------------|----------|-----------|-------------------------------|
| **Control environment** (P1-P5) | Tone at the top, code of conduct, governance | Indirect | Does NOT reduce process-level testing |
| **Management override controls** | Review of adjustments, related-party controls | Varies | Moderate reduction if precise |
| **Risk assessment process** (P6-P9) | Enterprise risk assessment, fraud risk assessment | Indirect | Does NOT reduce process-level testing |
| **Centralized processing / shared services** | Shared service centers, centralized reconciliation | Precise | May eliminate process-level testing |
| **Monitoring results of operations** | Budget vs. actual analysis, variance reporting | Monitoring | May reduce but not eliminate testing |
| **Monitoring other controls** | Internal audit, self-assessment, audit committee review | Monitoring | May reduce but not eliminate testing |
| **Period-end financial reporting** (AS 2201.26-.27) | Journal entry controls, accounting policy selection | Precise | May eliminate process-level testing |
| **Significant business control policies** | Risk management policies, compliance programs | Varies | Moderate reduction if precise |

### 7.2 ELC Precision Classification Logic

The agent SHALL classify each ELC as follows:

```
IF the control operates at a level of precision to prevent or detect
   misstatements that could result in material misstatement
   → CLASSIFY AS: Precise ELC
   → EFFECT: May eliminate need for additional testing at the process level

ELSE IF the control monitors the effectiveness of other controls
   → CLASSIFY AS: Monitoring ELC
   → EFFECT: May reduce but does not eliminate testing of monitored controls

ELSE (the control has a pervasive but indirect effect)
   → CLASSIFY AS: Indirect ELC
   → EFFECT: Important to evaluate but does NOT reduce process-level testing
```

### 7.3 Process-Level (Transaction-Level) Controls

The agent MUST identify and evaluate the following categories of process-level controls:

| Control Type | Description | Examples |
|--------------|-------------|----------|
| **Authorization controls** | Approval required before processing | Manager approval of purchase orders, supervisor approval of journal entries |
| **Verification controls** | Independent checking of processing | Three-way match (PO-receipt-invoice), bank reconciliation |
| **Reconciliation controls** | Comparison of records to identify differences | Account reconciliation, intercompany reconciliation |
| **Review controls** | Management review of output | Review of aging reports, review of trial balance |
| **Access controls** | Restriction of system access | Role-based access, segregation of duties enforcement |
| **Application controls** | Controls embedded in IT systems | Edit checks, automated calculations, required fields |
| **Business process controls** | Controls within specific processes | Revenue recognition checklist, inventory count procedures |

### 7.4 IT General Controls (ITGCs)

The agent MUST evaluate ITGCs that support the reliable operation of application controls:

| ITGC Category | What to Evaluate | AS 2201.B1-.B38 Reference |
|---------------|-----------------|---------------------------|
| **Access management** | User provisioning, de-provisioning, review of access rights, privileged access | AS 2201.B4-.B10 |
| **Change management** | Program change controls, emergency changes, change approval, testing, migration | AS 2201.B11-.B16 |
| **IT operations** | Job scheduling, backup/recovery, problem management, data center controls | AS 2201.B17-.B21 |

---

## 8. Control Deficiency Classification — Complete Decision Tree

### 8.1 Definitions (per AS 2201 Appendix A and .62-.70)

**Deficiency**: A defect in the design or operation of ICFR such that a control does not allow management or employees, in the normal course of performing their assigned functions, to prevent or detect misstatements on a timely basis.

**Significant Deficiency**: A deficiency, or combination of deficiencies, in ICFR that is less severe than a material weakness, yet important enough to merit attention by those responsible for oversight of the company's financial reporting.

**Material Weakness**: A deficiency, or combination of deficiencies, in ICFR such that there is a reasonable possibility that a material misstatement of the company's annual or interim financial statements will not be prevented or detected on a timely basis.

### 8.2 Deficiency Classification Decision Tree — Executable Logic

The agent MUST apply the following decision tree when classifying any control deficiency:

```
INPUT: Control deficiency identified
  - Deficiency description
  - Affected accounts/disclosures
  - Affected assertions
  - Compensating controls identified (if any)

STEP 1: DETERMINE IF DEFICIENCY EXISTS
  Question: Is there a defect in the design or operation of ICFR such that a
  control does not allow management or employees, in the normal course of
  performing their assigned functions, to prevent or detect misstatements on
  a timely basis?

  IF NO → NOT A DEFICIENCY → Document rationale → EXIT

  IF YES → PROCEED TO STEP 2

STEP 2: ASSESS REASONABLE POSSIBILITY OF MATERIAL MISSTATEMENT
  Question: Is there a reasonable possibility that the company's ICFR will
  fail to prevent or detect a misstatement of an account balance or disclosure?

  "Reasonable possibility" = neither remote nor certain; a likelihood that is
  more than insignificant.

  IF NO → CLASSIFY AS: DEFICIENCY
    Reporting: Communicate to management (written or oral)
    External: No public disclosure required
    ICFR Opinion Impact: No modification
    → PROCEED TO COMPENSATING CONTROL EVALUATION (Section 14)

  IF YES → PROCEED TO STEP 3

STEP 3: ASSESS MAGNITUDE OF POTENTIAL MISSTATEMENT
  Question: Could the potential misstatement be material to the financial
  statements (annual or interim)?

  Consider:
  - Size of the account balance or disclosure
  - Sensitivity of the assertion to misstatement
  - Likelihood that misstatement could aggregate across accounts
  - Does NOT depend on whether a misstatement actually occurred (AS 2201.65)

  IF MATERIAL → CLASSIFY AS: MATERIAL WEAKNESS
    Reporting: Communicate to audit committee IN WRITING
    External: Must disclose in public filings (Form 10-K)
    ICFR Opinion Impact: ADVERSE opinion — ICFR is NOT effective
     → CHECK MATERIAL WEAKNESS INDICATORS (Section 8.4)
     → PROCEED TO COMPENSATING CONTROL EVALUATION (Section 14)

  IF NOT MATERIAL, but important enough to merit attention by those
     responsible for oversight of financial reporting →
     CLASSIFY AS: SIGNIFICANT DEFICIENCY
    Reporting: Communicate to audit committee IN WRITING
    External: No public disclosure required
    ICFR Opinion Impact: Unqualified (if no material weakness exists)
     → PROCEED TO COMPENSATING CONTROL EVALUATION (Section 14)
```

### 8.3 Severity Assessment Factors (AS 2201.63-.68)

The agent MUST consider the following factors when assessing severity:

| Factor | Consideration |
|--------|---------------|
| **Reasonable possibility** | Likelihood that a misstatement could occur and not be prevented/detected |
| **Magnitude** | Size of the potential misstatement relative to materiality thresholds |
| **Vulnerability** | Susceptibility of the relevant assertion to misstatement |
| **Nature of the account** | Subjectivity, complexity, related-party involvement |
| **Aggregation** | Could small misstatements across multiple accounts aggregate to material? |
| **Actual misstatement** | If a misstatement has already occurred, it is strong evidence; however, absence of actual misstatement does NOT reduce severity |
| **Compensating controls** | Existence and effectiveness of compensating controls (see Section 8.5) |

**CRITICAL RULE**: The severity of a deficiency does NOT depend on whether a misstatement actually occurred. A deficiency may be a material weakness even if no misstatement has occurred (AS 2201.65).

### 8.4 Material Weakness Indicators (AS 2201.69)

The agent MUST treat the following as indicators that a material weakness EXISTS (not merely may exist). When any indicator is present, the agent SHALL classify the deficiency as a material weakness unless compelling evidence demonstrates otherwise:

1. **Identification of fraud, whether or not material, on the part of senior management** — fraud by any member of senior management is per se a material weakness indicator because it undermines the control environment (Principle 1, Principle 5) and suggests management override.

2. **Restatement of previously issued financial statements to reflect the correction of a material misstatement** — a restatement demonstrates that ICFR failed to prevent or detect the misstatement.

3. **Identification of a material misstatement by the auditor that would not have been detected by the company's ICFR** — the auditor's detection demonstrates ICFR failure.

4. **Ineffective oversight of the company's external financial reporting and internal control over financial reporting by the audit committee** — audit committee oversight failure undermines the entire monitoring component.

**Supplementary Consideration** (not per se an AS 2201.69 indicator): Adverse effects on ICFR that would cause prudent officials to conclude they lack reasonable assurance transactions are recorded properly. This is a general standard of reasonableness, not a standalone indicator.

### 8.5 Compensating Control Evaluation Procedure

When a deficiency is identified, the agent SHALL evaluate compensating controls. For the full detailed procedure, see **Section 14**.

```
STEP CC1: IDENTIFY POTENTIAL COMPENSATING CONTROLS — See Section 14.2 Step 2
STEP CC2: EVALUATE COMPENSATING CONTROL PRECISION — See Section 14.2 Step 3
STEP CC3: EVALUATE OPERATING EFFECTIVENESS — See Section 14.2 Step 4
STEP CC4: DOCUMENT AND CONCLUDE — See Section 14.2 Step 6
```

### 8.6 Deficiency Reporting Requirements

| Classification | Communicate to Management | Communicate to Audit Committee | Public Disclosure (SEC) | ICFR Opinion Impact |
|----------------|--------------------------|-------------------------------|------------------------|---------------------|
| **Deficiency** | Yes (oral or written) | Not required unless requested | No | No modification |
| **Significant Deficiency** | Yes (written) | Yes (written, required) | No | No modification (if no MW) |
| **Material Weakness** | Yes (written) | Yes (written, required) | Yes (Form 10-K) | Adverse opinion |

The auditor shall communicate significant deficiencies and material weaknesses in writing to the audit committee per AS 1305 (in addition to AS 2201.62-.70 requirements).

---

## 9. Monitoring Controls Guidance (COSO 2009)

### 9.1 Two Fundamental Principles

The agent SHALL apply the COSO 2009 "Guidance on Monitoring Internal Control Systems" two fundamental principles:

**Monitoring Principle 1**: Ongoing and/or separate evaluations enable management to determine if other components of internal control continue to function over time.

**Monitoring Principle 2**: Internal control deficiencies are identified and communicated in a timely manner to parties responsible for taking corrective action and to management and the board as appropriate.

### 9.2 Three Elements of Monitoring

The agent SHALL structure monitoring assessments using these three elements:

**Element 1 — Establish a Basis for Monitoring**:
- (a) Appropriate tone at the top supporting monitoring activities
- (b) Effective organizational structure assigning monitoring roles to people with appropriate capacity, objectivity, and authority
- (c) Starting point or "baseline" of known effective internal control — the agent MUST determine whether a baseline exists. If no baseline exists, the entity cannot rely on monitoring alone; separate evaluations are required.

**Element 2 — Design and Execute Monitoring Procedures**:
- Focus on **persuasive information** about the operation of **key controls** addressing **significant risks**
- Classify monitoring as:
  - **Ongoing monitoring**: Built into normal operations (e.g., management review of variance reports, continuous audit analytics, reconciliation reviews)
  - **Separate evaluations**: Periodic, specific reviews (e.g., internal audit engagements, self-assessment programs, external audit findings)
- The agent MUST evaluate whether the mix of ongoing and separate evaluations is sufficient given the rate of change and complexity of the entity

**Element 3 — Assess and Report Results**:
- Assess severity of identified deficiencies using the decision tree in Section 8.2
- Report results to appropriate staff and board
- Ensure timely corrective action and follow-up

### 9.3 Monitoring as a Source of Audit Evidence (AS 2201.24-.25)

The agent MAY consider using the results of management's monitoring activities as audit evidence when:
- The monitoring procedures are sufficiently rigorous
- The individuals performing monitoring have adequate competence and objectivity
- The monitoring is performed with sufficient frequency
- The monitoring addresses the same risks as the controls being tested

However, monitoring controls alone CANNOT eliminate the need to test the controls being monitored.

---

## 10. Risk and Control Matrix (RcM) Template

The agent MUST use or produce the following RcM template when documenting SOX scoping. Every column listed is required.

| Column # | Column Name | Description | Example |
|----------|-------------|-------------|---------|
| 1 | **Process Name / Sub-Process** | Business process and sub-process identifier | Revenue / Order-to-Cash |
| 2 | **Risk Statement** | "What could go wrong?" statement describing the risk | Invoices may be generated for fictitious sales, resulting in overstated revenue and receivables |
| 3 | **COSO Component** | Which of the 5 COSO components the risk relates to | Control Activities |
| 4 | **COSO Principle** | Which of the 17 principles the control addresses | P10 |
| 5 | **Control ID** | Unique identifier for the control | RC-010 |
| 6 | **Control Description** | Detailed description of the control | Three-way match of purchase order, receiving report, and vendor invoice prior to payment authorization |
| 7 | **Control Type** | Preventive or Detective | Preventive |
| 8 | **Control Nature** | Manual, Automated, or IT-Dependent Manual | Automated |
| 9 | **Control Frequency** | Daily, Weekly, Monthly, Quarterly, Annual | Daily |
| 10 | **Control Owner** | Role or individual responsible for executing the control | Accounts Payable Manager |
| 11 | **Relevant Assertions** | Existence, Completeness, Valuation, Rights & Obligations, Presentation | Existence, Completeness, Valuation |
| 12 | **Key / Non-Key** | Whether the control is key (sufficiently addresses risk to relevant assertions) or non-key | Key |
| 13 | **Design Effectiveness** | Effective / Ineffective — Does the control, if operated as prescribed, satisfy its objectives? | Effective |
| 14 | **Operating Effectiveness Test Method** | Inquiry, Observation, Inspection, Re-performance, Data Analytics | Re-performance of 25 samples |
| 15 | **Test Results** | Pass / Fail / Not Tested | Pass |
| 16 | **Deficiency Classification** | Deficiency / Significant Deficiency / Material Weakness / None | None |
| 17 | **Remediation Plan** | Planned corrective action with target date | N/A |

### 10.1 RcM Quality Requirements

The agent MUST ensure:
- Every risk has at least one control mapped to it
- Every key control is linked to at least one relevant assertion
- No "orphan" risks (risks with no controls) or "orphan" controls (controls with no mapped risks)
- Control descriptions are specific enough for an independent person to understand and test
- Fraud risk is explicitly addressed (Principle 8 risks must appear in the RcM)
- ITGCs are included for processes dependent on IT systems

---

## 11. COSO Principle Assessment Template

The agent SHALL use the following template to assess each of the 17 COSO 2013 ICIF principles. Complete one template per principle.

```
═══════════════════════════════════════════════════════════
COSO PRINCIPLE ASSESSMENT
═══════════════════════════════════════════════════════════

Principle Number:  [P1–P17]
Principle Title:   [Full principle title]
Component:         [Control Environment / Risk Assessment /
                    Control Activities / Information & Communication /
                    Monitoring Activities]

POINTS OF FOCUS ADDRESSED:
  [ ] PoF 1: [Description] — Assessed: Yes / No / Partially
  [ ] PoF 2: [Description] — Assessed: Yes / No / Partially
  [ ] PoF 3: [Description] — Assessed: Yes / No / Partially
  [ ] PoF 4: [Description] — Assessed: Yes / No / Partially
  [ ] PoF 5: [Description] — Assessed: Yes / No / Partially (if applicable)

ASSESSMENT:
  Present and Functioning?   [ ] Yes  [ ] No  [ ] Partially
  Basis for Assessment:      [Narrative explanation of evidence
                               supporting the assessment conclusion]

EVIDENCE SUPPORTING ASSESSMENT:
  1. [Evidence item 1 — document, interview, observation]
  2. [Evidence item 2]
  3. [Evidence item 3]

IDENTIFIED DEFICIENCIES:
  [ ] None identified
  [ ] Deficiency:            [Description]
  [ ] Significant Deficiency: [Description]
  [ ] Material Weakness:     [Description]

REMEDIAL ACTIONS:
  [ ] No remediation required
  [ ] Remediation Plan:      [Description, owner, target date]

INTEGRATED OPERATION:
  Operating in Integrated Manner with Other Components?
  [ ] Yes  [ ] No
  Explanation:               [How this principle interacts with the
                               other four components to collectively
                               reduce risk to acceptable levels]

═══════════════════════════════════════════════════════════
```

### 11.1 Principle-to-Component Reference

| Principle | Component | Points of Focus Count |
|----------|-----------|----------------------|
| P1 | Control Environment | 4 |
| P2 | Control Environment | 4 |
| P3 | Control Environment | 4 |
| P4 | Control Environment | 4 |
| P5 | Control Environment | 5 |
| P6 | Risk Assessment | 5 |
| P7 | Risk Assessment | 3 |
| P8 | Risk Assessment | 4 |
| P9 | Risk Assessment | 4 |
| P10 | Control Activities | 6 |
| P11 | Control Activities | 4 |
| P12 | Control Activities | 3 |
| P13 | Information & Communication | 4 |
| P14 | Information & Communication | 4 |
| P15 | Information & Communication | 5 |
| P16 | Monitoring Activities | 4 |
| P17 | Monitoring Activities | 4 |

---

## 12. Management's ICFR Report Template

The agent SHALL use the following template when drafting or reviewing Management's Report on Internal Control over Financial Reporting (per SEC Regulation S-K Item 308):

```
MANAGEMENT'S REPORT ON INTERNAL CONTROL OVER FINANCIAL REPORTING

[Company Name] (the "Company") management is responsible for
establishing and maintaining adequate internal control over
financial reporting (as defined in Rules 13a-15(f) and 15d-15(f)
under the Securities Exchange Act of 1934). The Company's internal
control over financial reporting is designed to provide reasonable
assurance regarding the reliability of financial reporting and the
preparation of financial statements for external purposes in
accordance with generally accepted accounting principles.

The Company's internal control over financial reporting includes
those policies and procedures that:

(1) Pertain to the maintenance of records that, in reasonable
    detail, accurately and fairly reflect the transactions and
    dispositions of the assets of the Company;

(2) Provide reasonable assurance that transactions are recorded
    as necessary to permit preparation of financial statements
    in accordance with generally accepted accounting principles,
    and that receipts and expenditures of the Company are being
    made only in accordance with authorizations of management
    and directors of the Company; and

(3) Provide reasonable assurance regarding prevention or timely
    detection of unauthorized acquisition, use, or disposition
    of the Company's assets that could have a material effect on
    the financial statements.

Because of its inherent limitations, internal control over
financial reporting may not prevent or detect misstatements.
Also, projections of any evaluation of effectiveness to future
periods are subject to the risk that controls may become
inadequate because of changes in conditions, or that the degree
of compliance with the policies or procedures may deteriorate.

Management assessed the effectiveness of the Company's internal
control over financial reporting as of [Date], based on the
criteria set forth by the Committee of Sponsoring Organizations
of the Treadway Commission (COSO) in the "Internal Control —
Integrated Framework" (2013).

[OPTIONAL — If no material weaknesses:]
Based on this assessment, management concluded that the Company
maintained effective internal control over financial reporting
as of [Date].

[REQUIRED — If material weaknesses exist:]
Based on this assessment, management identified the following
material weakness(es) as of [Date]:

  [Description of material weakness #1]
  [Description of material weakness #2]

As a result of the material weakness(es) described above,
management concluded that the Company did not maintain effective
internal control over financial reporting as of [Date].

[Remediation disclosure, if applicable:]

Management has taken / is taking the following remedial actions
to address the material weakness(es):

  [Description of remediation actions and timeline]

The Company's independent registered public accounting firm,
[Accounting Firm Name], has issued an attestation report on the
Company's internal control over financial reporting, which
appears [location in filing].

/s/ [Name of Principal Executive Officer]
/s/ [Name of Principal Financial Officer]
[Date]
```

---

## 13. Auditor's ICFR Report Template

The agent SHALL use the following template when drafting or reviewing the Auditor's Report on Internal Control over Financial Reporting (per PCAOB AS 2201.85-.87 and AS 3101):

```
REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM

To the Shareholders and the Board of Directors of [Company Name]

Opinion on Internal Control over Financial Reporting

We have audited [Company Name]'s (the "Company") internal
control over financial reporting as of [Date], based on
criteria established in Internal Control — Integrated Framework
(2013) issued by the Committee of Sponsoring Organizations of the
Treadway Commission (COSO). In our opinion, [Company Name]
maintained, in all material respects, effective internal control
over financial reporting as of [Date], based on criteria
established in Internal Control — Integrated Framework (2013)
issued by the Committee of Sponsoring Organizations of the
Treadway Commission (COSO).

[IF MATERIAL WEAKNESS EXISTS — ADVERSE OPINION:]
In our opinion, because of the effect of the material weakness(es)
described below on the achievement of the basic objectives of
internal control over financial reporting, [Company Name] has not
maintained effective internal control over financial reporting
as of [Date], based on criteria established in Internal Control —
Integrated Framework (2013) issued by the Committee of Sponsoring
Organizations of the Treadway Commission (COSO).

[IF SCOPE LIMITATION — DISCLAIMER:]
We were engaged to audit [Company Name]'s internal control over
financial reporting as of [Date]... [Disclaimer language per
AS 2201.87]

We also have audited, in accordance with the standards of the
Public Company Accounting Oversight Board (United States) (PCAOB),
the [consolidated] balance sheets of [Company Name] as of [Date]
and [Prior Date], and the related [consolidated] statements of
[income, comprehensive income, stockholders' equity, and cash
flows] for each of the [three] years in the period ended [Date],
and the related notes [and financial statement schedule(s)], and
our report dated [Report Date] expressed an [unqualified/adverse]
opinion on those [consolidated] financial statements.

Basis for Opinion

The Company's management is responsible for maintaining effective
internal control over financial reporting and for its assessment
of the effectiveness of internal control over financial reporting
included in the accompanying Management's Report on Internal
Control over Financial Reporting. Our responsibility is to express
an opinion on the Company's internal control over financial
reporting based on our audit. We conducted our audit in accordance
with the standards of the Public Company Accounting Oversight Board
(United States). Those standards require that we plan and perform
the audit to obtain reasonable assurance about whether effective
internal control over financial reporting was maintained in all
material respects.

An audit of internal control over financial reporting includes
obtaining an understanding of internal control over financial
reporting, assessing the risk that a material weakness exists,
testing and evaluating the design and operating effectiveness of
internal control based on the assessed risk, and performing such
other procedures as we considered necessary in the circumstances.
We believe that our audit provides a reasonable basis for our
opinion.

Definition and Inherent Limitations of Internal Control over
Financial Reporting

A company's internal control over financial reporting is a process
designed to provide reasonable assurance regarding the reliability
of financial reporting and the preparation of financial statements
for external purposes in accordance with generally accepted
accounting principles. Internal control over financial reporting
includes those policies and procedures that (1) pertain to the
maintenance of records that, in reasonable detail, accurately and
fairly reflect the transactions and dispositions of the assets of
the company; (2) provide reasonable assurance that transactions
are recorded as necessary to permit preparation of financial
statements in accordance with generally accepted accounting
principles, and that receipts and expenditures of the company are
being made only in accordance with authorizations of management
and directors of the company; and (3) provide reasonable assurance
regarding prevention or timely detection of unauthorized
acquisition, use, or disposition of the company's assets that
could have a material effect on the financial statements.

Because of its inherent limitations, internal control over
financial reporting may not prevent or detect misstatements.
Also, projections of any evaluation of effectiveness to future
periods are subject to the risk that controls may become
inadequate because of changes in conditions, or that the degree
of compliance with the policies or procedures may deteriorate.

[Critical Audit Matters, if applicable:]

Critical Audit Matters

[Description of CAM per AS 3101.18 — if applicable]

[Signature]
[Accounting Firm Name]
[City, State]
[Date]
```

---

## 14. Compensating Control Evaluation — Detailed Procedure

### 14.1 When to Evaluate Compensating Controls

The agent SHALL evaluate compensating controls whenever:
- A control deficiency (at any severity level) is identified
- Management or the auditor asserts that another control mitigates the deficiency
- The preliminary severity classification may change based on compensating controls

### 14.2 Step-by-Step Procedure

```
PROCEDURE: COMPENSATING CONTROL EVALUATION

1. IDENTIFY THE DEFICIENT CONTROL
   - Document the control that is deficient
   - Identify the risk(s) the control was designed to mitigate
   - Identify the relevant assertions affected
   - Determine the preliminary severity classification (per Section 8.2)

2. IDENTIFY POTENTIAL COMPENSATING CONTROLS
   Search for controls that:
   a. Address the SAME risk as the deficient control
   b. Operate at the SAME processing point or at a LATER point in
      the process that could still detect misstatements
   c. Operate INDEPENDENTLY of the deficient control
      (i.e., not dependent on the same personnel, system, or process)

   Types of controls to consider:
   - Reconciliation controls (account reconciliations, intercompany)
   - Analytical review and variance analysis (budget vs. actual, trend)
   - Management review controls (review of reports, KPIs)
   - Monitoring controls (internal audit reviews, continuous monitoring)
   - Alternative authorization controls (secondary approvals)
   - IT application controls (automated validations, edit checks)
   - Physical controls (inventory counts, asset verification)

3. EVALUATE COMPENSATING CONTROL PRECISION
   For each candidate compensating control, ask:
   a. Is the control designed to address the risk that the
      deficient control was intended to address?
   b. Does the control operate at a sufficient level of precision
      to prevent or detect a misstatement that could be material?
   c. Is the control's operating frequency sufficient to detect
      misstatement before financial statements are issued?

   PRECISION TEST:
   - A reconciliation control that matches subsidiary detail to the
     general ledger for the SAME account is generally precise enough.
   - A high-level variance analysis of total revenue is generally
     NOT precise enough to compensate for a specific revenue
     recognition control failure.

4. EVALUATE COMPENSATING CONTROL OPERATING EFFECTIVENESS
   a. Has the control been tested during the current period?
   b. Did the control operate effectively (pass test)?
   c. Was the control operating during the ENTIRE period the
      deficiency existed?
   d. Is the control performed by personnel with adequate
      competence and authority?

5. DETERMINE IMPACT ON SEVERITY CLASSIFICATION

   IF an effective compensating control EXISTS that is precise
   enough to mitigate the risk:
     → The severity of the deficiency MAY be reduced by one level
       - Material Weakness → Significant Deficiency
       - Significant Deficiency → Deficiency
       - Deficiency → Still a Deficiency (no further reduction)
     → Document the compensating control, its precision, its
       operating effectiveness, and the rationale for downgrade

   IF NO effective compensating control exists:
     → Maintain original severity classification
     → Document why no compensating control exists or why existing
       compensating controls are insufficient

6. DOCUMENT CONCLUSION
   Required documentation:
   - Deficient control description and preliminary severity
   - Compensating controls evaluated
   - Precision analysis for each
   - Operating effectiveness assessment for each
   - Final severity classification with rationale
   - Remediation recommendations
```

---

## 15. Cross-References to Other Frameworks and Standards

### 15.1 COSO 2013 ICIF ↔ SOX 404 Mapping

| COSO Component | SOX 404 Relevance |
|----------------|-------------------|
| Control Environment | Entity-level controls; 404(a) assessment requires evaluation of tone, governance, competence, accountability |
| Risk Assessment | Scoping of ICFR assessment; identification of significant accounts, relevant assertions |
| Control Activities | Process-level controls; key controls mapped to relevant assertions |
| Information & Communication | ICFR reporting infrastructure; data integrity; reporting channels |
| Monitoring Activities | Ongoing and separate evaluations; deficiency identification and communication |

### 15.2 COSO 2013 ICIF ↔ COSO 2017 ERM Mapping

| ICIF 2013 Component | ERM 2017 Component | Key Difference |
|----------------------|--------------------|---------------|
| Control Environment | Governance and Culture | ERM adds explicit strategy linkage |
| Risk Assessment | Strategy and Objective-Setting + Performance | ERM integrates risk with strategy; ICIF focuses on ICFR-relevant risks |
| Control Activities | Performance | ERM focuses on risk response; ICIF focuses on control activities |
| Information & Communication | Information, Communication, and Reporting | ERM adds risk reporting explicitly |
| Monitoring Activities | Review and Revision | ERM emphasizes continuous improvement; ICIF emphasizes deficiency communication |

### 15.3 COSO ↔ PCAOB AS 2201 Mapping

| COSO Component | AS 2201 Paragraphs | Key Alignment |
|----------------|-------------------|---------------|
| Control Environment | AS 2201.22-.27 | Entity-level controls; management override |
| Risk Assessment | AS 2201.10-.15, .28-.33 | Risk assessment for planning; significant accounts; relevant assertions |
| Control Activities | AS 2201.39-.61 | Control selection; design and operating effectiveness testing |
| Information & Communication | AS 2201.34-.38 | Understanding flow of transactions; walkthroughs |
| Monitoring Activities | AS 2201.62-.70 | Deficiency identification and evaluation |
| N/A | AS 2201.85-.87 | Auditor's report on ICFR |

### 15.4 COSO ↔ AICPA Standards Mapping

| COSO Component | AICPA Standard | Key Alignment |
|----------------|---------------|---------------|
| Control Environment | AU-C 315, SAS 145 | Understanding the entity and its environment; assessing risks |
| Risk Assessment | AU-C 315, AU-C 330 | Risk identification and assessment; responsive procedures |
| Control Activities | AU-C 330 | Testing controls when substantive approach alone is insufficient |
| Information & Communication | AU-C 260, AU-C 265 | Communication with those charged with governance; communication of deficiencies |
| Monitoring Activities | AU-C 265 | Communication of significant deficiencies and material weaknesses |
| Management Override | AICPA Management Override Guidance | Maps to COSO P1, P5 |

### 15.5 COSO ↔ ISACA/COBIT Mapping

| COSO Component | COBIT 2019 Domain | Key Alignment |
|----------------|-------------------|---------------|
| Control Environment | EDM01-EDM05 (Governance) | Governance objectives, ethical culture, organizational structures |
| Control Activities | APO01-APO13, BAI01-BAI14 | Management of IT processes; build/acquire/implement controls |
| Information & Communication | DSS01-DSS06 | Delivery of IT services; information management |
| Monitoring Activities | MEA01-MEA04 | Monitor, evaluate, and assess performance and compliance |
| Risk Assessment | APO12 (Managed Risk) | IT risk management processes |
| IT General Controls | BAI06 (Managed IT Changes), BAI08 (Managed Knowledge) | Change management, access management |

### 15.6 COSO ↔ NIST Mapping

| COSO Component | NIST Framework | Key Alignment |
|----------------|---------------|---------------|
| Control Environment | NIST CSF — Govern Function | Governance, risk management strategy, supply chain risk management |
| Risk Assessment | NIST RMF Steps 1-3 (Categorize, Select, Implement) | Risk categorization, control selection based on risk |
| Control Activities | NIST CSF — Protect Function, SP 800-53 Control Catalog | Access controls, awareness training, data security, protective technology |
| Information & Communication | NIST CSF — Identify Function | Asset management, governance, risk assessment, supply chain |
| Monitoring Activities | NIST CSF — Detect Function, Respond Function | Anomaly detection, continuous monitoring, incident response |
| NIST RMF Steps 4-6 | Monitor (COSO P16, P17) | Assess, authorize, monitor controls continuously |

### 15.7 COSO ↔ ISO 31000 Mapping

| Aspect | COSO ERM 2017 | ISO 31000:2018 |
|--------|---------------|----------------|
| Risk definition | Risk as potential for negative impact on objectives | Risk as effect of uncertainty on objectives (positive and negative) |
| Risk management approach | Integrated with strategy and performance | Framework + process approach; principles-based |
| Risk assessment steps | Identify → Assess severity → Respond | Identify → Analyze → Evaluate → Treat |
| Distinctive element | Governance & culture, strategy integration | Customization principle, no prescribed structure |
| Applicability | Designed for organizational use | Applicable to any context, organization, or activity |

### 15.8 COSO ↔ AICPA TSC (Trust Services Criteria) Mapping

| COSO 2013 Component | TSC Criteria | Key Alignment |
|----------------------|--------------|---------------|
| Control Environment | CC1.1–CC1.5 | Integrity, accountability, organizational structure, competence, board oversight |
| Communication and Information | CC2.1–CC2.3 | Quality information, internal communication, external communication |
| Risk Assessment | CC3.1–CC3.4 | Objectives, risk identification, fraud risk, change assessment |
| Control Activities | CC5.1–CC5.3 | Risk mitigation controls, IT controls, policy/procedure deployment |
| Monitoring Activities | CC4.1–CC4.2 | Ongoing/separate evaluations, deficiency communication |

Note: TSC criteria CC2-CC5 do NOT map to COSO components in the same numerical order. CC2=Communication & Information (COSO Component 4), CC3=Risk Assessment (COSO Component 2), CC4=Monitoring (COSO Component 5), CC5=Control Activities (COSO Component 3).

For the reverse mapping (TSC → COSO), see Section 22.

---

## 16. 2023–2026 COSO Updates and Emerging Technology Guidance

### 16.1 COSO Fraud Risk Management Guide, 2nd Edition (May 2023)

Published jointly by COSO and ACFE. Key updates:
- Updated anti-fraud developments including developments in cybersecurity and technology-facilitated fraud
- Revised terminology aligned with COSO ICIF 2013 and ERM 2017
- Expanded data analytics guidance for fraud detection and prevention
- Updated legal and regulatory environment (international and US)
- Five fraud risk management principles aligned to COSO ICIF:
  1. Make fraud risk management part of corporate governance
  2. Conduct fraud risk assessment periodically
  3. Select and deploy fraud risk mitigation controls
  4. Communicate fraud risk management policies and procedures
  5. Monitor and improve fraud risk management program

**Agent Action**: When assessing fraud risk (Principle 8), the agent SHALL incorporate COSO Fraud Risk Management Guide 2nd Edition guidance, including data analytics-based detection and the updated fraud risk management principles.

### 16.2 COSO ICSR — Internal Control Over Sustainability Reporting (2023)

Applies the COSO 2013 ICIF to sustainability/ESG reporting. Key points:
- The same 17 COSO principles apply to internal control over sustainability reporting (ICSR)
- "Present and functioning" and "operating in an integrated manner" criteria apply identically
- ICSR extends the Reporting objective category to include sustainability disclosures
- Framework applies regardless of which sustainability reporting standards are used (GRI, SASB/ISSB, TCFD)
- Mapping of COSO principles to sustainability data governance, data quality, and reporting

**Agent Action**: When assessing internal controls over sustainability/ESG reporting, the agent SHALL apply the same 17 principles and assessment methodology from ICIF 2013, adapted for sustainability data characteristics (estimation, forward-looking data, qualitative information, third-party data).

### 16.3 COSO RPA Guidance — Internal Control Over Robotic Process Automation (2024)

Addresses controls for RPA (software bot) environments. Key points:
- RPA bots execute tasks previously performed by humans; bots introduce new risks
- Map RPA risks to COSO ICIF principles:
  - **Control Environment (P1, P5)**: Governance over bot deployment; accountability for bot actions
  - **Risk Assessment (P7, P9)**: Identify risks from bot errors, unauthorized bot access, bot process changes
  - **Control Activities (P10, P11)**: Bot access controls (segregation of duties for bots vs. humans); bot change management controls; bot exception handling; bot monitoring
  - **Information & Communication (P13, P14)**: Data integrity for bot inputs/outputs; bot audit trails
  - **Monitoring (P16)**: Continuous monitoring of bot performance, bot error rates, bot availability

**Agent Action**: When the entity uses RPA, the agent SHALL:
1. Assess whether RPA governance exists (bot inventory, bot ownership, bot change management)
2. Evaluate bot access controls (logical access to bot credentials, bot system access)
3. Evaluate bot change management (bot code changes subject to same change controls as IT systems)
4. Evaluate bot exception handling (how are bot process exceptions identified, escalated, resolved)
5. Evaluate bot monitoring (bot performance metrics, error rates, availability)

### 16.4 COSO GenAI Guidance — Internal Control Over Generative AI (2026)

Addresses controls for generative AI use within organizations. Key points:
- GenAI introduces risks including hallucination, bias, data leakage, unauthorized use, and lack of explainability
- Map GenAI risks to COSO ICIF principles:
  - **Control Environment (P1, P5)**: AI governance policy; acceptable use policy for GenAI; accountability for AI output quality
  - **Risk Assessment (P7, P8, P9)**: AI-specific risk assessment; data poisoning risk; model drift risk; AI use in fraud schemes
  - **Control Activities (P10, P11)**: Input validation controls; output review controls; prompt engineering controls; access controls for AI systems; AI model change management
  - **Information & Communication (P13, P14)**: Data classification for AI training data; AI output quality assurance; AI use disclosure
  - **Monitoring (P16, P17)**: AI model performance monitoring; bias detection; hallucination detection; GenAI deficiency communication

**Agent Action**: When the entity uses generative AI, the agent SHALL:
1. Assess whether an AI governance framework exists (AI policy, AI oversight committee, acceptable use policy)
2. Evaluate AI access controls (who can access AI models, what data can be input, what outputs can be used)
3. Evaluate AI data integrity controls (training data quality, input data validation, output verification)
4. Evaluate AI output monitoring controls (human review of AI outputs, hallucination detection, bias monitoring)
5. Evaluate AI change management controls (model updates, prompt updates, integration changes)
6. Assess whether AI use is disclosed in financial reporting where required

### 16.5 COSO Blockchain and Internal Control (2020)

Addresses controls for blockchain-based systems. Key points:
- Blockchain introduces unique control considerations: decentralized validation, immutability, smart contracts
- Map blockchain risks to COSO principles:
  - Smart contract controls (code review, testing, audit)
  - Private key management (access controls, key custody)
  - Consensus mechanism controls (validation, participation)
  - Data integrity on-chain vs. off-chain

**Agent Action**: When the entity uses blockchain, the agent SHALL evaluate blockchain-specific controls mapped to COSO principles.

---

## 17. Key Terminology Glossary

The agent SHALL use these definitions when performing assessments. All definitions are official COSO or PCAOB terminology.

| # | Term | Definition |
|---|------|-----------|
| 1 | **Internal Control** | A process, effected by an entity's board of directors, management, and other personnel, designed to provide reasonable assurance regarding the achievement of objectives relating to operations, reporting, and compliance |
| 2 | **ICFR** | Internal Control over Financial Reporting — a process designed by or under the supervision of the registrant's principal executive and financial officers to provide reasonable assurance regarding the reliability of financial reporting and the preparation of financial statements for external purposes in accordance with GAAP |
| 3 | **Control Environment** | The set of standards, processes, and structures that provide the basis for carrying out internal control across the organization |
| 4 | **Risk Assessment** | The identification and analysis of relevant risks to the achievement of objectives, forming a basis for determining how risks should be managed |
| 5 | **Control Activities** | The actions established through policies and procedures that help ensure management directives to mitigate risks are carried out |
| 6 | **Information and Communication** | The systems and processes that support the identification, capture, and exchange of information in a form and time frame that enable people to carry out their responsibilities |
| 7 | **Monitoring Activities** | Evaluations to ascertain whether each of the five components of internal control is present and functioning |
| 8 | **Point of Focus** | A characteristic associated with a principle that provides additional detail important for consideration in designing, implementing, and conducting internal control and assessing whether a principle is present and functioning |
| 9 | **Present and Functioning** | A component or principle exists in the system of internal control and is operating as designed to support the achievement of objectives |
| 10 | **Operating in Integrated Manner** | The five components collectively reduce, to an acceptable level, the risk of not achieving an entity's objectives |
| 11 | **Reasonable Assurance** | A high but not absolute level of assurance; acknowledges that internal control cannot eliminate all risk of misstatement due to inherent limitations |
| 12 | **Material Weakness** | A deficiency, or combination of deficiencies, in ICFR such that there is a reasonable possibility that a material misstatement of the company's annual or interim financial statements will not be prevented or detected on a timely basis |
| 13 | **Significant Deficiency** | A deficiency, or combination of deficiencies, in ICFR that is less severe than a material weakness, yet important enough to merit attention by those responsible for oversight of the company's financial reporting |
| 14 | **Deficiency** | A defect in the design or operation of ICFR such that a control does not allow management or employees, in the normal course of performing their assigned functions, to prevent or detect misstatements on a timely basis |
| 15 | **Reasonable Possibility** | A likelihood that is neither remote nor certain; more than an insignificant chance that an event will occur |
| 16 | **Compensating Control** | A control that mitigates the effect of a deficiency in another control; must operate at a level of precision that would prevent or detect a misstatement that could be material |
| 17 | **Top-Down Approach** | An audit approach that begins at the financial statement level, focuses on entity-level controls, and works down to significant accounts, relevant assertions, and process-level controls (AS 2201.21) |
| 18 | **Walkthrough** | A procedure that follows a transaction from origination through the company's processes and information systems until reflected in the company's financial records (AS 2201.37) |
| 19 | **Design Effectiveness** | Whether a control, if operated as prescribed by persons possessing the necessary authority and competence, satisfies the company's control objectives (AS 2201.42) |
| 20 | **Operating Effectiveness** | Whether a control is operating as designed and whether the person performing the control possesses the necessary authority and competence (AS 2201.44) |
| 21 | **Significant Account or Disclosure** | An account or disclosure that has a reasonable possibility of containing a misstatement that would cause the financial statements to be materially misstated (AS 2201.28) |
| 22 | **Relevant Assertion** | A financial statement assertion that has a reasonable possibility of containing a misstatement that would cause the financial statements to be materially misstated (AS 2201.29) |
| 23 | **Entity-Level Control (ELC)** | A control that operates across the entity and has a pervasive effect on ICFR (AS 2201.22) |
| 24 | **Process-Level Control** | A control that operates within a specific business process at the transaction or application level |
| 25 | **Preventive Control** | A control designed to deter errors or fraud before they occur (e.g., segregation of duties, authorization procedures) |
| 26 | **Detective Control** | A control designed to discover errors or fraud after they have occurred (e.g., reconciliations, variance analyses) |
| 27 | **Manual Control** | A control performed by an individual without automation (e.g., manual approval, review of reports) |
| 28 | **Automated Control** | A control performed by information technology without human intervention (e.g., system validations, automated calculations) |
| 29 | **IT-Dependent Manual Control** | A manual control that relies on IT-generated data or reports for its execution |
| 30 | **IT General Control (ITGC)** | Controls that support the reliable operation of IT application controls, encompassing access management, change management, and IT operations |
| 31 | **IT Application Control** | Controls embedded in application software to prevent or detect errors in transaction processing (e.g., edit checks, automated three-way match) |
| 32 | **Management Override** | The ability of management to manipulate or circumvent controls for personal gain or to misstate financial results (COSO P8; AS 2201.14) |
| 33 | **Tone at the Top** | The ethical atmosphere created by an organization's leadership through their actions, communications, and attitudes toward internal control (COSO P1) |
| 34 | **Key Control** | A control that sufficiently addresses the assessed risk of misstatement to a relevant assertion, such that testing it provides sufficient evidence |
| 35 | **Critical Audit Matter (CAM)** | Any matter arising from the current period audit of financial statements that was communicated or required to be communicated to the audit committee, relates to accounts or disclosures that are material, and involved especially challenging, subjective, or complex auditor judgment (AS 3101.11) |
| 36 | **Ongoing Monitoring** | Monitoring activities that are built into normal operations and performed continuously (e.g., management review of variance reports, continuous audit analytics) (COSO P16) |
| 37 | **Separate Evaluation** | A monitoring activity that is performed periodically as a distinct assessment (e.g., internal audit engagement, self-assessment program) (COSO P16) |
| 38 | **Prudent Official Test** | A test considering whether a deficiency's adverse effects would cause prudent officials to conclude they do not have reasonable assurance that transactions are properly recorded (AS 2201 Appendix A) |
| 39 | **ICSR** | Internal Control over Sustainability Reporting — application of COSO ICIF 2013 to ESG/sustainability reporting (COSO 2023) |
| 40 | **RPA** | Robotic Process Automation — software bots that execute repeatable tasks previously performed by humans, requiring specific controls per COSO RPA Guidance (2024) |

---

## 18. Behavioral Requirements for the Agent

The agent SHALL adhere to the following behavioral requirements at all times:

### 18.1 Precision and Terminology
- Use official COSO and PCAOB terminology exclusively (see Section 17)
- Reference AS 2201 paragraph numbers when describing audit procedures
- Reference COSO principle numbers (P1-P17) when evaluating controls
- Never paraphrase definitions; use verbatim official definitions from Section 17
- When classifying deficiencies, apply the decision tree in Section 8.2 exactly

### 18.2 Assessment Rigor
- Assess BOTH "present and functioning" AND "operating in integrated manner" for each COSO component
- Never classify a deficiency without walking through the complete decision tree in Section 8.2
- Never skip the compensating control evaluation (Section 14) before finalizing severity
- Always verify material weakness indicators (Section 8.4) when a deficiency is identified
- Inquiry alone is NEVER sufficient to conclude on operating effectiveness

### 18.3 Documentation Standards
- Complete all columns of the RcM template (Section 10) — no blank required columns
- Complete the Principle Assessment template (Section 11) for all 17 principles
- Document walkthrough procedures per Section 6.2 with all four procedures at each point
- Document compensating control evaluations per Section 14 with all six steps
- Maintain a clear audit trail for every conclusion reached

### 18.4 Framework Compliance
- Always identify and name the framework used (COSO 2013 ICIF or COSO 2017 ERM)
- When assessing ICFR, use COSO 2013 ICIF (not ERM)
- When the entity is subject to SOX 404, follow both SOX 404(a) and 404(b) requirements
- When performing an ICFR audit, follow the AS 2201 top-down approach sequence exactly
- Scale procedures for entity size and complexity per AS 2201.13

### 18.5 Emerging Technology Awareness
- When the entity uses RPA, apply Section 16.3 guidance
- When the entity uses generative AI, apply Section 16.4 guidance
- When assessing sustainability reporting controls, apply Section 16.2 guidance
- When the entity uses blockchain, apply Section 16.5 guidance
- When assessing fraud risk, incorporate COSO Fraud Risk Management Guide 2nd Edition (Section 16.1)

### 18.6 Professional Skepticism
- Maintain professional skepticism throughout all assessments
- Do not accept management representations without corroborating evidence
- Consider the risk of management override in every assessment
- Consider the potential for collusion when evaluating segregation of duties
- Do not assume that absence of detected misstatements means controls are effective

### 18.7 Communication
- Communicate significant deficiencies and material weaknesses to the audit committee in writing
- Use the Management's ICFR Report template (Section 12) for management reporting
- Use the Auditor's ICFR Report template (Section 13) for auditor reporting
- Include all required elements in reports — no omissions
- Provide clear, unambiguous severity classifications with documented rationale

---

## 19. Examples — Realistic SOX/COSO Scenarios

### Example 1: Material Weakness — Fraud by Senior Management

**Scenario**: During the ICFR audit, the auditor discovers that the CFO has been overriding controls to record fictitious revenue in two subsidiary entities, inflating revenue by $8M (material). The CFO acted alone; no other management was involved.

**Agent Analysis**:
1. This is fraud by senior management (CFO).
2. Apply AS 2201.69 indicator #1: "Identification of fraud, whether or not material, on the part of senior management" → This is a per se material weakness indicator.
3. Even though the CFO acted alone, fraud by a member of senior management undermines the Control Environment (P1, P5) and indicates management override (P8).
4. No compensating control can mitigate fraud by the CFO because any control the CFO can override is ineffective.
5. **Classification: Material Weakness**.
6. **Reporting**: Communicate to audit committee in writing; disclose in Form 10-K; auditor issues adverse ICFR opinion.
7. **Affected Principles**: P1 (commitment to integrity and ethical values — NOT present and functioning), P5 (accountability — NOT present and functioning), P8 (fraud risk — NOT present and functioning).

### Example 2: Significant Deficiency — Ineffective IT Access Controls

**Scenario**: The SOX team identifies that IT access provisioning for the ERP system is not properly controlled. Terminated employees retain access for an average of 45 days after termination. No quarterly access review is performed. The deficiency affects the expenditure and payroll processes. No actual misstatement has been detected.

**Agent Analysis**:
1. **Is there a deficiency?** YES — Access provisioning and review controls are not designed or operating effectively. Terminated employee access is a defect in design and operation.
2. **Is there reasonable possibility of misstatement?** YES — Terminated employees could process unauthorized transactions (fictitious vendors, unauthorized payments, ghost employees).
3. **Could the misstatement be material?** ASSESS MAGNITUDE:
   - Average of 45 days' access for terminated employees
   - Number of terminated employees: 120 over the year
   - Maximum transaction authority per role: $5,000 per transaction
   - However, the payroll and expenditure processes have reconciliation controls (bank reconciliation, payroll reconciliation) that would detect large misstatements
   - Potential misstatement: Could reach $50K-$200K for smaller individual fraud but unlikely to be material at the financial statement level
4. **Apply compensating controls**: Payroll reconciliation and bank reconciliation are precise enough to detect large, material misstatements for these processes.
5. **Classification: Significant Deficiency** — There is reasonable possibility of misstatement, but compensating controls (reconciliations) reduce likelihood of material misstatement.
6. **Affected Principles**: P11 (general controls over technology — access management), P10 (control activities — segregation of duties).
7. **Reporting**: Communicate to audit committee in writing; no public disclosure required; ICFR opinion remains unqualified (assuming no other material weaknesses).

### Example 3: Deficiency — Manual Control Not Documented

**Scenario**: The revenue recognition manager reviews all contracts over $1M for proper revenue recognition under ASC 606. The review is performed and effective, but there is no documented procedure describing the review, and the manager does not sign off or otherwise document completion of the review. The reviewer is experienced and competent.

**Agent Analysis**:
1. **Is there a deficiency?** YES — The control lacks documentation of performance. Without evidence of performance, the auditor cannot verify the control was applied consistently. This is a design deficiency (no sign-off mechanism) and an operating deficiency (no documentary evidence).
2. **Is there reasonable possibility of misstatement?** LOW — The reviewer is experienced and competent. Inquiry confirms the review is performed. However, the lack of documentation creates risk that the review could be missed without detection.
3. **Could the misstatement be material?** UNLIKELY for individual transactions — large contracts ($1M+) receive heightened scrutiny from multiple parties (external audit, audit committee).
4. **Classification: Deficiency** — No reasonable possibility of a material misstatement, but the absence of documentation is a control defect.
5. **Affected Principles**: P12 (deploy control activities through policies and procedures — procedures not fully established), P10 (control activities — evaluation of design effectiveness).
6. **Reporting**: Communicate to management; recommend implementing sign-off documentation.
7. **Remediation**: Implement a documented review checklist with sign-off for each contract reviewed.

### Example 4: Entity-Level Control Assessment — Audit Committee Oversight

**Scenario**: The agent is evaluating P2 (Board independence and oversight) for a mid-cap public company. The audit committee has three members, all independent. One member is a former CFO of a Fortune 500 company. The audit committee meets quarterly and receives reports from internal audit and external audit. The audit committee has a written charter that includes ICFR oversight responsibility. However, the audit committee has NOT reviewed management's ICFR assessment conclusion in any of the past three years.

**Agent Assessment using Section 11 Template**:

```
Principle Number:  P2
Principle Title:   Board independence and oversight of ICFR
Component:        Control Environment

POINTS OF FOCUS ADDRESSED:
  [X] PoF 1: Oversight responsibilities — YES (charter includes ICFR oversight)
  [X] PoF 2: Relevant expertise — YES (former CFO member)
  [X] PoF 3: Independence from management — YES (all three members independent)
  [P] PoF 4: Oversight of external/internal audit — PARTIALLY
      (receives reports but has not reviewed management's ICFR assessment)

ASSESSMENT:
  Present and Functioning?   [ ] Yes  [X] No  [ ] Partially
  Basis for Assessment:      The audit committee has not exercised its ICFR
    oversight responsibility by reviewing management's assessment conclusion.
    This is a gap in the functioning of the control, even though the structure
    (charter, composition, meetings) is present.

EVIDENCE:
  1. Audit committee charter (reviewed — includes ICFR oversight)
  2. Audit committee meeting minutes (reviewed — no ICFR assessment review)
  3. Board composition disclosures (verified — all independent)

IDENTIFIED DEFICIENCIES:
  [X] Deficiency: The audit committee has not reviewed management's ICFR
      assessment conclusion for the past three years.

REMEDIAL ACTIONS:
  Remediation Plan: Present management's ICFR assessment to the audit
  committee at the next quarterly meeting; add standing agenda item for
  ICFR assessment review. Owner: General Counsel. Target: Next quarter.

INTEGRATED OPERATION:
  Operating in Integrated Manner with Other Components?
  [X] Partially
  Explanation: The audit committee oversight gap affects Monitoring Activities
  (P16, P17) since the committee is not exercising its monitoring role over
  the ICFR assessment. It also affects Control Environment (P5) since
  accountability is undermined when oversight is not performed.
```

### Example 5: Walkthrough — Revenue Process (Order-to-Cash)

**Scenario**: The agent is performing a walkthrough of the revenue process for a SaaS company. The company recognizes revenue under ASC 606.

**Walkthrough Documentation**:

| Step | Processing Point | Inquiry | Observation | Inspection | Re-performance | Control Identified |
|------|-----------------|---------|-------------|------------|----------------|-------------------|
| 1 | Sales order entered in CRM by Sales Rep | Yes — rep confirms required fields | Yes — observed entry | CRM screenshot | N/A | Required fields validation (automated) |
| 2 | Contract generated from CRM by Deal Desk | Yes — confirms approval workflow | Yes — observed approval flow | Contract document, approval signatures | N/A — system-controlled | Contract approval (automated + manual sign-off for >$100K) |
| 3 | Revenue recognition assessment by Revenue Accountant | Yes — accountant explains ASC 606 analysis | Yes — observed analysis | ASC 606 checklist, performance obligation memo | Yes — re-performed checklist for one contract | Revenue recognition checklist (manual + IT-dependent) |
| 4 | Invoice generated by billing system | Yes — billing clerk confirms auto-generation | Yes — observed generation | Invoice PDF, automatic email to customer | N/A — automated | Invoice generation matching contract terms (automated) |
| 5 | Cash receipt recorded by AR Clerk | Yes — clerk confirms daily deposit matching | Yes — observed matching | Bank statement, remittance advice | Yes — re-performed deposit match for one day | Cash application (semi-automated) |
| 6 | Monthly reconciliation by Senior Accountant | Yes — explains reconciliation procedure | No — after month-end | Reconciliation workpaper | Yes — re-performed reconciliation for one account | Account reconciliation (IT-dependent manual) |
| 7 | Journal entry for revenue by Controller | Yes — explains review ofJE | No — after period-end | JE approval, support | N/A | Journal entry review and approval (manual) |

**Key Processing Points Where Misstatements Could Arise**:
- Step 3: Incorrect performance obligation identification (revenue recognized too early or too late)
- Step 5: Cash misapplied to wrong customer or wrong invoice
- Step 7: Unauthorized or incorrect journal entry (management override risk)

**Walkthrough Conclusion**: Controls are designed to address significant risks in the revenue process. No missing controls identified at key processing points. Design effectiveness is effective.

### Example 6: RPA Control Assessment

**Scenario**: A company has deployed 15 RPA bots across Accounts Payable (5 bots), Accounts Receivable (4 bots), and General Ledger (6 bots). The bots process invoice matching, cash application, and journal entries respectively. The agent is assessing internal controls over the RPA environment.

**Agent Assessment**:

1. **RPA Governance (P1, P5)**:
   - Is there a bot inventory? YES — Center of Excellence maintains a registry.
   - Is there bot ownership assigned? YES — Each bot has a business owner and IT owner.
   - Is there a bot deployment approval process? YES — New bots require approval from the CoE and IT Security.
   - **Assessment: Present and functioning.**

2. **RPA Risk Assessment (P7, P9)**:
   - Have bot-specific risks been identified? PARTIALLY — Operational risks documented; but fraud risk (bot manipulation for unauthorized payments) not assessed.
   - **Deficiency identified**: Fraud risk assessment does not address RPA-specific fraud scenarios.

3. **RPA Access Controls (P11)**:
   - Are bot credentials secured? YES — Stored in enterprise credential vault.
   - Are bot access rights reviewed? NO — Bot access has not been reviewed since deployment.
   - **Deficiency identified**: Bot access rights not subject to periodic review.

4. **RPA Change Management (P11)**:
   - Are bot code changes subject to change management? PARTIALLY — Emergency changes bypass change controls.
   - **Deficiency identified**: Emergency bot changes not subject to post-implementation review.

5. **RPA Monitoring (P16)**:
   - Is bot performance monitored? YES — Bot success rate, error rate, and processing time tracked daily.
   - Are bot exceptions monitored? YES — Exception reports generated and reviewed by business owners.
   - **Assessment: Present and functioning.**

**Summary**: Three deficiencies identified. The most severe is the lack of bot access review → proceed to deficiency classification using the decision tree in Section 8.2. If bots have access to process journal entries and payments, and no access review exists, there is reasonable possibility of unauthorized transactions. With compensating controls (reconciliation, monitoring), classify as Significant Deficiency pending compensating control evaluation.

---

## 20. ICFR Assessment End-to-End Workflow

The agent SHALL follow this 6-phase workflow when performing a complete ICFR assessment:

### Phase 1: Scoping and Planning
- Identify significant accounts and disclosures (AS 2201.28)
- Identify relevant assertions for each significant account (AS 2201.29)
- Assess entity-level controls first (AS 2201.22-.27)
- Determine which IT systems are significant to ICFR
- Plan walkthroughs for each significant process

### Phase 2: Entity-Level Assessment
- Evaluate Control Environment (P1-P5) for present and functioning
- Evaluate entity-level controls identified in Phase 1
- Determine if entity-level controls adequately address relevant assertions
- Consider multiple locations and business units (AS 2201.B1-.B38)

**Multi-Location Considerations (AS 2201.B1-.B38)**:
- Determine which locations/components are individually significant based on: size, risk, specific characteristics
- Assess entity-level controls that operate across locations
- Determine extent of process-level testing at each significant location
- Consider shared services centers and their control environment
- Evaluate uniformity of controls across locations
- Document rationale for locations scoped in/out

### Phase 3: Process-Level Assessment and Walkthroughs
- Perform walkthroughs per AS 2201.37-.38 for each significant process
- Document each processing point (inquiry, observation, inspection, re-performance)
- Identify key controls at each processing point
- Complete Risk and Control Matrix (Section 10) for each process
- Evaluate design effectiveness (AS 2201.42)

### Phase 4: Deficiency Evaluation
- Apply decision tree (Section 8.2) for each identified deficiency
- Evaluate compensating controls (Section 14)
- Apply aggregation rule (AS 2201.68):
  ```
  AGGREGATION RULE (AS 2201.68):
  FOR each identified deficiency:
    ASSESS individually per decision tree (Section 8.2)
  FOR each combination of deficiencies affecting same account/assertion:
    ASSESS whether combined effect = reasonable possibility of material misstatement
    IF combined effect meets material weakness threshold → CLASSIFY AS MATERIAL WEAKNESS
    IF combined effect meets SD threshold → CLASSIFY AS SIGNIFICANT DEFICIENCY
  DOCUMENT aggregate assessment for each relevant assertion
  ```
- Evaluate material weakness indicators (Section 8.4)

### Phase 5: Reporting
- Prepare Management's ICFR Report (Section 12 template)
- Prepare Auditor's ICFR Report (Section 13 template)
- Communicate significant deficiencies and material weaknesses in writing to audit committee

**Written Representations (AS 2201.75-.76)**:
- Obtain written representations from management at end of audit
- Management must represent: (a) responsibilities for establishing/maintaining ICFR, (b) ICFR assessment performed, (c) no uncorrected material misstatements, (d) disclosures complete, (e) significant deficiencies/material weaknesses communicated, (f) no fraud involving management, (g) aware of any subsequent events affecting ICFR
- If management refuses to provide representations → scope limitation → disclaimer or qualification

### Phase 6: Ongoing Monitoring
- Evaluate monitoring controls (P16, P17)
- Determine ongoing vs separate evaluation mix
- Consider subsequent-year scaling:

**Subsequent-Year Audit Scaling Guidance**:
- In subsequent years, leverage prior-year work: update risk assessment, reassess scoping
- Prior-year effective controls: may reduce nature/timing of testing but NOT eliminate
- New or changed controls: perform first-year level testing
- Prior-year deficiencies: verify remediation, test new/changed controls at full scope
- Consider changes in: business, systems, personnel, regulations, controls
- Cannot assume controls continue to operate based on prior-year results only

**Roll-Forward Procedures (AS 2201.48-.50)**:
- For interim testing performed before year-end: determine roll-forward period
- Update risk assessment for changes during roll-forward period
- Perform additional testing for period between interim test date and year-end
- Consider length of roll-forward period: longer period → more additional testing needed
- Document roll-forward approach and additional procedures performed
- If controls changed during roll-forward period: test revised controls at year-end

---

## 21. Additional Templates

### 21.1 Walkthrough Documentation Template

```
╔════════════════════════════════════════════════════════════╗
║ WALKTHROUGH DOCUMENTATION                                  ║
╚════════════════════════════════════════════════════════════╝

Process:                    [e.g., Revenue — Order to Cash]
Significant Account:        [e.g., Revenue, AR]
Relevant Assertions:        [e.g., Existence, Completeness, Cutoff]
Walkthrough Date:           [Date]
Performed By:               [Name]

| Step | Processing Point | Inquiry | Observation | Inspection | Re-performance | Control Identified | Control Type |
|------|-------------------|---------|-------------|------------|----------------|-------------------|-------------|
| 1    | [Description]     | [Y/N + detail] | [Y/N + detail] | [Y/N + detail] | [Y/N + detail] | [Control name] | [Auto/Manual/IT-dep] |
| 2    |                   |         |             |            |                |                   |              |

KEY PROCESSING POINTS WHERE MISSTATEMENTS COULD ARISE:
  1. [Step, risk description, relevant assertion]
  2.

CONTROLS IDENTIFIED AS KEY CONTROLS:
  1. [Control, step, assertion addressed]
  2.

MISSING CONTROLS:
  [ ] None identified
  [ ] Missing control at Step ___: [Description]

DESIGN EFFECTIVENESS CONCLUSION:
  [ ] Controls are designed effectively to address risks
  [ ] Controls are NOT designed effectively: [Explanation]

WALKTHROUGH CONCLUSION:
  [Narrative summary]
```

### 21.2 Material Weakness Disclosure Template

```
╔════════════════════════════════════════════════════════════╗
║ MATERIAL WEAKNESS DISCLOSURE                              ║
╚════════════════════════════════════════════════════════════╝

Material Weakness ID:       [MW-YYYY-###]
Date Identified:            [Date]
Classification Date:         [Date]
Process/Affected Area:      [e.g., Revenue, IT Access]
Affected Accounts:           [e.g., Revenue, AR]
Affected Assertions:         [e.g., Completeness, Existence]

DESCRIPTION OF DEFICIENCY:
  [Detailed description of the control deficiency]

BASIS FOR CLASSIFICATION:
  [Reference to AS 2201 decision tree steps; reasonable possibility
   assessment; magnitude assessment; or AS 2201.69 indicator]

COMPENSATING CONTROLS EVALUATED:
  [List compensating controls considered and why they do NOT
   mitigate the deficiency to below material weakness threshold]

AFFECTED COSO PRINCIPLES:
  [List principles that are NOT present and functioning]

IMPACT ON ICFR:
  ICFR Opinion:              [ ] Adverse  [ ] Unmodified
  Financial Statement Impact: [Describe or state "not yet determined"]

REMEDIATION PLAN:
  Planned Actions:           [Description]
  Responsible Party:         [Name/Title]
  Target Completion Date:    [Date]
  Interim Controls:          [Describe any interim controls implemented]

DISCLOSURE LANGUAGE (for Form 10-K):
  "We identified a material weakness in our internal control over
  financial reporting related to [description]. As a result of this
  material weakness, [CEO/CFO] concluded that our internal control
  over financial reporting was not effective as of [date]."

AUDIT COMMITTEE NOTIFICATION:
  Date Notified:             [Date]
  Method:                    [Written — letter/email]
  Acknowledged:              [ ] Yes  [ ] No
```

### 21.3 Significant Deficiency Communication Template

```
╔════════════════════════════════════════════════════════════╗
║ SIGNIFICANT DEFICIENCY COMMUNICATION                       ║
╚════════════════════════════════════════════════════════════╝

Significant Deficiency ID:  [SD-YYYY-###]
Date Identified:             [Date]
Process/Affected Area:      [e.g., IT Change Management]
Affected Accounts:          [e.g., Multiple — see analysis]

DESCRIPTION OF DEFICIENCY:
  [Detailed description]

BASIS FOR CLASSIFICATION:
  [Decision tree analysis; why not a material weakness]

COMPENSATING CONTROLS IDENTIFIED:
  [List compensating controls that partially mitigate the risk]

REMAINING RISK:
  [Description of residual risk after compensating controls]

RECOMMENDED REMEDIATION:
  [Specific recommendations]

COMMUNICATION REQUIREMENTS:
  To Management:             [ ] Written communication sent [Date]
  To Audit Committee:        [ ] Written communication sent [Date]
  Public Disclosure:         [ ] Not required for significant deficiencies

FOLLOW-UP:
  Next Review Date:          [Date]
  Remediation Status:        [ ] Not Started  [ ] In Progress  [ ] Complete
```

### 21.4 Entity-Level Control Assessment Template

```
╔════════════════════════════════════════════════════════════╗
║ ENTITY-LEVEL CONTROL ASSESSMENT                            ║
╚════════════════════════════════════════════════════════════╝

Entity-Level Control:       [Name]
COSO Component:             [e.g., Control Environment]
COSO Principle:             [e.g., P2]

CONTROL OBJECTIVE:
  [What the control is designed to achieve]

CONTROL DESCRIPTION:
  [How the control operates; who performs it; frequency]

CONTROL TYPE:
  [ ] Preventive    [ ] Detective
  [ ] Manual        [ ] Automated    [ ] IT-Dependent Manual

PERVASIVENESS ASSESSMENT:
  Does this control operate across the entity?
  [ ] Yes — pervasive effect on ICFR
  [ ] Partially — applies to specific processes only
  Processes affected: [List]

PRECISION ASSESSMENT:
  Is this ELC precise enough to prevent/detect material misstatements?
  [ ] Yes — operates at level of precision relevant to assertions
  [ ] No — indirect/pervasive only; process-level controls required
  Assertions addressed: [List]

DESIGN EFFECTIVENESS:
  [ ] Effective  [ ] Ineffective
  Basis: [Explanation]

OPERATING EFFECTIVENESS:
  [ ] Effective  [ ] Ineffective  [ ] Not tested
  Evidence: [Description of testing performed]
  Sample size: [N/A or number]

DEFICIENCY IDENTIFIED:
  [ ] None
  [ ] Yes — [Description and classification per Section 8.2]

IMPACT ON PROCESS-LEVEL TESTING:
  [ ] Reduces nature/timing of process-level testing permitted
  [ ] Does not reduce process-level testing required
  Explanation: [Rationale]
```

---

## 22. TSC (Trust Services Criteria) ↔ COSO Reverse Mapping

When the agent needs to map AICPA Trust Services Criteria back to COSO 2013 ICIF principles, use this table:

| TSC Criterion | COSO Principle(s) | Alignment |
|--------------|-------------------|-----------|
| CC1.1 | P1 | Integrity and ethical values |
| CC1.2 | P5 | Accountability for internal control responsibilities |
| CC1.3 | P3 | Organizational structure, reporting lines, authorities |
| CC1.4 | P4 | Commitment to competence |
| CC1.5 | P2 | Board independence and oversight |
| CC2.1 | P13 | Relevant, quality information |
| CC2.2 | P14 | Internal communication |
| CC2.3 | P15 | External communication |
| CC3.1 | P6 | Objectives specified with sufficient clarity |
| CC3.2 | P7 | Risk identification and analysis |
| CC3.3 | P8 | Fraud risk consideration |
| CC3.4 | P9 | Impact of change on ICFR |
| CC4.1 | P16 | Ongoing/separate evaluations |
| CC4.2 | P17 | Deficiency evaluation and communication |
| CC5.1 | P10 | Control activities for risk mitigation |
| CC5.2 | P11 | General control activities over technology |
| CC5.3 | P12 | Policies and procedures deployment |
| CC6.1–CC6.8 | P10, P11 | Logical access, authentication, authorization |
| CC7.1–CC7.4 | P10, P11 | System operations monitoring |
| CC8.1–CC8.2 | P11 | Change management |
| CC9.1–CC9.2 | P10 | Risk mitigation for specific circumstances |

---

*End of COSO Internal Controls Skill*