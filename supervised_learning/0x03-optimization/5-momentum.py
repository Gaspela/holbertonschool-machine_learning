#!/usr/bin/env python3
""" Momentum """

import numpy as np


def update_variables_momentum(alpha, beta1, var, grad, v):
    """
    alpha is the learning rate.
    beta1 is the momentum weight.
    var is a numpy.ndarray containing the variable to be updated.
    grad is a numpy.ndarray containing the gradient of var.
    v is the previous first moment of var.
    """
    beta_v = np.multiply(beta1, v) + np.multiply((1 - beta1), grad)
    var = var - np.multiply(alpha, beta_v)
    return (var, beta_v)
