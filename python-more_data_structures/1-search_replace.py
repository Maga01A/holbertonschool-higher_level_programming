#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Search and replace in a list.
    Args:
        my_list (list): The list to search and replace in.
        search: The value to search for.
        replace: The value to replace with.
    Returns:
        list: A new list with the searched value replaced.
    """
    return [replace if i == search else i for i in my_list]
