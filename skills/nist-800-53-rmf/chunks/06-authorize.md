---
chunk_id: 06-authorize
parent_skill: nist-800-53-rmf
topic: "Authorization Decision (RMF Step 6) — ATO Letter and POA&M"
load_when: "user asks for an ATO, ATO with conditions, denial, or POA&M"
---

# Chunk 05 — Authorize (RMF Step 6)

## ATO decision logic

```
SAR + POA&M + SSP ──► AO review
    IF no findings, all controls satisfied or N/A justified:
        DECISION := AUTHORIZE (full ATO)
    ELSE IF findings have documented POA&M, risk-acceptable:
        DECISION := AUTHORIZE WITH CONDITIONS (ATO w/ conditions)
    ELSE IF residual risk > risk tolerance:
        DECISION := DENY (denial of authorization)
```

An AO's "risk acceptance" must be specific: identify the findings, the residual risk, the rationale (e.g., compensating control, business case, time-bound remediation), and a remediation date.

## Procedure

1. AO reviews SSP, SAR, POA&M, and any risk-acceptance memos.
2. AO documents residual risk, rationale, and decision.
3. Issue the **ATO letter**: full ATO / ATO with conditions / Denial. Specify duration (typically **1 year for federal agency** with annual assessment, **1 year for FedRAMP** with continuous monitoring (FedRAMP Authorization Act requires annual assessment, not 3-year authorization)).
4. Publish the authorization package to the agency's repository (e.g., CFACTS, CSAM) and to FedRAMP Marketplace (for FedRAMP).

## POA&M item template

```yaml
poam_id: POA&M-001
finding_id: SAR-001
control_id: AC-2(4)
weakness_description: <string>
weakness_source: <assessment finding | vulnerability scan | penetration test | incident response | audit finding>
identified_by: <assessor name or organization>
weakness_detected_date: YYYY-MM-DD
risk_level: Low|Moderate|High|Critical
scheduled_completion_date: YYYY-MM-DD
status: Open|In-Progress|Completed|Risk-Accepted
vendor_dependent: <true|false>
product: <vendor product name if vendor_dependent>
vendor_dependency: <description>
remediation_plan: <action>
milestones: [<list of intermediate steps>]
  submission_date: YYYY-MM-DD
  resources_required: <string>
  deviation_from_baseline: <true|false>
```

## ATO decision letter template

```
[Agency Letterhead]

[Date]

MEMORANDUM FOR [System Owner]
FROM: [Authorizing Official]
SUBJECT: Authorization Decision — [System Name]

1. AUTHORIZATION DECISION: [Authorize | Authorize with Conditions | Deny]
2. DURATION: [N years from this date]
3. CONDITIONS (if "with conditions"): [list each condition, with date]
4. RESIDUAL RISK: [Accepted | Not Accepted — see denial]
5. NEXT CONTINUOUS MONITORING REVIEW: [Date]
6. SIGNATURE: [AO name, title, date]
```

## Risk-acceptance memo (per finding)

For each risk-accepted finding, the AO signs a memo that:

- Identifies the finding (by ID and control).
- States the residual risk.
- States the rationale (compensating control, business case, time-bound remediation).
- States the remediation date and the trigger for re-review.

## Anti-hallucination note

The AO is a designated official with statutory authority; this skill does not designate AOs. The skill helps produce the artifacts (SAR, POA&M, ATO letter); the AO signs the ATO.

## Citations in this chunk

- `[NIST-SP-800-37-Rev2 Step 6]` — authorize
- `[FedRAMP-Rev5]` — FedRAMP authorization process
- `[OMB-A-130]` — federal information security

See `## 10. References & Citation Manifest` in SKILL.md.
