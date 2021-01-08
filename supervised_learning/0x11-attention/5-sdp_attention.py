#!/usr/bin/env python3
"""
Scaled Dot Product Attention
"""

import tensorflow as tf


def sdp_attention(Q, K, V, mask=None):
    """
    Q is a tensor with its last two dimensions as (..., seq_len_q, dk)
    containing the query matrix.
    K is a tensor with its last two dimensions as (..., seq_len_v, dk)
    containing the key matrix.
    V is a tensor with its last two dimensions as (..., seq_len_v, dv)
    containing the value matrix.
    mask is a tensor that can be broadcast into (..., seq_len_q, seq_len_v)
    containing the optional mask, or defaulted to None.
    """
    query_key_mat = tf.matmul(Q, K, transpose_b=True)
    dk = tf.cast(tf.shape(K)[-1], tf.float32)
    query_key_scaled = query_key_mat / tf.math.sqrt(dk)
    if mask is not None:
        query_key_scaled += (mask * -1e9)
    weights = tf.nn.softmax(query_key_scaled, axis=-1)
    output = tf.matmul(weights, V)

    return (output, weights)
