#!/usr/bin/python3
"""CountedIterator - Keeping Track of Iteration"""


class CountedIterator:
    """ CountedIterator class"""
    def __init__(self, iterator):
        """Init counted iterator"""
        self._iter = iter(iterator)
        self._count = 0

    def __next__(self):
        """Get next item and increment count"""
        self._count += 1
        return next(self._iter)

    def get_count(self):
        """Get current count of items iterated"""
        return self._count

    def __iter__(self):
        """Return self as an iterator"""
        return self
