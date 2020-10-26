#!/usr/bin/env python3
"""
that represents a Multivariate Normal distribution
"""
import numpy as np


class MultiNormal:
    """Multinormal Class"""

    def __init__(self, data):
        """
        data is a numpy.ndarray of shape (d, n) containing the data set:
        n is the number of data points
        d is the number of dimensions in each data point
        If data is not a 2D numpy.ndarray, raise a TypeError with the message
        data must be a 2D numpy.ndarray
        If n is less than 2, raise a ValueError with the message data must
        contain multiple data points
        """
        if type(data) is not np.ndarray or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")

        mean = np.mean(data, axis=1).reshape((data.shape[0], 1))
        self.mean = mean
        self.cov = np.matmul(data - self.mean, data.T) / (data.shape[1] - 1)
