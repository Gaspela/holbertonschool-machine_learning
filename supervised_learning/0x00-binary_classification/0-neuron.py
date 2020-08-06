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
        W: The weights vector for the neuron. Upon instantiation,
        it should be initialized using a random normal distribution.
        b: The bias for the neuron. Upon instantiation,
        it should be initialized to 0.
        A: The activated output of the neuron (prediction). Upon instantiation,
        it should be initialized to 0.
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.W = np.ndarray((1, nx))
        self.W[0] = np.random.normal(size=nx)
        self.b = 0
        self.A = 0
