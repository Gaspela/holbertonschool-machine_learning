#!/usr/bin/env python3
""" represents a binomial distribution """


class Binomial:
    """ binomial distribution """

    def __init__(self, data=None, n=1, p=0.5):
        """ calculate binomial distribution """
        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
            else:
                self.n = n
                self.p = p
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            else:
                mean = sum(data) / len(data)
                variance = sum([(x - mean) ** 2 for x in data]) / len(data)
                self.p = -1 * (variance / mean - 1)
                n = mean/self.p
                self.n = round(n)
                self.p *= n/self.n

    def pmf(self, k):
        """ Calculates the value of the PMF for a given number"""
        k = int(k)
        if k > self.n or k < 0:
            return 0
        return (factorial(self.n) / factorial(k) / factorial(self.n - k)
                * self.p ** k * (1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """ Calculates the value of the CDF for a given number"""
        if k > self.n or k < 0:
            return 0
        sumcdf = 0
        for x in range(0, int(k) + 1):
            sumcdf += self.pmf(x)
        return sumcdf


def factorial(n):
    """ Calculate factorial of n """
    fact = 1
    for x in range(1, n + 1):
        fact = x * fact
    return fact
