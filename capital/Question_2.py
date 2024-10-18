# Question 2: Palindromic Transaction IDs
    # Imagine you are developing a financial reporting system that highlights notable transaction IDs for special analysis.
    # Specifically, you need to identify palindromic transaction IDs, i.e., those that read the same forward and backward.
    # Given an array of integers 'transactions', your task is to find all palindromic integers, sort them in descending order, and return the sorted array.
    # Example:
    # For transactions = [33, 123, 121, 44, 78, 98], the output should be [121, 44, 33].
    # Explanation:
    # - The palindromic integers in the transactions array are 33, 121, and 44.
    # - Sorting these in descending order gives [121, 44, 33].
    # For transactions = [123, 456, 789], the output should be [].
    # - Since there are no palindromic integers, the output is an empty list [].
def solution(transactions):
    # Check if a number is a palindrome
    palindromic_transactions = []
    for transaction in transactions:
        str_num = str(transaction)
        if str_num == str_num[::-1]:
            palindromic_transactions.append(transaction)

    # Sort the palindromic transactions in descending order
    palindromic_transactions.sort(reverse=True)

    return palindromic_transactions


# Example usage
print(solution([33, 123, 121, 44, 78, 98]))  # Output: [121, 44, 33]
print(solution([123, 456, 789]))  # Output: []
print(solution([111, 22, 343, 44, 55]))  # Output: [343, 111, 55, 44, 22]