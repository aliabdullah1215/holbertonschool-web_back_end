#!/usr/bin/env python3
"""Module to update school topics"""


def update_topics(mongo_collection, name, topics):
    """Update topics of school documents based on name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
