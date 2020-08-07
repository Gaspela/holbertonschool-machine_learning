#!/usr/bin/env python3
"""
Class Neuron that defines a single neuron performing binary
classification
"""


import numpy as np
""" Single neuron performing binary classification """


class Neuron:
    """Neuron performing binary classification"""

    def __init__(self, nx):
        """
        nx: number of input features
        _W: The weights vector for the neuron. Upon instantiation,
        it should be initialized using a random normal distribution.
        _b: The bias for the neuron. Upon instantiation,
        it should be initialized to 0.
        _A: The activated output of the neuron (prediction).
        Upon instantiation, it should be initialized to 0.
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        # Private instance attributes
        self.__W = np.ndarray((1, nx))
        self.__W[0] = np.random.normal(size=nx)
        self.__b = 0
        self.__A = 0

    # getter function
    @property
    def W(self):
        """Return weights vector for the neuron """
        return self.__W

    @property
    def b(self):
        """Return bias for the neuron """
        return self.__b

    @property
    def A(self):
        """Return activated output of the neuron """
        return self.__A

    def forward_prop(self, X):
        """
        Calculate the forward propagation of the neuron
        nx: is the number of input features to the neuron
        m: is the number of examples,
        """
        z = np.dot(self.__W, X) + self.__b
        sigmoid = 1 / (1 + np.exp(-z))
        self.__A = sigmoid

        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        Y: is a numpy.ndarray with shape (1, m),
        that contains the correct labels for the input data.
        A: is a numpy.ndarray with shape (1, m)
        containing the activated output of the neuron for each example
        """
        y1 = 1 - Y
        y2 = 1.0000001 - A
        m = Y.shape[1]
        cost = -1 * (1 / m) * np.sum(Y * np.log(A) + y1 * np.log(y2))

        return cost
