"""
Given a sorted list and a target value, return the index of the target value if the value is present in the list. If the value is not present, return the index at which the value should be inserted.

You may assume that no duplicates are in the list.

Input
A sorted list and a target value

Output
The index at which the list should be inserted OR the index at which it is already present

Sample input
  lst = [1, 3, 5, 6]
  value = 5
Sample output
  result = 2

Time complexity - O(n)
Time complexity binary - O(log n)
"""


def search_insert_position(lst, value):
    """
    A function to search insert position of a given value in a list
    :param lst:  A list of integers
    :param value: An integer
    :return: The position of the value to be in the list
    """

    # Write your code here!
    for i in range(0, len(lst) - 1):
        if lst[i] < value and lst[i + 1] >= value:
            return i + 1
    return i + 1


def search_insert_position_binary(lst, value):
    """
    A function to search insert position of a given value in a list
    :param lst:  A list of integers
    :param value: An integer
    :return: The position of the value to be in the list
    """

    size = len(lst)

    if size < 1:
        return -1

    start = 0
    end = size - 1

    pos = 0

    while start <= end:
        mid = start + (end - start) // 2

        if lst[mid] == value:
            return mid
        elif lst[mid] > value:
            end = mid - 1
            pos = mid
        else:
            start = mid + 1
            pos = mid + 1

    return pos


print(search_insert_position([1, 3, 5, 6], 5))
print(search_insert_position([1, 3, 5, 6], 10))
