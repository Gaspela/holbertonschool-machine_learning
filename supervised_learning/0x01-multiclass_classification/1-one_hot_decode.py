#!/usr/bin/env python3
"""
that converts a one-hot matrix into a vector of labels
"""


import numpy as np
""" matrix into a vector of labels """


def one_hot_decode(one_hot):
    """
    one_hot: is a one-hot encoded numpy.ndarray with shape (classes, m)
    classes: is the maximum number of classes
    m: is the number of examples
    """
    if type(one_hot) is not np.ndarray:
        return None
    if len(one_hot.shape) != 2:
        return None
    if not np.all((one_hot == 0) | (one_hot == 1)):
        return None

    return np.argmax(one_hot, axis=0)
