#!/usr/bin/env python3
"""
Valid Convolution
"""


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    m is the number of images.
    h is the height in pixels of the images.
    w is the width in pixels of the images.
    kh is the height of the kernel.
    kw is the width of the kernel.
    Returns: a numpy.ndarray containing the convolved images.
    """
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    height_conv = h - kh + 1
    width_conv = w - kw + 1

    conv = np.zeros((m, height_conv, width_conv))
    for i in range(height_conv):
        for j in range(width_conv):
            data = np.multiply(images[:, i:i+kh, j:j+kw], kernel)
            data = np.reshape(data, (m, kh * kw))
            conv[:, i, j] = np.sum(data, axis=1)
    return conv
