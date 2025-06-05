#!/usr/bin/python3
"""Load, add, save"""
import json
import sys


def save_to_json_file(my_obj, filename):
    """Save object to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


filename = 'add_item.json'
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []
for arg in sys.argv[1:]:
    items.append(arg)
save_to_json_file(items, filename)
