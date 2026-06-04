---
chunk_id: 03-itaf-and-maturity
parent_skill: isaca-audit-methodology
topic: "ITAF Standards and COBIT Maturity Model"
load_when: "user asks about ITAF, audit standards, ISACA standards S1-S18, maturity assessment, COBIT maturity, or CMMI capability levels"
---

# Chunk 03 - ITAF and COBIT Maturity

**IMPORTANT: S1-S18 and G1-G18 numbering is a pedagogical reconstruction. It does NOT correspond to official ISACA ITAF numbering. Always verify against current ITAF publication before citing in audit workpapers.**

## ITAF Three-Tier Structure

| Tier | Level | Requirement |
|------|-------|------------|
| Tier 1 | Standards | MANDATORY |
| Tier 2 | Guidelines | Strongly recommended |
| Tier 3 | Procedures/Techniques | Optional |

## Tier 1: Audit Standards (Pedagogical S1-S18)

| ID | Standard | Key Requirement |
|----|---------|---------------|
| S1 | Audit Charter | Ensure charter defines purpose, authority, responsibility |
| S2 | Independence | Maintain organizational, personal, external independence |
| S3 | Professional Competence | Maintain competency through CPE |
| S4 | Due Professional Care | Exercise professional skepticism and judgment |
| S5 | Audit Planning | Risk-based planning for every engagement |
| S6 | Performance of Audit Work | Execute to achieve objectives; supervise and document |
| S7 | Audit Reporting | Report scope, objectives, findings, recommendations |
| S8 | Follow-Up Activities | Verify remediation effectiveness |
| S9 | Irregularities and Illegal Acts | Detect and report irregularities |
| S10 | IT Governance | Evaluate governance per COBIT |
| S11 | Use of Data Analytics | Apply data analytics per ISACA guidance |
| S12 | Third-Party/Service Provider | Apply standards for third-party controls (SOC reports) |
| S13 | Audit Evidence | Evidence must be sufficient, reliable, relevant, useful |
| S14 | Sampling | Apply statistical or non-statistical sampling |
| S15 | Documentation | Working papers covering all engagement work |
| S16 | IT Control Self-Assessment | Validate self-assessment results independently |
| S17 | Audit Risk and Materiality | AR = IR x CR x DR; set materiality thresholds |
| S18 | Using Work of Other Auditors | Assess competence, independence, quality |

Audit Risk Model: Both ISACA and AICPA/PCAOB use AR = IR x CR x DR. Do not confuse with sampling-level risk decompositions. Use one model consistently within an engagement.

## Tier 2: Guidelines (G1-G18)

G1-G18 correspond to S1-S18 with detailed application guidance.

## Topic-Specific Guidance Areas

Supplementary topic areas organized by audit topic. These are NOT formal ITAF numbered guidelines. Reference actual ISACA publication names.

| Topic Area | ISACA Reference |
|-----------|---------------|
| Privacy audit | ISACA Privacy Audit Program |
| IT security audit | ISACA IT Security Audit Program |
| BCP/DRP audit | ISACA BCP/DRP Audit Program |
| SDLC audit | ISACA SDLC Audit Guidance |
| Cloud computing audit | ISACA Cloud Audit Program |
| AI audit | ISACA AI Audit Toolkit (published) |
| Cybersecurity audit | ISACA Cybersecurity Audit Program (NIST CSF 2.0 aligned) |
| Vendor/supply chain audit | ISACA Vendor/Third-Party Audit Guidance |

## Tier 3: Procedures and Techniques

AI Audit Toolkit, Cybersecurity Audit Program (NIST CSF 2.0), PCI DSS v4.0 Audit Program, Biometrics Audit Program, IT Audit Fundamentals procedures.

## COBIT Maturity Models

### Legacy Model (COBIT 4.x/5)

| Level | Name | What You Observe |
|-------|------|-----------------|
| 0 | Non-Existent | No process; no awareness |
| 1 | Initial/Ad Hoc | Isolated efforts; individual reliance; inconsistent |
| 2 | Repeatable but Intuitive | Tribal knowledge; not formally defined |
| 3 | Defined Process | Documented; standardized but inconsistently followed |
| 4 | Managed and Measurable | Metrics; management review; consistent compliance |
| 5 | Optimized | Continuous improvement; automation; benchmarking |

### CMMI-Based Model (Official COBIT 2019)

| Level | Name | Description |
|-------|------|------------|
| 0 | Incomplete | Process not implemented or fails purpose |
| 1 | Performed | Process achieves its purpose |
| 2 | Managed | Planned, monitored, adjusted; work products managed |
| 3 | Established | Defined and deployed using a standard process |
| 4 | Predictable | Operates within defined limits |
| 5 | Innovating | Continuously improved for business goals |

Use the CMMI-based model for all COBIT 2019 assessments. Bridge to legacy model only when stakeholders reference it.

## Maturity Assessment Process

1. Select COBIT process to assess. 2. Gather evidence (interviews, documentation, observation, testing). 3. Rate current level based on evidence. 4. Determine target level (business needs, risk appetite, benchmarks). 5. Identify gaps. 6. Develop improvement roadmap (quick wins: 1-3 months +0.5; short-term: 3-6 months +1.0; medium-term: 6-12 months +1.0; long-term: 12-24 months +1.5).

**Decision rule:** Rate at the highest level where ALL attributes of that level are fully satisfied. If any attribute is not met, rate at the lower level.

## Output template (Maturity Assessment)

```yaml
process_id: APO13
current_maturity: 2.5
target_maturity: 4
gap: 1.5
assessment_date: YYYY-MM-DD
practice_areas:
  - name: "Security policy"
    current_level: 3
    evidence: "Documented policy exists, updated 18 months ago"
  - name: "Security monitoring"
    current_level: 3
    evidence: "SIEM deployed, 24/7 SOC, covers 80% of critical systems"
improvement_roadmap:
  - phase: Quick Win
    initiative: "Refresh security policy for cloud"
    gain: 0.5
    timeline: "1-3 months"
```

## Citations

Standards from `[ITAF]`. Maturity model from `[COBIT-2019]`. See SKILL.md S10.