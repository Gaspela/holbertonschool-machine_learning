#!/usr/bin/env python3
"""
Initialize K-means
"""
import numpy as np


def initialize(X, k):
    """
    X is a numpy.ndarray of shape (n, d) containing the dataset that will be
    used for K-means clustering
    n is the number of data points
    d is the number of dimensions for each data point
    k is a positive integer containing the number of clusters
    """
    if type(X) is not np.ndarray or len(X.shape) != 2\
            or type(k) is not int or k <= 0:
        return None
    try:
        return np.random.uniform(np.amin(X, axis=0),
                                 np.amax(X, axis=0),
                                 (k, X.shape[1]))
    except Exception:
        return None
