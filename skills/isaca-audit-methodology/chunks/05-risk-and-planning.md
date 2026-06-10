---
chunk_id: 05-risk-and-planning
parent_skill: isaca-audit-methodology
topic: "Risk-Based Audit Planning, Audit Universe, Risk Scoring"
load_when: "user asks about risk assessment, audit plan, risk score, audit universe, or risk-based audit planning"
---

# Chunk 05 - Risk-Based Audit Planning

## Terminology Clarification: Audit Risk vs Planning Risk

This skill uses two distinct risk concepts that should not be conflated:

| Term | Definition | Uses |
|------|-----------|------|
| **Audit Risk** (AR) | Risk of expressing an incorrect audit opinion on materially misstated information. AR = Inherent Risk x Control Risk x Detection Risk. | Audit opinion formulation; materiality assessment; applied in planning under ITAF 1201. |
| **Planning Risk** (Risk-Based Planning) | Risk assessment performed during engagement planning to prioritize audit resources and determine scope/frequency. Uses Risk Score = (Likelihood x Impact) x Control Risk Factor. | Audit universe prioritization; annual planning; resource allocation. |

In chunks/05, "risk" in the context of planning and the 5-step methodology refers to Planning Risk (resource allocation), not Audit Risk (opinion risk). The Planning Risk assessment feeds into but is distinct from the Audit Risk model applied under ITAF 1201 (Risk Assessment in Planning). Do not interchange the two concepts.

## 5-Step Planning Methodology

1. **Establish Audit Universe** - Define all auditable entities: systems, processes, departments, applications, third parties, infrastructure. Classify by business function, technology platform, regulatory requirement.
2. **Perform Risk Assessment** - Assess inherent risk factors (financial, operational, regulatory, reputational impact). Score on consistent scale (1-5) for Likelihood x Impact.
3. **Prioritize Audit Engagements** - Rank by residual risk score. Apply coverage requirements, cycle requirements, resource constraints. Categories: High (annual), Medium (biennial), Low (triennial+).
4. **Develop Annual Audit Plan** - Define engagements (scope, objectives, timing, resources). Allocate resources. Build quarterly calendar. Obtain audit committee approval.
5. **Execute and Monitor** - Track progress vs plan. Adjust for emerging risks. Report quarterly to audit committee. Document all plan changes.

## Audit Universe Approaches

| Approach | Organization | When to Use |
|----------|-------------|------------|
| Process-Based | By business processes (O2C, P2P, HR) | Business process-focused audits |
| System/Application-Based | By IT systems (ERP, CRM, core banking) | Technology-dependent organizations |
| Control-Based | By control domains (access, change, ops) | SOX compliance; horizontal testing |
| Regulatory/Compliance-Based | By regulatory requirements (SOX, GDPR, HIPAA) | Highly regulated industries |

## Risk Score Formula (Primary)

> **Attribution note:** the L x I x CRF formula, the CRF values, and the priority bands
> below are this skill's illustrative house methodology -- a common practitioner pattern,
> NOT a formula prescribed by the CISA CRM or ITAF. Adopt your audit function's approved
> scoring model where one exists. With CRF applied, scores range 0.5-50.

```
Risk Score = (Likelihood x Impact) x Control Risk Factor

Likelihood: 1 (Rare) to 5 (Almost Certain)
Impact: 1 (Insignificant) to 5 (Catastrophic)
Control Risk Factor:
  0.5 = Strong Controls (well-designed, consistently operating)
  1.0 = Moderate Controls (designed but inconsistent)
  1.5 = Weak Controls (incomplete design or operation)
  2.0 = No Controls (non-functional)
```

Alternative formulation sometimes encountered: Risk Rating = Inherent Risk x (1 - Control Effectiveness). Do not mix approaches in the same assessment. For a cross-framework reconciliation of ISACA, PCAOB, and COSO risk formulas, see `audit-workpapers/chunks/04-risk-and-opinion.md`.

## Likelihood Scale

| Rating | Descriptor | Definition |
|--------|-----------|-----------|
| 1 | Rare | Exceptional circumstances only |
| 2 | Unlikely | Not expected but possible |
| 3 | Possible | Could occur at some time |
| 4 | Likely | Will probably occur |
| 5 | Almost Certain | Expected in most circumstances |

## Impact Scale

| Rating | Financial | Operational | Regulatory | Reputational |
|--------|-----------|------------|------------|-------------|
| 1 | <$10K | Minor disruption | No impact | No media |
| 2 | $10K-$100K | Short-term | Minor concern | Local media |
| 3 | $100K-$1M | Significant disruption | Inquiry | Regional media |
| 4 | $1M-$10M | Extended disruption | Action | National media |
| 5 | >$10M | Critical failure | Significant penalties | International media |

## Priority Classification

| Priority | Risk Score | Audit Frequency |
|----------|-----------|----------------|
| Critical | >= 15 | Within 6 months |
| High | 10-14 | Within 12 months |
| Medium | 5-9 | Within 24 months |
| Low | < 5 | Within 36 months |

## Risk Heat Map (L x I, before CRF; labels per the priority bands above)
```
       Impact 1   2   3   4   5
L  1 |  1 L  2 L  3 L  4 L  5 M
i  2 |  2 L  4 L  6 M  8 M 10 H
k  3 |  3 L  6 M  9 M 12 H 15 C
e  4 |  4 L  8 M 12 H 16 C 20 C
l  5 |  5 M 10 H 15 C 20 C 25 C
```

Always use CRF-adjusted score for priority classification.

## Finding Severity - Cross-Framework Mapping

| ISACA Severity | Closest PCAOB/COSO Concept | Definition |
|---------------|--------------------------|------------|
| Critical | (May warrant MW evaluation) | Severe control failure with material-misstatement exposure |
| High | (May warrant SD evaluation) | Significant control failure important to oversight |
| Medium | Deficiency (Other) | Does not rise to SD or MW |
| Low | Observation | Minor gap or enhancement opportunity |

**This mapping is directional only -- severity labels NEVER auto-derive an ICFR deficiency
classification.** Material weakness / significant deficiency determinations require a
magnitude-and-likelihood evaluation of the potential misstatement, considering compensating
controls (see `coso-internal-controls/chunks/05`), and apply only in ICFR contexts.
A count of exceptions or a planning risk score is not a deficiency classification. For
government performance audits, use GAGAS significance concepts instead. For a full
cross-framework severity reconciliation, see `audit-workpapers/chunks/07-qc-compliance-cross-refs.md`.

## Output template (Risk Assessment)

```yaml
risk_register:
  - risk_id: "RSK-001"
    description: "Data breach via misconfigured cloud storage"
    likelihood: 4
    impact: 5
    crf: 1.5
    risk_score: 30
    priority: "Critical"
  - risk_id: "RSK-002"
    description: "Vendor lock-in"
    likelihood: 3
    impact: 3
    crf: 1.0
    risk_score: 9
    priority: "Medium"
audit_plan_recommendations:
  - entity: "Legacy CRM"
    priority: "Critical"
    frequency: "Within 6 months"
    estimated_effort: 200
```

## Citations

5-step planning discipline aligned with `[CISA-CRM-28E]` and `[ITAF]`. The L x I x CRF
scoring model, CRF values, and priority bands are this skill's illustrative house
methodology (see Attribution note above), not content of the cited publications. See SKILL.md S10.
