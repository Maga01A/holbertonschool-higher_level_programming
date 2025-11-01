#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Updates a dictionary with a key-value pair.
    Args:
        a_dictionary (dict): The dictionary to update.
        key: The key to add or update.
        value: The value associated with the key.
    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
