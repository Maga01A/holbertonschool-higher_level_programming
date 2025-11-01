#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete the item at a specific position in a list.
    Args:
        my_list (list): The list of integers.
        idx (int): The index of the element to delete.
    Returns:
        list: The modified list with the element at idx removed.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list