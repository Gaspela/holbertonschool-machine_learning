#!/usr/bin/env python3
"""
Initialize Q-table
"""
import numpy as np


def q_init(env):
    """
    env is the FrozenLakeEnv instance
    Returns: the Q-table as a numpy.ndarray of zeros
    """
    action_space = env.action_space.n
    observation_space = env.observation_space.n
    q_table_init = np.zeros((observation_space, action_space))

    return (q_table_init)
