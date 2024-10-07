"""
Question:
The current selected programming language is Python3. We emphasize the submission of a fully working code over partially
correct but efficient code. Use of certain header files are restricted. Once submitted, you cannot review this problem
again. You can use print to debug your code. The print may not work in case of syntax/runtime error. The version of
Python being used is 3.5.2.

A pilot was asked to drop food packets in a terrain. He must fly over the entire terrain only once but cover a maximum
number of drop points. The points are given as inputs in the form of integer co-ordinates in a two-dimensional field.
The flight path can be horizontal or vertical, but not a mix of the two or diagonal.

Write an algorithm to find the maximum number of drop points that can be covered by flying over the terrain once.

Input:
- The first line of input consists of an integer - xCoordinate_size, representing the number of x coordinates (N).
- The next line consists of N space-separated integers representing the x coordinates.
- The third line consists of an integer - yCoordinate_size, representing the number of y coordinates (M).
- The next line consists of M space-separated integers representing the y coordinates.

Output:
Print an integer representing the number of coordinates in the best path which covers the maximum number of drop points
by flying over the terrain once.

Note:
- A path is valid if more than one drop point is connected (single coordinate does not create any path, so the pilot
cannot fly over it).

Constraints:
- 1 <= N, M <= 700 (where N is always equal to M)

Example:
Input:
5
2 3 2 4 5
2 2 6 5 8
Output:
3

Explanation:
There are 5 coordinates: (2,2), (3,2), (2,6), (4,5), and (2,8).
The best path is the horizontal one covering (2,2), (2,6), and (2,8).
So, the output is 3.
"""


def max_drop_points(x_coords, y_coords):
    # Create dictionaries to count occurrences of each x and y coordinate
    x_count = {}
    y_count = {}

    # Count occurrences manually for x coordinates
    for x in x_coords:
        if x in x_count:
            x_count[x] += 1
        else:
            x_count[x] = 1

    # Count occurrences manually for y coordinates
    for y in y_coords:
        if y in y_count:
            y_count[y] += 1
        else:
            y_count[y] = 1

    max_x_coverage = 0
    max_y_coverage = 0

    for count in x_count.values():
        if count > 1:
            max_x_coverage = max(max_x_coverage, count)

    for count in y_count.values():
        if count > 1:
            max_y_coverage = max(max_y_coverage, count)

        # The result is the maximum coverage in either direction
    return max(max_x_coverage, max_y_coverage)
