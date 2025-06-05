#!/usr/bin/python3
"""Class to JSON"""
import json


def class_to_json(obj):
    """Class to JSON"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
