#!/usr/bin/env python3
"""
Specificity
"""


import numpy as np


def specificity(confusion):
    """
    confusion: is a confusion numpy.ndarray of shape (classes, classes) where
    row indices represent the correct labels and column indices represent
    the predicted labels.
    classes is the number of classes
    Returns: a numpy.ndarray of shape (classes,) containing the specificity
    of each class.
    """
    true_p = np.diag(confusion)
    false_n = np.sum(confusion, axis=1) - true_p
    false_p = np.sum(confusion, axis=0) - true_p
    true_n = np.sum(confusion) - (true_p + false_n + false_p)
    spec = true_n / (true_n + false_p)
    return spec
