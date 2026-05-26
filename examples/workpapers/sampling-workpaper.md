# Example: Audit Sampling Workpaper

**Skill**: audit-workpapers
**Scenario**: You are a senior auditor documenting sampling procedures for the accounts receivable and inventory accounts of "RetailCo" ($500M revenue, year-end December 31, 2026).

---

## Prompt

```
I need to design and document sampling procedures for RetailCo:
1. Accounts Receivable: Attribute sampling to test sales transaction controls
2. Inventory: MUS to test accounts receivable valuation
3. Inventory count observation: Variables sampling for physical inventory

Materiality: $15M overall; Performance materiality: $10M
Tolerable misstatement for AR: $8M
Risk assessments: IR=60%, CR=40% (some ITGC issues), AP=50%

Provide complete sampling workpapers per PCAOB AS 2315.
```

## Expected Agent Output Structure

### 1. Risk Model Calculation (§7.1-7.4)

```
Audit Risk (AR) = 5% (by convention)

IR = 60% = 0.60
CR = 40% = 0.40  (ITGC partially effective — access review gaps)
AP = 50% = 0.50

TD = AR / (IR × CR × AP)
   = 0.05 / (0.60 × 0.40 × 0.50)
   = 0.05 / 0.12
   = 41.7%

DR = AP × TD = 0.50 × 0.417 = 20.8%

→ High TD (41.7%) means less reliance on tests of details
→ Moderate substantive testing required
```

**AS 2315 Appendix Table 2 Assessment (§7.4)**:
| Risk Level | IR | CR | AP | Combined | TD | Extent |
|-----------|-----|-----|-----|----------|-----|--------|
| High IR, Moderate CR, Moderate AP | 60% | 40% | 50% | 12% | 41.7% | Moderate substantive testing |

### 2. Attribute Sampling — Sales Transaction Controls (§6.1)

**Objective**: Test operating effectiveness of the 3-way match control for sales invoices

**Parameters**:
- Tolerable deviation rate: 5%
- Expected deviation rate: 1%
- Risk of overreliance (alpha risk): 5% (but using AS 2315 terminology: "risk of assessing control risk too low")

**Sample Size**: Per AICPA sample size tables (or formula approx):
```
n = (Z² × p × (1-p)) / E²
where Z = 1.96 (95% confidence), p = 0.01, E = 0.05-0.01 = 0.04
n = (3.8416 × 0.01 × 0.99) / 0.0016
n ≈ 24

Per AICPA tables: n = 77 (at 5% ROR, 1% EDR, 5% TDR)
```

**Note**: ISACA CISA CRM references AICPA sample size tables for practical use — formula shown for illustration only.

**Test Results**:
- 77 invoices sampled
- 2 deviations found (2.6% deviation rate)
- Per AICPA tables: 2 deviations at n=77, 5% ROR → upper limit = 6.2%
- 6.2% > 5% tolerable deviation rate → **CANNOT reduce assessed CR**

**Workpaper Conclusion**: Control is not operating effectively at the required precision.

### 3. MUS — Accounts Receivable Valuation (§6.2-6.3)

**Parameters**:
- Population: $85,000,000 (2,400 accounts)
- Tolerable misstatement (TM): $8,000,000
- Expected misstatement: $400,000
- Risk of incorrect acceptance: 10%

**Calculation**:
```
Sampling interval (SI) = TM / reliability factor
For 10% RIA, 0 expected errors → factor = 2.31 (per MUS table)

SI = $8,000,000 / 2.31 = $3,463,203

Sample size = Population / SI = $85,000,000 / $3,463,203 ≈ 25 items

High-value items (100% examination): 3 accounts > $3,463,203
Remaining sample: 22 items selected at SI intervals
```

**Test Results**:
- 3 high-value accounts: $4.2M, $5.1M, $3.8M — confirmed, no errors
- 22 sampled accounts tested: 1 overstatement found
  - Book value: $520,000; Audited value: $480,000; Error: $40,000
  - Taint = $40,000 / $520,000 = 7.7%
  - Projected error = Taint × SI = 0.077 × $3,463,203 = $266,667

**Evaluation**:
```
Basic Precision = SI × reliability factor = $3,463,203 × 2.31 = $7,999,799
Incremental allowance = $266,667 × 1.0 (1 error, incremental factor from table)
Upper limit on misstatement = $266,667 + $7,999,799 = $8,266,466

Comparison to Tolerable:
$8,266,466 > $8,000,000 (TM)
→ Upper limit EXCEEDS tolerable misstatement

CONCLUSION: Cannot conclude AR is fairly stated at TM threshold.
Pending additional procedures.
† Rounding differences ≤$1 are immaterial.
```

### 4. Variables Sampling — Physical Inventory (§6.4, §21.3)

**Objective**: Test whether physical inventory count supports recorded amount

**Parameters**:
- Population: $120,000,000 (4,000 SKU locations)
- Strata: 40 high-value items (100% exam), 3,960 remaining
- Difference estimation for remaining items

**Sample from remaining (n=195)**:
- Mean difference per item: -$101.61
- Sample standard deviation (s_d): $485

**Projection**:
```
Projected Misstatement = d̄ × N_remaining = -$101.61 × 3,960 = -$402,376
+ High-value stratum results = $0 (all confirmed)
Total projected misstatement = -$402,376
```

**Precision**:
```
Adjusted precision = (Z × s_d × N / √n) × √(1 - n/N)
= (1.96 × $485 × 3,960 / 13.964) × √(1 - 195/3,960)
= $268,856 × 0.9751
≈ $262,167

Note: The FPC √(1-n/N) is a multiplier applied to precision, not a divisor.
s_d denotes the sample standard deviation (estimated, not population σ).

Confidence interval:
Lower limit = -$402,376 - $262,167 = -$664,543
Upper limit = -$402,376 + $262,167 = -$140,209

Comparison to Tolerable:
$664,543 < TM of $8,000,000 → Inventory is fairly stated
```

### 5. Workpaper Documentation (§11)

Per the sampling workpaper template (§11.2):
- Section A: Objective, population, sampling unit
- Section B: Method (MUS/difference estimation), parameters, sample size calculation
- Section C: Sample selection method, random start, intervals
- Section D: Test results, deviations, projected error, comparison to tolerable
- Section E: Conclusion, cross-references to lead schedule

---

## Key Agent Behaviors to Verify

1. **Risk model consistent**: AR = IR × CR × AP × TD throughout; DR = AP × TD in glossary
2. **AS 2315 terminology**: No "Alpha Risk" or "Beta Risk" in risk types table — only in clearly-labeled supplementary note
3. **FPC applied correctly**: √(1-n/N) as multiplier, not divisor (the Cycle 3 fix)
4. **s_d notation**: Uses s_d (sample estimate), not σ (population parameter) in formulas
5. **Oral evidence**: Any oral representations properly documented with AS 1215.06 caveat
6. **5-part findings**: Condition-Criteria-Cause-Effect-Recommendation format for any identified deficiencies
7. **MUS rounding footnote**: "Rounding differences ≤$1 are immaterial"