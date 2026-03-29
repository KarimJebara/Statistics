# Statistics for Computer Scientists — Exam Study System
## Leiden University 2526 (2025-2026)

---

# EXAM STRUCTURE (Based on 3 Past Exams)

| Question | Topic | Points | Strategy |
|----------|-------|--------|----------|
| Q1 | Sampling & Data Collection | 2 pts | Identify method + bias type |
| Q2 | Choosing the Right Test | 2 pts | Decision tree (below) |
| Q3 | Regression (simple/multiple) | 2-2.5 pts | Highest value — master this |
| Q4 | Significance Test / Sample Size | 1.5-2 pts | 5-step framework or n formula |
| Q5 | Contingency Tables / Chi-squared | 1.5-2 pts | Expected counts + chi-squared |
| Q6-Q7 | Concept Questions | 1-1.5 pts each | Simpson's paradox, Type I/II, overfitting, publication bias |

**Total: 10 points. You need to nail Q2 and Q3 — together they're ~4.5 points (45%).**

---

# 1. SAMPLING & DATA COLLECTION (Q1)

## Sampling Methods

| Method | How it works | Key feature |
|--------|-------------|-------------|
| **Simple Random Sample (SRS)** | Every member has equal probability of selection | Gold standard, uses random number generator |
| **Systematic** | Every k-th element from ordered list | Need random starting point; risk if list has periodic pattern |
| **Stratified** | Divide population into strata, SRS within each | Guarantees representation of subgroups |
| **Cluster** | Randomly select entire groups, sample all within | Cheaper for geographically spread populations |
| **Multistage** | Cluster sampling + SRS within selected clusters | Most practical for large populations |

## Bias Types

| Bias | What it is | Example |
|------|-----------|---------|
| **Sampling bias / Undercoverage** | Some groups systematically excluded from sampling frame | Online survey excludes people without internet |
| **Nonresponse bias** | Selected people don't respond; non-responders differ from responders | Health survey — sickest people can't respond |
| **Response bias** | Answers are systematically wrong | Leading questions, social desirability, recall bias |
| **Publication bias** | Only significant results get published | File drawer problem — null results hidden |

## How to Identify (Exam Pattern)
- They describe a scenario → you name the sampling method AND the type of bias
- **Trap**: Convenience sampling is NOT a probability method — it's a source of sampling bias
- **Trap**: Voluntary response = nonresponse bias (self-selection)

---

# 2. CHOOSING THE RIGHT TEST — DECISION TREE (Q2)

This question gives you 4-5 scenarios. For each, identify the correct test.

```
START: What type of data?
│
├── Response variable is CATEGORICAL
│   ├── One proportion (one sample, one categorical var)
│   │   └── z-test for proportion
│   ├── Two proportions (two groups, categorical response)
│   │   └── z-test for difference of proportions
│   └── Two categorical variables (r × c table)
│       └── Chi-squared test of independence
│
├── Response variable is QUANTITATIVE
│   ├── One mean (one sample)
│   │   └── One-sample t-test
│   ├── Two means
│   │   ├── Same subjects measured twice (before/after, matched pairs)
│   │   │   └── Paired t-test (on differences d = x₁ - x₂)
│   │   └── Two independent groups
│   │       └── Independent two-sample t-test
│   └── Relationship between two quantitative variables
│       ├── One explanatory → Simple regression t-test (for slope β)
│       └── Multiple explanatory → Multiple regression F-test / individual t-tests
│
└── COMPARING MODELS
    └── Nested models (one is subset of other)
        └── F-test for model comparison
```

## Quick Identification Clues

| Clue in the question | Test |
|---------------------|------|
| "proportion", "percentage", "probability" | z-test for proportion(s) |
| "mean", "average", measurement data | t-test |
| "before and after", "same subjects", "matched" | **Paired** t-test |
| "relationship between two categorical" | Chi-squared |
| "predict Y from X", "slope", "regression" | Regression t-test (slope) |
| "does adding variable improve model" | F-test (nested models) |
| "is there a relationship" + both quantitative | Could be regression or correlation |

## Common Traps
- **Paired vs independent**: If the SAME people are measured twice → paired. If DIFFERENT people in two groups → independent.
- **One-sided vs two-sided**: Read the research question carefully. "Is there a difference?" = two-sided. "Is it higher/lower?" = one-sided.
- **Chi-squared is always two-sided** — you cannot do a one-sided chi-squared test.

