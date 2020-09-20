#!/usr/bin/env python3
"""ResNet-50"""


import tensorflow.keras as K
identity_block = __import__('2-identity_block').identity_block
projection_block = __import__('3-projection_block').projection_block


def resnet50():
    """
    shape (224, 224, 3)
    Returns: the keras model
    """
    inputs = K.layers.Input((224, 224, 3))
    out_l = K.layers.Conv2D(64, 7, 2, padding='same',
                            kernel_initializer='he_normal')(inputs)
    out_l = K.layers.BatchNormalization()(out_l)
    out_l = K.layers.Activation('relu')(out_l)
    out_l = K.layers.MaxPool2D(3, 2, padding='same')(out_l)
    filters = [64, 64, 256]
    out_l = projection_block(out_l, filters, 1)
    out_l = identity_block(out_l, filters)
    out_l = identity_block(out_l, filters)
    filters = [128, 128, 512]
    out_l = projection_block(out_l, filters, 2)
    out_l = identity_block(out_l, filters)
    out_l = identity_block(out_l, filters)
    out_l = identity_block(out_l, filters)
    filters = [256, 256, 1024]
    out_l = projection_block(out_l, filters, 2)
    out_l = identity_block(out_l, filters)
    out_l = identity_block(out_l, filters)
    out_l = identity_block(out_l, filters)
    out_l = identity_block(out_l, filters)
    out_l = identity_block(out_l, filters)
    filters = [512, 512, 2048]
    out_l = projection_block(out_l, filters, 2)
    out_l = identity_block(out_l, filters)
    out_l = identity_block(out_l, filters)
    out_l = K.layers.AvgPool2D(7)(out_l)
    out_l = K.layers.Dense(1000, kernel_initializer='he_normal',
                           activation='softmax')(out_l)
    return K.Model(inputs, out_l)
