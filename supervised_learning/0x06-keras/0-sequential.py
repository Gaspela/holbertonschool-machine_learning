#!/usr/bin/env python3
"""
Sequential 
"""


import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    nx is the number of input features to the network.
    layers is a list containing the number of nodes in each layer of the network.
    activations is a list containing the activation functions used for each layer of the network.
    lambtha is the L2 regularization parameter.
    keep_prob is the probability that a node will be kept for dropout.
    Returns: the keras model.
    """
    model = K.Sequential()
    reg = K.regularizers.l2
    model.add(K.layers.Dense(layers[0], input_shape=(nx,),
                             activation=activations[0],
                             kernel_regularizer=reg(lambtha)))
                             
    for layer, act in zip(layers[1:], activations[1:]):
        model.add(K.layers.Dropout(1 - keep_prob))
        model.add(K.layers.Dense(layer, activation=act,
                                 kernel_regularizer=reg(lambtha)))

    return model