---

# 3. REGRESSION — THE BIG QUESTION (Q3, 2-2.5 pts)

## Simple Linear Regression

**Population model**: μ_y = α + βx
**Sample prediction equation**: ŷ = a + bx

### Key Formulas

| What | Formula |
|------|---------|
| Slope | b = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)² |
| Intercept | a = ȳ - b·x̄ |
| Residual | eᵢ = yᵢ - ŷᵢ |
| Residual std dev | s = √(SSE / (n-2)) |
| Standard error of b | se = s / (sₓ · √(n-1)) |
| t-test for slope | t = b / se, df = n - 2 |
| Correlation | r = b · (sₓ / sᵧ) |
| r² | r² = 1 - SSE/Total SS = Regression SS / Total SS |

### Sums of Squares Decomposition

```
Total SS = Regression SS + Residual SS (SSE)
Σ(yᵢ - ȳ)² = Σ(ŷᵢ - ȳ)² + Σ(yᵢ - ŷᵢ)²
```

- **Total SS**: Total variability in Y
- **Regression SS (RSS)**: Variability explained by the model
- **Residual SS (SSE)**: Unexplained variability (error)

### Interpreting r²
- r² = 0.73 means "73% of the variability in Y is explained by X"
- r² = (Total SS - SSE) / Total SS
- r² is the proportional reduction in prediction error when using X instead of ȳ

### 5-Step Inference for Slope β

1. **Assumptions**: (a) Randomization, (b) Linear relationship (check scatter plot), (c) Constant σ at each x (check residual plot), (d) Normal distribution of Y at each x (check Q-Q plot / histogram of residuals)
2. **Hypotheses**: H₀: β = 0 (no linear relationship) vs Hₐ: β ≠ 0 (or one-sided)
3. **Test statistic**: t = b / se, df = n - 2
4. **P-value**: From t-table (Table B) with df = n - 2
5. **Conclusion**: "There is (in)sufficient evidence at α = 0.05 that [context-specific statement about slope]"

## Multiple Regression

**Model**: μ_y = α + β₁X₁ + β₂X₂ + ... + βₖXₖ

### Key Differences from Simple Regression

| Concept | Simple | Multiple |
|---------|--------|----------|
| Slope interpretation | "For each 1-unit increase in X, Y changes by b" | "For each 1-unit increase in Xⱼ, Y changes by bⱼ, **holding all other X constant**" |
| Correlation | r (can be negative) | R (always ≥ 0) |
| R² | r² | R² = 1 - SSE/Total SS (can never decrease when adding predictors) |
| df for residuals | n - 2 | n - (k + 1) |
| Overall test | t-test for slope | F-test |

### F-Test for Overall Model

Tests H₀: β₁ = β₂ = ... = βₖ = 0 (none of the predictors matter)

```
F = (R² / k) / ((1 - R²) / (n - (k+1)))
  = Mean Square Regression / Mean Square Error
```

- df₁ = k (number of predictors)
- df₂ = n - (k + 1)
- **Always one-sided (right tail)** — large F = evidence against H₀
- Use F-table at α = 0.05

### F-Test for Comparing Nested Models

If Model 1 has k₁ predictors and Model 2 has k₂ predictors (k₂ > k₁), and Model 1 is nested within Model 2:

```
F = ((SSE₁ - SSE₂) / (k₂ - k₁)) / (SSE₂ / (n - (k₂ + 1)))
```

- df₁ = k₂ - k₁
- df₂ = n - (k₂ + 1)

### Individual Coefficient t-Test

For each βⱼ: t = bⱼ / se(bⱼ), df = n - (k + 1)

**Important**: A predictor can be significant in simple regression but NOT in multiple regression (and vice versa) due to collinearity.

### Standardized Coefficients

b* = b · (sₓ / sᵧ)

Allows comparison of relative importance of predictors (unit-free).

### Interaction Terms

Model with interaction: μ_y = α + β₁X₁ + β₂X₂ + β₃(X₁·X₂)

- β₃ ≠ 0 means the effect of X₁ on Y depends on the value of X₂
- The slope of X₁ becomes: β₁ + β₃·X₂

### Residual Plots — What to Check

