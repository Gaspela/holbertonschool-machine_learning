#!/usr/bin/env python3
"""
Rotate
"""
import tensorflow as tf


def rotate_image(image):
    """
    image is a 3D tf.Tensor containing the image to rotate
    Returns the rotated image
    """
    rotate = tf.image.rot90(image, k=1)

    return (rotate)
