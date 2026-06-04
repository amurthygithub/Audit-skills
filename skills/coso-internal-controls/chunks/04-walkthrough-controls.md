---
chunk_id: 04-walkthrough-controls
parent_skill: coso-internal-controls
topic: "Walkthrough Procedures + Entity-Level vs Process-Level Controls Classification"
load_when: "user asks about walkthrough procedures, entity-level controls, ELC, or process-level controls"
---

# Chunk 04 — Walkthrough Procedures and Control Classification

## Walkthrough Definition (AS 2201.37-.38)

A walkthrough follows a transaction from origination through the company''s processes including information systems, until it is reflected in the company''s financial records, using the same documents and IT that company personnel use.

Perform walkthroughs for each major class of transactions in each significant process.

## Required Walkthrough Procedures (4 at each processing point)

1. **Inquiry**: Ask appropriate personnel about prescribed procedures and controls:
   - What is required by prescribed procedures?
   - How are exceptions handled?
   - What happens when an error is identified?
   - How are different types of significant transactions handled?

2. **Observation**: Observe operations and processes in action to verify procedures are actually performed as described.

3. **Inspection**: Inspect relevant documentation at each processing point — transaction initiation documents, system input screens/outputs, approval signatures, reconciliation documents, exception reports.

4. **Re-performance**: Re-perform selected controls to verify they function as designed.

## Walkthrough Documentation

Document for each walkthrough:
- Process name, sub-process, transaction type
- Each processing point traversed
- At each point: inquiry responses, observations, documents inspected, controls re-performed
- IT systems traversed
- Journal entries and GL posting
- Control points where misstatements could arise
- Controls present at key processing points
- Identified gaps (missing or ineffective controls)
- Assessment: Does the walkthrough confirm the design of internal control?

## Probing Questions Template

At each key processing point, ask and document:

| Question | Purpose |
|----------|---------|
| What does the prescribed procedure require? | Verify understanding vs policy |
| Who performs this step? | Confirm SoD and competence |
| What happens when an exception is identified? | Verify error handling and escalation |
| How are errors corrected? | Verify correction controls |
| What happens when volumes spike? | Verify scalability and stress controls |
| How does this process interact with IT systems? | Verify IT application and general controls |
| What reports are produced? | Verify detective monitoring controls |
| Who reviews the output? | Verify review and approval controls |

## Entity-Level Controls (ELC) — AS 2201.22-.27

| ELC Category | Examples | Precision | Effect on Process-Level Testing |
|--------------|----------|-----------|-------------------------------|
| Control environment (P1-P5) | Tone at the top, code of conduct | Indirect | Does NOT reduce process-level testing |
| Management override controls | Review of adjustments, related-party controls | Varies | Moderate reduction if precise |
| Risk assessment process (P6-P9) | Enterprise risk assessment, fraud risk assessment | Indirect | Does NOT reduce process-level testing |
| Centralized processing / shared services | Shared service centers | Precise | May eliminate process-level testing |
| Monitoring results of operations | Budget vs. actual analysis | Monitoring | May reduce but not eliminate |
| Monitoring other controls | Internal audit, self-assessment | Monitoring | May reduce but not eliminate |
| Period-end financial reporting | Journal entry, accounting policy | Precise | May eliminate process-level testing |
| Significant business control policies | Risk management policies | Varies | Moderate reduction if precise |

## ELC Precision Classification Logic

IF the control operates at a level of precision to prevent or detect misstatements that could result in material misstatement → Precise ELC → May eliminate need for additional process-level testing.

ELSE IF the control monitors the effectiveness of other controls → Monitoring ELC → May reduce but does not eliminate testing of monitored controls.

ELSE (pervasive but indirect effect) → Indirect ELC → Important to evaluate but does NOT reduce process-level testing.

## Process-Level (Transaction-Level) Controls

| Control Type | Description | Examples |
|--------------|-------------|----------|
| Authorization controls | Approval required before processing | Manager approval of POs, supervisor approval of JEs |
| Verification controls | Independent checking of processing | Three-way match, bank reconciliation |
| Reconciliation controls | Comparison of records to identify differences | Account reconciliation, intercompany reconciliation |
| Review controls | Management review of output | Review of aging reports, review of trial balance |
| Access controls | Restriction of system access | Role-based access, SoD enforcement |
| Application controls | Controls embedded in IT systems | Edit checks, automated calculations |
| Business process controls | Controls within specific processes | Revenue recognition checklist, inventory counts |

## IT General Controls (ITGCs)

| Category | What to Evaluate | AS 2201 Ref |
|----------|-----------------|------------|
| Access management | User provisioning, de-provisioning, access review, privileged access | AS 2201.B4-.B10 |
| Change management | Program change controls, emergency changes, approval, testing, migration | AS 2201.B11-.B16 |
| IT operations | Job scheduling, backup/recovery, problem management, data center controls | AS 2201.B17-.B21 |
