#!/usr/bin/env python3
"""
Sparse Autoencoder
"""


import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims, lambtha):
    """
    input_dims is an integer containing the dimensions of the model input
    hidden_layers is a list containing the number of nodes for each hidden
    i in the encoded, respectively
    the hidden layers should be reversed for the decoder
    latent_dims is an integer containing the dimensions of the latent space
    representation
    lambtha is the regularization parameter used for L1 regularization on the
    encoded output
    Returns: encoded, decoder, auto
    encoded is the encoded model
    decoder is the decoder model
    auto is the sparse auto model
    The sparse auto model should be compiled using adam optimization
    and binary cross-entropy loss
    All layers should use a relu activation except for the last i in the
     decoder, which should use sigmoid
    """
    input_encoder = keras.Input(shape=(input_dims,))
    input_encoded = input_encoder

    for i in hidden_layers:
        input_encoded = keras.layers.Dense(i, activation="relu")(input_encoded)

    regular = keras.regularizers.l1(lambtha)
    input_encoded = keras.layers.Dense(
        latent_dims, activation="relu",
        activity_regularizer=regular)(input_encoded)
    encoded = keras.Model(input_encoder, input_encoded)
    decoded = keras.Input(shape=(latent_dims,))
    input_decoder = decoded

    for i in hidden_layers[::-1]:
        input_decoder = keras.layers.Dense(i, activation="relu")(input_decoder)
    input_decoder = keras.layers.Dense(
        input_dims, activation="sigmoid")(input_decoder)
    decoder = keras.Model(decoded, input_decoder)
    auto = keras.Model(input_encoder, decoder(encoded(input_encoder)))
    auto.compile(optimizer="adam", loss="binary_crossentropy")

    return encoded, decoder, auto
