"""
Given the head of a linked list, return the n th node from the end of the linked list.
"""
from LinkedList import LinkedList
from Node import Node
from PrintList import print_list_with_forward_arrow


def find_nth(head, n):
    current = head
    count = 1
    while current is not None:
        val = current.data
        # print(f"val = {val}")
        if count == n:
            # print(f"found element at n = {n}, coiunt = {count}, val = {val}")
            return current
        count += 1
        current = current.next

    return None


def main():
    input_data = (
        [7, 10, 14, 21, 22],
        [3, 6, 9, 12],
        [23, 19, 15, 22, 34, 76, 12],
        [5],
        [1, 3, 5, 7, 9, 11, 6],
    )
    n = [4, 2, 6, 1, 3]
    for i in range(len(input_data)):
        index = n[i]
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_data[i])
        print("{0}.\tInput linked list: ".format(i + 1), end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tn: ", index)
        print("\n\tNode returned:", find_nth(input_linked_list.head, index).data)
        print("-" * 100)


if __name__ == "__main__":
    main()
