"""
Question:
Imagine you are developing a sophisticated text processing tool editors use to format lists of words for publication
quickly. You are given an array of strings `wordsList`. Your tool needs to automatically adjust the format of each word
based on its length:
- If the length of a string is even, the word should be reversed.
- If the length of a string is odd, the word should be converted to uppercase.

Your task is to write a function that processes the input array `wordsList` according to these rules and returns a new
array where each string has been formatted correctly.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than
`O(wordsList.length * max(wordsList[i].length)^2)` will fit within the execution time limit.

Example:
- For `wordsList = ["HeLLo", "Data", "science"]`, the output should be `solution(wordsList) = ["HELLO", "ataD",
"SCIENCE"]`.

Explanation:
- `"HeLLo"` has an odd length, so it is converted to uppercase: `"HELLO"`.
- `"Data"` has an even length, so it is reversed: `"ataD"`.
- `"science"` has an odd length, so it is converted to uppercase: `"SCIENCE"`.
"""


def solution(wordsList):
    result = []
    for word in wordsList:
        if len(word) % 2 == 0:
            # If length is even, reverse the word
            result.append(word[::-1])
        else:
            # If length is odd, convert the word to uppercase
            result.append(word.upper())
    return result


# Example test case
print(solution(["HeLLo", "Data", "science"]))  # Output: ["HELLO", "ataD", "SCIENCE"]
