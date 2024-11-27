"""
We're given a sorted list, nums, containing positive integers only. We have to rearrange the list so that when returned,
the 0th index of the list will have the largest number, the 1st index will have the smallest number, the 2nd index will
have the second largest number, the 3rd index will have the second smallest number, and so on.

In the end, we’ll have the largest remaining numbers in descending order and the smallest in ascending order at even
and odd positions, respectively.


"""


def rearrange_list(nums):
    res = [0] * len(nums)
    mid = len(nums) // 2

    dec = len(nums) - 1
    inc = 0
    index = 0
    for i in range(0, mid):
        res[index] = nums[dec]
        dec = dec - 1
        res[index + 1] = nums[inc]
        inc = inc + 1
        index = index + 2
    if len(nums) % 2 == 1:
        res[len(nums) - 1] = nums[mid]

    return res


print(rearrange_list([1, 2, 3, 4, 5, 6, 7]))
print(rearrange_list([1, 2, 3, 4, 5, 6, 7, 8]))
