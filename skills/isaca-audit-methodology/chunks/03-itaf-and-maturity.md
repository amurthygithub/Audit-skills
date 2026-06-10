---
chunk_id: 03-itaf-and-maturity
parent_skill: isaca-audit-methodology
topic: "ITAF Standards (1000/1200/1400 series) and COBIT Capability/Maturity"
load_when: "user asks about ITAF, audit standards, ISACA IS audit standards, maturity assessment, COBIT maturity, or CMMI capability levels"
---

# Chunk 03 - ITAF and COBIT Maturity

ITAF standard numbers below are the official ISACA series (verified against ITAF 4th Edition full text, 2026-06-10). The current edition is **ITAF 5th Edition (2026)**, which retains the 1000/1200/1400 series numbering -- verify individual standard titles against the 5th Edition before citing in audit workpapers.

**Scope note:** ITAF standards govern the *auditor's* conduct and work. They are generally NOT finding criteria -- criteria measure the *auditee* against its obligations (policy, regulation, COBIT practices). See chunk 06 Part 2.

## ITAF Three-Tier Structure

| Tier | Level | Requirement |
|------|-------|------------|
| Tier 1 | Standards (1000/1200/1400 series) | MANDATORY |
| Tier 2 | Guidelines (2000 series) | Strongly recommended |
| Tier 3 | Procedures/Techniques | Optional |

## Tier 1: IS Audit and Assurance Standards

### General Standards (1000 series)

| ID | Standard | Key Requirement |
|----|---------|---------------|
| 1001 | Audit Charter | Charter defines purpose, authority, responsibility |
| 1002 | Organizational Independence | Audit function independent of audited area |
| 1003 | Auditor Objectivity | Maintain objectivity in conduct and reporting |
| 1004 | Reasonable Expectation | Engagement achievable per standards; scope realistic |
| 1005 | Due Professional Care | Exercise skepticism and professional judgment |
| 1006 | Proficiency | Maintain competency through skills and CPE |
| 1007 | Assertions | Assess that assertions are capable of evaluation |
| 1008 | Criteria | Select objective, complete, relevant, measurable criteria |

### Performance Standards (1200 series)

| ID | Standard | Key Requirement |
|----|---------|---------------|
| 1201 | Risk Assessment in Planning | Risk-based approach to engagement planning |
| 1202 | Audit Scheduling | Plan engagements per risk and priorities |
| 1203 | Engagement Planning | Define scope, objectives, timeline, deliverables |
| 1204 | Performance and Supervision | Execute to achieve objectives; supervise and document |
| 1205 | Evidence | Evidence must be sufficient and appropriate |
| 1206 | Using the Work of Other Experts | Assess competence, independence, relevance |
| 1207 | Irregularities and Illegal Acts | Detect and report irregularities and illegal acts |

### Reporting Standards (1400 series)

| ID | Standard | Key Requirement |
|----|---------|---------------|
| 1401 | Reporting | Report scope, objectives, findings, conclusions |
| 1402 | Follow-up Activities | Monitor and verify remediation effectiveness |

Audit Risk Model: Both ISACA and AICPA/PCAOB practice use AR = IR x CR x DR (applied in planning under ITAF 1201). Do not confuse with sampling-level risk decompositions. Use one model consistently within an engagement.

## Tier 2: Guidelines (2000 series)

Guidelines mirror the standards series with detailed application guidance (e.g., 2001 corresponds to 1001). Cite guidelines by their actual 2000-series numbers from the current ITAF publication.

## Topic-Specific Guidance and Programs (Tier 3 / supplementary)

Audit programs and toolkits organized by topic. These are NOT numbered ITAF guidelines -- reference actual ISACA publication names and verify availability at ISACA.org.

| Topic Area | ISACA Reference |
|-----------|---------------|
| Cloud computing audit | ISACA Cloud Audit Program |
| AI audit | ISACA AI Audit Toolkit |
| Cybersecurity audit | ISACA Cybersecurity Audit Program |
| Privacy / BCP-DRP / SDLC / vendor audit | Respective ISACA audit programs |

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

### CMMI-Based Capability Model (Official COBIT 2019 CPM)

| Level | Name | Description |
|-------|------|------------|
| 0 | Incomplete | Process not implemented or fails purpose |
| 1 | Performed | Process achieves its purpose |
| 2 | Managed | Planned, monitored, adjusted; work products managed |
| 3 | Established | Defined and deployed using a standard process |
| 4 | Predictable | Operates within defined limits |
| 5 | Innovating | Continuously improved for business goals |

Use the CMMI-based model for all COBIT 2019 assessments. Bridge to legacy model only when stakeholders reference it. COBIT 2019 distinguishes process *capability* (rated per process, above) from focus-area *maturity* -- keep the terms distinct.

## Maturity Assessment Process

1. Select COBIT process to assess. 2. Gather evidence (interviews, documentation, observation, testing). 3. Rate current level based on evidence. 4. Determine target level (business needs, risk appetite, benchmarks). 5. Identify gaps. 6. Develop improvement roadmap in four phases (Quick Win 1-3 months; Short-Term 3-6 months; Medium-Term 6-12 months; Long-Term 12-24 months). Roadmap "gain" values are illustrative planning estimates of capability improvement -- actual gains depend on which practices the initiatives close, not on elapsed time.

**Decision rule:** Rate at the highest level where ALL attributes of that level are fully satisfied. If any attribute is not met, rate at the lower level. The official COBIT 2019 CPM therefore yields INTEGER capability levels. Fractional scores in this skill's templates (e.g., `2.5`) are a house convention meaning "level 2 fully achieved, level 3 partially achieved" -- label them as such in deliverables; do not present fractional levels as official CPM ratings.

## Output template (Maturity Assessment)

Field names below are the skill's output contract (matched by the use-case oracles). The
result envelope wraps the assessment with a `classification` field of the form `GAP_<max gap>`
(e.g., `GAP_1.5`) summarizing the largest process gap; the assessment object's envelope key
is `maturity_assessment`.

```yaml
classification: "GAP_1.5"
maturity_assessment:
  date: YYYY-MM-DD
  processes:
    - id: APO13
      name: "Managed Security"
      current_maturity: 2.5   # house convention -- see Decision rule note above
      target_maturity: 4.0
      gap: 1.5
      practice_areas:
        - name: "Security policy"
          current_level: 3
          evidence: "Documented policy exists, updated 18 months ago"
        - name: "Security monitoring"
          current_level: 3
          evidence: "SIEM deployed, 24/7 SOC, covers 80% of critical systems"
  improvement_roadmap:
    - phase: "Quick Win (1-3 months)"
      gain: 0.5               # illustrative estimate, not a promised increment
      initiatives:
        - "Refresh security policy for cloud"
```

## Citations

Standards series and titles from `[ITAF]` (4th Edition full text; 5th Edition retains the series -- verify titles). Capability model from `[COBIT-2019]`. See SKILL.md S10.
