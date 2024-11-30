"""
Given two lists, determine whether or not they are disjoint.

Total Time Complexity:
The dominant factors are the time to convert the lists to sets (O(n1) and O(n2)) and the time to compute the intersection (O(min(n1, n2))).
Overall time complexity: O(n1 + n2), where n1 and n2 are the lengths of list1 and list2, respectively.
"""


def is_disjoint(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    intersect = set1.intersection(set2)

    if len(intersect) == 0:
        return True
    return False