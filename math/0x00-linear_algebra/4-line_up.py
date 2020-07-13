#!/usr/bin/env python3
""" Adds two arrays element-wise """


def add_arrays(arr1, arr2):
    """ two arrays element-wise """
    if len(arr1) != len(arr2):
        """ print(add_arrays(arr1, [1, 2, 3])) arr2 is diferent Return None"""
        return None
    return [a + b for a, b in zip(arr1, arr2)]
