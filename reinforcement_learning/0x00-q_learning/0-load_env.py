#!/usr/bin/env python3
"""
Load the Environment
"""
import gym


def load_frozen_lake(desc=None, map_name=None, is_slippery=False):
    """
    desc is either None or a list of lists containing a custom description of
    the map to load for the environment
    map_name is either None or a string containing the pre-made map to load
    is_slippery is a boolean to determine if the ice is slippery
    """
    environment = gym.make("FrozenLake-v0", desc=desc,
                           map_name=map_name, is_slippery=is_slippery)

    return (environment)
