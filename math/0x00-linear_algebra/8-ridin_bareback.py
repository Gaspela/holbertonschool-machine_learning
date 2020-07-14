#!/usr/bin/env python3
""" performs matrix multiplication """


def mat_mul(mat1, mat2):
    """ matrix multiplication """
    if len(mat1[0]) != len(mat2):
        return None

    new_mat = [[row[zero] for row in mat2]
               for zero in range(len(mat2[0]))]
    return [[sum([a * b for a, b in zip(row1, row2)]) for row2 in new_mat]
            for row1 in mat1]
