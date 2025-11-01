#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary sorted by keys.
    Args:
        a_dictionary (dict): The dictionary to print.
    """
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")