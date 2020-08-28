#!/usr/bin/env python3
""" Forward Propagation with Dropout """


import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """
    X is a numpy.ndarray of shape (nx, m) containing the input data for the
    network.
    nx is the number of input features.
    m is the number of data points.
    weights is a dictionary of the weights and biases of the neural network.
    L the number of layers in the network.
    keep_prob is the probability that a node will be kept.
    All layers except the last should use the tanh activation function.
    The last layer should use the softmax activation function.
    Returns: a dictionary containing the outputs of each layer and the dropout
    mask used on each layer (see example for format).
    """
    cache = {}
    for i in range(L):
        m = 'D' + str(i)
        if i > 0:
            cache[m] = (np.random.rand(X.shape[0],
                                       X.shape[1])
                        < keep_prob).astype(int)
            X = np.multiply(X, cache[m])
            X = X / keep_prob
        cache["A" + str(i)] = X
        Z = np.dot(weights["W" + str(i + 1)], X) + weights["b" + str(i + 1)]
        if i == L - 1:
            t = np.exp(Z)
            X = t / np.sum(t, axis=0, keepdims=True)
            cache["A" + str(i + 1)] = X
        else:
            X = np.sinh(Z) / np.cosh(Z)
    return (cache)
