#!/usr/bin/env python3
"""
neural network performing binary classification
"""


import numpy as np
""" performing binary classification """


class DeepNeuralNetwork:
    """
    class DeepNeuralNetwork that defines a deep neural network.
    """

    def __init__(self, nx, layers):
        """
        nx: is the number of input features
        layers: is a list representing the number of nodes in each layer of
        the network.
        Sets the public instance attributes:
        L: The number of layers in the neural network.
        cache: A dictionary to hold all intermediary values of the network.
        weights: A dictionary to hold all weights and biased of the network.
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list:
            raise TypeError("layers must be a list of positive integers")
        if len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        # public
        self.nx = nx
        self.layers = layers
        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for i in range(self.L):
            if type(layers[i]) is not int or layers[i] <= 0:
                raise TypeError("layers must be a list of positive integers")

            w_i = "W" + str(i + 1)
            b_i = "b" + str(i + 1)

            self.weights[b_i] = np.zeros((layers[i], 1))

            if i == 0:
                w = np.random.randn(layers[i], nx) * np.sqrt(2 / nx)
            else:
                w = np.random.randn(layers[i], layers[i - 1])
                w = w * np.sqrt(2 / layers[i - 1])
            self.weights[w_i] = w
