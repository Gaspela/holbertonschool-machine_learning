#!/usr/bin/env python3
""" calculates the integral of a polynomial """


def poly_integral(poly, C=0):
    """ Calculate polynomial """

    if C is None or type(C) not in (int, float):
        return None

    if poly is None or poly == [] or type(poly) is not list:
        return None

    if poly == [0]:
        return [C]

    integrate = [C]
    i = 0

    while i < len(poly):
        if type(poly[i]) not in (int, float) or poly[i] is None:
            return None
        coef = poly[i] / (i + 1)
        if coef.is_integer():
            coef = int(coef)
        integrate.append(coef)
        i += 1

    return integrate
