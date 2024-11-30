"""
Given a list of integers nums and an integer target, k, find two numbers in the list that sum up to the target k.

There is exactly one solution for each input, and each element of the list can only be used once in the solution.
The order of the returned elements does not matter.

Solution:

The algorithm uses a dictionary to store the traversed values and their complements needed to reach k. We iterate
through the list and check if the complement of the current element is in the dictionary. If it is, we return the
current element and its complement as a pair that sums to k. Otherwise, we add the current element to the dictionary
for future lookups.

    - Initialize an empty dictionary, found_values, that will store the elements of the nums as keys.

    - Iterate through each element, num, in nums. For each element, perform the following steps:

        - Calculate the complement, which is k - num. The complement represents the value that, when added to num,
        gives the target sum k.

        - Check whether the complement is already in found_values. If it is, it means that num and its complement
        together form the target sum, k. In this case, return a pair of the complement and the current element,
        [complement, num].

        - If the complement is not found in found_values, add the current element num as a key to the dictionary with
        a corresponding value, 0. The value 0 doesn’t carry any significance; it’s just used to indicate that the
        element has been encountered.

Time complexity

The time complexity of this solution is O(n), where n is the number of elements in the list. This is because the list is
traversed only once, and the insertion and lookup operations into the dictionary take constant time.

Space complexity

The space complexity of this solution is O(n) because we are using the dictionary to store values, where n is the number
of elements in the list.

"""


def find_sum(nums, k):
    my_dict = {}
    for num in nums:
        comp = k - num
        if my_dict.get(comp):
            return [num, comp]
        else:
            my_dict[num] = comp
    return []


def main():
    inputs = [[1, 2, 3, 4], [1, 2], [2, 2], [-4, -1, -9, 1, -7], [25, 50, 75, 100, 400]]

    k = [5, 3, 4, -3, 425]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\tk: ", k[i], sep="")
        print("\n\tResult: ", find_sum(inputs[i], k[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
