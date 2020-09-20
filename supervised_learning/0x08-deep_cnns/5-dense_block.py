#!/usr/bin/env python3
"""Dense Block"""


import tensorflow.keras as K


def dense_block(X, nb_filters, growth_rate, layers):
    """
    X is the output from the previous layer
    nb_filters is an integer representing the number of filters in X
    growth_rate is the growth rate for the dense block
    layers is the number of layers in the dense block
    """
    concat = X
    for layer in range(layers):
        tf_layer = K.layers.BatchNormalization()(concat)
        tf_layer = K.layers.Activation('relu')(tf_layer)
        tf_layer = K.layers.Conv2D(growth_rate * 4, 1,
                                   kernel_initializer='he_normal')(tf_layer)
        tf_layer = K.layers.BatchNormalization()(tf_layer)
        tf_layer = K.layers.Activation('relu')(tf_layer)
        tf_layer = K.layers.Conv2D(growth_rate, 3, padding='same',
                                   kernel_initializer='he_normal')(tf_layer)
        concat = K.layers.concatenate([concat, tf_layer])
        nb_filters += growth_rate
    return concat, nb_filters
