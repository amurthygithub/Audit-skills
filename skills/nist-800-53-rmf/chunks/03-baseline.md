---
chunk_id: 03-baseline
parent_skill: nist-800-53-rmf
topic: "Baseline Selection & Tailoring (RMF Step 3)"
load_when: "user asks to select a baseline, tailor controls, or perform Step 3"
---

# Chunk 02 — Select Baseline & Tailor (RMF Step 3)

## Control baselines (FIPS 199-driven)

| FIPS 199 Category | Baseline | Approx. controls (Rev 5) | Approx. controls (Rev 5.1.1) |
|-------------------|----------|--------------------------|------------------------------|
| Low | LOW | ~156 | ~161 |
| Moderate | MOD | ~325 | ~341 |
| High | HIGH | ~421 | ~437 |

Tailoring per 800-37 Rev 2 + 800-53 §2:

- **Scoping** — apply only to parts of the system in scope.
- **Common control** — apply once at organization level; inheritable.
- **Parameter** — set a value (e.g., session lock timeout, password length).
- **Compensating** — alternate control meets intent; document why.
- **Supplementing** — add controls above the baseline (e.g., privacy controls for PII).

Document every tailoring decision in the SSP.

## Decision logic

```
BASELINE := table_lookup(SYSTEM_CATEGORY)
# Document any controls where the customer is replacing the FedRAMP-defined
# responsibility (e.g., a service that does NOT inherit physical controls).

# Tailoring:
#   - SCOPING: drop controls whose scope doesn't apply (e.g., wireless SC-8(1) if no wireless).
#   - COMMON: mark controls as inherited from enterprise-level common control catalog.
#   - PARAMETER: set any required parameter.
#   - COMPENSATING: if a control cannot be implemented as written, document the
#     alternate, why it meets the intent, and how the assessor will evaluate it.
#   - SUPPLEMENT: add controls above the baseline (e.g., privacy controls for PII).
```

## Procedure

1. Look up baseline: Low / Moderate / High (from categorization in chunk 01).
2. Apply **scoping** (drop controls whose scope does not apply, with justification).
3. Apply **common control** designation (mark as inherited from enterprise catalog).
4. Set **parameters** (e.g., session timeout, password length, retention days).
5. Identify **compensating** controls where the standard cannot be met as written.
6. Identify **supplemental** controls (privacy, supply chain, organization-specific).
7. Produce **§8 / §9 / §10 of the SSP** with the selected and tailored control set, the control narrative, and the implementation status.

## Output template (control selection YAML)

```yaml
system_name: <string>
baseline: LOW|MODERATE|HIGH
selected_controls:
  - control_id: AC-2
    enhancements: [AC-2(1), AC-2(2), AC-2(3)]
    status: Implemented|Partially Implemented|Planned|Alternative|N/A
    implementation_summary: <one paragraph>
    responsible_role: <ISSO|System Owner|Common Control Provider>
    inherited_from: <provider-name> or null
    evidence_refs: [<doc-id-1>, <doc-id-2>]
    nist_800_53a_objectives_met: [OBJ-1, OBJ-2, ...]
tailoring_decisions:
  - control_id: AC-2(8)
    decision: SCOPING
    rationale: <one paragraph>
```

## Anti-hallucination note

The control counts (~156 / ~325 / ~421 for Rev 5; ~161 / ~341 / ~437 for 5.1.1) are **derived** from the catalog and the count of base controls + enhancements. The actual count varies depending on how one counts enhancements. **Always verify against the current NIST SP 800-53 Rev 5 / 5.1.1 publication and the FedRAMP baseline** for cloud services. FedRAMP High is NOT identical to NIST 800-53 High.

## Citations in this chunk

- `[NIST-SP-800-53-Rev5 §2]` — tailoring
- `[NIST-SP-800-37-Rev2 Step 3]` — select
- `[FedRAMP-Rev5]` — FedRAMP baseline overlays

See `## 10. References & Citation Manifest` in SKILL.md.
