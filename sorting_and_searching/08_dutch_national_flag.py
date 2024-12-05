"""
Problem statement
Implement a function that sorts a list of 0s, 1s and 2s. This is called the Dutch National Flag Problem. Since the
number O can be represented by the blue color, 1 by the white color, and 2 as the red color, the task is to transform
the list input to the Dutch flag.

Try solving this problem in-place and in linear time without using any extra space.

Input
An array of 0s, 1s and 2s
Output
An array where the numbers 0s, 1s and 2s are sorted

Sample input
lst = [2, 0, 0, 1, 2, 1, 0]
Sample output
result = [0, 0, 0, 1, 1, 2, 2]

Solution:

This can be solved using the three-way partitioning or Dutch National Flag Algorithm. The idea is to use three pointers
to segregate the elements into three groups in one pass.

    Low pointer: This pointer will keep track of the boundary of the elements less than the middle value.
    Mid pointer: This will traverse through the array.
    High pointer: This will track the boundary of the elements greater than the middle value.

The key idea is:

    - If the current element is smaller than the middle value, it belongs to the "low" group, so we swap it with the
    element at the low pointer and move both the low and mid pointers forward.
    - If the current element is equal to the middle value, it is already in the right place, so we just move the mid
    pointer forward.
    - If the current element is greater than the middle value, it belongs to the "high" group, so we swap it with the
    element at the high pointer and move the high pointer backward.


Time Complexity: O(n) because each element is processed exactly once by the mid pointer.

"""


def dutch_national_flag(lst):
    low = 0
    mid = 0
    high = len(lst) - 1

    while mid <= high:
        if lst[mid] == 0:
            lst[low], lst[mid] = lst[mid], lst[low]
            low += 1
            mid += 1
        if lst[mid] == 2:
            lst[mid], lst[high] = lst[high], lst[mid]
            high -= 1
        if lst[mid] == 1:
            mid += 1

    return lst


if __name__ == "__main__":
    lst = [2, 0, 0, 1, 2, 1]

    print(dutch_national_flag(lst))
