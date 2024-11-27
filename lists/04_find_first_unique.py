"""
Given a list nums, find the first nonrepeating integer in it.
"""


def find_first_unique(nums):
    for i in range(0, len(nums)):
        print(f"i = {i}")
        count = 0
        for j in range(0, len(nums)):
            if nums[i] == nums[j]:
                count = count + 1
                print(f"\t j {nums[j],  count}")
        if count == 1:
            return nums[i]

    return 0


print(find_first_unique([5, 5, 6, 6, 7]))
print(find_first_unique([4]))
