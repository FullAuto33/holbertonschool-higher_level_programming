#!/usr/bin/python3
"""Class to JSON"""
import json


def class_to_json(obj):
    """Class to JSON"""
    obj = {}
    if hasattr(obj, "__dict__"):
        obj = obj.__dict__
    return obj

