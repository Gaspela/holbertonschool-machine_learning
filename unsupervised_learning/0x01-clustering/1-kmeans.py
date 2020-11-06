#!/usr/bin/env python3
"""
K-means
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


def kmeans(X, k, iterations=1000):
    """
    C is a numpy.ndarray of shape (k, d) containing the centroid means for
    each cluster
    clss is a numpy.ndarray of shape (n,) containing the index of the cluster
    in C that each data point belongs to
    """
    if type(iterations) is not int or iterations <= 0:
        return None, None

    C = initialize(X, k)

    clss = None
    while iterations:
        iterations -= 1

        centr_copy = C.copy()
        clss = np.apply_along_axis(np.subtract, 1, X, C)
        clss = np.argmin(np.square(clss).sum(axis=2), axis=1)

        for j in range(C.shape[0]):
            index = np.argwhere(clss == j)
            if index.shape[0] == 0:
                C[j] = initialize(X, 1)
            else:
                C[j] = np.mean(X[index], axis=0)
        if np.all(centr_copy == C):
            return C, clss

    clss = np.apply_along_axis(np.subtract, 1, X, C)
    clss = np.argmin(np.square(clss).sum(axis=2), axis=1)

    return C, clss
