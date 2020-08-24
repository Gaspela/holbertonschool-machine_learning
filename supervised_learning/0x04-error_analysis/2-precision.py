#!/usr/bin/env python3
"""
Precision 
"""

import numpy as np


def precision(confusion):
    """
    confusion is a confusion numpy.ndarray of shape (classes, classes) where
    row indices represent the correct labels and column indices represent
    the predicted labels.
    classes is the number of classes.
    Returns: a numpy.ndarray of shape (classes,) containing the precision
    of each class.
    """
    true_p = np.diag(confusion)
    false_p = np.sum(confusion, axis=0) - true_p
    prec = true_p / (true_p + false_p)
    return prec
