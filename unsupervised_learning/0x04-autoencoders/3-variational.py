#!/usr/bin/env python3
"""
Variational Autoencoder
"""


import tensorflow.keras as keras


def sampling(args):
    """Sample sampling """
    z_mean, z_logvar = args
    batch = keras.backend.shape(z_mean)[0]
    dim = keras.backend.int_shape(z_mean)[1]
    epsilon = keras.backend.random_normal(shape=(batch, dim))
    return z_mean + keras.backend.exp(0.5 * z_logvar) * epsilon


def autoencoder(input_dims, hidden_layers, latent_dims):
    """
    input_dims is an integer containing the dimensions of the model input
    hidden_layers is a list containing the number of nodes for each hidden
    layer in the encoder, respectively
    the hidden layers should be reversed for the decoder
    latent_dims is an integer containing the dimensions of the latent space
    representation
    Returns: encoder, decoder, auto
    encoder is the encoder model, which should output the latent
    representation, the mean, and the log variance, respectively
    decoder is the decoder model
    auto is the full auto model
    The auto model should be compiled using adam optimization and
    binary cross-entropy loss
    All layers should use a relu activation except for the mean and log
    variance layers in the encoder, which should use None, and the last layer
    in the decoder, which should use sigmoid
    """
    input_encoder = keras.Input(shape=(input_dims,))
    input_encoded = input_encoder

    for i in hidden_layers:
        input_encoded = keras.layers.Dense(
            i, activation="relu")(input_encoded)
    z_mean = keras.layers.Dense(latent_dims)(input_encoded)
    z_logvar = keras.layers.Dense(latent_dims)(input_encoded)
    latents = keras.layers.Lambda(sample,
                                  output_shape=latent_dims)([z_mean, z_logvar])
    encoded = keras.Model(input_encoder, [z_mean, z_logvar, latents])
    decoded = keras.Input(shape=(latent_dims,))
    input_decoder = decoded

    for i in hidden_layers[::-1]:
        input_decoder = keras.layers.Dense(i, activation="relu")(input_decoder)
    input_decoder = keras.layers.Dense(
        input_dims, activation="sigmoid")(input_decoder)

    decoder = keras.Model(decoded, input_decoder)
    output = decoder(encoded(input_encoder)[2])
    auto = keras.Model(input_encoder, output)
    recons_loss = keras.losses.binary_crossentropy(input_encoder, output)
    recons_loss *= input_dims
    kl_loss = 1 + z_logvar - keras.backend.square(z_mean)
    kl_loss -= keras.backend.exp(z_logvar)
    kl_loss = keras.backend.sum(kl_loss, axis=-1)
    kl_loss /= -2
    vae_loss = keras.backend.z_mean(recons_loss + kl_loss)
    auto.add_loss(vae_loss)
    auto.compile(optimizer="adam", loss="mse")

    return encoded, decoder, auto
