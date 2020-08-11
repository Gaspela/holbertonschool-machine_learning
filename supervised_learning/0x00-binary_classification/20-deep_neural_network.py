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

        # private
        self.__nx = nx
        self.__layers = layers
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for i in range(self.L):
            if type(layers[i]) is not int or layers[i] <= 0:
                raise TypeError("layers must be a list of positive integers")

            w_i = "W" + str(i + 1)
            b_i = "b" + str(i + 1)

            self.__weights[b_i] = np.zeros((layers[i], 1))

            if i == 0:
                w = np.random.randn(layers[i], nx) * np.sqrt(2 / nx)
            else:
                w = np.random.randn(layers[i], layers[i - 1])
                w = w * np.sqrt(2 / layers[i - 1])
            self.__weights[w_i] = w

    @property
    def L(self):
        """ The number of layers in the neural network. """
        return self.__L

    @property
    def cache(self):
        """ A dictionary to hold all intermediary values of the network. """
        return self.__cache

    @property
    def weights(self):
        """ A dictionary to hold all weights and biased of the network """
        return self.__weights

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neural network.
        X: is a numpy.ndarray with shape (nx, m) that contains the input data.
        nx: is the number of input features to the neuron.
        m: is the number of examples.
        """
        self.__cache['A0'] = X
        for layer in range(self.__L):
            w_i = "W" + str(layer + 1)
            b_i = "b" + str(layer + 1)
            a_i = "A" + str(layer + 1)
            prev_a = "A" + str(layer)
            z = (np.dot(self.__weights[w_i], self.__cache[prev_a]) +
                 self.__weights[b_i])
            self.__cache[a_i] = 1 / (1 + np.exp(-z))
        return self.__cache["A" + str(self.__L)], self.__cache

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression.
        Y is a numpy.ndarray with shape (1, m) that contains the correct
        labels for the input data.
        A is a numpy.ndarray with shape (1, m) containing the activated
        output of the neuron for each example.
        """
        y1 = 1 - Y
        y2 = 1.0000001 - A
        m = Y.shape[1]
        cost = -1 * (1 / m) * np.sum(Y * np.log(A) + y1 * np.log(y2))

        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neural network’s predictions.
        X: is a numpy.ndarray with shape (nx, m) that contains the input data.
        nx: is the number of input features to the neuron.
        m: is the number of examples.
        Y: is a numpy.ndarray with shape (1, m) that contains the correct
        labels for the input data.
        """
        A, cache = self.forward_prop(X)
        cost = self.cost(Y, A)
        return (np.round(A).astype(int), cost)
