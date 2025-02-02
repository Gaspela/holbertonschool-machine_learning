#!/usr/bin/env python3
"""
Shear
"""
import tensorflow as tf


def shear_image(image, intensity):
    """
    image is a 3D tf.Tensor containing the image to shear
    intensity is the intensity with which the image should be sheared
    Returns the sheared image
    """
    img = tf.keras.preprocessing.image.img_to_array(image)
    shear = tf.keras.preprocessing.image.random_shear(img, intensity,
                                                      row_axis=0,
                                                      col_axis=1,
                                                      channel_axis=2)
    shears = tf.keras.preprocessing.image.array_to_img(shear)

    return (shears)
