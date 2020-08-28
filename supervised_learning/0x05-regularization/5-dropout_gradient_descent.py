#!/usr/bin/env python3
"""
Gradient Descent with Dropout
"""

import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """
    Y is a one-hot numpy.ndarray of shape (classes, m) that contains the
    correct labels for the data.
    classes is the number of classes.
    m is the number of data points.
    weights is a dictionary of the weights and biases of the neural network.
    cache is a dictionary of the outputs and dropout masks of each layer of
    the neural network.
    alpha is the learning rate.
    keep_prob is the probability that a node will be kept.
    L is the number of layers of the network.
    """
    m = Y.shape[1]
    dAl = cache['A' + str(L)] - Y
    for i in reversed(range(1, L + 1)):

        W_key = 'W' + str(i)
        b_key = 'b' + str(i)
        A_key = 'A' + str(i - 1)
        D_key = 'D' + str(i - 1)

        dw = (np.matmul(cache[A_key], dAl.T) / m)
        db = (np.sum(dAl, axis=1, keepdims=True) / m)
        if i - 1 > 0:
            dAl = np.matmul(weights['W' + str(
                i)].T, dAl) * (1 - (cache[A_key] ** 2)) * (cache[D_key]
                                                           / keep_prob)
        weights[W_key] = weights['W' + str(
            i)] - (alpha * dw).T
        weights[b_key] = weights['b' + str(
            i)] - (alpha * db)
