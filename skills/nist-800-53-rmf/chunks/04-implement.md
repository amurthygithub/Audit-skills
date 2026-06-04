---
chunk_id: 04-implement
parent_skill: nist-800-53-rmf
topic: "Implementation & SSP Documentation (RMF Step 4)"
load_when: "user asks to implement controls, draft the SSP, or perform Step 4"
---

# Chunk 03 — Implement & SSP (RMF Step 4)

## Control structure (800-53 Rev 5)

```
AC-2(1) — Account Management | Physical Access Control for Non-Organizational Users
   └─ control statement
   └─ supplemental guidance
   └─ control enhancements (1)..(N) (when applicable)
   └─ assessment objective (assessed via 800-53A)
   └─ related controls
   └─ references
```

A control is **satisfied** when each **assessment objective** in 800-53A yields a "satisfied" or "other than satisfied" determination; **other than satisfied** drives a finding in the SAR (see chunk 04).

## Implementation status taxonomy

For each in-scope control, document the implementation status:

- **Implemented** — control is fully in place and operating.
- **Partially Implemented** — some parts in place, some planned.
- **Planned** — not yet implemented; target date documented.
- **Alternative Implementation** — a compensating or alternate implementation; document why it meets the intent.
- **Not Applicable** — control does not apply; document justification.

## Common control & inheritance model

- **Common control** — implemented and assessed at the organization/enterprise level; inheritable by multiple systems.
- **System-specific control** — implemented at the system level.
- **Hybrid control** — partly inherited, partly system-specific.
- **Inheritance** (FedRAMP): a system inherits controls from a cloud service provider (e.g., AWS, Azure, GCP FedRAMP-authorized offerings) when the boundary, control narrative, and assessment evidence are inherited via the provider's package.

### Inheritance authorization gating

A CSP inheriting controls from another CSP **must** verify the source CSP's current authorization status before claiming inheritance:

- **Acceptable evidence:** the source CSP's current FedRAMP PMO ATO letter (not a self-attestation, not an expired ATO, and not a third-party report without PMO concurrence). The inheriting CSP must cite the FedRAMP package ID and ATO date in the SSP.
- **Not acceptable:** the source CSP's own assertion of authorization, a marketing claim of "FedRAMP-ready," or an ATO letter that has expired or been revoked.
- **Residual responsibility:** even when inheritance is validated, the inheriting CSP remains responsible for control implementation validation. The inheritor must demonstrate that the inherited control is operating effectively in its own environment (e.g., that the inherited boundary protection is correctly configured for the inheriting system's data flows). The 3PAO will sample inherited controls against the provider's package and test the inheriting CSP's configuration.

When inheritance is invoked, document: provider, FedRAMP package ID, ATO date, PMO ATO letter reference, boundary overlap, inherited controls, residual controls the system must implement.

## Procedure

1. Deploy controls in the operational environment.
2. Document **implementation status** per control: Implemented / Partially Implemented / Planned / Alternative / N/A.
3. For inherited controls, cite the provider's FedRAMP package ID, ATO date, PMO ATO letter reference, and the inheritance line in the customer responsibility matrix.
4. For system-specific controls, attach evidence references (policy doc, config screenshot, runbook, system-generated log).
5. Update SSP §13 "Continuous Monitoring Strategy" with assessment frequency and triggers.

## SSP §10 implementation status template (per control)

```yaml
- control_id: AC-2
  enhancements: [AC-2(1), AC-2(2), AC-2(3)]
  status: Implemented
  implementation_summary: <one paragraph>
  inherited_from: <provider-name> or null
  inherited_pmo_ato_ref: <FedRAMP package ID + ATO date> or null
  evidence_refs: [<doc-id-1>, <doc-id-2>]
  nist_800_53a_objectives_met: [OBJ-1, OBJ-2, ...]
```

## Customer Responsibility Matrix (CRM) for FedRAMP

A CSP's CRM lists which controls the customer (agency) is responsible for vs. which the CSP inherits. Pattern (one row per control family or per control):

| Control | Status | Source | Narrative |
|---------|--------|--------|-----------|
| AC-2 | hybrid | AWS GovCloud + App | Cloud IAM + app-layer accounts |
| SC-7 | inherited | AWS GovCloud | VPC + security groups |
| AU-2 | hybrid | AWS GovCloud + App | CloudTrail + app events |

## Citations in this chunk

- `[NIST-SP-800-37-Rev2 Step 4]` — implement
- `[NIST-SP-800-53-Rev5 §2]` — control structure
- `[FedRAMP-Rev5]` — CRM and inheritance

See `## 10. References & Citation Manifest` in SKILL.md.
