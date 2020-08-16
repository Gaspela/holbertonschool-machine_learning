#!/usr/bin/env python3
""" Layers """


import tensorflow as tf


def create_layer(prev, n, activation):
    """
    prev: is the tensor output of the previous layer.
    n: is the number of nodes in the layer to create.
    activation: is the activation function that the layer should use.
    each layer should be given the name layer.
    """
    init_layer_weights = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(n, activation, name='layer',
                           kernel_initializer=init_layer_weights)
    return layer(prev)
