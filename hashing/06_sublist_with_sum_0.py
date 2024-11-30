"""
Given a list containing both positive and negative integers, determine if there exists a sublist of consecutive elements
whose elements sum to zero. Return TRUE if such a sublist exists; otherwise, return FALSE.

Solution:
We can utilize a hash table to track cumulative sums while iterating through the input list. At each iteration, we check
for three conditions: if the current element is zero, if the cumulative sum up to the current point is zero, or if the
same cumulative sum has been encountered previously. If any of these conditions are met, we return TRUE, indicating the
presence of a sublist whose sum is zero. Otherwise, return FALSE, indicating that no such sublist exists.

The steps of the algorithm are given below:

    1. Iterate through the elements of the input list lst.
    2. While iterating, maintain a total_sum variable, which keeps track of the cumulative sum of elements encountered
    so far.
    3. Initialize a hash table ht, to store the cumulative sums encountered along with their corresponding indices. The
    key here will represent the cumulative sum, and the value will represent the index of the element in lst.
    4. As you traverse each element, elem, in lst, update total_sum by adding the elem to it.
    5. At each iteration, return True if any of these conditions are met:
        i.The current element is 0.
        ii.The cumulative sum is 0.
        iii.The cumulative sum has been encountered before.
    6. Store the current total_sum and its index in ht if none of the conditions are met during the iteration.
    7. Return FALSE if the loop completes without finding any sublist with a sum of zero, indicating no such sublist
    exists in the list.

Time complexity

The time complexity of the algorithm is O(n), where n is the number of elements in the input list. This is because the
algorithm iterates over the list exactly once.

Space complexity

The space complexity of the algorithm is O(n), where n is the number of elements in the input list. In the worst case,
it will have all the elements in it.

"""
def find_sub_zero(lst):
    ht = dict()
    total_sum = 0

    for elem in lst:
        print(ht)
        total_sum += elem
        if elem == 0 or total_sum == 0 or ht.get(total_sum) != None:
            print(elem, total_sum)
            return True
        ht[total_sum] = elem

    return False


def main():
    inputs = [[10, 4, 10, -56, 23, 7, 2, -2, 9],
              [-3, 3],
              [2, -5, -4, 43, 2],
              [-7, 1, 2, 5, -6, 1, -3, 3, -17],
              [25, 50, 75, 100, 400],
              [2, -3, -2, 4, -3, 1, 6, -6, 7, 8]]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tResult: ", find_sub_zero(inputs[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()
