"""
Given a list of integers, nums, and a positive integer, k, find the k largest elements in the list.



"""

from MaxHeap import MaxHeap


# Function to find the k largest elements from a list
def find_k_largest(nums, k):
    max_heap = MaxHeap()

    # Push all elements of the array into the max heap
    max_heap.buildHeap(nums)

    # Extract the k largest elements from the max heap

    k_largest = [max_heap.removeMax() for i in range(k)]

    return k_largest


# Driver code
def main():
    nums = [
        [3, 4, 6, 8, 2, 9],
        [10, -20, -40, -30, 50, -10, 90],
        [1, -2, 3, -4, 5, -6, 7],
        [90],
        [11, 41, 71, 91, 31],
    ]
    k = [3, 5, 7, 1, 5]

    for i in range(len(nums)):
        print(i + 1, ".\tList:", nums[i])
        print("\tK: ", k[i])
        print("\tK largest elements: ", find_k_largest(nums[i], k[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()
