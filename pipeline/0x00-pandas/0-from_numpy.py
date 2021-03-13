#!/usr/bin/env python3
"""
From Numpy
"""
import pandas as pd


def from_numpy(array):
    """
    array is the np.ndarray from which you should create the pd.DataFrame
    """
    abc = list("ABCDEFGHIJKLMNOPQRSTUVW")
    cols = array.shape[1]
    return pd.DataFrame(array, columns=abc[:cols])
