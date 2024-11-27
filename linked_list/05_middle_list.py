"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node. This happens when the length of the list is even, and the
second middle node occurs at length/2. Otherwise, if the length of the list is odd, the middle node occurs at
(length/2) + 1.
"""

from LinkedList import LinkedList
from PrintList import print_list_with_forward_arrow


def find_mid(head):
    node = head
    mid = 0

    mid = length(head) // 2 + 1

    for i in range(mid - 1):
        node = node.next

    return node


def find_mid_two_pointer(head):
    mid_node = head
    fast_pointer = head
    # Move mid_node (slower) one step at a time and fast_pointer (faster) two steps at a time
    while fast_pointer and fast_pointer.next:
        mid_node = mid_node.next
        fast_pointer = fast_pointer.next.next
    return mid_node


def length(head):
    # Start from the first element
    curr = head
    length = 0

    # Traverse the list and count the number of nodes
    while curr is not None:
        length += 1
        curr = curr.next
    return length


def main():
    input = (
        [7, 10, 14, 21, 22],
        [3, 6, 9, 12],
        [23, 19, 15, 22, 34, 76, 12],
        [5],
        [1, 3, 5, 7, 9, 11, 6],
    )

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(i + 1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tMiddle Node: ", end="")
        print(find_mid(input_linked_list.head).data)
        print("-" * 100)


if __name__ == "__main__":
    main()
