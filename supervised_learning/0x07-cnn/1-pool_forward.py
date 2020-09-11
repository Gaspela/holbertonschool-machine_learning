#!/usr/bin/env python3
"""
Pooling Forward Prop
"""

import numpy as np


def pool_forward(A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """
    m is the number of examples
    h_prev is the height of the previous layer
    w_prev is the width of the previous layer
    c_prev is the number of channels in the previous layer
    kh is the filter height
    kw is the filter width
    c_prev is the number of channels in the previous layer
    c_new is the number of channels in the output
    sh is the stride for the height
    sw is the stride for the width
    Returns: the output of the pooling layer
    """
    m = A_prev.shape[0]
    h_prev = A_prev.shape[1]
    w_prev = A_prev.shape[2]
    c_prev = A_prev.shape[3]
    kh = kernel_shape[0]
    kw = kernel_shape[1]
    sh = stride[0]
    sw = stride[1]

    ph = int(((h_prev - kh) / sh) + 1)
    pw = int(((w_prev - kw) / sw) + 1)

    conv = np.zeros((m, ph, pw, c_prev))

    for i in range(ph):
        for j in range(pw):
            data = np.reshape(A_prev[:, i * sh:i * sh + kh,
                                     j * sw:j * sw + kw, :],
                              (m, kh * kw, c_prev))
            if mode is 'max':
                conv[:, i, j, :] = np.amax(data, axis=1)
            elif mode is 'avg':
                conv[:, i, j, :] = np.sum(data, axis=1) / (kh * kw)

    return conv
