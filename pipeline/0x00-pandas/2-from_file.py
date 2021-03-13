#!/usr/bin/env python3
"""
From File
"""
import pandas as pd


def from_file(filename, delimiter):
    """ 
    filename is the file to load from
    delimiter is the column separator
    """
    return pd.read_csv(filename, sep=delimiter)
