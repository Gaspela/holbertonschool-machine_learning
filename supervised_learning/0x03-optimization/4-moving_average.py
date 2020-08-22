#!/usr/bin/env python3
"""  Calculates the weighted moving average of a data """

import tensorflow as tf


def moving_average(data, beta):
    """
    data is the list of data to calculate the moving average of
    beta is the weight used for the moving average
    Your moving average calculation should use bias correction
    Returns: a list containing the moving averages of data
    """
    beta_v = [0]
    moving = []
    for idx in range(len(data)):
        beta_v.append((beta * beta_v[idx]) + ((1 - beta) * data[idx]))
    for idx in range(1, len(beta_v)):
        moving.append(beta_v[idx] / (1 - (beta ** idx)))
    return moving
