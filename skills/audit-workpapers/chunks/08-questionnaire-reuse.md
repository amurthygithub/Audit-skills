---
chunk_id: 08-questionnaire-reuse
parent_skill: audit-workpapers
topic: "Questionnaire Evidence Reuse (CAIQ / SIG Lite / VSAQ / Customer Security Questionnaires)"
load_when: "user asks to map audit workpaper evidence (sampling, 5-part findings, evidence hierarchy) to CAIQ, SIG Lite, VSAQ, or customer security questionnaires"
---

# Audit Workpaper Evidence Reuse for Customer Security Questionnaires

Audit workpapers produced for financial statement audits, ICFR assessments, and SOC examinations contain structured, tested evidence that can be systematically reused for customer security questionnaires. The key advantage: workpaper evidence has already undergone independent review, making it the strongest possible answer for due diligence questionnaires.

## Mapping Table: Workpaper Evidence Types -> CAIQ / SIG Lite / VSAQ

| Workpaper Type | CAIQ v4 Section(s) | SIG Lite Domain(s) | VSAQ Module | Key Fields Answered |
|---------------|--------------------|--------------------|--------------------|----------------------|
| MUS Sampling (AS 2315) | N/A (statistical backing) | N/A | N/A | Provides statistical confidence for "how did you test X" |
| IPE Validation (AS 1105) | DCS, IAM | Data Integrity, Access Ctrl | Section 2, 3 | Completeness/accuracy of reports used for control operation |
| Walkthrough Documentation (AS 2201) | GRM, CHM | Control Environment, Change | Section 1, 5 | Process documentation, I/O/I/R evidence |
| 5-Part Finding (C-C-C-E-R) | AAC | Compliance | Section 1 | Finding documentation, severity, remediation |
| Engagement Completion Doc (AS 1215.13) | AAC | Compliance | Section 1 | Sign-off, EQR review, evidence of supervision |
| ICFR Draft Report | GRM | Governance | Section 1 | Control effectiveness conclusions |
| Management Letter | GRM, AAC | Governance, Compliance | Section 1 | Auditor communications, recommendations |
| Sampling Plan | N/A (methodology) | N/A | N/A | Demonstrates testing rigor, sample methodology |

## Evidence Reuse Strategy

### Step 1: Create an Evidence Hierarchy for Questionnaires
Rank evidence sources by strength for questionnaire purposes:
1. **External auditor reports** (SOC 2 Type II, ICFR opinion) -- strongest.
2. **Independently tested workpaper evidence** (MUS samples, IPE validation) -- strong.
3. **Management-asserted evidence** (policies, narratives) -- moderate.
4. **Self-attestation only** -- weakest. Always elevate to higher tiers when possible.

### Step 2: Build a Cross-Referenced Evidence Map
- Index workpapers by the A-N indexing system (see chunk 01).
- Cross-reference each workpaper to questionnaire domains using the mapping table above.
- When a questionnaire asks "how do you test access controls?" reference the sampling workpaper index and sample size.

### Step 3: Ensure Workpaper Quality for Questionnaire Use
- Workpapers used for questionnaire evidence must meet the AS 1215 experienced auditor standard.
- All three required elements (purpose, source, conclusion) must be present.
- If a workpaper will be shared externally, redact sensitive client/sample detail.
- Consider a "questionnaire-ready" version of key workpapers with redacted detail preserved.

## Questionnaire-Specific Tips

- **CAIQ**: Reference workpaper indexes for quantitative evidence ("tested 40 samples of control X with 0 deviations").
- **SIG Lite**: The IPE validation workpaper directly answers data integrity questions.
- **VSAQ**: Walkthrough documentation answers process description questions.
- **Custom questionnaires**: Use the 5-part finding format to describe known gaps transparently and build credibility.

## When Questionnaires Exceed Workpaper Scope

Customer questionnaires often ask questions outside the scope of financial/operational audit workpapers (e.g., "do you use a specific security tool?"). For these:
- Answer from the broader compliance program evidence (SOC 2, ISO 27001, NIST 800-53).
- Use workpaper evidence to supplement, not replace, security-specific evidence.
- Document the scope boundary: "This workpaper covers X; see SOC 2 report for Y."

## Cross-Reference to Other Skills

- `aicpa-soc-reporting` -- SOC 2 report is the primary questionnaire evidence artifact (see its chunk 08).
- `coso-internal-controls` -- ICFR workpapers map to governance questionnaire domains.
- `isaca-audit-methodology` -- ITGC workpapers answer IT-specific questionnaire domains.
- `nist-800-53-rmf` -- SSP and SAR workpapers answer federal/government questionnaires.

## When to Load This Chunk

Load when the user asks about reusing audit workpaper evidence for customer questionnaires, mapping workpaper types to CAIQ/SIG/VSAQ, or building an evidence hierarchy for questionnaire responses.
