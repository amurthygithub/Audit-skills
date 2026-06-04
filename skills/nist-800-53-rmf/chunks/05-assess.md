---
chunk_id: 05-assess
parent_skill: nist-800-53-rmf
topic: "Assessment (800-53A) and Security Assessment Report (SAR)"
load_when: "user asks to assess controls, run 800-53A, draft SAR, or perform Step 5"
---

# Chunk 04 — Assess (800-53A / RMF Step 5)

## Decision logic

```
FOR each in-scope control (incl. enhancements):
    FOR each assessment objective in 800-53A:
        METHOD := one of [EXAMINE, INTERVIEW, TEST]
        EVIDENCE := collect per method
        DETERMINATION := satisfied | other_than_satisfied | not_applicable
    AGGREGATE:
        satisfied → PASS
        any other_than_satisfied → FINDING (severity per Severity levels below)
        all not_applicable → N/A (must be justified)
```

## Assessment methods (800-53A)

- **Examine** — review documentation, configuration, logs, records.
- **Interview** — talk to system owners, ISSO, system administrators, users.
- **Test** — perform a technical or procedural test (e.g., attempt to access, re-perform a calculation, run a script).

Each assessment objective in 800-53A is mapped to one or more methods. The 3PAO (FedRAMP) or independent assessor uses all three as appropriate.

## Severity levels

| Severity | Definition | Remediation | Reporting |
|----------|-----------|-------------|-----------|
| **Critical** | Imminent threat of system compromise; active exploitation or control failure that would cause catastrophic impact to confidentiality, integrity, or availability | Must be remediated within 48 hours | Must be reported to FedRAMP PMO within 24 hours |
| **High** | Operational or design failure on a HIGH-impact control with no compensating control; often blocks ATO or requires ATO with conditions | POA&M with aggressive timeline | Report in SAR; may trigger significant-change notification |
| **Moderate** | Design weakness or operational lapse on a MOD or HIGH control; risk manageable with compensating controls or remediation plan | Remediation plan + risk acceptance | Report in SAR; track to closure |
| **Low** | Operational lapse on a MOD control with compensating control exists; minor documentation gaps | Track to closure | Report in SAR |

**FedRAMP risk categorization** (per FedRAMP Continuous Monitoring Strategy Guide): a deviation from an approved baseline requires a POA&M with risk level (Low / Moderate / High / Critical) and remediation date.

## Finding severity → POA&M risk

| Finding (800-53A "other than satisfied") | Typical POA&M risk | Comment |
|------------------------------------------|--------------------|---------|
| Imminent compromise, active exploitation, control failure with catastrophic impact | Critical | Remediate within 48 hours; report to FedRAMP PMO within 24 hours |
| Operational lapse on a MOD control, compensating control exists | Low | Track to closure |
| Design weakness on a MOD or HIGH control, no compensating | Moderate | Remediation plan + risk acceptance |
| Operational failure on a HIGH control, no compensating | High | Often blocks ATO or requires ATO with conditions |
| Design failure on a HIGH control (control does not exist as designed) | High / blocker | AO rarely accepts; re-implementation |

## Procedure

1. Generate the **Security Assessment Plan (SAP)** mapping each in-scope control to assessment objectives and methods.
2. Execute assessment — collect artifacts, interview SMEs, perform tests, capture raw evidence.
3. For each assessment objective, record determination: Satisfied / Other Than Satisfied / Not Applicable.
4. Aggregate to control-level findings. **Do not aggregate across controls** (one finding per control / enhancement).
5. Draft the **SAR**: scope, methodology, findings (per control), risk categorization, recommended actions.
6. Hold **out-brief** with the system owner; finalize the SAR.

## SAR header metadata (FedRAMP-required)

Every SAR must carry the following metadata block before the findings:

```yaml
sar_header:
  system_name: <official system name as recorded in SSP>
  system_identifier: <agency system ID, FISMA ID, or FedRAMP package ID>
  fips_199_categorization: {confidentiality: <Low|Moderate|High>, integrity: <Low|Moderate|High>, availability: <Low|Moderate|High>, overall: <Low|Moderate|High>}
  authorization_boundary: <description — cite SSP boundary>
  date_of_assessment: YYYY-MM-DD
  assessment_period:
    start: YYYY-MM-DD
    end: YYYY-MM-DD
  assessor:
    name: <lead assessor name>
    firm: <3PAO or assessment team name>
    role: <Lead Assessor | Assessment Team Member>
  assessment_scope: <full baseline or partial; list in-scope controls>
  assessment_methodology: [EXAMINE, INTERVIEW, TEST]
  sap_reference: <SAP document ID or filename>
```

## SAR Finding output template

```yaml
finding_id: SAR-001
control_id: AC-2(4)
control_title: "Account Management | Automated Audit Actions"
severity: Critical|High|Moderate|Low
determination: Other Than Satisfied
description: <one paragraph — what was tested, what was found>
condition: <what is>
criteria: <what should be — cite 800-53A assessment objective ID>
cause: <why — design, operation, training, oversight>
effect: <risk to system>
recommendation: <action — specific, testable>
compensating_control: <description if exists>
remediation_plan: <POA&M item>
risk_acceptance_required: <true|false>
vendor_dependency:
  vendor_product: <name if finding involves a vendor component>
  vendor_name: <vendor organization>
  vendor_ticket_id: <vendor support ticket reference>
  vendor_eta: <vendor-provided remediation ETA>
deviation_from_baseline: <true|false — whether this finding represents a deviation from the approved baseline>
milestones:
  - date: YYYY-MM-DD
    description: <intermediate remediation step>
    status: Pending|In Progress|Complete
  - date: YYYY-MM-DD
    description: <final validation step>
    status: Pending
```

## Anti-hallucination note

800-53A assessment procedures are published in SP 800-53A Rev 5; the "objectives" enumeration varies by control and is not the same as the "control enhancements" enumeration. Always cite the specific 800-53A assessment objective ID (e.g., `AC-2.01`, `AC-2.04`).

## Citations in this chunk

- `[NIST-SP-800-53A-Rev5]` — assessment procedures
- `[NIST-SP-800-37-Rev2 Step 5]` — assess
- `[FedRAMP-Rev5 ConMon Strategy]` — POA&M risk categorization

See `## 10. References & Citation Manifest` in SKILL.md.
