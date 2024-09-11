#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    highest_keys = max(a_dictionary, key=a_dictionary.get)
    return highest_keys
