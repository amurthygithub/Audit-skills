---
chunk_id: 05-deficiency-classification
parent_skill: coso-internal-controls
topic: "Control Deficiency Classification — Complete Decision Tree (D/SD/MW)"
load_when: "user asks to classify a deficiency, determine material weakness vs significant deficiency, or apply AS 2201 deficiency criteria"
---

# Chunk 05 — Deficiency Classification

## Definitions (PCAOB AS 2201 Appendix A, .62-.70)

**Deficiency**: A defect in the design or operation of ICFR such that a control does not allow management or employees, in the normal course of their assigned functions, to prevent or detect misstatements on a timely basis.

**Significant Deficiency**: A deficiency, or combination of deficiencies, in ICFR that is less severe than a material weakness, yet important enough to merit attention by those responsible for oversight of financial reporting.

**Material Weakness**: A deficiency, or combination of deficiencies, in ICFR such that there is a reasonable possibility that a material misstatement of annual or interim financial statements will not be prevented or detected on a timely basis.

## Decision Tree — Executable Logic

INPUT: Control deficiency (description, affected accounts/disclosures, affected assertions, compensating controls if any).

### Step 1: Determine If Deficiency Exists

Question: Is there a defect in the design or operation of ICFR such that a control does not allow management or employees to prevent or detect misstatements on a timely basis?

IF NO → NOT A DEFICIENCY → Document rationale → EXIT
IF YES → PROCEED TO STEP 2

### Step 2: Assess Reasonable Possibility of Material Misstatement

Question: Is there a reasonable possibility that ICFR will fail to prevent or detect a misstatement of an account balance or disclosure?

Reasonable possibility = the likelihood is either "reasonably possible" or "probable" as those terms are used in FASB Statement No. 5 (ASC 450) — i.e., more than remote (AS 2201 note to the material-weakness definition). The old AS 2 "more than inconsequential" threshold was deliberately rescinded by AS 5.

IF NO → CLASSIFY AS: DEFICIENCY
  Reporting: Communicate to management (oral or written)
  External: No public disclosure required
  ICFR Opinion: No modification

IF YES → PROCEED TO STEP 3

### Step 3: Assess Magnitude of Potential Misstatement

Question: Could the potential misstatement be material to financial statements (annual or interim)?

Consider: size of account, sensitivity of assertion, likelihood of aggregation, does NOT depend on whether misstatement actually occurred (AS 2201.65).

IF MATERIAL → CLASSIFY AS: MATERIAL WEAKNESS
  Reporting: Communicate to audit committee IN WRITING
  External: Must disclose in public filings (Form 10-K)
  ICFR Opinion: ADVERSE opinion — ICFR is NOT effective
  CHECK MW INDICATORS (AS 2201.69)

IF NOT MATERIAL, but important enough to merit attention → CLASSIFY AS: SIGNIFICANT DEFICIENCY
  Reporting: Communicate to audit committee IN WRITING
  External: No public disclosure required
  ICFR Opinion: Unqualified (if no MW exists)


### Step 4: Aggregation Evaluation (AS 2201.68)

CRITICAL RULE (AS 2201.68,.65-.70): AS 2201.68 requires evaluation of deficiencies both individually and in combination; the broader framework at AS 2201.65-.70 considers likelihood, magnitude, pervasiveness, and interaction effects. After classifying each deficiency individually, the auditor MUST also evaluate whether multiple deficiencies, when aggregated, create a material weakness — even if individually they are only significant deficiencies or control deficiencies.

Aggregation Procedure:
1. Group deficiencies by affected account, disclosure, assertion, or financial statement line item.
2. Assess whether the combined effect of aggregated deficiencies creates a reasonable possibility of a material misstatement.
3. Consider interaction effects: a design deficiency in one control may compound an operating deficiency in a related control, increasing the combined severity.
4. Document the aggregation analysis: list of deficiencies aggregated, shared accounts/assertions, combined risk assessment, conclusion.

EXECUTABLE LOGIC:
IF (aggregated deficiencies affect same account AND combined failure potential > remote) AND (combined magnitude could be material) → CLASSIFY AS: MATERIAL WEAKNESS

This rule can elevate multiple SDs to a single MW even when no individual deficiency meets the MW threshold.


## Severity Assessment Factors (AS 2201.63-.68)

| Factor | Consideration |
|--------|---------------|
| Reasonable possibility | Likelihood misstatement could occur and not be prevented/detected |
| Magnitude | Size of potential misstatement relative to materiality |
| Nature of account | Subjectivity, complexity, related-party involvement |
| Vulnerability | Susceptibility of assertion to misstatement |
| Aggregation | Could small misstatements aggregate to material? |
| Actual misstatement | If already occurred, strong evidence; absence does NOT reduce severity |
| Compensating controls | Existence and effectiveness |

CRITICAL RULE: Severity does NOT depend on whether a misstatement actually occurred (AS 2201.65).

## Material Weakness Indicators (AS 2201.69)

AS 2201.69 lists these as INDICATORS of material weaknesses ("Indicators of material weaknesses ... include") — not automatic determinations. Treat each as a strong, rebuttable presumption: overcoming one requires documented evaluation and is rare.

1. **Fraud by senior management**, whether or not material — undermines control environment (P1, P5), suggests management override.

2. **Restatement of previously issued financial statements** to correct a material misstatement — demonstrates ICFR failed to prevent/detect.

3. **Identification of material misstatement by auditor** that would not have been detected by ICFR.

4. **Ineffective oversight** of external financial reporting and ICFR by the audit committee.

## Deficiency Reporting Requirements

| Classification | To Management | To Audit Committee | Public Disclosure | ICFR Opinion |
|----------------|---------------|--------------------|-------------------|--------------|
| Deficiency | Yes (oral or written) | Not required | No | No modification |
| Significant Deficiency | Yes (written) | Yes (written) | No | No modification (if no MW) |
| Material Weakness | Yes (written) | Yes (written) | Yes (Form 10-K) | Adverse |

Per AS 2201.78-.84 (integrated audit of internal control and financial statements), the auditor shall communicate SDs and MWs in writing to the audit committee.

## Citations

- [PCAOB-AS-2201 .62-.70, .68, .69] — Deficiency classification, aggregation rule, and MW indicators
- [PCAOB-AS-1305] — Communications about control deficiencies
- [PCAOB-AS-2201 .78-.84] — Integrated audit communications
