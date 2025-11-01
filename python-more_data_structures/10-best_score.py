#!/usr/bin/python3
def best_score(a_dictionary):
    """Finds the key with the highest value in a dictionary.
    Args:
        a_dictionary (dict): The dictionary to search.
    Returns:
        The key with the highest value, or None if the dictionary is empty.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
