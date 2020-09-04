#!/usr/bin/env python3
"""
Same Convolution
"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    m is the number of images
    h is the height in pixels of the images
    w is the width in pixels of the images
    kh is the height of the kernel
    kw is the width of the kernel
    Returns: a numpy.ndarray containing the convolved images
    """
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    ph = max((kh - 1) // 2, kh // 2)
    pw = max((kw - 1) // 2, kw // 2)

    images = np.pad(images, pad_width=((0, 0), (ph, ph),
                                       (pw, pw)), mode='constant')

    conv = np.zeros((m, h, w))
    for i in range(h):
        for j in range(w):
            data = np.multiply(images[:, i:i+kh, j:j+kw], kernel)
            conv[:, i, j] = np.sum(data, axis=(1, 2))
    return conv
