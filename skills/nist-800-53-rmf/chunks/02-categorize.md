---
chunk_id: 02-categorize
parent_skill: nist-800-53-rmf
topic: "FIPS 199 Categorization (RMF Step 2)"
load_when: "user asks to categorize a system, run FIPS 199, or perform Step 2"
---

# Chunk 01 — Categorize (FIPS 199 / RMF Step 2)

## Decision logic

```
INPUT: system description, information types processed, data sensitivity, user population, downstream consequences of breach.

FOR each of (C, I, A):
    consider worst-case impact if:
        C: data is disclosed to unauthorized party
        I: data is modified or destroyed by unauthorized party
        A: system is unavailable or inaccessible when needed
    IMPACT := max of:
        - business process impact
        - financial impact
        - reputational impact
        - legal/regulatory impact
        - privacy impact (PHI, PII, FERPA, etc.)
    IF any dimension is "severe or catastrophic" → HIGH
    ELSE IF any dimension is "serious" → MODERATE
    ELSE → LOW

SYSTEM_CATEGORY := max(IMPACT_C, IMPACT_I, IMPACT_A)  # high-water
```

## FIPS 199 impact definitions

| Impact | Definition |
|--------|-----------|
| Low | Limited adverse effect (e.g., minor financial loss, minor harm) |
| Moderate | Serious adverse effect (e.g., significant financial loss, significant harm) |
| High | Severe or catastrophic adverse effect (e.g., major financial loss, loss of life) |

The **system security category** is the high-water mark across the three objectives. Example: `(C: M, I: M, A: L) → overall MODERATE`. The system inherits the **highest** of its sub-system categorizations.

## Procedure

1. Inventory **information types** the system processes. Use NIST SP 800-60 Vol 1/2 as the taxonomy (legacy) or the organization's own information-type catalog aligned to FIPS 199.
2. For each information type, determine CIA impact using 800-60 or organizational guidance.
3. Roll up to system level using **high-water mark** across the three objectives.
4. Document in **§2 of the SSP** with rationale per information type.
5. If the system processes PII, add privacy impact assessment (PIA) inputs.
6. Validate categorization with the AO or AO delegate before baseline selection.

## Output template (FIPS 199 YAML)

```yaml
system_name: <string>
information_types:
  - name: <string>
    fips_199_c: LOW|MODERATE|HIGH
    fips_199_i: LOW|MODERATE|HIGH
    fips_199_a: LOW|MODERATE|HIGH
    rationale: <one paragraph>
system_security_category:
  c: MODERATE
  i: MODERATE
  a: LOW
  overall: MODERATE
  high_water_mark: MODERATE
pia_required: <true|false>
special_factors:
  - <e.g., "processes PII of 250k+ individuals", "processes CUI", "interconnected with HIGH system">
```

## Anti-hallucination note

Categorization judgment is a professional determination informed by the system's business context; this skill encodes the framework but does not make the call for you. Validate with the AO before applying the baseline.

## Citations in this chunk

- `[FIPS-199 §1]` — security categorization definition
- `[NIST-SP-800-30-Rev1 §3]` — risk assessment methodology (input to categorization)
- `[NIST-SP-800-60]` — information-type taxonomy

See `## 10. References & Citation Manifest` in SKILL.md for the full list.
