#!/usr/bin/env python3
"""
Early Stopping
"""


import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False, patience=0,
                verbose=True, shuffle=False):
    """
    early_stopping is a boolean that indicates whether early stopping should
    be used.
    early stopping should only be performed if validation_data exists
    early stopping should be based on validation loss
    patience is the patience used for early stopping
    """
    callbacks = []
    if early_stopping and validation_data:
        callbacks.append(K.callbacks.EarlyStopping(patience=patience))

    history = network.fit(data, labels, batch_size=batch_size, epochs=epochs,
                          shuffle=shuffle, verbose=verbose,
                          validation_data=validation_data,
                          callbacks=callbacks)

    return history
