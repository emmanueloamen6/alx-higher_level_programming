#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Print the number on the list.

    Args:
        my_list(list): The list of the element to print.
        x(int):  Number of elements to print.

        Returns:
            Number of elements printed.
        """
    i = 0
    count = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
