# Odds Ratio Calculator

Odds Ratio Calculator and Fisher's Exact Test

### Definition

An odds ratio (OR) is a measure of association between an exposure and an outcome. The OR represents the odds that an outcome will occur given a particular exposure, compared to the odds of the outcome occurring in the absence of that exposure. Odds ratios are most commonly used in case-control studies, however they can also be used in cross-sectional and cohort study designs as well.

Odds ratios are used to compare the relative odds of the occurrence of the outcome of interest (e.g. disease or disorder), given exposure to the variable of interest (e.g. health characteristic, aspect of medical history). The odds ratio can also be used to determine whether a particular exposure is a risk factor for a particular outcome, and to compare the magnitude of various risk factors for that outcome.

- OR=1 Exposure does not affect odds of outcome
- OR>1 Exposure associated with higher odds of outcome
- OR<1 Exposure associated with lower odds of outcome

### Calculation
$OR = \frac{a/c}{b/d} = \frac{ad}{bc}$

* a - positive (bad)  cases in exposed group
* b - negative (good) cases in exposed group
* c - positive (bad)  cases in control group
* d - negative (good) cases in control group

Haldane-Anscombe correction for zero：add 0.5 for a/b/c/d.

### Confidence interval (CI)

The 95% confidence interval (CI) is used to estimate the precision of the OR. A large CI indicates a low level of precision of the OR, whereas a small CI indicates a higher precision of the OR. It is important to note however, that unlike the p value, the 95% CI does not report a measure’s statistical significance. In practice, the 95% CI is often used as a proxy for the presence of statistical significance if it does not overlap the null value (e.g. OR=1). Nevertheless, it would be inappropriate to interpret an OR with 95% CI that spans the null value as indicating evidence for lack of association between the exposure and outcome.

### Fisher's Exact Test

Fisher’s Exact Test is used to determine whether or not there is a significant association between two categorical variables. It is typically used as an alternative to the `Chi-Square Test` of Independence when one or more of the cell counts in a 2×2 table is less than 5. 

## Installation

1. `pip install scipy`
2. `git clone https://github.com/JiguangPeng/odds_ratio`


## Usage

Module mode

```python
from odds_ratio import OddsRatio

test = OddsRatio(18, 2, 10, 10)

# Odds Ratio
test.odds_ratio          # 9.0

# The 95% confidence interval (CI)
test.odds_ratio_lower    # 1.6381043384832557
test.odds_ratio_upper    # 49.447399715087194
test.odds_ratio_ci       # '[1.64, 49.45]'

# Fisher's Exact Test
test.pvalue       # 0.013814147851967653
test.prob         # 0.006283257673691489
```

Command mode

```shell

python odds_ratio.py -i a b c d

#OR

python odds_ratio.py -a INT -b INT -c INT -d INT

```


## Reference
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2938757/
- https://www.medcalc.org/calc/odds_ratio.php
- https://en.wikipedia.org/wiki/Fisher%27s_exact_test
