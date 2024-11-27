"""
Given the head of a singly linked list, find the length of the linked list.
"""
from LinkedList import LinkedList
from Node import Node
from PrintList import print_list_with_forward_arrow


def length(head):
    current = head
    count = 0
    if head is None:
        return 0
    while current is not None:
        count = count + 1
        current = current.next

    return count


def main():
    inputs = [
        [10, 20, 30, 40, 50],
        [-1, -2, -3, -4, -5, -6],
        [3, 2, 1],
        [],
        [12],
    ]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])
        if len(inputs[i]) == 0:
            print(i + 1, ".\tInput linked list: null", sep="", end="")
        else:
            print(i + 1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tLength of linked list: ", end="")
        print(length(input_linked_list.head))
        print("\n", "-" * 100)


if __name__ == "__main__":
    main()
