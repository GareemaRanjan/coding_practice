"""
Given a list, nums, and an integer, k, rotate the list to the right by k positions so that each rotation involves
shifting the elements one position at a time.
"""


def right_rotate(nums, k):
    res = [0] * len(nums)
    for i in range(0, len(nums)):
        res[(i + k) % len(nums)] = nums[i]

    return res


print(right_rotate([10, 20, 30, 40, 50], 3))
