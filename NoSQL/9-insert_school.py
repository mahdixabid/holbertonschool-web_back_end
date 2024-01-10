#!/usr/bin/env python3
""" Inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """

    # insert_one
    _id = mongo_collection.insert(kwargs)
    return _id
