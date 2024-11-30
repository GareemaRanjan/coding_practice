"""
Given the head of a linked list, check whether or not a cycle is present in the linked list. A cycle is present in a
linked list if at least one node can be reached again by traversing the next pointer. If a cycle exists, return TRUE,
otherwise return FALSE.

Solution:

The algorithm uses a set to track visited nodes while traversing the linked list, returning true if a repeated node is
encountered (indicating a cycle) and false otherwise.

The steps of the algorithm are given below:

    - Initialize a set visited to store the nodes that have been visited.

    - Initialize a pointer current to the head of the linked list.

    - Traverse the linked list using the current pointer until current becomes NULL (reaches the end of the list).
    While traversing, perform the following steps:

        - Check if the current is already in the visited set. If it is, this indicates that there is a cycle in the linked list, so return TRUE.

        - If the current is not in the visited set, add the current to the set.

        - Move current to the next node in the linked list (current = current.next) to proceed to the next iteration.

    - If the traversal completes without finding a repeated node (i.e., current becomes NULL), it means there is no
    cycle in the linked list and returns FALSE.

Time complexity

The time complexity of this solution is O(n), where n is the number of elements in the linked list. This is because the
entire linked list is traversed once to check for a cycle, and the lookup operations in the set take constant time.

Space complexity

The space complexity of this solution is O(n) because we are using the set to store the elements, where n is the number
of elements in the linked list.

"""
from linked_list.LinkedList import LinkedList
from linked_list.PrintList import (
    print_list_with_forward_arrow,
    print_list_with_forward_arrow_loop,
)


def detect_cycle(head):
    current = head
    visited = set()
    while current is not None:
        if current.data in visited:
            return True
        else:
            visited.add(current.data)
        current = current.next

    return False


def main():
    input = (
        [2, 4, 6, 8, 10, 12],
        [1, 3, 5, 7, 9, 11],
        [0, 1, 2, 3, 4, 6],
        [3, 4, 7, 9, 11, 17],
        [5, 1, 4, 9, 2, 3],
    )
    pos = [0, -1, 1, -1, 2]
    j = 1

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(f"{j}.\tInput: ", sep="", end="")
        if pos[i] == -1:
            print_list_with_forward_arrow(input_linked_list.head)
        else:
            print_list_with_forward_arrow_loop(input_linked_list.head)
        print("\n\tPosition:", pos[i])
        if pos[i] != -1:
            length = input_linked_list.get_length(input_linked_list.head)
            last_node = input_linked_list.get_node(input_linked_list.head, length - 1)
            last_node.next = input_linked_list.get_node(input_linked_list.head, pos[i])

        print(f"\n\tDetected cycle = {detect_cycle(input_linked_list.head)}")
        j += 1
        print("-" * 100, "\n")


if __name__ == "__main__":
    main()
