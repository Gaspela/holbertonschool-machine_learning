#!/usr/bin/env python3
"""
Optimize k
"""


import numpy as np
kmeans = __import__('1-kmeans').kmeans
variance = __import__('2-variance').variance


def optimum_k(X, kmin=1, kmax=None, iterations=1000):
    """
    X is a numpy.ndarray of shape (n, d) containing the data set
    kmin is a positive integer containing the minimum number of clusters to
    check for (inclusive)
    kmax is a positive integer containing the maximum number of clusters to
    check for (inclusive)
    iterations is a positive integer containing the maximum number of
    iterations for K-means
    This function should analyze at least 2 different cluster sizes
    """
    if type(X) is not np.ndarray:
        return None, None

    if kmax is None:
        kmax = X.shape[0]

    if ((X.ndim != 2 or type(kmin) is not int
         or kmin < 1 or type(iterations) is not int or iterations < 1
         or type(kmax) is not int or kmax <= kmin)):
        return None, None

    results = []
    d_vars = []
    for k in range(kmin, kmax + 1):
        C, clss = kmeans(X, k, iterations)
        results.append((C, clss))
        var = variance(X, C)
        if k == kmin:
            min_var = var
        d_vars.append(min_var - var)

    return results, d_vars
