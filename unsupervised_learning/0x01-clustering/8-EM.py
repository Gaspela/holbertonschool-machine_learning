#!/usr/bin/env python3
"""
EM
"""

import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """
    X is a numpy.ndarray of shape (n, d) containing the data set
    k is a positive integer containing the number of clusters
    iterations is a positive integer containing the maximum number of
    iterations for the algorithm
    tol is a non-negative float containing tolerance of the log likelihood,
    used to determine early stopping i.e. if the difference is less than or
    equal to tol you should stop the algorithm
    verbose is a boolean that determines if you should print information about
    the algorithm
    If True, print Log Likelihood after {i} iterations: {l} every 10
    iterations and after the last iteration
    {i} is the number of iterations of the EM algorithm
    {l} is the log likelihood, rounded to 5 decimal places
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return (None, None, None, None, None)

    if type(k) is not int or type(iterations) is not int:
        return (None, None, None, None, None)

    if k <= 0 or iterations <= 0:
        return (None, None, None, None, None)

    if type(tol) is not float or tol < 0:
        return (None, None, None, None, None)

    if type(verbose) is not bool:
        return (None, None, None, None, None)

    n, d = X.shape
    pi, m, S = initialize(X, k)
    g, ll = expectation(X, pi, m, S)
    ll_old = 0
    text = 'Log Likelihood after {} iterations: {}'

    for i in range(iterations):
        if verbose and i % 10 == 0:
            print(text.format(i, ll.round(5)))
        pi, m, S = maximization(X, g)
        g, ll = expectation(X, pi, m, S)
        if np.abs(ll_old - ll) <= tol:
            break
        ll_old = ll
    if verbose:
        print(text.format(i + 1, ll.round(5)))
    return (pi, m, S, g, ll)
