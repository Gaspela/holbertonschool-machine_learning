#!/usr/bin/env python3
"""
that calculates the minor matrix of a matrix
"""


def determinant(matrix):
    """
    matrix is a list of lists whose determinant should be calculated
    """
    if not isinstance(matrix, list) or len(matrix) is 0:
        raise TypeError("matrix must be a list of lists")

    if len(matrix) is 1 and len(matrix[0]) is 0:
        return 1

    for r in matrix:
        if not isinstance(r, list):
            raise TypeError("matrix must be a list of lists")

    for r in matrix:
        if len(r) != len(matrix):
            raise ValueError('matrix must be a square matrix')

    if len(matrix) is 1 and len(matrix[0]) is 1:
        return matrix[0][0]

    if len(matrix) is 2 and len(matrix[0]) is 2:
        det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return det

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


def minor(matrix):
    """
    matrix is a list of lists whose minor matrix should be calculated
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    if not matrix:
        raise TypeError("matrix must be a list of lists")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

    for row in matrix:
        if len(matrix) != len(row):
            raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) is 1 and len(matrix[0]) is 1:
        return [[1]]

    minres = [x[:] for x in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            minres[i][j] = submatrixminor(matrix, i, j)
    return minres


def submatrixminor(matrix, i, j):
    """
    Get matrix minnor
    """
    return determinant([row[:j]
                        + row[j+1:] for row in (matrix[:i]+matrix[i+1:])])
