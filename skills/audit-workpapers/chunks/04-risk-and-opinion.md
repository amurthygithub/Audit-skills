---
chunk_id: 04-risk-and-opinion
parent_skill: audit-workpapers
topic: "Audit Risk Model (AR = IR x CR x AP x TD) and Opinion Determination (AS 3105)"
load_when: "user asks about audit risk model, AR = IR x CR, TD calculation, or audit opinion determination"
---

# Chunk 04 — Risk Model & Opinion

## Audit Risk Model

AR = IR x CR x AP x TD

Where:
AR = Allowable Audit Risk (typically 5% or 10%)
IR = Inherent Risk
CR = Control Risk
AP = Risk that analytical procedures fail to detect misstatement
TD = Allowable risk of incorrect acceptance for substantive test of details

### Computing TD

```
TD = AR / (IR x CR x AP)
```

Example: AR=5%, IR=80%, CR=60%, AP=50% -> TD = 0.05/(0.80x0.60x0.50) = 20.8%.



## Cross-Framework Risk Formula Reconciliation

Three risk formulas appear across the audit family skills. They express the same underlying concept using different notation:

| Skill | Formula | Notation | Scope |
|-------|---------|----------|-------|
| audit-workpapers | AR = IR x CR x AP x TD | Audit Risk = Inherent Risk x Control Risk x Analytical Procedure Risk x Test of Details risk | PCAOB AS 1101/AS 2110; decomposed substantive-testing precision |
| isaca-audit-methodology | Risk = Likelihood x Impact | Likelihood x Impact, adjusted by Control Risk Factor (CRF) | ISACA CISA-CRM-28E risk-based audit planning; engagement-level prioritization |
| coso-internal-controls | Inherent Risk = Impact x Likelihood | Impact x Likelihood | COSO ERM 2017; enterprise risk assessment |

**Reconciliation:** Inherent Risk (IR) = Likelihood x Impact = Impact x Likelihood. All three frameworks assess the same two dimensions -- probability of occurrence and magnitude of consequence. The difference is:
- **ISACA** multiplies by a Control Risk Factor (CRF) to get Residual Risk (post-controls).
- **PCAOB/AICPA** decomposes Audit Risk into component sub-risks including Control Risk (CR), Analytical Procedures risk (AP), and Test of Details risk (TD) for precise sample-size calculation at the substantive-testing level.
- **COSO** uses Inherent Risk as input to the Risk Assessment component; Residual Risk is determined after evaluating control effectiveness.

Do NOT mix formulas in the same engagement. Choose one based on the governing framework and apply it consistently. The PCAOB decomposition (AR = IR x CR x AP x TD) is specifically designed for financial statement audit substantive testing, while ISACA's Risk = L x I is designed for IT audit planning prioritization.

### Risk Types Summary

| Risk Type | Effect | Impact |
|-----------|--------|--------|
| Risk of Incorrect Acceptance | Affects EFFECTIVENESS | More serious |
| Risk of Incorrect Rejection | Affects EFFICIENCY | Less serious |
| Risk of Assessing CR Too Low | Affects EFFECTIVENESS | More serious |
| Risk of Assessing CR Too High | Affects EFFICIENCY | Less serious |

### AS 2315 Appendix — Risk Assessment Matrix (AR=5%)

| IR | CR | AP | Combined | TD | Extent |
|----|-----|-----|----------|-----|--------|
| Max(100%) | Max(100%) | High(100%) | 1.00 | 5% | Maximum |
| High(80%) | High(80%) | High(80%) | 0.512 | ~10% | Very extensive |
| High(80%) | High(80%) | Mod(50%) | 0.32 | ~16% | Extensive |
| High(80%) | Mod(50%) | Mod(50%) | 0.20 | 25% | Mod-large |
| Mod(50%) | Mod(50%) | Mod(50%) | 0.125 | 40% | Moderate |
| Mod(50%) | Low(30%) | Low(20%) | 0.03 | >100% | Minimal |

### Required TD to Sample Size (MUS)

| TD Level | RIA | RF | Extent |
| Very Low (<=5%) | <=1% | >=4.61 | Very large |
| Low (5-10%) | 1-5% | 3.00-4.61 | Large |
| Moderate (10-30%) | 5-10% | 2.31-3.00 | Moderate |
| High (30-50%) | 10-15% | 1.90-2.31 | Small |
| Very High (>50%) | 15-20% | 1.61-1.90 | Minimal |

## Opinion Determination (AS 3105)

### Decision Flow

Is audit scope limited?
- YES: limitation material and pervasive? -> Disclaimer / Qualified-scope
- NO: GAAP departure?
  - YES: material and pervasive? -> Adverse / Qualified-GAAP
  - NO: -> Unqualified

### Opinion Types

| Opinion | When | Report Language |
|---------|------|-----------------|
| Unqualified | FS present fairly in all material respects | "In our opinion, the financial statements present fairly..." |
| Qualified (scope) | Unable to obtain sufficient evidence; not pervasive | "Except for the effects of adjustments, if any... we were unable to..." |
| Qualified (GAAP) | FS not in conformity with GAAP; not pervasive | "Except for the effects of the matter discussed in Note X..." |
| Adverse | GAAP departure so material and pervasive | "...do not present fairly..." |
| Disclaimer | Scope limitation so material and pervasive; or independence impaired | "We do not express an opinion..." |

### Critical Audit Matters (AS 3101)

CAM: matter arising from audit communicated to audit committee involving especially challenging, subjective, or complex auditor judgment on accounts/disclosures material to FS. Document each CAM, why CAM, and how addressed.

### Report Elements (AS 3101)

Title, Addressee, Opinion section, Basis for Opinion, Critical Audit Matters (if applicable), Signature/firm/city/state, Date, Auditor tenure disclosure.
