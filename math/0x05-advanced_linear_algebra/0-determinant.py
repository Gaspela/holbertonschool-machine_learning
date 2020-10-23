#!/usr/bin/env python3
"""
that calculates the determinant of a matrix
"""


def determinant(matrix):
    """
    matrix is a list of lists whose determinant should be calculated
    """
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError('matrix must be a list of lists')

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

    if len(matrix) is 1 and len(matrix[0]) is 0:
        return 1

    if len(matrix) is not len(matrix[0]):
        raise ValueError('matrix must be a square matrix')

    if len(matrix) == 1:
        return matrix[0][0]

    detres = 0
    for i, j in enumerate(matrix[0]):
        row = [r for r in matrix[1:]]
        tmp = []

        for r in row:
            aux = []
            for c in range(len(matrix)):
                if c != i:
                    aux.append(r[c])
            tmp.append(aux)

        detres += j * (-1) ** i * determinant(tmp)

    return detres
