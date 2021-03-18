#!/usr/bin/env python3
"""
Insert a document in Python
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection will be the pymongo collection object
    Returns the new _id
    """
    id_ = mongo_collection.insert_one(kwargs).inserted_id

    return (id_)
