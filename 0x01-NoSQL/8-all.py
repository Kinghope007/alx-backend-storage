#!/usr/bin/env python3
"""
list all doc in collection
"""


def list_all(mongo_collection):
    """
    lsit all doc
    """
    doc = list(mongo_collection.find())
    return doc
