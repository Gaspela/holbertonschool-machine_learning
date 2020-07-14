#!/usr/bin/env python3
""" performs element-wise addition, subtraction, multiplication, division """


def np_elementwise(mat1, mat2):
    """ performs element-wise """
    add = mat1 + mat2
    sub = mat1 - mat2
    multi = mat1 * mat2
    divi = mat1 / mat2

    return add, sub, multi, divi
