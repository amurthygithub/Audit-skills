---
chunk_id: 02-evidence-and-reperformance
parent_skill: audit-workpapers
topic: "Audit Evidence Types, Hierarchy, Re-Performance and Re-Computation (AS 1105)"
load_when: "user asks about evidence hierarchy, AS 1105, re-performance, re-computation, or IPE validation"
---

# Chunk 02 — Evidence & Re-Performance

## Evidence Categories (AS 1105.03)

A. Risk Assessment Procedures — Required for every engagement.
B. Further Audit Procedures: Tests of Controls (when relying on operating effectiveness), Substantive Procedures (tests of details, substantive analytical procedures).

## Audit Evidence Types (AS 1105.15-.21)

| Type | Standard | Description |
|------|----------|-------------|
| Inspection | AS 1105.15 | Examining documents/records and physical examination of tangible assets |
| Observation | AS 1105.16 | Looking at process/procedure performed by others (point-in-time evidence) |
| Inquiry | AS 1105.17 | Seeking info from knowledgeable persons. CRITICAL: inquiry alone is NOT sufficient |
| Confirmation | AS 1105.18 | Direct written communication from third party |
| Recalculation | AS 1105.19 | Checking mathematical accuracy |
| Reperformance | AS 1105.20 | Independent execution of procedures/controls originally by entity |
| Analytical Procedures | AS 1105.21 | Evaluation of plausible relationships among financial/nonfinancial data |

## Evidence Reliability Hierarchy (AS 1105, AICPA Audit Guide)

1. External evidence directly obtained > Internal evidence
2. Independent source > Company source
3. Directly obtained by auditor > Indirectly obtained
4. Original documents > Photocopies/facsimiles
5. Effective IT controls over data > Systems without controls
6. Written evidence > Oral evidence

Note: The numbered hierarchy above reflects general audit practice guidance, not a specific enumerated list in AS 1105.08. AS 1105.08 discusses reliability factors of evidence in general prose. The numbered structure is drawn from AICPA AU-C 500 and the AICPA Audit Guide guidance on evidence reliability.

## Financial Statement Assertions (AS 1105.11)

| Assertion | Definition | Typical Procedures |
|-----------|-----------|-------------------|
| Existence/Occurrence | Assets/liabilities exist; transactions occurred | Confirmation, inspection, observation |
| Completeness | All transactions/accounts included | Tracing, cutoff testing |
| Valuation/Allocation | Amounts appropriate; allocations reasonable | Recalculation, fair value testing |
| Rights and Obligations | Entity holds rights to assets; liabilities are obligations | Contract review, confirmation |
| Presentation and Disclosure | Components properly classified and disclosed | Disclosure checklist |

## Contradictory Evidence (AS 1105.29)

When evidence contradicts other evidence: investigate inconsistency, obtain further corroborating evidence, evaluate reliability, consider implications, document resolution. Do not disregard contradictory evidence without investigation.

## Re-Performance Documentation Template

Required: source of original, procedure independently re-performed, inputs used with sources, method/formula applied, result of independent re-performance, comparison to original, conclusion. If not in agreement: investigation of difference, root cause, implications.

### Re-Performance Template

```
WP INDEX: [ref]
OBJECTIVE: [what is being re-performed]
ORIGINAL: source, method/formula, inputs, result
INDEPENDENT RE-PERFORMANCE: procedure, inputs, method, result
COMPARISON: agrees [Y/N], difference, investigation, root cause
CONCLUSION: [statement]
```

## IPE Risk Assessment (AS 1105.10)

When relying on information produced by the company (IPE): assess extraction/parameters risk, data integrity/ITGC risk, end-user computing (EUC) risk.

### IPE Classification

Source dimension: SYSTEM-GENERATED (ERP extract) vs END-USER COMPUTING (Excel, Access).
Purpose dimension: POPULATION (items to test) vs ANALYTICAL INPUT (feeds calculation) vs SUPPORTING EVIDENCE.

### IPE Mandatory Procedures

1. Establish population completeness: reconcile to GL, sequence testing.
2. Verify data accuracy: source document vouching, logic/formula recalculation.
3. Evaluate system reliability: ITGC reference, automated application controls.
