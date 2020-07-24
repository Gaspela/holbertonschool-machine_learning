#!/usr/bin/env python3
""" that calculates \sum_{i=1}^{n} i^2 """


def summation_i_squared(n):
    """ Sum """
    if type(n) is not int or n < 1:
        return None
    return int(n*(n+1)*((2*n)+1)/6)
