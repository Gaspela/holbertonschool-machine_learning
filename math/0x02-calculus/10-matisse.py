#!/usr/bin/env python3
""" that calculates the derivative of a polynomial """


def poly_derivative(poly):
    """ derivative of a polynomial """
    if poly is None or poly == [] or type(poly) is not list:
        return None
    deriv_poly = [poly[i] * i for i in range(1, len(poly))]
    return deriv_poly
