#!/usr/bin/env python3
"""
Self Attention
"""

import tensorflow as tf


class SelfAttention(tf.keras.layers.Layer):
    """
    Calculate the attention for machine translation
    """

    def __init__(self, units):
        """
        Units is an integer representing the number of hidden units in the
        alignment model.
        """
        super().__init__()
        self.W = tf.keras.layers.Dense(units)
        self.U = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, s_prev, hidden_states):
        """
        s_prev is a tensor of shape (batch, units) containing the previous
        decoder hidden state.
        hidden_states is a tensor of shape (batch, input_seq_len, units)
        containing the outputs of the encoder.
        """
        prev = tf.expand_dims(s_prev, axis=1)
        enco = self.V(tf.nn.tanh(self.W(prev) + self.U(hidden_states)))
        weights = tf.nn.softmax(enco, axis=1)
        context = weights * hidden_states
        context = tf.reduce_sum(context, axis=1)

        return (context, weights)
