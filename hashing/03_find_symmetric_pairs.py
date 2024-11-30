"""
Given a list of pairs, nums, find all the symmetric pairs from it. If no symmetric pair is found, return an empty list.

Solution:
In this solution, we use a set to store the encountered pairs and check whether the symmetric pairs exist.

Here are the steps of the algorithm:

    1. Initialize an empty set, lookup, to store encountered pairs, and an empty list, result, to store symmetric pairs.

    2. Iterate through nums, and for each pair, check if the reverse of it exists in lookup.

        i. If the reverse exists, append the current pair and its reverse to the result list.

        ii. Otherwise, add the current pair to lookup.

    3. After iterating through nums, return the result containing symmetric pairs.

Time complexity

The time complexity of this solution is O(n), where n is the number of pairs in the list. This is because the list is
traversed only once, and the lookup operations in the set take constant time.

Space complexity

The space complexity of this solution is O(n) because we are using the set to store pairs, where n is the number of
pairs in the list.
"""
def find_symmetric(nums):
    res = []
    reverse_list = set()
    for pair in nums:

        if tuple(pair) in reverse_list: ## done in O(1) for sets
            res.append([pair[0], pair[1]])
            res.append([pair[1], pair[0]])
        else:
            reverse_list.add((pair[1], pair[0])) ## you can only add tup[les to sets


    return res

def main():
    test_cases = [
        [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]],
        [[1, 2], [2, 1], [3, 4], [5, 5], [6, 7]],
        [[1, 9], [9, 1]],
        [[1, 2], [3, 4], [5, 6]],
        [[-8, -4], [7, 7], [1, 1], [2, 2], [-4, -8]]
    ]
    i = 1
    for case in test_cases:
        print(i, ".\tInput list: ", case, sep="")
        symmetric = find_symmetric(case)
        print("\n\tSymmetric pairs: ", symmetric)
        print("-"*100)
        i+=1

if __name__ == "__main__":
    main()