#!/usr/bin/env python3
"""Inception Network"""


import tensorflow.keras as K
inception_block = __import__('0-inception_block').inception_block


def inception_network():
    """
    You can assume the input data will have shape (224, 224, 3)
    All convolutions inside and outside the inception block should
    use a rectified linear activation (ReLU)
    """
    inputs = K.Input(shape=(224, 224, 3))
    out_l = K.layers.Conv2D(64, 7, 2, activation='relu', padding='same',
                            input_shape=inputs.shape)(inputs)
    out_l = K.layers.MaxPool2D(3, 2, padding='same')(out_l)
    out_l = K.layers.Conv2D(64, 1, 1, activation='relu', padding='same')(out_l)
    out_l = K.layers.Conv2D(
        192, 3, 1, activation='relu', padding='same')(out_l)
    out_l = K.layers.MaxPool2D(3, 2, padding='same')(out_l)
    out_l = inception_block(out_l, [64, 96, 128, 16, 32, 32])
    out_l = inception_block(out_l, [128, 128, 192, 32, 96, 64])
    out_l = K.layers.MaxPool2D(3, 2, padding='same')(out_l)
    out_l = inception_block(out_l, [192, 96, 208, 16, 48, 64])
    out_l = inception_block(out_l, [160, 112, 224, 24, 64, 64])
    out_l = inception_block(out_l, [128, 128, 256, 24, 64, 64])
    out_l = inception_block(out_l, [112, 144, 288, 32, 64, 64])
    out_l = inception_block(out_l, [256, 160, 320, 32, 128, 128])
    out_l = K.layers.MaxPool2D(3, 2, padding='same')(out_l)
    out_l = inception_block(out_l, [256, 160, 320, 32, 128, 128])
    out_l = inception_block(out_l, [384, 192, 384, 48, 128, 128])
    out_l = K.layers.AvgPool2D(7, 1)(out_l)
    out_l = K.layers.Dropout(.4)(out_l)
    out_l = K.layers.Dense(1000)(out_l)
    return K.Model(inputs, out_l)
