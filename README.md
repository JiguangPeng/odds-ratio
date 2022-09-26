# odds_ratio

Odds Ratio Calculator

a — positive (bad)  cases in exposed group
b - negative (good) cases in exposed group
c - positive (bad)  cases in control group
d - negative (good) cases in control group

Haldane-Anscombe correction for zero：add 0.5 for a/b/c/d.


## Installation

1. `pip install scipy`
2. `git clone https://github.com/JiguangPeng/odds_ratio`


## Usage


```python
from odds_ratio import OddsRatio

test = OddsRatio(18, 2, 10, 10)

test.odds_ratio          # 9.0
test.odds_ratio_lower    # 1.6381043384832557
test.odds_ratio_upper    # 49.447399715087194
test.odds_ratio_ci       # '[1.64, 49.45]'


test.pvalue_fisher       # 0.013814147851967653
test.prob_fisher         # 0.006283257673691489
```
