#!/usr/bin/env python3
"""
Input
"""


import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    nx is the number of input features to the network.
    layers is a list containing the number of nodes in each layer of the
    network.
    activations is a list containing the activation functions used for each
    layer of the network.
    lambtha is the L2 regularization parameter.
    keep_prob is the probability that a node will be kept for dropout.

    Returns: the keras model.
    """
    inputs = K.Input(shape=(nx,))
    l2 = K.regularizers.l2(lambtha)
    x = K.layers.Dense(layers[0], activation=activations[0],
                       kernel_regularizer=l2)(inputs)

    for layer, act in zip(layers[1:], activations[1:]):
        x = K.layers.Dropout(1 - keep_prob)(x)
        x = K.layers.Dense(layer, activation=act,
                           kernel_regularizer=l2)(x)

    model = K.Model(inputs=inputs, outputs=x)

    return model
