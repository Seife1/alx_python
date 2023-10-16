#!/usr/bin/python3
"""function that returns a key with the biggest integer value"""

def best_score(a_dictionary):
    if a_dictionary:
        best_value = None
        best_key = None

        for key in a_dictionary:
            if isinstance(a_dictionary[key], int):
                if best_value is None or a_dictionary[key] > best_value:
                    best_value = a_dictionary[key]
                    best_key = key
        return best_key
    else:
        return None