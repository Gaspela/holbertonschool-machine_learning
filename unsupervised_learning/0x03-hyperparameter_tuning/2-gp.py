#!/usr/bin/env python3
"""Gaussian Process Prediction"""


import numpy as np


class GaussianProcess:
    """
    X_init is a numpy.ndarray of shape (t, 1) representing the inputs already
    sampled with the black-box function
    Y_init is a numpy.ndarray of shape (t, 1) representing the outputs of the
    black-box function for each input in X_init
    t is the number of initial samples
    l is the length parameter for the kernel
    sigma_f is the standard deviation given to the output of the black-box
    function
    Sets the public instance attributes X, Y, l, and sigma_f corresponding to
    the respective constructor inputs
    Sets the public instance attribute K, representing the current covariance
    kernel matrix for the Gaussian process
    """

    def __init__(self, X_init, Y_init, l=1, sigma_f=1):

        self.X = X_init
        self.Y = Y_init
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """
        X1 is a numpy.ndarray of shape (m, 1)
        X2 is a numpy.ndarray of shape (n, 1)
        the kernel should use the Radial Basis Function (RBF)
        Returns: the covariance kernel matrix as a numpy.ndarray of shape (m,
        n)
        """
        sqdist = np.sum(X1 ** 2, 1).reshape(-1, 1) +\
            np.sum(X2 ** 2, 1) - 2 * np.dot(X1, X2.T)
        return self.sigma_f**2 * np.exp(-0.5 / self.l**2 * sqdist)

    def predict(self, X_s):
        """
        X_s is a numpy.ndarray of shape (s, 1) containing all of the points
        whose mean and standard deviation should be calculated
        s is the number of sample points
        Returns: mu, sigma
        mu is a numpy.ndarray of shape (s,) containing the mean for each point
        in X_s, respectively
        sigma is a numpy.ndarray of shape (s,) containing the variance for
        each point in X_s, respectively
        """
        Ks = self.kernel(self.X, X_s)
        Kss = self.kernel(X_s, X_s)
        Kinv = np.linalg.inv(self.K)
        mus = Ks.T.dot(Kinv).dot(self.Y)
        covs = Kss - Ks.T.dot(Kinv).dot(Ks)
        return mus.T[0], np.diag(covs)

    def update(self, X_new, Y_new):
        """
        X_new is a numpy.ndarray of shape (1,) that represents the new sample
        point
        Y_new is a numpy.ndarray of shape (1,) that represents the new sample
        function value
        Updates the public instance attributes X, Y, and K
        """
        self.X = np.vstack((self.X, X_new))
        self.Y = np.vstack((self.Y, Y_new))
        self.K = self.kernel(self.X, self.X)
