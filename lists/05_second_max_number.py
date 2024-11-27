"""
Given a list of integers, nums, find the second maximum value from the list.
"""


def find_second_maximum(nums):
    first = -100000
    second = -100000
    for i in range(0, len(nums)):
        ele = nums[i]
        if ele > first:
            second = first
            first = ele
        elif ele > second and ele != first:
            second = ele

        print(f"first = {first}, second = {second}")

    return second


print(find_second_maximum([4, 2, 1, 5, 0]))
print(find_second_maximum([2, 9, 5, 4, 0]))
print(find_second_maximum([4, 10, 10, 8, 9]))
