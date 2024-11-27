"""
Given a list of integers, nums, and an integer target, k, find two numbers in the list that sum up to the target k.

There is exactly one solution for each input, and each element of the list can only be used once in the solution.
The order of the returned elements does not matter.
"""


def find_sum(nums, k):
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                return [nums[i], nums[j]]

    return [0, 0]


def find_sum_two_pointer(nums, k):
    nums.sort()

    left = 0
    right = len(nums) - 1

    result = []

    # Iterate until the pointers meet
    while left < right:
        # Calculate the sum of the current pair
        sum_val = nums[left] + nums[right]

        # If the sum is less than the target sum, move the left pointer to the right
        if sum_val < k:
            left += 1
        # If the sum is greater than the target sum, move the right pointer to the left
        elif sum_val > k:
            right -= 1
        # If the sum equals the target sum, add the pair to the result list and break the loop
        else:
            result.append(nums[left])
            result.append(nums[right])
            break

    return result


find_sum([1, 10, 8, 4, 9], 17)