| Plot | What it checks | Good sign | Bad sign |
|------|---------------|-----------|----------|
| Residuals vs predicted | Constant variance + linearity | Random scatter around 0 | Fan shape (non-constant σ) or curve |
| Residuals vs each Xⱼ | Linearity for that predictor | Random scatter | Curve pattern |
| Histogram of residuals | Normality | Symmetric, bell-shaped | Skewed, outliers beyond ±3 |
| Q-Q plot | Normality | Points on diagonal line | Systematic departure from line |

### Overfitting & Model Selection

- **Overfitting**: Model fits training data too well, performs poorly on new data
- **PRESS** (Predicted Residual Sum of Squares): Leave-one-out cross-validation measure. Lower = better predictive ability.
- **R² always increases** with more predictors (even useless ones) — don't use R² alone for model selection
- **AIC, BIC/MDL**: Penalize model complexity. Lower = better. Use for non-nested model comparison.

---

# 4. HYPOTHESIS TESTING — 5-STEP FRAMEWORK

**Every hypothesis test on the exam follows this structure:**

### Step 1: Assumptions
State and verify the conditions for the test.

### Step 2: Hypotheses
- H₀: parameter = value (null, status quo, "no effect")
- Hₐ: parameter ≠ / > / < value (alternative, research hypothesis)

### Step 3: Test Statistic
Calculate the test statistic using the appropriate formula.

### Step 4: P-value
Find the P-value from the appropriate table (z, t, χ², F).

### Step 5: Conclusion
- If P-value ≤ α: "Reject H₀. There is sufficient evidence that [Hₐ in context]."
- If P-value > α: "Fail to reject H₀. There is insufficient evidence that [Hₐ in context]."

**NEVER say "accept H₀"** — you only "fail to reject" it.

## z-Test for Proportion

| | |
|---|---|
| Assumptions | Random sample, nπ₀ ≥ 15 and n(1-π₀) ≥ 15 |
| H₀ | π = π₀ |
| Test statistic | z = (p̂ - π₀) / √(π₀(1-π₀)/n) |
| P-value | From Table A (standard normal) |

## One-Sample t-Test for Mean

| | |
|---|---|
| Assumptions | Random sample, n > 30 or population approximately normal |
| H₀ | μ = μ₀ |
| Test statistic | t = (x̄ - μ₀) / (s/√n), df = n - 1 |
| P-value | From Table B (t-distribution) |

## Two-Sample t-Test (Independent)

| | |
|---|---|
| Assumptions | Two independent random samples, both n > 30 or populations approx normal |
| H₀ | μ₁ - μ₂ = 0 |
| Test statistic | t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂) |
| df | Use software or min(n₁-1, n₂-1) as conservative approximation |

## Paired t-Test

| | |
|---|---|
| Assumptions | Random sample of pairs, differences approximately normal |
| H₀ | μ_d = 0 (mean difference is zero) |
| Test statistic | t = d̄ / (s_d/√n), df = n - 1 (n = number of pairs) |
| Key | Compute differences FIRST, then do a one-sample t-test on the differences |

## Sample Size for Proportion

```
n = π(1-π) · (z*/M)²
```
- M = desired margin of error
- z* = critical value (1.96 for 95% CI)
- If π unknown, use π = 0.5 (gives maximum n, most conservative)
- **Always round UP** to next whole number

## Confidence Intervals

General form: **estimate ± z* · se** (or t* · se for t-based intervals)

| Parameter | CI Formula |
|-----------|-----------|
| Proportion π | p̂ ± z* · √(p̂(1-p̂)/n) |
| Mean μ | x̄ ± t* · (s/√n), df = n-1 |
| Difference of means | (x̄₁ - x̄₂) ± t* · √(s₁²/n₁ + s₂²/n₂) |
| Slope β | b ± t* · se(b), df = n-2 |

**Connection between CI and test**: If the CI at confidence level (1-α) does NOT contain 0 (or the null value), then you would reject H₀ at significance level α.

---

# 5. CHI-SQUARED TEST (Q5)

## Chi-Squared Test of Independence

**When**: Two categorical variables, testing if they are independent.

### Expected Counts

```
fₑ = (row total × column total) / n
```

**Assumption**: ALL expected counts fₑ ≥ 5

### Test Statistic

```
χ² = Σ (fₒ - fₑ)² / fₑ
```

- df = (r - 1)(c - 1), where r = rows, c = columns
- **Always right-tailed** (large χ² = more evidence against independence)
- P-value from Table C

### Standardized Residuals

