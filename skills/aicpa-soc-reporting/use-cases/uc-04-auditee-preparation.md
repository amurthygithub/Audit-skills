---
uc_id: UC-04
title: Auditee Preparation for SOC 2 Type II Examination
industries: [saas-technology, healthcare, financial-services]
frameworks: [SOC-2-TSC-2017]
status: stub
inputs:
  - "Service description document"
  - "Control inventory (spreadsheet mapping controls to TSC criteria)"
  - "Evidence repository or folder structure"
  - "Prior year SOC report (if any)"
  - "Subservice organization list with contracts/BAAs"
  - "Customer list (for CUEC identification)"
procedure:
  - "SKILL.md §2: Framework Overview — understand SOC 2 report structure"
  - "chunks/02-engagement-type-decision.md — confirm SOC 2 Type II scope"
  - "chunks/03-tsp-criteria.md — map existing controls to TSC categories"
  - "chunks/06-cuec-csoc-inheritance.md — identify CUECs and CSOCs"
expected_outputs:
  - "Gap analysis: controls mapped to TSC with identified gaps"
  - "Remediation plan: timeline for closing control gaps before examination period"
  - "Evidence readiness checklist per criterion"
  - "CUEC disclosure draft"
  - "Subservice organization CSOC list"
oracle: |
  Manual review by qualified practitioner.
  Automated checks: all 33 CC criteria addressed; evidence exists for each testable control; CUECs are
  reasonable for the service description; CSOCs align with subservice contracts.
data_refs: [data/seeds/tsc-to-hipaa.json, data/seeds/tsc-to-hitrust.json]
tests: []
---

# UC-04: Auditee Preparation for SOC 2 Type II Examination

## Scenario

You are the Head of Compliance at a growing SaaS company. Your largest enterprise customer requires a SOC 2 Type II report within 12 months. You have never undergone a SOC 2 examination. You need to prepare your organization, controls, and evidence before engaging a CPA firm.

## 1. Pre-Engagement Preparation

### 1.1 Service Description

Before contacting a CPA firm, draft a service description. It must define:

- **System boundary:** what is in scope (application, infrastructure, processes)?
- **Services provided:** what does the customer get?
- **Principal service commitments and system requirements:** the promises you make to customers (SLAs, security commitments, compliance obligations).
- **Subservice organizations:** IaaS provider (AWS/Azure/GCP), third-party services, subcontractors.

The service description is Section II of the SOC 2 report. Write it yourself — the auditor validates it, but management owns it.

### 1.2 Control Inventory

Map your existing controls to TSC criteria. Create a spreadsheet with columns:

| Control ID | Description | TSC Criteria | Evidence Available? | Evidence Type | Owner | Notes |
|-----------|-------------|-------------|---------------------|---------------|-------|-------|
| CTRL-001 | Quarterly access reviews | CC6.1, CC6.2 | Yes | Review logs, screenshots | Engineering | Monthly would be better for Type II |

If you have no controls for a CC criterion, that's a gap. Fix gaps before the examination period starts.

### 1.3 Evidence Repository

Organize evidence by TSC category. For Type II, you need evidence that controls operated effectively throughout the examination period (minimum 6 months). Common structure:

```
evidence/
  cc1-control-environment/
  cc2-communication/
  cc3-risk-assessment/
  cc4-monitoring/
  cc5-control-activities/
  cc6-access-controls/
  cc7-system-operations/
  cc8-change-management/
  cc9-risk-mitigation/
  a-availability/
  pi-processing-integrity/
  c-confidentiality/
  p-privacy/
```

### 1.4 CUEC Identification

Complementary User Entity Controls are controls YOUR CUSTOMERS must implement for YOUR controls to work. Examples:

- Customer must enforce MFA for their own users
- Customer must review audit logs for their own tenant
- Customer must configure their own access policies

Write CUEC disclosures yourself. The auditor evaluates reasonableness, but management specifies them.

### 1.5 Subservice Organizations

List every vendor that touches your system or processes customer data. For each:

- Do they have their own SOC 2 report? (Carve-out method — you rely on their CSOCs)
- If not, do you need to include them in your scope? (Inclusive method)
- For healthcare: ensure BAAs are in place for PHI-processing vendors.

## 2. During the Examination

### 2.1 The Readiness Assessment

Many CPA firms offer a readiness assessment BEFORE the examination period. This is NOT part of the formal report but identifies gaps early. Strongly recommended for first-time SOC 2 candidates.

### 2.2 What the Auditor Will Ask For

- **Walkthroughs:** Demonstrate a control end-to-end (e.g., show how a new hire gets provisioned, how access is reviewed, how changes are approved).
- **Population completeness:** Prove you provided the complete set of records (e.g., all users, not a filtered subset).
- **Sample selections:** Auditor picks specific items to test. You must provide evidence for those items within the requested timeframe.

### 2.3 Responding to Auditor Requests

- Respond promptly. Delays can extend the examination or raise suspicion.
- Do not filter or curate evidence beyond what's requested. Let the auditor request clarification if needed.
- If the auditor finds an exception, discuss it candidly. Hiding exceptions risks a qualified opinion.

## 3. Reviewing Your Vendors' SOC Reports (as a User Entity)

Terminology: when you review a VENDOR's SOC report, you are the user entity — the CUECs in that report are controls the vendor requires YOU to operate. (CUECs you WRITE in your own report are controls you require of YOUR customers. Keep the directions straight.)

When your own vendors provide SOC 2 reports, evaluate them as a CUEC:

### 3.1 CUEC Report Review Checklist

- [ ] Report type (Type I or Type II) — Type I provides point-in-time only
- [ ] Examination period — does it cover the period relevant to your reliance?
- [ ] Opinion — unqualified, qualified, adverse, disclaimer?
- [ ] Scope — which TSC categories are included? Does it cover what you need?
- [ ] CUECs — do the vendor's CUECs align with controls you already implement?
- [ ] CSOCs — are subservice carve-outs reasonable?
- [ ] Exceptions — are any exceptions material to your reliance?

### 3.2 Vendor SOC Review for Government Procurement

When responding to RFPs or government procurement, your vendor SOC review must demonstrate:

- **Evidence of review:** date, reviewer, scope of assessment
- **Mapping to procurement requirements:** which TSC criteria address the RFP's security requirements
- **Residual risk acknowledgment:** if the vendor has exceptions, how do you compensate?
- **Periodic re-evaluation:** annually or upon vendor SOC report updates

## 4. Cost-Aware Implementation

### 4.1 Common Over-Implementation Traps

- Scoping all 5 TSC categories when only Security is required by most customers
- Implementing every CC6 sub-criterion before confirming what the auditor will actually test
- Building custom tooling for evidence collection when screenshots + logs suffice

### 4.2 Audit Fatigue Management

- Align evidence collection with your existing operational cadence (use sprint reviews, incident post-mortems, existing change management logs)
- Maintain a "SOC evidence" tag in your ticketing system rather than a separate process
- If pursuing multiple frameworks (SOC 2 + ISO 27001 + HITRUST), design controls once to satisfy all three, then map evidence bidirectionally

## 5. Oracle and Test Plan

Automated checks:
- All 33 CC criteria are addressed in the control inventory
- Evidence file paths resolve for each testable control
- CUEC disclosures are consistent with the service description
- CSOC list aligns with subservice contracts

Manual review:
- Practitioner evaluates reasonableness of CUECs, CSOCs, and control design
- Edge cases: first-time SOC 2 (no prior report to reference), multi-framework overlap, inherited controls from parent organization
