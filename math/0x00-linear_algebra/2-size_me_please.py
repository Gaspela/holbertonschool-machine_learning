#!/usr/bin/env python3
""" that calculates the shape of a matrix """


def matrix_shape(matrix):
    """ Shape matrix """
    shape = []
    try:
        while(len(matrix) > 0):
            """ Number of rows of a list """
            shape.append(len(matrix))
            """ Number of columns list"""
            matrix = matrix[0]
    """ SyntaxError: unexpected EOF while parsing """
    except TypeError:
        pass
        return shape
