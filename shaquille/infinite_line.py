"""
Question:
Given an infinite number line, you would like to build a few blocks and obstacles on it. Specifically, you have to
implement code which supports two types of operations:

1. [1, x] - builds an obstacle at coordinate `x` along the number line. It is guaranteed that coordinate `x` does not
contain any obstacles when the operation is performed.

2. [2, x, size] - checks whether it's possible to build a block of size `size` beginning at position `x`. For example,
for `size = 2` and `x = 0`, it will check `0` and `1` on the number line for obstacles. Returns `1` if it is possible,
i.e. there are no obstacles at the occupied coordinates, and returns `0` otherwise. Please note that this operation does
not actually build the block, it only checks whether a block can be built.

Given an array of `operations` containing both types of operations above, your task is to return a binary string
representing the outputs for all `[2, x, size]` operations.

Example:
For
    operations = [
        [1, 2],
        [1, 5],
        [2, 3, 2],
        [2, 3, 3],
        [2, 1, 1],
        [2, 1, 2]
    ],
the output should be `solution(operations) = "1010"`.

Explanation:
- `[1, 2]` - builds an obstacle at coordinate `2`.
- `[1, 5]` - builds an obstacle at coordinate `5`.
- `[2, 3, 2]` - checks and returns `"1"` as it is possible to build a block occupying coordinates `3` and `4`.
- `[2, 3, 3]` - checks and returns `"0"` as it is not possible to build a block occupying coordinates `3`, `4`, and `5`,
because there is an obstacle at coordinate `5`.
- `[2, 1, 1]` - checks and returns `"1"` as it is possible to build a block occupying coordinate `1`.
- `[2, 1, 2]` - checks and returns `"0"` as it is not possible to build a block occupying coordinates `1` and `2`
because there is an obstacle at coordinate `2`.

The output is `"1010"`.
"""


def solution(operations):
    obstacles = set()
    result = []

    # Maintain a list to keep track of obstacle positions in sorted order
    obstacle_list = []

    for operation in operations:
        if operation[0] == 1:
            # Add obstacle at coordinate x
            _, x = operation
            if x not in obstacles:
                obstacles.add(x)
                # Insert obstacle in sorted order (using binary insertion)
                from bisect import insort

                insort(obstacle_list, x)
        elif operation[0] == 2:
            # Check if we can build a block of size `size` starting from `x`
            _, x, size = operation
            end = x + size - 1

            # Use binary search to efficiently check if there are obstacles in the range [x, end]
            from bisect import bisect_left, bisect_right

            left_index = bisect_left(obstacle_list, x)
            right_index = bisect_right(obstacle_list, end)

            # If there are any obstacles in the range, we can't build
            if left_index < right_index:
                result.append("0")
            else:
                result.append("1")

    return "".join(result)


# Example usage
operations = [[1, 2], [1, 5], [2, 3, 2], [2, 3, 3], [2, 1, 1], [2, 1, 2]]

print(solution(operations))  # Output should be "1010"
