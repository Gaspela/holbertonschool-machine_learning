#!/usr/bin/env python3
"""
Transformer Encoder Block
"""

import tensorflow as tf
MultiHeadAttention = __import__('6-multihead_attention').MultiHeadAttention


class EncoderBlock(tf.keras.layers.Layer):
    """
    encoder block for a transformer
    """

    def __init__(self, dm, h, hidden, drop_rate=0.1):
        """
        dm - the dimensionality of the model
        h - the number of heads
        hidden - the number of hidden units in the fully connected layer
        drop_rate - the dropout rate
        """
        super().__init__()
        self.mha = MultiHeadAttention(dm, h)
        self.dense_hidden = tf.keras.layers.Dense(hidden, activation='relu')
        self.dense_output = tf.keras.layers.Dense(dm)
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = tf.keras.layers.Dropout(drop_rate)
        self.dropout2 = tf.keras.layers.Dropout(drop_rate)

    def call(self, x, training, mask=None):
        """
        Call method call()
        """
        attn_output, _ = self.mha(x, x, x, mask)
        attn_output = self.dropout1(attn_output, training=training)
        dout1 = self.layernorm1(x + attn_output)
        ffn_output = self.dense_hidden(dout1)
        ffn_output = self.dense_output(ffn_output)
        ffn_output = self.dropout2(ffn_output, training=training)
        dout2 = self.layernorm2(dout1 + ffn_output)

        return (dout2)
