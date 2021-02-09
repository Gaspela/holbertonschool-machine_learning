#!/usr/bin/env python3
"""
Epsilon Greedy
"""
import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """
    Q is a numpy.ndarray containing the q-table
    state is the current state
    epsilon is the epsilon to use for the calculation
    """
    if np.random.uniform(0, 1) < epsilon:
        action = np.argmax(Q[state, :])
    else:
        action = np.random.randint(0, 3, None)

    return (action)
