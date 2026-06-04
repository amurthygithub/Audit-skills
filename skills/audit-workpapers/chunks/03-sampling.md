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
| Population size | Large (>500) | Small (<500) |
| Quantified sampling risk | Yes | No (but must consider) |
| Projection | Required and quantified | Required but not quantified |

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
| 2% | 0% | 150 |
| 5% | 0% | 60 |
| 5% | 1% | 90 |
| 7% | 0% | 45 |
| 10% | 0% | 30 |

Procedure: define objective, define population, set parameters, determine sample size, select sample, perform tests, evaluate (sample deviation rate vs tolerable rate), document conclusion.

## Monetary Unit Sampling (MUS/PPS)

Purpose: substantive test for overstatement. Each dollar is a selection unit.

Parameters: Tolerable Misstatement (TM), Risk of Incorrect Acceptance (RIA), Expected Misstatement, Sampling Interval (SI = TM / RF), Population Book Value (BV), Reliability Factor (RF).

### Reliability Factors

| Overstatements | 1% | 5% | 10% | 15% | 20% |
|---------------|-----|-----|------|------|------|
| 0 | 4.61 | 3.00 | 2.31 | 1.90 | 1.61 |
| 1 | 6.64 | 4.75 | 3.89 | 3.38 | 2.95 |
| 2 | 8.41 | 6.30 | 5.33 | 4.72 | 4.17 |
| 3 | 10.05 | 7.76 | 6.69 | 5.98 | 5.32 |

### Formulas

```
SI = TM / RF
n = (BV x RF) / TM          [basic]
n = (BV x RF) / (TM - E[M]) [with expected misstatement]
```

Selection: random start between $0.01 and SI; select items where cumulative amount crosses interval boundary; items > SI automatically selected (100%).

### MUS Evaluation — ULM

```
BP = RF x SI
Tainting = Misstatement / Book Value
IA = (Additional RF - Previous RF) x SI
ULM = BP + sum(IA)
If ULM <= TM -> population not materially misstated; accept
If ULM > TM -> consider additional procedures
```

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

n = N x [1 - (1 - D)^(1/d)]
where N = population size, D = desired detection confidence (typically 95%), d = expected occurrences (typically 0 for critical attributes).

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
