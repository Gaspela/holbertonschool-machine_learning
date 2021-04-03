#!/usr/bin/env python3
"""
Hue
"""
import tensorflow as tf


def change_hue(image, delta):
    """
    image is a 3D tf.Tensor containing the image to change
    delta is the amount the hue should change
    Returns the altered image
    """
    Hue = tf.image.adjust_hue(image, delta)

    return (Hue)
