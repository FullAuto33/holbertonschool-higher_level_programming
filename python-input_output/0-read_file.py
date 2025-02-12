#!/usr/bin/python3
""" Read text file UTF"""


def read_file(filename=""):
    """Print content of file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
