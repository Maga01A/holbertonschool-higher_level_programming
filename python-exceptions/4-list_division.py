#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        list: A new list of length list_length containing the results of the divisions.
    """
    result = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            division = 0
            print("division by 0")
        except TypeError:
            division = 0
            print("wrong type")
        except IndexError:
            division = 0
            print("out of range")
        finally:
            result.append(division)
    return result
