#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """Write file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
