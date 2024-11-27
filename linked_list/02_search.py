"""
Given the head of a singly linked list, search for a specific value. If the value is found, return TRUE; otherwise,
return FALSE.
"""
from LinkedList import LinkedList
from PrintList import print_list_with_forward_arrow


def search(head, value):
    current = head
    while current != None:
        if current.data == value:
            return True
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
        print("\n\tSearched value: ", value[i])
        print(
            "\n\tSingly linked list value found : ",
            search(input_linked_list.head, value[i]),
        )
        print("\n", "-" * 100)


if __name__ == "__main__":
    main()
