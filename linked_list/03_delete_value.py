"""
Given the head of a singly linked list and a value to be deleted from the linked list, if the value exists in the linked
list, delete the value and return TRUE. Otherwise, return FALSE.
"""
from LinkedList import LinkedList
from PrintList import print_list_with_forward_arrow
from Node import Node


def delete(head, value):
    current = head
    if head is not None:
        if current.data == value:
            temp = head
            head = head.next
            temp.next = None
            print_list_with_forward_arrow(head)
            return True

        prev = current
        current = current.next
        while current is not None:
            if value == current.data:
                prev.next = current.next
                current.next = None
                print_list_with_forward_arrow(head)
                return True
            prev = current
            current = current.next

    return False


def main():
    inputs = [
        [10, 20, 30, 40, 50],
        [-1, -2, -3, -4, -5, -6],
        [3, 2, 1],
        [],
        [12],
    ]
    value = [50, -7, 3, 55, 12]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])
        if len(inputs[i]) == 0:
            print(i + 1, ".\tInput linked list: null", sep="", end="")
        else:
            print(i + 1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tTo be deleted value: ", value[i])
        print("\n\tDeleted : ", delete(input_linked_list.head, value[i]))
        print("\n", "-" * 100)


if __name__ == "__main__":
    main()
