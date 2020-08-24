#!/usr/bin/env python3
"""
Batch Normalization Upgraded
"""

import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """
    prev is the activated output of the previous layer.
    n is the number of nodes in the layer to be created.
    activation is the activation function that should be used on the output of
    the layer.
    you should use the tf.layers.Dense layer as the base layer with kernal
    initializer tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG").
    your layer should incorporate two trainable parameters, gamma and beta,
    initialized as vectors of 1 and 0 respectively.
    you should use an epsilon of 1e-8.
    Returns: a tensor of the activated output for the layer.
    """
    kernal = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    model = tf.layers.Dense(units=n, name="layer", kernel_initializer=kernal)
    X = model(prev)
    beta = tf.Variable(tf.constant(0.0, shape=[n]), trainable=True)
    gamma = tf.Variable(tf.constant(1.0, shape=[n]), trainable=True)
    mean, variance = tf.nn.moments(X, [0])
    norm_z = tf.nn.batch_normalization(X, mean, variance, offset=beta,
                                       scale=gamma, variance_epsilon=1e-8)
    return activation(norm_z)
