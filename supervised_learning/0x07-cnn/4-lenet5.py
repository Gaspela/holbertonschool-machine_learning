#!/usr/bin/env python3
"""
LeNet-5 (Tensorflow)
"""

import tensorflow as tf


def lenet5(x, y):
    """
    m is the number of images
    Convolutional layer with 6 kernels of shape 5x5 with same padding
    Max pooling layer with kernels of shape 2x2 with 2x2 strides
    Convolutional layer with 16 kernels of shape 5x5 with valid padding
    Max pooling layer with kernels of shape 2x2 with 2x2 strides
    Fully connected layer with 120 nodes
    Fully connected layer with 84 nodes
    Fully connected softmax output layer with 10 nodes
    he_normal initialization method:
    tf.contrib.layers.variance_scaling_initializer().
    relu activation function
    Returns:
        a tensor for the softmax activated output
        a training operation that utilizes Adam optimization (with default
        hyperparameters).
        a tensor for the loss of the netowrk
        a tensor for the accuracy of the network
    """
    init = tf.contrib.layers.variance_scaling_initializer()

    conv_1 = tf.layers.Conv2D(filters=6, kernel_size=5, padding='same',
                              activation=tf.nn.relu,
                              kernel_initializer=init)(x)
    pool_1 = tf.layers.MaxPooling2D(2, 2)(conv_1)
    conv_2 = tf.layers.Conv2D(filters=16, kernel_size=5, padding='valid',
                              activation=tf.nn.relu,
                              kernel_initializer=init)(pool_1)
    pool_2 = tf.layers.MaxPooling2D(2, 2)(conv_2)
    flatten = tf.layers.Flatten()(pool_2)
    dense_1 = tf.layers.Dense(units=120,
                              activation=tf.nn.relu,
                              kernel_initializer=init)(flatten)
    dense_2 = tf.layers.Dense(units=84,
                              kernel_initializer=init,
                              activation=tf.nn.relu)(dense_1)
    dense_3 = tf.layers.Dense(units=10,
                              kernel_initializer=init)(dense_2)
    softmax = tf.nn.softmax(dense_3)
    equality = tf.equal(tf.argmax(dense_3, 1), tf.argmax(y, 1))
    acc = tf.reduce_mean(tf.cast(equality, tf.float32))
    loss = tf.losses.softmax_cross_entropy(y, dense_3)
    optimizer = tf.train.AdamOptimizer()
    adam = optimizer.minimize(loss)

    return (softmax, adam, loss, acc)
