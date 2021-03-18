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
    list_all = []
    result = mongo_collection.find({'topics': {'$all': [topic]}})
    for res in result:
        list_all.append(res)

    return (list_all)
