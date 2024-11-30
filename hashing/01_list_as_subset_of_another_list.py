"""
Given two lists, list1 and list2, implement a function that takes the two lists as input and checks whether list2 is a subset of list1.

Total Time Complexity:
The dominant factors are the time to convert the lists to sets (O(n1) and O(n2)) and the time to compute the intersection (O(min(n1, n2))).
Overall time complexity: O(n1 + n2), where n1 and n2 are the lengths of list1 and list2, respectively.


"""


def is_subset(list1, list2):
    s1 = set(list1)
    s2 = set(list2)

    intersec = s1.intersection(s2)
    if len(intersec) == len(list2):
        return True
    return False


if __name__ == "__main__":
    list1 = [
        [9, 4, 7, 1, -2, 6, 5],
        [34, 19],
        [1, 2, 5, 0, 7, 4, 23],
        [-4, 6, 8, 1, 3, 14, 5, 7, 29],
        [52, 57, 23, -6, 22, -16, 78, 98, 46, 24, 19],
    ]
    list2 = [[7, 1, -2], [34], [], [14, -4, 29], [7, -6, 8, -4]]
    for i in range(len(list1)):
        print(i + 1, "\tList1:: ", list1[i])
        print("\tList2:: ", list2[i])
        result = is_subset(list1[i], list2[i])
        print("\tOutput:", result)
        print("-" * 100)