```
z = (fₒ - fₑ) / se
where se = √(fₑ · (1 - row proportion) · (1 - column proportion))
```

- **|z| > 3** → noteworthy (that cell contributes significantly to the chi-squared)
- Positive z = more observed than expected
- Negative z = fewer observed than expected

### 2×2 Table Special Case

For a 2×2 contingency table: **χ² = z²** (chi-squared equals the square of the z-test for difference of proportions). They give the SAME p-value for a two-sided test.

### Goodness of Fit Test

Tests if a single categorical variable follows a specified distribution.
- fₑ = n · πⱼ (where πⱼ is the hypothesized proportion for category j)
- df = k - 1 (k = number of categories)

## Measures of Association (for Categorical Data)

| Measure | Formula | Interpretation |
|---------|---------|---------------|
| Difference of proportions | p̂₁ - p̂₂ | Absolute difference in group rates |
| Relative risk | p̂₁ / p̂₂ | "Group 1 is X times as likely as Group 2" |
| Odds ratio | (p̂₁/(1-p̂₁)) / (p̂₂/(1-p̂₂)) | Ratio of odds; used in logistic regression |

- Odds of event = P(event) / P(not event) = π / (1-π)
- If odds ratio = 1 → no association
- If odds ratio > 1 → higher odds in group 1

---

# 6. CONCEPT QUESTIONS — QUICK REFERENCE (Q6-Q7)

## Simpson's Paradox
- An association between two variables **reverses direction** when you control for a third variable (lurking/confounding variable)
- Classic exam question: Show that pooled data shows one trend, but within each subgroup the trend is opposite
- **Why it happens**: The lurking variable is unevenly distributed across groups

## Type I and Type II Errors

| | H₀ is true | H₀ is false |
|---|---|---|
| Reject H₀ | **Type I error** (false positive) | Correct (power) |
| Fail to reject H₀ | Correct | **Type II error** (false negative) |

- P(Type I error) = α (significance level)
- P(Type II error) = β
- **Power** = 1 - β = P(correctly reject false H₀)
- Power increases with: larger n, larger effect size, larger α

## Publication Bias
- Studies with significant results (small p-values) are more likely to be published
- Creates a distorted literature where effects appear larger than they really are
- If many researchers test the same H₀ at α = 0.05, about 5% will get significant results by chance alone

## Observational vs Experimental Studies
- **Observational**: Researcher observes without intervening → can show association, NOT causation
- **Experimental**: Researcher assigns treatments (ideally randomly) → CAN establish causation
- **Key**: Regression/correlation shows association. Only randomized experiments prove causation.

## Correlation Properties
- r is between -1 and 1
- r is **unit-free** (doesn't depend on measurement units)
- r measures **linear** association only (can be 0 with strong nonlinear relationship)
- r is **symmetric**: corr(X,Y) = corr(Y,X)
- r is sensitive to outliers
- r does NOT measure the slope (r is a standardized slope)

## Sampling Distribution Key Facts
- **Sampling distribution of p̂**: mean = π, se = √(π(1-π)/n)
- **Sampling distribution of x̄**: mean = μ, se = σ/√n
- **CLT**: For n > 30, x̄ is approximately normal regardless of population shape
- Standard error **decreases** with larger n (by factor of √n)

---

# 7. FORMULA QUICK REFERENCE

## Descriptive Statistics
- Mean: x̄ = Σxᵢ / n
- Standard deviation: s = √(Σ(xᵢ - x̄)² / (n-1))
- IQR = Q3 - Q1
- Outlier rule: below Q1 - 1.5·IQR or above Q3 + 1.5·IQR

## Test Statistics Summary

| Test | Statistic | df |
|------|-----------|-----|
| z-test (proportion) | z = (p̂ - π₀) / √(π₀(1-π₀)/n) | — (use z-table) |
| 1-sample t-test | t = (x̄ - μ₀) / (s/√n) | n - 1 |
| 2-sample t-test | t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂) | min(n₁-1, n₂-1) |
| Paired t-test | t = d̄ / (s_d/√n) | n - 1 (pairs) |
| Regression slope | t = b / se(b) | n - 2 |
| Multiple regression (individual) | t = bⱼ / se(bⱼ) | n - (k+1) |
| Chi-squared | χ² = Σ(fₒ - fₑ)²/fₑ | (r-1)(c-1) |
| F-test (overall model) | F = (R²/k) / ((1-R²)/(n-(k+1))) | k, n-(k+1) |
| F-test (nested models) | F = ((SSE₁-SSE₂)/(k₂-k₁)) / (SSE₂/(n-(k₂+1))) | k₂-k₁, n-(k₂+1) |

