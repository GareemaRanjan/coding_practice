"""
Merge sort is a recursive divide & conquer algorithm that essentially divides a given list into two halves, sorts those
halves, and merges them in order. The base case is to merge two lists of size 1 so, eventually, single elements are
merged in order; the merge part is where most of the heavy lifting happens.

Time complexity
The time complexity of merge sort is nlog(n).
"""


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":

    lst = [3, 2, 1, 5, 4]
    merge_sort(lst)

    print("Sorted list is: ", lst)
