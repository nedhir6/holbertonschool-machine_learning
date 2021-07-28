#!/usr/bin/env python3
"""Binomial distribution"""


class Binomial:
    """binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """n number of trials, p probability of a success"""
        self.data = data
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not(p < 1 or p > 0):
                raise ValueError("p must be greater than 0 and less than 1")
            else:
                self.n = int(n)
                self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) <= 2:
                raise ValueError("data must contain multiple values")
            mean = float(sum(data) / len(data))
            ns = 0
            for i in data:
                ns = ns + ((i - mean) ** 2)
            self.n = round(mean ** 2 / (mean - (ns/len(data))))
            self.p = float(mean / self.n)