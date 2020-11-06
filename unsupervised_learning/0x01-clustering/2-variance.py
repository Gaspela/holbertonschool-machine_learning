#!/usr/bin/env python3
"""
Variance
"""


import numpy as np


def variance(X, C):
    """
    X is a numpy.ndarray of shape (n, d) containing the data set
    C is a numpy.ndarray of shape (k, d) containing the centroid means for
    each cluster
    You are not allowed to use any loops
    Returns: var, or None on failure
    var is the total variance
    """
    if type(X) is not np.ndarray or len(X.shape) != 2:
        return None
    if type(C) is not np.ndarray or len(C.shape) != 2:
        return None
    try:
        return (np.square(np.apply_along_axis(np.subtract, 1, X, C))
                .sum(axis=2).min(axis=1).sum())
    except Exception:
        return None