## Critical Values to Know (α = 0.05)
- z* = 1.645 (one-sided), 1.96 (two-sided)
- For 95% CI: z* = 1.96
- t* depends on df — look up in Table B
- χ² and F — look up in Table C / F-table

---

# 8. COMMON EXAM TRAPS

1. **Paired vs Independent**: Same subjects → paired. Different groups → independent. Getting this wrong = wrong test = zero points.

2. **One-sided vs Two-sided**: Read the question. "Is there a difference?" ≠ "Is it higher?"

3. **"Accept H₀"**: NEVER write this. Write "fail to reject H₀" or "insufficient evidence."

4. **Causation from correlation**: Regression shows association, not causation (unless it's a randomized experiment).

5. **r vs r²**: r = 0.7 does NOT mean 70% explained. r² = 0.49, so 49% explained.

6. **Chi-squared one-sided**: Chi-squared test is ALWAYS two-sided. You cannot do one-sided.

7. **R² always increases**: Adding a predictor can never decrease R². This doesn't mean the predictor is useful.

8. **Standard error of b**: se = s / (sₓ · √(n-1)), NOT s / √n.

9. **df in multiple regression**: n - (k+1), not n - 2. k = number of predictors.

10. **Interaction interpretation**: With interaction term X₁·X₂, you cannot interpret β₁ as "the effect of X₁" without specifying the value of X₂.

11. **Sample size formula**: Always round UP. Use π = 0.5 if unknown (conservative).

12. **Confidence interval interpretation**: "We are 95% confident that the TRUE parameter lies in this interval." NOT "There is a 95% probability that..."

13. **P-value interpretation**: P-value = probability of getting data this extreme OR MORE, assuming H₀ is true. It is NOT the probability that H₀ is true.

14. **Publication bias + Type I**: If 100 researchers each test at α = 0.05 and H₀ is actually true, about 5 will get significant results. If only those 5 publish → publication bias creates false findings.

15. **Standardized residuals in contingency tables**: The threshold is |z| > 3, not |z| > 2.

---

# 9. EXAM WALKTHROUGH STRATEGIES

## Q1 Strategy (Sampling, 2 pts)
1. Read the scenario carefully
2. Identify the sampling method (SRS, systematic, stratified, cluster, multistage)
3. Identify the potential bias (sampling, nonresponse, response)
4. If asked for sample size: n = π(1-π)(z*/M)², round UP

## Q2 Strategy (Test Selection, 2 pts)
1. For each scenario, ask: What is the response variable type? (categorical or quantitative)
2. How many groups/variables?
3. Same subjects or different? (paired vs independent)
4. Match to the decision tree above
5. State: test name, H₀, Hₐ, one-sided or two-sided

## Q3 Strategy (Regression, 2-2.5 pts)
1. Write the model equation first
2. Interpret coefficients IN CONTEXT with correct wording ("holding all other variables constant" for multiple regression)
3. For r² or R²: "[value]% of the variability in [Y] is explained by [X / the model]"
4. For hypothesis test on slope: use the 5-step framework
5. For F-test: state H₀ (all slopes = 0), calculate F, find p-value
6. Check residual plots if asked (random scatter = good)
7. For interaction: "the effect of X₁ on Y depends on X₂"

## Q4 Strategy (Significance Test, 1.5-2 pts)
1. Apply the 5-step framework precisely
2. Show ALL steps — partial credit for correct steps even if final answer wrong
3. State assumptions explicitly
4. Use correct table (A for z, B for t, C for χ², F-table for F)

## Q5 Strategy (Contingency Tables, 1.5-2 pts)
1. Calculate expected counts: fₑ = (row total × col total) / n
2. Verify all fₑ ≥ 5
3. Calculate χ² = Σ(fₒ - fₑ)²/fₑ
4. df = (r-1)(c-1)
5. P-value from Table C
6. If asked about specific cells: calculate standardized residuals

## Q6-Q7 Strategy (Concepts, 1-1.5 pts each)
- Be concise but precise
- Use correct terminology
- Give an example if it helps clarify
- Common topics: Simpson's paradox, Type I/II errors, publication bias, overfitting, observational vs experimental, R² interpretation
