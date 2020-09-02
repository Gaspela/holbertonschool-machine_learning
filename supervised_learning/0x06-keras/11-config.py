#!/usr/bin/env python3
"""
Save and Load Configuration
"""


import tensorflow.keras as K


def save_config(network, filename):
    """
    network is the model whose configuration should be saved
    filename is the path of the file that the configuration should be saved to
    Returns: None
    """
    with open(filename, 'w') as file:
        file.write(network.to_json())

    return None


def load_config(filename):
    """
    filename is the path of the file containing the model’s configuration in
    JSON format
    Returns: the loaded model
    """
    with open(filename, 'r') as file:
        model = K.models.model_from_json(file.read())

    return model
