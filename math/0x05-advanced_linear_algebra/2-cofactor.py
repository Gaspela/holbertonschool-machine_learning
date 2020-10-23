#!/usr/bin/env python3
"""
that calculates the cofactor matrix of a matrix
"""


def determinant(matrix):
    """
    matrix is a list of lists whose determinant should be calculated
    """
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError('matrix must be a list of lists')

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a list of lists')

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")

    if len(matrix) is 1 and len(matrix[0]) is 0:
        return 1

    if len(matrix) is not len(matrix[0]):
        raise ValueError('matrix must be a square matrix')

    if len(matrix) is 1 and len(matrix[0]) is 1:
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


def minor(matrix):
    """
    matrix is a list of lists whose minor matrix should be calculated
    """
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError('matrix must be a list of lists')

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a list of lists')

    if matrix is [[]]:
        raise ValueError('matrix must be a non-empty square matrix')

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


def cofactor(matrix):
    """
    matrix is a list of lists whose cofactor matrix should be calculated
    """
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError('matrix must be a list of lists')

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a list of lists')

    if matrix is [[]]:
        raise ValueError('matrix must be a non-empty square matrix')

    for row in matrix:
        if len(matrix) != len(row):
            raise ValueError("matrix must be a non-empty square matrix")

    cofres = minor(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            cofres[i][j] *= (-1) ** (i+j)
    return cofres


def submatrixminor(matrix, i, j):
    """
    Get matrix minnor
    """
    return determinant([row[:j]
                        + row[j+1:] for row in (matrix[:i]+matrix[i+1:])])
