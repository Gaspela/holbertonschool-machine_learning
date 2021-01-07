#!/usr/bin/env python3
"""
RNN Encoder
"""
import tensorflow as tf


class RNNEncoder(tf.keras.layers.Layer):
    """
    Encode for machine translation
    """

    def __init__(self, vocab, embedding, units, batch):
        """
        vocab is an integer representing the size of the input vocabulary
        embedding is an integer representing the dimensionality of the
        embedding vector.
        units is an integer representing the number of hidden units in the RNN
        cell.
        batch is an integer representing the batch size
        """
        super().__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(vocab, embedding)
        self.gru = tf.keras.layers.GRU(units,
                                       recurrent_initializer='glorot_uniform',
                                       return_sequences=True,
                                       return_state=True)

    def initialize_hidden_state(self):
        """
        Initializes the hidden states for the RNN cell to a tensor of zeros
        """
        initializer = tf.keras.initializers.Zeros()
        values = initializer(shape=(self.batch, self.units))

        return (values)

    def call(self, x, initial):
        """
        Call method call()
        """
        embedding = self.embedding(x)
        outputs, hidden = self.gru(embedding, initial_state=initial)

        return (outputs, hidden)
