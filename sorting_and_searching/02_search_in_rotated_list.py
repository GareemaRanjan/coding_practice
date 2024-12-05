"""
Given a sorted list of n integers that has been rotated an unknown number of times, write some code to find an element
in the list. You may assume that the list was originally sorted in an ascending order.

Input
A sorted list that has been rotated a number of times

Output
The index of the element

Sample input
lst = [7, 8, 9, 0, 3, 5, 6]
n = size of the list
key = 3 # Element that is being searched for

Sample output
result = 4 # Index of the element that was searched for

time complexity: nlogn ##doubtful, maybe O(n)
"""


def binary_search(lst, key):
    print(lst)

    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def pivoted_binary_search(lst, key):
    count = 0
    for num in lst:
        if num == key:
            return count
        if num < key:
            return count + binary_search(lst[count:], key)
        count = count + 1

    return -1


print(pivoted_binary_search([7, 8, 9, 0, 3, 5, 6], 3))
