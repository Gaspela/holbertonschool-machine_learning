#!/usr/bin/env python3
"""
Sensitivity
"""

import numpy as np


def sensitivity(confusion):
    """
    confusion: is a confusion numpy.ndarray of shape (classes, classes)
    where row indices represent the correct labels and column indices
    represent the predicted labels.
    classes: is the number of classes
    Returns: a numpy.ndarray of shape (classes,) containing the
    sensitivity of each class.
    """
    true_p = np.diag(confusion)
    false_n =np.sum(confusion, axis=1) - true_p
    sens = true_p / (true_p + false_n)
    return sens
