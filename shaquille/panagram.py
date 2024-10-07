"""
Question 2:
A string is a pangram if it contains all letters of the English alphabet, ascii['a'-'z']. Given a list of strings,
determine if each one is a pangram or not. Return "1" if true and "0" if false.

Example:
pangram = ['pack my box with five dozen liquor jugs', 'this is not a pangram']

- The string 'pack my box with five dozen liquor jugs' is a pangram because it contains all the letters 'a' through 'z'.
- The string 'this is not a pangram' is not a pangram.
- Assemble a string of the two results, in order. The result is '10'.

Function Description:
Complete the function isPangram in the editor below.

isPangram has the following parameter(s):
- string pangram[n]: the sentences to check.

Returns:
- string: a string where each position represents the results of a test. Use '1' for true and '0' for false.

Constraints:
- 1 <= n <= 100
- Each string pangram[i] (where 0 <= i < n) is composed of lowercase letters and spaces.
- 1 <= length of pangram[i] <= 10^5
"""


def isPangram(pangram):
    result = []
    all_chars = set("abcdefghijklmnopqrstuvwxyz")

    for sentence in pangram:
        # Create a set of characters from the current sentence, ignoring spaces
        sentence_chars = set(sentence.replace(" ", ""))

        # Check if all characters from 'a' to 'z' are present in the sentence
        if all_chars.issubset(sentence_chars):
            result.append("1")
        else:
            result.append("0")

    # Join the result list into a string and return
    return "".join(result)
