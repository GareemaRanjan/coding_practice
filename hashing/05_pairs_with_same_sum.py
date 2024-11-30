"""
Given an array of distinct integers, nums, determine whether there exist two pairs, (a,b) and (c,d), such that a+b=c+d,
where a, b, c, and dbare unique elements within the array. If there are multiple solutions, return any one of them.

Time Complexity: O(n²)

"""


def find_pairs(nums):
    my_dict = (
        {}
    )  # Initialize an empty dictionary to store the sums and corresponding pairs

    # Step 1: Generate all possible pairs and store their sums
    for i in range(0, len(nums)):
        for j in range(
            i + 1, len(nums)
        ):  # Check all pairs of nums[i] and nums[j] where i < j
            # If this sum already exists in the dictionary, append the pair to the list
            if my_dict.get(nums[i] + nums[j]):
                my_dict.get(nums[i] + nums[j]).append([nums[i], nums[j]])
            else:
                my_dict[nums[i] + nums[j]] = [[nums[i], nums[j]]]

    # Step 2: Check the dictionary for sums that have exactly 2 pairs
    for key, value in my_dict.items():
        if len(value) == 2:  # If the sum occurs exactly twice, return those pairs
            return value
    return None  # Return None if no such sum is found


def main():
    # List of test cases
    nums_list = [
        [3, 4, 7, 1, 12, 9, 0],  # Example 1
        [1, 2, 3, 5, 8],  # Example 2
        [10, 20, 30, 40, 50, 60, 70, 5, 65, 15, 25],  # Example 3
        [-5, -3, -1, 0, 2, 4, 6],  # Example 4
        [0, 1, 2, 3, 4, 99],  # Example 5
    ]

    # Iterate through each test case
    for i, nums in enumerate(nums_list):
        print(f"{i + 1}.\tnums =  {nums}")
        result = find_pairs(nums)
        if result:
            print(f"\tFound pairs: {result}\n")
        else:
            print("\tNo matching pairs found.\n")
        print("-" * 100)


if __name__ == "__main__":
    main()
