#!/usr/bin/env python3
"""
Flip
"""
import tensorflow as tf


def flip_image(image):
    """
    image is a 3D tf.Tensor containing the image to flip
    Returns the flipped image
    """
    flip = tf.image.flip_left_right(image)

    return (flip)
