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
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None

    if type(iterations) != int or iterations <= 0:
        return None, None

    if kmax is None:
        kmax = X.shape[0]

    if type(kmin) != int or kmin <= 0 or kmin >= X.shape[0]:
        return None, None

    if type(kmax) != int or kmax <= 0 or kmax > X.shape[0]:
        return None, None

    if kmin >= kmax:
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
