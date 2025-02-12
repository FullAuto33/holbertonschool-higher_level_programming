#!/usr/bin/python3
"""Defines write file in UTF8"""


def write_file(filename="", text=""):
    """Function write in file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
