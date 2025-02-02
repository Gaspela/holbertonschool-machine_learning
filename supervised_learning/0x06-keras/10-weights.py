#!/usr/bin/env python3
"""
Save and Load Weights
"""


import tensorflow.keras as K


def save_weights(network, filename, format='h5'):
    """
    network is the model whose weights should be saved.
    filename is the path of the file that the weights should be saved to.
    save_format is the format in which the weights should be saved.
    Returns: None.
    """
    network.save_weights(filename, format)

    return None


def load_weights(network, filename):
    """
    network is the model to which the weights should be loaded.
    filename is the path of the file that the weights should be loaded from.
    Returns: None.
    """
    return network.load_weights(filename)

    return None
