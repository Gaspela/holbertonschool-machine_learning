#!/usr/bin/env python3
""" Layer with L2 Regularization """


import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """
    prev is a tensor containing the output of the previous layer
    n is the number of nodes the new layer should contain
    activation is the activation function that should be used on the layer
    lambtha is the L2 regularization parameter
    Returns: the output of the new layer
    """
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    reg = tf.contrib.layers.l2_regularizer(lambtha)
    model = tf.layers.Dense(name='layer', units=n, activation=activation,
                            kernel_initializer=init, kernel_regularizer=reg)
    return model(prev)
