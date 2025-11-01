#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list.
    Args:
        my_list (list): The list of integers.
    Returns:
        int: The sum of all unique integers.
    """
    unique_integers = set(my_list)
    return sum(unique_integers)