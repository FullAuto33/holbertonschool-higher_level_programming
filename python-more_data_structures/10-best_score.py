#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        result = len(a_dictionary.values())
        if result > 0:
            count = max(a_dictionary.values())
            for i in a_dictionary.keys():
                if a_dictionary[i] == count:
                    return i
    return None
