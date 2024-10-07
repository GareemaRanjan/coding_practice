"""
Question:
You are given an array of numbers, with each being a 0 or 1. All 1s are arranged at the beginning of the array and 0s
stand at the end.

A process is executed on this array until it halts. You are given a variable `zerosToOne`, which represents the number
of 0s that can be deleted and exchanged for one 1.

Each second, one of the three events happens:
- Option 1: If there are at least `zerosToOne` zeros, then the last `zerosToOne` zeros are removed and one 1 is added
at the beginning of the array.
- Option 2: If there is at least one 1, the last 1 changes to 0.
- Option 3: If neither Option 1 nor Option 2 can be completed, then the process halts.

Follow the process and compute how many seconds will pass until the process halts. Refer to the examples below for
better understanding.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than
`O(numbers.length × zerosToOne^2)` will fit within the execution time limit.

Examples:
Example 1:
- For `numbers = [1, 1, 1, 0, 0, 0, 0]` and `zerosToOne = 2`, the output should be `13`.
    Explanation:
    - At the beginning, `numbers = [1, 1, 1, 0, 0, 0, 0]`.
    - After the 1st second, `numbers = [1, 1, 1, 0, 0, 0]`.
    - After the 2nd second, `numbers = [1, 1, 1, 0, 0]`.
    - After the 3rd second, `numbers = [1, 1, 1, 0]`.
    - After the 4th second, `numbers = [1, 1, 1]`.
    - After the 5th second, `numbers = [1, 1, 0]`.
    - After the 6th second, `numbers = [1, 1]`.
    - After the 7th second, `numbers = [1, 0]`.
    - After the 8th second, `numbers = [1]`.
    - After the 9th second, `numbers = [0]`.
    - After the 10th second, `numbers = []`.
    - After the 11th second, `numbers = [0]`.
    - After the 12th second, `numbers = [1]`.
    - After the 13th second, `numbers = [0]`.
    - After 13 seconds, the process halts, hence the answer is `13`.

Example 2:
- For `numbers = [1, 1]` and `zerosToOne = 2`, the output should be `4`.
    Explanation:
    - At the beginning, `numbers = [1, 1]`.
    - After the 1st second, `numbers = [1, 0]`.
    - After the 2nd second, `numbers = [0, 0]`.
    - After the 3rd second, `numbers = [1]`.
    - After the 4th second, `numbers = [0]`.
    - After 4 seconds, the process halts, hence the answer is `4`.

Example 3:
- For `numbers = [0, 0, 0]` and `zerosToOne = 3`, the output should be `2`.
    Explanation:
    - At the beginning, `numbers = [0, 0, 0]`.
    - After the 1st second, `numbers = [1]`.
    - After the 2nd second, `numbers = [0]`.
    - After 2 seconds, the process halts, hence the answer is `2`.
"""


def solution(numbers, zerosToOne):
    seconds = 0
    while True:
        # Count the number of 0's and 1's in the list
        count_zeros = numbers.count(0)
        count_ones = len(numbers) - count_zeros

        # Option 1: Replace zerosToOne zeros with one 1
        if count_zeros >= zerosToOne:
            # Remove zerosToOne zeros from the end and add one 1 at the beginning
            numbers = [1] + numbers[:-zerosToOne]
        # Option 2: Convert the last 1 to a 0
        elif count_ones >= 1:
            # Change the last 1 to a 0
            for i in range(len(numbers) - 1, -1, -1):
                if numbers[i] == 1:
                    numbers[i] = 0
                    break
        # Option 3: Halt the process
        else:
            break

        # Increment the seconds counter
        seconds += 1

    return seconds


# Example test cases
print(solution([1, 1, 0, 0, 0], 2))  # Output: 13
print(solution([1, 1], 2))  # Output: 4
print(solution([0, 0, 0], 3))  # Output: 2
