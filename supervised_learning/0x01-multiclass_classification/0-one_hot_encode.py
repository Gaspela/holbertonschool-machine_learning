#!/usr/bin/env python3
"""
Converts a numeric label vector into a one-hot matrix
"""


import numpy as np
""" vector into a one-hot matrix """


def one_hot_encode(Y, classes):
    """
    Y: is a numpy.ndarray with shape (m,) containing numeric class labels.
    m: is the number of examples.
    classes: is the maximum number of classes found in Y.
    """
    if type(Y) is not np.ndarray:
        return None
    if len(Y) == 0:
        return None
    if type(classes) is not int or classes <= Y.max():
        return None

    one_hot = np.zeros((classes, Y.shape[0]))
    for e, labels in enumerate(Y):
        one_hot[labels][e] = 1

    return one_hot
