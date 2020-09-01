#!/usr/bin/env python3
"""
Validate
"""


import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, verbose=True, shuffle=False):
    """
    validation_data is the data to validate the model with, if not None
    """
    history = network.fit(data, labels, batch_size=batch_size, epochs=epochs,
                          shuffle=shuffle, verbose=verbose,
                          validation_data=validation_data)

    return history
