#!/usr/bin/env python3
"""returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    documents = mongo_collection.find({"topics": topic})
    docs = [i for i in documents]
    return docs
