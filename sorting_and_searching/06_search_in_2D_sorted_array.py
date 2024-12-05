"""
Implement a function that tells whether a given number is present in a row-wise and column wise sorted 2D list or not.

Input
A sorted 2D list and the number that needs to be checked if it is present or not

Output
Return True if the target number is found and False otherwise

Sample input
2D_list  =[[10, 11, 12, 13],
           [14, 15, 16, 17],
           [27, 29, 30, 31],
           [32, 33, 39, 50]]

number = 30
Sample output
result = True

Time complexity - O(n+m)
Time complexity binary - O(log m + log n)
"""


def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    # Write your code here!

    row = -1
    for i in range(0, len(lst) - 1):
        if lst[i][0] <= number and lst[i + 1][0] > number:
            row = i
            break

    print(row)
    if row == -1:
        row = len(lst) - 1

    for j in lst[row]:
        if j == number:
            return True

    return False


def find_in_binary(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    # Total number of rows
    rows = len(lst)

    # If list has no rows
    if lst is None:
        return False

    # Total Number of cols
    cols = len(lst[0])

    # If list has no cols
    if cols == 0:
        return False

    i = 0
    j = rows - 1

    if rows > 1:
        while i <= j:
            mid = i + (j - i) // 2
            if number == lst[mid][cols - 1]:
                return True

            if number > lst[mid][cols - 1]:
                i = mid + 1
            else:
                j = mid - 1

        if number > lst[mid][cols - 1]:
            rows = mid + 1
        else:
            rows = mid
    else:
        rows = 0

    if rows >= len(lst):
        return False

    i = 0
    j = cols - 1

    while i <= j:
        mid = i + (j - i) // 2
        if number == lst[rows][mid]:
            return True

        if number > lst[rows][mid]:
            i = mid + 1
        else:
            j = mid - 1

    return False


print(
    find_in(
        [[10, 11, 12, 13], [14, 15, 16, 17], [27, 29, 30, 31], [32, 33, 39, 50]], 30
    )
)

print(
    find_in(
        [[10, 11, 12, 13], [14, 15, 16, 17], [27, 29, 30, 31], [32, 33, 39, 50]], 300
    )
)

print(
    find_in(
        [[10, 11, 12, 13], [14, 15, 16, 17], [27, 29, 30, 31], [32, 33, 39, 80]], 10
    )
)
print(
    find_in(
        [[10, 11, 12, 13], [14, 15, 16, 17], [27, 29, 30, 31], [32, 33, 39, 80]], 80
    )
)
