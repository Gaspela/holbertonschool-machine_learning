#!/usr/bin/env python3
"""
Convolutional Forward Prop
"""

import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
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
    """
    m = A_prev.shape[0]
    h_prev = A_prev.shape[1]
    w_prev = A_prev.shape[2]
    kh = W.shape[0]
    kw = W.shape[1]
    c_new = W.shape[3]
    sh = stride[0]
    sw = stride[1]

    if padding == 'same':
        ph = int(((h_prev - 1) * sh + kh - h_prev) / 2)
        pw = int(((w_prev - 1) * sw + kw - w_prev) / 2)
    if padding == 'valid':
        ph, pw = 0, 0

    height_conv = int(((h_prev - kh + (2 * ph)) / sh) + 1)
    width_conv = int(((w_prev - kw + (2 * pw)) / sw) + 1)

    images = np.pad(A_prev, pad_width=((0, 0), (ph, ph), (pw, pw), (0, 0)),
                    mode='constant', constant_values=0)

    conv = np.zeros((m, height_conv, width_conv, c_new))

    for i in range(c_new):
        for j in range(height_conv):
            for k in range(width_conv):
                data = images[:, j * sh:j * sh + kh, k * sw:k * sw + kw] \
                    * W[:, :, :, i]
                conv[:, j, k, i] = np.sum(data, axis=(1, 2, 3)) + b[:, :, :, i]

    return activation(conv)
