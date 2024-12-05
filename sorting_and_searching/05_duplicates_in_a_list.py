"""
Given a list of integers, find all the duplicates that exist in that list.

Input
A list of duplicate integers

Note: All the integers are less than the size of the list.

Output
A list with the duplicates if they exist, and an empty list if they don’t

Sample input
  lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
Sample output
  result = [1, 3, 7]

Time complexity - O(n)
"""


def find_duplicates(lst):
    """
    Function to find duplicates in a given lst
    :param lst: A list of integers
    :return: A list of duplicate integers with no repetition
    """

    result = []  # A list to store duplicates

    ht = {}
    for num in lst:
        # print(f"*** {num}")
        if ht.get(num):

            ht[num] = ht[num] + 1
            # print(f"getting added {ht}")
        else:

            ht[num] = 1
            # print(f"new number {ht}")

    for key, val in ht.items():
        if val > 1:
            result.append(key)

    return result


print(find_duplicates([1, 3, 1, 3, 5, 1, 4, 7, 7]))
