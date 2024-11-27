"""
Given an unsorted list nums, find the sum of the maximum sum sublist. The maximum sum sublist is a list of contiguous
elements in nums for which the sum of the elements is maximum.

Solution
The maximum sublist sum problem inherently involves examining various sublists to check if their sum is maximized, and
the most convenient and efficient way to do this is using dynamic programming. The key idea is to efficiently find the
maximum sublist ending at any position based on the maximum sublist ending at the previous position.

In the context of this problem, we’ll use Kadane’s algorithm. It uses the bottom-up approach of dynamic programming to
solve subproblems iteratively, starting from the smallest subproblems and building up toward the larger problem. The
subproblem here is to find the maximum sublist sum that ends at a specific index i. We need to calculate this for every
index i in the array. The base case is the first element of the array, where both the current sublist sum and maximum
sublist sum are initialized with the first element’s value. This is the starting point for solving the subproblems. We
reuse the previously computed maximum sublist sum at each step to find the solution for the current subproblem.

The steps of the algorithm are given below:

    1. Initialize a curr_max variable to keep track of the maximum sum of the current list index and another
    global_max variable to keep track of the largest sum seen so far. Both variables will be initialized with the
    first element of nums.

    2. Traverse the list from the second element until the end of the list is reached.

    3. While traversing, if curr_max is less than 0, assign it the element at the current index. Otherwise, add the
    element at the current index to curr_max.

    4. Next, if global_max is less than curr_max, reassign it to curr_max.
"""


def find_max_sum_sublist(nums):
    if len(nums) < 1:
        return 0

    curr_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        if curr_max < 0:
            curr_max = nums[i]
        else:
            curr_max += nums[i]
        if global_max < curr_max:
            global_max = curr_max

    return global_max


# Driver code
def main():
    inputs = [
        [1, 2, 2, 3, 3, 1, 4],
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [-4, -1, -2, -1, -2],
        [-4, 2, -5, 1, 2, 3, 6, -5, 1],
        [25],
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\tMaximum Sum: ", find_max_sum_sublist(inputs[i]), sep="")
        print("-" * 75)


if __name__ == "__main__":
    main()
