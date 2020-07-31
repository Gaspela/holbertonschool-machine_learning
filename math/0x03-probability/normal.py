#!/usr/bin/env python3
""" Represents a normal distribution """


class Normal:
    """ Normal distribution """

    def __init__(self, data=None, mean=0., stddev=1.):
        """ Calculate normal distribution """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
                self.mean = float(mean)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) <= 2:
                raise ValueError("data must contain multiple values")
            else:
                self.mean = float(sum(data) / len(data))
                self.stddev = float(
                    (sum([(x - self.mean) **
                          2 for x in data]) / (len(data))) ** .5)

    def z_score(self, x):
        """ Calculates the z-score of a given x-value """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """ Calculates the x-value of a given z-score """
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        """ Calculates the value of the PDF for a given x-value """
        return (pow(2.7182818285, ((x - self.mean) ** 2 /
                                   (-2 * self.stddev ** 2))) /
                (2 * 3.1415926536 * self.stddev ** 2) ** .5)

    def cdf(self, x):
        """ Calculates the value of the CDF for a given x-value """
        e = (x - self.mean) / (self.stddev * 2 ** .5)
        return (1 + (e - e ** 3 / 3 + e ** 5 / 10 - e ** 7 /
                     42 + e ** 9 / 216) * 2 / 3.1415926536 ** .5) / 2
