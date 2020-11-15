#!/usr/bin/env python3
"""
Markov Chain
"""

import numpy as np


def markov_chain(P, s, t=1):
    """
    P is a square 2D numpy.ndarray of shape (n, n) representing the transition
    matrix
    P[i, j] is the probability of transitioning from state i to state j
    n is the number of states in the markov chain
    s is a numpy.ndarray of shape (1, n) representing the probability of
    starting in each state
    t is the number of iterations that the markov chain has been through
    Returns: a numpy.ndarray of shape (1, n) representing the probability of
    being in a specific state after t iterations, or None on failure
    """
    if type(P) is not np.ndarray or type(s) is not np.ndarray:
        return None

    if len(P.shape) != 2 or len(s.shape) != 2:
        return None

    if P.shape[0] != P.shape[1] or s.shape[1] != P.shape[0]:
        return None

    if s.shape[0] != 1:
        return None

    s = np.copy(s)
    for i in range(t):
        s = np.matmul(s, P)
    return s
