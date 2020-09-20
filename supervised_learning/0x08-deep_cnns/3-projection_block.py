#!/usr/bin/env python3
"""Projection Block"""


import tensorflow.keras as K


def projection_block(A_prev, filters, s=2):
    """
    A_prev is the output from the previous layer
    filters is a tuple or list containing F11, F3, F12, respectively:
    F11 is the number of filters in the first 1x1 convolution
    F3 is the number of filters in the 3x3 convolution
    F12 is the number of filters in the second 1x1 convolution as well as the
    1x1 convolution in the shortcut connection
    s is the stride of the first convolution in both the main path and the
    shortcut connection
    """
    out_l = K.layers.Conv2D(filters[0], 1, s,
                            kernel_initializer='he_normal')(A_prev)
    out_l = K.layers.BatchNormalization()(out_l)
    out_l = K.layers.Activation('relu')(out_l)
    out_l = K.layers.Conv2D(filters[1], 3, padding='same',
                            kernel_initializer='he_normal')(out_l)
    out_l = K.layers.BatchNormalization()(out_l)
    out_l = K.layers.Activation('relu')(out_l)
    out_l = K.layers.Conv2D(filters[2], 1,
                            kernel_initializer='he_normal')(out_l)
    out_l = K.layers.BatchNormalization()(out_l)
    out2 = K.layers.Conv2D(filters[2], 1, s,
                           kernel_initializer='he_normal')(A_prev)
    out2 = K.layers.BatchNormalization()(out2)
    out_l = K.layers.add([out_l, out2])
    return K.layers.Activation('relu')(out_l)
