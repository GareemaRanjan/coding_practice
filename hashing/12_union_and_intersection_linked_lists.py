"""
Time complexity

The time complexity of the union operation is O(n+m+k), where n and m are the lengths of the input linked lists,
and k is the number of common elements between them.
"""

from linked_list.LinkedList import LinkedList
from linked_list.PrintList import (
    print_list_with_forward_arrow,
    print_list_with_forward_arrow_loop,
)


# class LinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


def get_set(head):
    my_set = set()
    current = head
    while current is not None:
        my_set.add(current.data)
        current = current.next
    return my_set


def union(head1, head2):
    u_set = get_set(head1).union(get_set(head2))
    result = LinkedList()
    for item in u_set:
        result.insert_at_head(item)
    return result.head


def intersection(head1, head2):
    i_set = get_set(head1).intersection(get_set(head2))
    result = LinkedList()
    for item in i_set:
        result.insert_at_head(item)
    return result.head


def main():
    union_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 1, 2, 2, 3, 3, 4, 4, 5],
        [-45, 34, -54, 45, -65, 54],
        [12],
        [0, 1, 2],
    ]

    intersection_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 1, 2],
        [1, 1, 2, 2, 3, 3, 4, 4, 5],
        [-45, 34, -54, 45, -65, 54],
        [12],
    ]

    input_list2 = [
        [7, 8, 9, 10, 11, 12, 13, 14],
        [1, 3, 4, 1],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [12],
    ]

    for i in range(len(union_list)):
        input_linked_list1 = LinkedList()
        input_linked_list2 = LinkedList()
        input_linked_list3 = LinkedList()

        input_linked_list1.create_linked_list(union_list[i])
        input_linked_list2.create_linked_list(intersection_list[i])
        input_linked_list3.create_linked_list(input_list2[i])

        print(i + 1, ".\tInput linked list 1: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list1.head)

        print("\n\tInput linked list 2: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list3.head)

        print("\n\n\tUnion: ", end="")
        print_list_with_forward_arrow(
            union(input_linked_list1.head, input_linked_list3.head)
        )

        print("\n\tIntersection: ", end="")
        print_list_with_forward_arrow(
            intersection(input_linked_list2.head, input_linked_list3.head)
        )
        print("\n", "-" * 100)


if __name__ == "__main__":
    main()
