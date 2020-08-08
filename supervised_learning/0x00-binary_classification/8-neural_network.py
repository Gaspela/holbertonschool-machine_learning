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
        
        """
