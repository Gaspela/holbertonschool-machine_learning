#!/usr/bin/env python3
"""
Bayesian Optimization - Acquisition
"""

import numpy as np
from scipy.stats import norm
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization:
    """
    performs Bayesian optimization on a noiseless 1D Gaussian process
    """

    def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1,
                 sigma_f=1, xsi=0.01, minimize=True):
        """
        f is the black-box function to be optimized
        X_init is a numpy.ndarray of shape (t, 1) representing the inputs
        already sampled with the black-box function
        Y_init is a numpy.ndarray of shape (t, 1) representing the outputs of
        the black-box function for each input in X_init
        t is the number of initial samples
        bounds is a tuple of (min, max) representing the bounds of the space in
        which to look for the optimal point
        ac_samples is the number of samples that should be analyzed during
        acquisition
        l is the length parameter for the kernel
        sigma_f is the standard deviation given to the output of the black-box
        function
        xsi is the exploration-exploitation factor for acquisition
        minimize is a bool determining whether optimization should be performed
        for minimization (True) or maximization (False)
        """
        self.f = f
        self.gp = GP(X_init, Y_init, l, sigma_f)
        X_s = np.linspace(bounds[0], bounds[1], num=ac_samples)
        self.X_s = X_s.reshape(-1, 1)
        self.xsi = xsi
        self.minimize = minimize

    def acquisition(self):
        """
        X_next is a numpy.ndarray of shape (1,) representing the next best
        sample point
        EI is a numpy.ndarray of shape (ac_samples,) containing the expected
        improvement of each potential sample
        """
        mu_s, sigma_s = self.gp.predict(self.X_s)

        if self.minimize is True:
            Y_opts = np.min(self.gp.Y)
            imp = Y_opts - mu_s - self.xsi
        else:
            Y_opts = np.max(self.gp.Y)
            imp = mu_s - Y_opts - self.xsi

        with np.errstate(divide='ignore'):
            Z = imp / sigma_s
            EI = (imp * norm.cdf(Z)) + (sigma_s * norm.pdf(Z))
            EI[sigma_s == 0.0] = 0.0

        X_next = self.X_s[np.argmax(EI)]

        return X_next, EI
