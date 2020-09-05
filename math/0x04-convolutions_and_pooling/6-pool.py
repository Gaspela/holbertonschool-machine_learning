#!/usr/bin/env python3
"""
Pooling
"""


import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    m is the number of images.
    h is the height in pixels of the images.
    w is the width in pixels of the images.
    kh is the height of the kernel.
    kw is the width of the kernel.
    sh is the stride for the height of the image
    sw is the stride for the width of the image
    max indicates max pooling
    avg indicates average pooling
    Returns: a numpy.ndarray containing the convolved images.
    """

    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    c = images.shape[3]
    kh = kernel_shape[0]
    kw = kernel_shape[1]
    sh = stride[0]
    sw = stride[1]

    height_conv = int(((h - kh) / sh) + 1)
    width_conv = int(((w - kw) / sw) + 1)
    conv = np.zeros((m, height_conv, width_conv, c))
    img = np.arange(0, m)

    for i in range(height_conv):
        for j in range(width_conv):
            if mode == 'max':
                data = np.max(images[img, i*sh:kh+(i*sh),
                                     j*sw:kw+(j*sw)], axis=(1, 2))
            if mode == 'avg':
                data = np.mean(images[img, i*sh:kh+(i*sh),
                                      j*sw:kw+(j*sw)], axis=(1, 2))
            conv[img, i, j] = data
    return conv
