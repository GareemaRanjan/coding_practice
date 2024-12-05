"""
Implement a function find_max_prod(lst) that takes a list of numbers and returns a maximum product pair.

Input
A list of integer numbers

Output
Two integers

Sample input#
lst = [1, 3, 5, 2, 6]
Sample output
result1, result2 = 5, 6

"""


def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """

    lst.sort()
    n = len(lst) - 1
    first = lst[0] * lst[1]
    last = lst[n] * lst[n - 1]
    if first > last:
        return lst[0], lst[1]
    else:
        return lst[n], lst[n - 1]


print(find_max_prod([-48, -2, 6, 0, -9, 1]))
