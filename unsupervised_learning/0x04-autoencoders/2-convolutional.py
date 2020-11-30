#!/usr/bin/env python3
"""
Convolutional Autoencoder
"""


import tensorflow.keras as keras


def autoencoder(input_dims, filters, latent_dims):
    """
    input_dims is a tuple of integers containing the dimensions of the model
    input
    filters is a list containing the number of filters for each convolutional
    i in the encoded, respectively
    the filters should be reversed for the decoder
    latent_dims is a tuple of integers containing the dimensions of the latent
    space representation
    Each convolution in the encoded should use a kernel size of (3, 3) with
    same padding and relu activation, followed by max pooling of size (2, 2)
    Each convolution in the decoder, except for the last two, should use a
    filter size of (3, 3) with same padding and relu activation, followed by
    upsampling of size (2, 2)
    The second to last convolution should instead use valid padding
    The last convolution should have the same number of filters as the number
    of channels in input_dims with sigmoid activation and no upsampling
    Returns: encoded, decoder, auto
    encoded is the encoded model
    decoder is the decoder model
    auto is the full auto model
    The auto model should be compiled using adam optimization and
    binary cross-entropy loss
    """
    input_encoder = keras.Input(shape=input_dims)
    input_encoded = input_encoder

    for i in filters:
        input_encoded = keras.layers.Conv2D(i, 3, activation="relu",
                                            padding="same")(input_encoded)
        input_encoded = keras.layers.MaxPool2D(padding="same")(input_encoded)

    encoded = keras.Model(input_encoder, input_encoded)
    decoded = keras.Input(shape=latent_dims)
    input_decoder = decoded

    for i in filters[::-1][:-1]:
        input_decoder = keras.layers.Conv2D(i, 3, activation="relu",
                                            padding="same")(input_decoder)
        input_decoder = keras.layers.UpSampling2D()(input_decoder)

    if len(filters):
        input_decoder = keras.layers.Conv2D(
            filters[0], 3, activation="relu")(input_decoder)
        input_decoder = keras.layers.UpSampling2D()(input_decoder)
    input_decoder = keras.layers.Conv2D(input_dims[2],
                                        input_dims[0:2],
                                        activation="sigmoid",
                                        padding="same")(input_decoder)

    decoder = keras.Model(decoded, input_decoder)
    auto = keras.Model(input_encoder, decoder(encoded(input_encoder)))
    auto.compile(optimizer="adam", loss="binary_crossentropy")

    return encoded, decoder, auto
