#!/usr/bin/env python3
"""
Multi Head Attention
"""

import tensorflow as tf
sdp_attention = __import__('5-sdp_attention').sdp_attention


class MultiHeadAttention(tf.keras.layers.Layer):
    """
    perform multi head attention
    """

    def __init__(self, dm, h):
        """
        dm is an integer representing the dimensionality of the model
        h is an integer representing the number of heads
        dm is divisible by h
        """
        super().__init__()
        self.h = h
        self.dm = dm
        self.depth = int(dm / h)
        self.Wq = tf.keras.layers.Dense(dm)
        self.Wk = tf.keras.layers.Dense(dm)
        self.Wv = tf.keras.layers.Dense(dm)
        self.linear = tf.keras.layers.Dense(dm)

    def split_heads(self, m, batch):
        """
        to split last dim shape(self.h, self.depth)
        transpose result shape(batch, -1, self.h, self.depth)
        """
        m = tf.reshape(m, (batch, -1, self.h, self.depth))
        return tf.transpose(m, perm=[0, 2, 1, 3])

    def call(self, Q, K, V, mask):
        """
        Call method call()
        """
        batch = tf.shape(K)[0]

        Q = self.Wq(Q)
        K = self.Wk(K)
        V = self.Wv(V)

        Q = self.split_heads(Q, batch)
        K = self.split_heads(K, batch)
        V = self.split_heads(V, batch)

        scaled_attention, weights = sdp_attention(Q, K, V, mask)
        scaled_attention = tf.transpose(scaled_attention, perm=[0, 2, 1, 3])
        concat_attention = tf.reshape(scaled_attention,
                                      (batch, -1, self.dm))
        scaled_attention = self.linear(concat_attention)

        return (scaled_attention, weights)
