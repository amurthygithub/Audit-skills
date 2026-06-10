---
chunk_id: 03-sampling
parent_skill: audit-workpapers
topic: "Complete Sampling Methodology (MUS/PPS, Attribute, Variables, Non-Statistical, Dual-Purpose)"
load_when: "user asks about sampling plans, MUS, attribute sampling, variables, ULM, sample size, or selection methods"
---

# Chunk 03 — Sampling Methodology

## Sampling Decision Framework

1. 100% examination suitable? -> test 100%.
2. Specific items appropriate? -> select specific items. Results CANNOT be projected.
3. Audit sampling appropriate? -> proceed to statistical vs non-statistical.

### Statistical vs Non-Statistical

| Factor | Statistical | Non-Statistical |
|--------|-------------|-----------------|
| Population size | Any (more cost-effective at scale) | Any (often small populations) |
| Quantified sampling risk | Yes | No (but must consider) |
| Projection | Required and quantified | Required but not quantified |

No standard sets a population-size bright line (AS 2315/AU-C 530); the real drivers are the test objective, the need to quantify sampling risk, and cost.

### Method Selection

| Objective | Method | When |
|-----------|--------|------|
| Control operating effectiveness | Attribute Sampling | Tests of controls |
| Monetary overstatement | MUS/PPS | Substantive; positive balances |
| Overstatement AND understatement | Variables (Diff/Ratio) | Both directions |
| Estimate population value | Variables (MPU) | Book values unavailable |

## Attribute Sampling

Purpose: estimate deviation rate. Parameters: tolerable rate, expected deviation rate, risk of assessing CR too low, risk of assessing CR too high.

Sample size table (95% confidence, 5% risk):

| Tolerable Rate | Expected Dev Rate | n |
|---------------|------------------|------|
| 2% | 0% | 149 |
| 5% | 0% | 59 |
| 5% | 1% | 93 |
| 7% | 0% | 42 |
| 10% | 0% | 29 |

Values tie to the AICPA Audit Sampling Guide Table A-1 (zero-expected-deviation rows are exact binomial: smallest n with (1 - TR)^n <= 5%).

Procedure: define objective, define population, set parameters, determine sample size, select sample, perform tests, evaluate — compute the achieved upper deviation limit (reliability factor for the number of deviations found / n) and compare it to the tolerable rate; comparing the raw sample deviation rate alone ignores sampling risk and silently passes failed controls — then document the conclusion.

## Monetary Unit Sampling (MUS/PPS)

Purpose: substantive test for overstatement. Each dollar is a selection unit.

Parameters: Tolerable Misstatement (TM), Risk of Incorrect Acceptance (RIA), Expected Misstatement, Sampling Interval (SI = TM / RF), Population Book Value (BV), Reliability Factor (RF).

### Reliability Factors

| Overstatements | 1% | 5% | 10% | 15% | 20% |
|---------------|-----|-----|------|------|------|
| 0 | 4.61 | 3.00 | 2.31 | 1.90 | 1.61 |
| 1 | 6.64 | 4.75 | 3.89 | 3.38 | 3.00 |
| 2 | 8.41 | 6.30 | 5.33 | 4.72 | 4.28 |
| 3 | 10.05 | 7.76 | 6.69 | 6.02 | 5.52 |

### Formulas

```
SI = TM / RF
n = (BV x RF) / TM          [basic]
n = (BV x RF) / (TM - E[M]) [with expected misstatement]
```

Selection: random start between $0.01 and SI; select items where cumulative amount crosses interval boundary; items > SI automatically selected (100%).

### MUS Evaluation — ULM

```
BP = RF(0 misstatements) x SI                       # basic precision
For each misstated sampled item with book value < SI (rank taintings DESCENDING):
  Tainting_i = Misstatement_i / Book Value_i
  PM_i = Tainting_i x SI                            # projected misstatement
  IA_i = (RF_i - RF_(i-1) - 1) x Tainting_i x SI    # incremental allowance (RF at i misstatements)
Top stratum (book value >= SI): add ACTUAL misstatement — no sampling allowance
ULM = BP + sum(PM_i) + sum(IA_i) + top-stratum actual misstatements
If ULM <= TM -> population not materially misstated; accept
If ULM > TM -> consider additional procedures
Understatements are evaluated separately (MUS is an overstatement test).
```
Method per the AICPA Audit Sampling Guide; a $1 and a $150,000 misstatement in sampled items must NOT produce the same ULM — the tainting term is what differentiates them.

## Variables Sampling

Three methods: Mean-per-Unit (MPU), Difference Estimation, Ratio Estimation.

```
n = (Z x sigma / A)^2
Z: 90%->1.64, 95%->1.96, 99%->2.58
sigma = estimated population standard deviation
A = TM - Expected Misstatement

For difference/ratio: A_per_item = A / N
n = (Z x sigma / A_per_item)^2

n_adj = n / (1 + n/N)     [finite population correction]
```

Sigma estimation: pilot sample (>=30 items), prior-year data, range rule (sigma approx= Range/4).

### Projection
MPU: Est Pop = x-bar x N
Difference: Projected Misstatement = d-bar x N
Ratio: Est Pop = (sum audit / sum book) x Total BV

## Non-Statistical Sampling

Required documentation: rationale, sample size determination, selection method, evaluation methodology, sampling risk consideration, qualitative evaluation.


## Discovery Sampling (AICPA Audit Guide)

Purpose: determine whether a population contains occurrences of a critical attribute (e.g., fraud, regulatory non-compliance, material error). Used when even a single occurrence would cause the auditor to reject the population.

Parameters: acceptable occurrence rate (typically zero), detection risk, population size.

n >= ln(1 - D) / ln(1 - p)
where D = desired detection confidence (typically 95%) and p = the critical (minimum unacceptable) occurrence rate, p > 0.
Example: D = 95%, p = 1% -> n = ln(0.05)/ln(0.99) ~= 299. The expected occurrences are zero by design — the sizing parameter is the critical rate, never expected occurrences (a formula parameterized on expected occurrences of 0 is undefined).

Decision rule:
- Zero deviations found -> population is acceptable at the specified confidence level.
- One or more deviations found -> population is unacceptable; expand investigation or reject population.

Common applications: suspected fraud, regulatory violations, systemic control failures, testing segregation of duties.

## Dual-Purpose Sampling (AS 2315.44)

Sample size = larger of two separate required samples. Evaluate deviations and misstatements separately.

## Sample Selection Methods

| Method | Appropriate For |
|--------|-----------------|
| Random | Statistical |
| Systematic | Statistical and nonstatistical |
| PPS | MUS |
| Haphazard | Nonstatistical |
| Stratified | All methods with significant variability |
| Key Items | Nonstatistical; results NOT projected |
