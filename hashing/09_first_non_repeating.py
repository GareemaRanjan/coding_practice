"""
Given a list of integers, nums, find the first non-repeating integer in the list.

Time Complexity - O(n)
Space Complexity - O(n)
"""
import collections


def find_first_unique(nums):
    ht = dict()
    for num in nums:
        if ht.get(num):
            ht[num] += 1
        else:
            ht[num] = 1

    print(ht)

    for num in nums:
        if ht[num] == 1:
            return num
    return -1


def find_first_unique_collections(nums):
    counts = collections.OrderedDict()
    # Count occurrences of each number in the input list
    for num in nums:
        if num in counts:
            # Increment count if number is already in counts
            counts[num] += 1
        else:
            # Initialize count to 1 if number is not in counts
            counts[num] = 1
    # Iterate through the ordered dictionary to find the first unique number
    for num in counts:
        # If count is 1, it means the number is unique
        if counts[num] == 1:
            return num


def main():
    inputs = [
        [9, 2, 3, 2, 6, 6],
        [-5, -4, -4, 6, -1],
        [-1, 2, -1, -4, -10],
        [1, 1, 2, 9],
        [-2, 2, -2, 2, 5],
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tfirst unique number: ", find_first_unique(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
