#!/usr/bin/env python3
"""
RMSProp
"""

import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """
    loss: is the learning rate.
    beta2: is the RMSProp weight.
    epsilon: is a small number to avoid division by zero.
    Returns: the RMSProp optimization operation.
    """
    optimizer = tf.train.RMSPropOptimizer(alpha, beta2, epsilon=epsilon)
    return (optimizer.minimize(loss))
