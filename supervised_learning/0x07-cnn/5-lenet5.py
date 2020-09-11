#!/usr/bin/env python3
"""
LeNet-5 (Keras)
"""

import tensorflow.keras as K


def lenet5(X):
    """
    m is the number of images
    Convolutional layer with 6 kernels of shape 5x5 with same padding
    Max pooling layer with kernels of shape 2x2 with 2x2 strides
    Convolutional layer with 16 kernels of shape 5x5 with valid padding
    Max pooling layer with kernels of shape 2x2 with 2x2 strides
    Fully connected layer with 120 nodes
    Fully connected layer with 84 nodes
    Fully connected softmax output layer with 10 nodes
    Returns: a K.Model compiled to use Adam optimization (with default
    hyperparameters) and accuracy metrics
    """
    conv_1 = K.layers.Conv2D(filters=6, kernel_size=5, padding='same',
                             activation='relu',
                             kernel_initializer='he_normal')(X)
    pool_1 = K.layers.MaxPool2D(2, 2)(conv_1)
    conv_2 = K.layers.Conv2D(filters=16, kernel_size=5,
                             activation='relu',
                             kernel_initializer='he_normal')(pool_1)
    pool_2 = K.layers.MaxPool2D(2, 2)(conv_2)
    flatten = K.layers.Flatten()(pool_2)
    dense_1 = K.layers.Dense(120, input_shape=X.shape,
                             activation='relu',
                             kernel_initializer='he_normal')(flatten)
    dense_2 = K.layers.Dense(84, activation='relu',
                             kernel_initializer='he_normal')(dense_1)
    dense_3 = K.layers.Dense(10, activation='softmax',
                             kernel_initializer='he_normal')(dense_2)
    model = K.Model(inputs=X, outputs=dense_3)
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model
