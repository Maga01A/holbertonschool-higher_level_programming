#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list.

    Args:
        my_list (list): The list of integers.

    Returns:
        list: A new list with True or False, depending on whether the
        integer at the same position in the original list is a multiple of 2.
    """
    return [i % 2 == 0 for i in my_list]      