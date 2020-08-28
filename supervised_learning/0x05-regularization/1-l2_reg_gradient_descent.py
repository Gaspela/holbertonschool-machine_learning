#!/usr/bin/env python3
""" Gradient Descent with L2 Regularization """


import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
    Y is a one-hot numpy.ndarray of shape (classes, m) that contains the
    correct labels for the data.
    classes is the number of classes.
    m is the number of data points.
    weights is a dictionary of the weights and biases of the neural network.
    cache is a dictionary of the outputs of each layer of the neural network.
    alpha is the learning rate.
    lambtha is the L2 regularization parameter.
    L is the number of layers of the network    .
    """
    dz = cache['A' + str(L)] - Y
    m = Y.shape[1]
    for layer in range(L, 0, -1):
        dW1 = (lambtha / m) * weights['W' + str(layer)]
        db1 = (np.sum(dz, axis=1, keepdims=True) / m)
        dw = (np.matmul(dz, cache['A' + str(layer - 1)].T) / m) + dW1
        dz = np.matmul(weights['W' + str(
            layer)].T, dz) * (1 - (cache['A' + str(
                layer - 1)] ** 2))
        weights['b' + str(layer)] = weights['b' + str(
            layer)] - (alpha * db1)
        weights['W' + str(layer)] = weights['W' + str(
            layer)] - (alpha * dw)
