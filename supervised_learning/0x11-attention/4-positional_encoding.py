#!/usr/bin/env python3
"""
Positional Encoding
"""
import numpy as np


def positional_encoding(max_seq_len, dm):
    """
    max_seq_len is an integer representing the maximum sequence length
    dm is the model depth
    """

    positional_enco = np.zeros([max_seq_len, dm])

    for i in range(dm):
        for j in range(max_seq_len):
            positional_enco[j, i] = j / \
                np.power(10000, (2 * (i // 2) / dm))

    positional_enco[:, 0::2] = np.sin(positional_enco[:, 0::2])
    positional_enco[:, 1::2] = np.cos(positional_enco[:, 1::2])

    return (positional_enco)
