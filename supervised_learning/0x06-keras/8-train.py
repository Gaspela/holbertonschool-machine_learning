#!/usr/bin/env python3
"""
Learning Rate Decay
"""


import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False, patience=0,
                learning_rate_decay=False, alpha=0.1, decay_rate=1,
                save_best=False, filepath=None,
                verbose=True, shuffle=False):
    """
    save_best is a boolean indicating whether to save the model after each
    epoch if it is the best.
    a model is considered the best if its validation loss is the lowest that
    the model has obtained.
    filepath is the file path where the model should be saved.
    """
    callbacks = []
    if early_stopping and validation_data:
        callbacks.append(K.callbacks.EarlyStopping(patience=patience))

    if learning_rate_decay and validation_data:
        def schedule(epoch):
            return alpha / (1 + decay_rate * epoch)
        callbacks.append(K.callbacks.LearningRateScheduler(schedule, 1))

    if save_best:
        callbacks.append(K.callbacks.ModelCheckpoint(filepath))

    history = network.fit(data, labels, batch_size=batch_size, epochs=epochs,
                          shuffle=shuffle, verbose=verbose,
                          validation_data=validation_data,
                          callbacks=callbacks)

    return history
