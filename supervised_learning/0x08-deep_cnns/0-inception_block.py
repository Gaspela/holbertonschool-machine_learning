#!/usr/bin/env python3
"""Inception Block"""


import tensorflow.keras as K


def inception_block(A_prev, filters):
    """
    A_prev is the output from the previous layer
    filters is a tuple or list containing F1, F3R, F3,F5R, F5, FPP,
    respectively:
    F1 is the number of filters in the 1x1 convolution
    F3R is the number of filters in the 1x1 convolution before the 3x3
    convolution
    F3 is the number of filters in the 3x3 convolution
    F5R is the number of filters in the 1x1 convolution before the 5x5
    convolution
    F5 is the number of filters in the 5x5 convolution
    FPP is the number of filters in the 1x1 convolution after the max pooling
    """
    conv_1 = K.layers.Conv2D(filters[0], 1, activation='relu')(A_prev)
    conv_2 = K.layers.Conv2D(filters[1], 1, activation='relu')(A_prev)
    conv_2 = K.layers.Conv2D(filters[2], 3, padding='same',
                             activation='relu')(conv_2)
    conv_3 = K.layers.Conv2D(filters[3], 1, activation='relu')(A_prev)
    conv_3 = K.layers.Conv2D(filters[4], 5, padding='same',
                             activation='relu')(conv_3)
    pooling = K.layers.MaxPool2D(3, 1, padding='same')(A_prev)
    pooling = K.layers.Conv2D(filters[5], 1,
                              activation='relu')(pooling)
    return K.layers.concatenate([conv_1, conv_2, conv_3, pooling])
