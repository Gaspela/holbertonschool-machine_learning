#!/usr/bin/env python3
""" that calculates the shape of a matrix """


def matrix_shape(matrix):
    """ Shape matrix """
    shape = []
    while type(matrix) is list:
        """ Number of rows of a list """
        shape.append(len(matrix))
        """ Number of columns list"""
        if matrix[0]:
            matrix = matrix[0]
        else:
            break

    return shape
