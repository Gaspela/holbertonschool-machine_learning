#!/usr/bin/env python3
""" rmalization (standardization) constants of a matrix """


import numpy as np


def normalization_constants(X):
    """
    X: is the numpy.ndarray of shape (m, nx) to normalize.
    m: is the number of data points.
    nx: is the number of features.
    Returns: the mean and standard deviation of each feature, respectively.
    """
    mean = np.mean(X, axis=0)
    standard_deviation = np.std(X, axis=0)
    return mean, standard_deviation
    
