"""
Implement a function sort_binary_list(lst) that takes a binary list of numbers and returns a sorted list.

Input
A list having binary numbers

Output
A sorted binary list

Sample input
lst = [1, 0, 1, 0, 1, 1, 0, 0]
Sample output
result = [0, 0, 0, 0, 1, 1, 1, 1]

Solution
There’s nothing tricky going on here. We are pushing all ones towards the right and all the zeros towards the left. For
this, we have maintained two variables i and j. The index i moves forward in the list and finds out if the element at
index i is zero. If it is, it swaps it with the element at index j. Index j is keeping track of the last position where
we have placed our last zero element in the list. As soon as we swap, we move the index j ahead to the next index, where
zero can be placed in the next swap.

Time complexity
Since the list is iterated only once, the time complexity is O(n).

"""


def sort_binary_list(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """

    j = 0

    for i in range(len(lst)):
        if lst[i] < 1:  # Swapping with jth element if the number is less than 1
            lst[i], lst[j] = lst[j], lst[i]  # Swapping
            j = j + 1

    return lst


# Driver to test above code
if __name__ == "__main__":
    lst = [1, 0, 1, 0, 1, 0, 1, 0]
    result = sort_binary_list(lst)

    print(result)
