#!/usr/bin/env python3
""" NeuralNetwork,binary classification """


import numpy as np
"""
neural network with one hidden
layer performing binary classification
"""


class NeuralNetwork:
    """
    NeuralNetwork that defines a neural network with one hidden
    layer performing binary classification.
    """

    def __init__(self, nx, nodes):
        """
        nx: is the number of input features.
        nodes is the number of nodes found in the hidden laye.
        W1: The weights vector for the hidden layer. Upon instantiation,
        it should be initialized using a random normal distribution.
        b1: The bias for the hidden layer. Upon instantiation,
        it should be initialized with 0’s.
        A1: The activated output for the hidden layer. Upon instantiation,
        it should be initialized to 0.
        W2: The weights vector for the output neuron. Upon instantiation,
        it should be initialized using a random normal distribution.
        b2: The bias for the output neuron. Upon instantiation,
        it should be initialized to 0.
        A2: The activated output for the output neuron (prediction).
        Upon instantiation, it should be initialized to 0.
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        # private
        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """ The weights vector for the hidden layer """
        return self.__W1

    @property
    def W2(self):
        """ The bias for the hidden layer """
        return self.__W2

    @property
    def b1(self):
        """ The activated output for the hidden layer """
        return self.__b1

    @property
    def b2(self):
        """ The weights vector for the output neuron """
        return self.__b2

    @property
    def A1(self):
        """ The bias for the output neuron """
        return self.__A1

    @property
    def A2(self):
        """ The activated output for the output neuron (prediction) """
        return self.__A2
