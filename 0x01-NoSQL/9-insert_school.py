#! /usr/bin/env python3


def insert_scholl(monogo_collection, **kwargs):
    result = mongo_collection.insertOne(kwargs)
    return result.inserted_id
