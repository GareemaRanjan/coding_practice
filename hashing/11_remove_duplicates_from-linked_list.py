"""
Given the head of a singly linked list, remove any duplicate nodes from the list in place, ensuring that only one
occurrence of each value is retained in the modified list.

Time Complexity - O(n)
Space Complexity - O(n)
"""
from linked_list.LinkedList import LinkedList
from linked_list.PrintList import (
    print_list_with_forward_arrow,
    print_list_with_forward_arrow_loop,
)


def remove_duplicates(head):
    # Create a set to track the values we have seen so far
    visited = set()

    # Initialize a pointer 'prev' to the head of the list
    prev = head

    # Add the data of the first node (head) to the visited set since it's the first element
    visited.add(prev.data)

    # Start from the second node (head.next)
    current = head.next

    # Iterate through the linked list until we reach the end
    while current is not None:
        # Check if the current node's data has already been visited
        if current.data in visited:
            # If a duplicate is found, print a message
            print(f"found duplicate {current.data}")

            # Remove the current node by skipping it. 'prev.next' now points to the next node
            prev.next = current.next

            # Store the current node temporarily, then move 'current' to the next node
            temp = current
            current = current.next

            # Set 'temp.next' to None to completely disconnect the node from the list
            temp.next = None
        else:
            # If current data is not a duplicate, add it to the visited set
            visited.add(current.data)

            # Move 'prev' and 'current' forward in the list
            prev = current
            current = current.next

    # Return the modified head of the list
    return head


def main():
    inputs = [
        [50, 10, 50, 10, 50],
        [-3, -4, 3, -3, -4, -7],
        [20, 20, 20, 20],
        [100, 100],
        [200],
    ]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])
        print(i + 1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tLinked list without duplicates: ", sep="", end="")
        print_list_with_forward_arrow(remove_duplicates(input_linked_list.head))

        print("\n", "-" * 100)


if __name__ == "__main__":
    main()
