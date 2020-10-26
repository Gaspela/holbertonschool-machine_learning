#!/usr/bin/env python3
"""
Function that calculates a correlation matrix
"""

import numpy as np


def correlation(C):
    """
    d is the number of dimensions
    If C is not a numpy.ndarray, raise a TypeError with the message C must be
    a numpy.ndarray
    If C does not have shape (d, d), raise a ValueError with the message C
    must be a 2D square matrix
    """
    if type(C) is not np.ndarray:
        raise TypeError('C must be a numpy.ndarray')

    if len(C.shape) is not 2 or C.shape[0] is not C.shape[1]:
        raise ValueError('C must be a 2D square matrix')

    D = np.sqrt(np.diag(C))
    corr = np.outer(D, D)
    return C / corr
