#!/usr/bin/env python3
""" returns the transpose of a 2D matrix """


def matrix_transpose(matrix):
    """ the transpose of a 2D matrix """
    return [[row[zero] for row in matrix] for zero in range(len(matrix[0]))]
    """  t_matrix = zip(*matrix)
    for row in t_matrix:
        print(row) """
