"""
Given the head of a linked list and a target, value, return the updated linked list head after adding the target
value at the end of the linked list.
"""
from LinkedList import LinkedList
from Node import Node
from PrintList import print_list_with_forward_arrow


def insert_at_tail(head, val):
    temp = Node(val)
    if head is None:
        head = temp
    else:
        current = head
        while current.next is not None:
            current = current.next

        current.next = temp
    return head


def main():
    inputs = [
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4, -6],
        [3, 2, 1],
        [],
        [1, 2],
    ]

    values = [4, -5, 2, 0, -98]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])

        print(i + 1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)

        print("\n\tNew node to be added: ", values[i], sep="", end="")

        print("\n\tUpdated linked list: ", end="")
        print_list_with_forward_arrow(insert_at_tail(input_linked_list.head, values[i]))
        print("\n", "-" * 100, sep="")


if __name__ == "__main__":
    main()
