#!/usr/bin/env python3

from math import log, exp, sqrt, factorial
from scipy.stats import fisher_exact


class OddsRatio():
    """
    Odds Ratio Calulator
    a — positive (bad)  cases in exposed group
    b - negative (good) cases in exposed group
    c - positive (bad)  cases in control group
    d - negative (good) cases in control group

    Haldane-Anscombe correction for zero：add 0.5 for abcd
    """

    def __init__(self, a, b, c, d):
        if int(a) * int(b) * int(c) * int(d) == 0:
            self.a = int(a) + 0.5
            self.b = int(b) + 0.5
            self.c = int(c) + 0.5
            self.d = int(d) + 0.5
        else:
            self.a = int(a)
            self.b = int(b)
            self.c = int(c)
            self.d = int(d)
        self.odds_ratio = (self.a/self.b) / (self.c/self.d)
        self.standerr = sqrt(1/self.a + 1/self.b + 1/self.c + 1/self.d)
        self.odds_ratio_upper = exp(log(self.odds_ratio) + 1.96 * self.standerr)
        self.odds_ratio_lower = exp(log(self.odds_ratio) - 1.96 * self.standerr)

    
    @property
    def odds_ratio_ci(self):
        if self.odds_ratio >= 1:
            upper = '{:.2f}'.format(self.odds_ratio_upper)
            lower = '{:.2f}'.format(self.odds_ratio_lower)
        else:
            upper = '{:.3g}'.format(self.odds_ratio_upper)
            lower = '{:.3g}'.format(self.odds_ratio_lower)
            
        return f'[{lower}, {upper}]'


    @property
    def odds_ratio_text(self):
        if self.odds_ratio >= 1:
            return '{:.2f}'.format(self.odds_ratio)
        else:
            return '{:.3g}'.format(self.odds_ratio)

        
    @property
    def or_ci_qc(self):
        if float(self.odds_ratio_lower) <= 1 <= float(self.odds_ratio_upper):
            return 'FAIL'
        else:
            return 'PASS'

    @property
    def pvalue(self):
        pvalue = fisher_exact([[self.a,self.b], [self.c,self.d]])[1]
        return pvalue


    @property
    def pvalue_text(self):
        return '{:.3g}'.format(self.pvalue_fisher)


    @property
    def prob(self):
        a, b, c, d = map(int, (self.a, self.b, self.c, self.d))
        m = factorial(a+b) * factorial(c+d) * factorial(a+c)  * factorial(b+d)
        n = factorial(a) * factorial(b) * factorial(c) * factorial(d) * factorial(a+b+c+d)
        return m/n

