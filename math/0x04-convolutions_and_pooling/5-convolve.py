#!/usr/bin/env python3
"""
Multiple Kernels
"""


import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    m is the number of images.
    h is the height in pixels of the images.
    w is the width in pixels of the images.
    c is the number of channels in the image
    kh is the height of the kernel.
    kw is the width of the kernel.
    nc is the number of kernels
    ph is the padding for the height of the image
    pw is the padding for the width of the image
    sh is the stride for the height of the image
    sw is the stride for the width of the image
    Returns: a numpy.ndarray containing the convolved images.
    """

    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    c = images.shape[3]
    kh = kernels.shape[0]
    kw = kernels.shape[1]
    nc = kernels.shape[3]
    sh = stride[0]
    sw = stride[1]

    if padding == 'same':
        ph = int(((h - 1) * sh + kh - h) / 2) + 1
        pw = int(((w - 1) * sw + kw - w) / 2) + 1
    if padding == 'valid':
        ph, pw = 0, 0
    if type(padding) is tuple:
        ph = padding[0]
        pw = padding[1]

    height_conv = int(((h - kh + (2 * ph)) / sh) + 1)
    width_conv = int(((w - kw + (2 * pw)) / sw) + 1)

    img = np.arange(0, m)
    images = np.pad(images, [(0, 0), (ph, ph), (pw, pw), (0, 0)], 'constant',
                    constant_values=0)
    conv = np.zeros((m, height_conv, width_conv, nc))

    for i in range(height_conv):
        for j in range(width_conv):
            for k in range(nc):
                data = np.sum(np.multiply(images[img, i*sh:kh+(i*sh),
                                                 j*sw:kw+(j*sw)],
                                          kernels[:, :, :, k]), axis=(1, 2, 3))
                conv[img, i, j, k] = data
    return conv
