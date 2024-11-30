from linked_list.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return (
            self.head
        )  # you can use this to traverse the LL. So no need to return head.data

    def is_empty(self):
        if not self.head:
            return True

        return False

    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            current = self.head
            print("\nPrinting linked list")
            while current is not None:
                print(f"{current.data} -->")
                current = current.next

    def insert_at_head(self, data):
        temp = Node(data)
        if self.is_empty():
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

        # The create_linked_list method will create the linked list using the
        # given integer array with the help of the insert_node_at_head method

    def create_linked_list(self, lst):
        for x in reversed(lst):
            self.insert_at_head(x)

    # The __str__(self) method will display the elements of the linked list
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result

    def delete_at_head(self):
        first = self.get_head()
        if first is not None:
            self.head = self.head.next
            first.next = None

    def get_length(self, head):
        temp = head
        length = 0
        while (temp):
            length += 1
            temp = temp.next
        return length

    # returns the node at the specified position(index) of the linked list
    def get_node(self, head, pos):
        if pos != -1:
            p = 0
            ptr = head
            while p < pos:
                ptr = ptr.next
                p += 1
            return ptr




if __name__ == "__main__":
    ll = LinkedList()

    print(f"LL is empty: {ll.is_empty()}")
    ll.print_list()
    ll.insert_at_head(2)
    ll.insert_at_head(3)
    ll.print_list()
    ll.delete_at_head()
    ll.print_list()
