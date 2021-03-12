#!/usr/bin/env python3
"""
Policy and policy_gradient methods
"""

import numpy as np


def policy(matrix, weight):
    """
    Simple Policy function
    """
    res = state @ weight
    res = np.exp(res)

    return (res / res.sum())


def policy_gradient(state, weight):
    """
    Compute the Monte-Carlo policy gradient
    state: matrix representing the current observation of the environment
    weight: matrix of random weight
    """
    state = policy_value.reshape(-1, 1)
    policy_value = policy(state, weight)
    action = np.random.choice(len(policy_value[0]), p=policy_value[0])
    softmax = np.diagflat(state) - np.dot(state, state.T)
    dsoftmax = softmax[action, :]
    dlog = dsoftmax / policy_value[0, action]
    grad = state.T.dot(dlog[None, :])

    return (action, grad)
