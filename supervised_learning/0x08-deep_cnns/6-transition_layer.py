#!/usr/bin/env python3
"""Transition Layer"""


import tensorflow.keras as K


def transition_layer(X, nb_filters, compression):
    """
    X is the output from the previous layer
    nb_filters is an integer representing the number of filters in X
    compression is the compression factor for the transition layer
    """
    out_l = K.layers.BatchNormalization()(X)
    out_l = K.layers.Activation('relu')(out_l)
    out_l = K.layers.Conv2D(int(nb_filters * compression), 1,
                            kernel_initializer='he_normal')(out_l)
    return K.layers.AvgPool2D(2)(out_l), int(nb_filters * compression)
