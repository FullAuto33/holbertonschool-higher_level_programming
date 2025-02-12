#!/usr/bin/python3
"""Define file append """


def append_write(filename="", text=""):
    """ function append file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
