#!/usr/bin/env python3
"""
that calculates the mean and covariance of a data set
"""
import numpy as np


def mean_cov(X):
    """
    n is the number of data points
    d is the number of dimensions in each data point
    If X is not a 2D numpy.ndarray, raise a TypeError with the message X must
    be a 2D numpy.ndarray
    If n is less than 2, raise a ValueError with the message X must contain
    multiple data points
    """
    if type(X) is not np.ndarray or len(X.shape) is not 2:
        raise TypeError('X must be a 2D numpy.ndarray')

    if X.shape[0] < 2:
        raise ValueError("X must contain multiple data points")

    mean = np.zeros((1, X.shape[1]))
    mean[0] = np.mean(X, axis=0)
    cov = np.dot(X.T, X - mean) / (X.shape[0] - 1)
    return (mean, cov)
