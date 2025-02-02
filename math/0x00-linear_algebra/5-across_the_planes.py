#!/usr/bin/env python3
"""  adds two matrices element-wise """


def add_matrices2D(mat1, mat2):
    """ two matrices element-wise """

    """ Condition row """
    if len(mat1) != len(mat2):
        return None
    """ Condition colunms """
    if len(mat1[0]) != len(mat2[0]):
        return None

    return [[a + b for a, b in zip(row1, row2)]
            for row1, row2 in zip(mat1, mat2)]
