"""
Given an unsorted list lst and an integer k, find the k smallest elements from the list using a Heap.

Solution
The solution involves populating a MinHeap with the elements from lst. The smallest element in the MinHeap is removed
k times, and the resulting list is returned.

Here are the steps of this solution:

    1. Initialize a MinHeap.

    2. Initialize an empty result list.

    3. Populate MinHeap with elements from lst.

    4. Remove the smallest element from MinHeap and append it to result.

    5. Finally, return result.

Time complexity

The time complexity of the solution is O(k×log(n)), where n is the number of elements in the list. This is because
populating the MinHeap takes O(n) time, and removing a minimum element from the MinHeap takes O(log(n)) time. Because
we remove the minimum element k times, the resulting time complexity is O(k×log(n)) + O(n) which reduces to O(k×log(n)).

Space complexity

The space complexity is O(n), where n is the number of elements in the list because all elements from the list are
stored in the MinHeap.
"""

from MinHeap import MinHeap


def find_k_smallest(lst, k):
    heap = MinHeap()  # Create a minHeap
    # Populate the minHeap with lst elements
    heap.buildHeap(lst)
    # Create a list of k elements such that:
    # It contains the first k elements from
    # removeMin() function
    kSmallest = [heap.removeMin() for i in range(k)]
    return kSmallest


def main():
    inputs = [
        [3, 2, 41, 3, 34],
        [-5, -4, -3, -2, -1],
        [-1, 2, 3, -4, -10],
        [1, 2],
        [-3],
    ]

    k = [3, 4, 2, 1, 1]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tk: ", k[i], sep="")
        print("\n\tFinal list: ", find_k_smallest(inputs[i], k[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
