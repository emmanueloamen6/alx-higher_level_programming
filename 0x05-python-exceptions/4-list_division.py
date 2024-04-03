#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ function that divides element by element 2 lists.

        Args:
            my_list_1 (list): list of elements.
            my_list_2 (list): list of elements.
            list_length (int): length of elements.

        Returns: newlist
    """
    new_list = []
    result = 0
    i = 0
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            reult = 0
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
