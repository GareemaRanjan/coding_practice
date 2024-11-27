"""
Given the head of a singly linked list, remove any duplicate nodes from the list in place, ensuring that only one
occurrence of each value is retained in the modified list.
"""
from LinkedList import LinkedList
from PrintList import print_list_with_forward_arrow


def remove_duplicates(head):
    try:
        if head is not None:
            current = head
            while current is not None:
                val = current.data
                new_current = current.next
                prev = current
                print(f"current = {val}")
                while new_current is not None:
                    if new_current.data == val:
                        print(f"Found {val} again prev = {prev.data}")
                        prev.next = new_current.next
                    else:
                        prev = new_current
                    new_current = new_current.next
                    print(
                        f"\t new current updted val {new_current.data if new_current else None}"
                    )
                current = current.next
                print_list_with_forward_arrow(head)
            return head
    except Exception as e:
        print(e)


def main():
    inputs = [
        [30, 20, 30, 10, 50],
        [-7, -7, -22, -1, -5, -5],
        [1, 1, 1],
        [9, -9, 9],
        [1, -2, -2],
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
