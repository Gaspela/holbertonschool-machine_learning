#!/usr/bin/env python3
"""
Regular Chains
"""

import numpy as np


def regular(P):
    """
    P is a is a square 2D numpy.ndarray of shape (n, n) representing the
    transition matrix
    P[i, j] is the probability of transitioning from state i to state j
    n is the number of states in the markov chain
    Returns: a numpy.ndarray of shape (1, n) containing the steady state
    probabilities, or None on failure
    """
    if type(P) is not np.ndarray or len(P.shape) != 2:
        return None

    if P.shape[0] != P.shape[1]:
        return None

    if np.any(P <= 0):
        return None

    if np.min(P ** 2) < 0 or np.min(P ** 3) < 0:
        return None

    evals, evecs = np.linalg.eig(P.T)
    evecs = evecs[:, np.isclose(evals, 1)]

    return (evecs / evecs.sum()).T
