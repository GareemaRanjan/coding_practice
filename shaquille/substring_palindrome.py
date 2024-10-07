"""
Question:
The current selected programming language is Python3. We emphasize the submission of a fully working code over partially
correct but efficient code. Use of certain header files are restricted. Once submitted, you cannot review this problem
again. You can use print to debug your code. The print may not work in case of syntax/runtime error. The version of
Python being used is 3.5.2.

Ray likes puzzles. One day, he challenged Ansh with a puzzle to find a string that is the same when read forwards and
backwards.

Write an algorithm to find the sub-string from the given string that is the same when read forwards and backwards.

Input:
The input consists of a string - inputStr, representing the given string for the puzzle.

Output:
From the given string, print a sub-string which is the same when read forwards and backwards.

Note:
- If there are multiple sub-strings of equal length, choose the lexicographically smallest one.
- If there are multiple sub-strings of different length, choose the one with maximum length.
- If there is no sub-string that is the same when read forwards and backwards, print "None".
- Sub-string is only valid if its length is more than 1.
- Strings only contain uppercase characters (A-Z).

Examples:
Example 1:
Input: YABCCBAZ
Output: ABCCBA
Explanation: Given string is "YABCCBAZ", in this only sub-string which is the same when read forward and backward is
"ABCCBA".

Example 2:
Input: ABC
Output: None
Explanation: Given string is "ABC", and no sub-string is present which is the same when read forward and backward.
So, the output is "None".
"""


def is_palindrome(s):
    # Check if the given string is the same forwards and backwards
    return s == s[::-1]


def find_longest_palindrome(inputStr):
    n = len(inputStr)
    longest_palindrome = "None"

    # Loop over each possible starting point of the substring
    for start in range(n):
        # Loop over each possible ending point of the substring (ensure length > 1)
        for end in range(start + 2, n + 1):
            substring = inputStr[start:end]
            # If the substring is a palindrome and longer than the current longest, update it
            if is_palindrome(substring):
                if longest_palindrome == "None":
                    longest_palindrome = substring
                elif len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
                elif (
                    len(substring) == len(longest_palindrome)
                    and substring < longest_palindrome
                ):
                    longest_palindrome = substring

    return longest_palindrome
