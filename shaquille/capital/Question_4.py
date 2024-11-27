# You are given an array called 'operations' which contains instructions of two types:
# 1. Type [0, a, b]: Create and save a rectangle of size a x b.
# 2. Type [1, a, b]: Check if a box of size a x b can fit inside any of the earlier saved rectangles.
#    - It is possible to rotate the box or the saved rectangles by 90 degrees.
#    - This means you need to check both dimensions (a x b) and (b x a) to see if it fits.
# The task is to return an array of boolean values representing the results for each type [1, a, b] operation.
# The results should indicate whether the box can fit inside one of the previously stored rectangles.

# Example 1:
# operations = [[1, 1, 1]]
# There are no rectangles created before this check, so the output is [True].
# This is because there's no rectangle that the box was "unable to fit inside" (implying there is nothing it couldn't fit in).

# Example 2:
# operations = [[0, 100000, 100000]]
# A rectangle of size 100000 x 100000 is created.
# Since there are no further checks, the answer is an empty array [] as there is nothing to check.

# Example 3:
# operations = [[0, 3, 3], [0, 5, 2], [1, 3, 2], [1, 3, 4]]
# - A rectangle of size 3 x 3 is created.
# - A rectangle of size 5 x 2 is created.
# - The first check is for a box of size 3 x 2 to see if it can fit in any saved rectangle.
#   Since it can fit inside the 5 x 2 rectangle, the output for this check is True.
# - The second check is for a box of size 3 x 4. It cannot fit inside any of the saved rectangles, so the output is False.
# Expected output: [True, False]
def solution(operations):
    saved_rectangles = []
    result = []

    for op in operations:
        if op[0] == 0:
            # Save the rectangle with sorted sides
            a, b = op[1], op[2]
            s_small = min(a, b)
            s_large = max(a, b)
            saved_rectangles.append((s_small, s_large))
        elif op[0] == 1:
            # Check if the box can fit into all saved rectangles
            a, b = op[1], op[2]
            w_small = min(a, b)
            w_large = max(a, b)

            if not saved_rectangles:
                # By definition, it fits when there are no saved rectangles
                result.append('true')
            else:
                can_fit = True
                for s_small, s_large in saved_rectangles:
                    if w_small > s_small or w_large > s_large:
                        can_fit = False
                        break
                result.append(str(can_fit).lower())

    return result


# Test cases
operations_list = [
    # Test case 1: No rectangles stored, only query
    [[1, 1, 1]],  # Expected output: [True]

    # Test case 2: One large rectangle, no queries
    [[0, 100000, 100000]],  # Expected output: []

    # Test case 3: Multiple rectangles with queries
    [[0, 3, 3], [0, 5, 2], [1, 3, 2], [1, 2, 4]],  # Expected output: [True, False]

    # Test case 4: Rotated fitting
    [[0, 4, 2], [1, 2, 4], [1, 4, 2]],  # Expected output: [True, True]

    # Test case 5: Multiple queries, no fit
    [[0, 2, 2], [1, 3, 3], [1, 2, 3]],  # Expected output: [False, False]

    # Test case 6: Exact fit
    [[0, 5, 5], [1, 5, 5]],  # Expected output: [True]

]

for i, operations in enumerate(operations_list, 1):
    print(f"Test case {i}: {solution(operations)}")