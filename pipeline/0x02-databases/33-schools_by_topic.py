#!/usr/bin/env python3
"""
Where can I learn Python?
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    mongo_collection will be the pymongo collection object
    topic (string) will be topic searched
    """
    mongo_collection.find({'topics': topic})
