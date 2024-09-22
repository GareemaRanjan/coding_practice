from Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        return False

    def insert_at_head(self, value):
        temp_node = Node(value)
        if self.is_empty():
            self.head_node = temp_node
        else:
            temp_node.next_element = self.head_node
            self.head_node = temp_node
        return self.head_node

    def insert_at_tail(self, value):
        temp_node = Node(value)
        if self.is_empty():
            self.head_node = temp_node
        else:
            current_node = self.head_node
            while current_node.next_element is not None:
                current_node = current_node.next_element
            current_node.next_element = temp_node

    def length(self):
        len = 0
        current_node = self.get_head()
        while current_node is not None:
            len = len + 1
            current_node = current_node.next_element

        return len

    def print_list(self):
        current_node = self.get_head()
        if self.is_empty():
            print("Empty List")
            return
        while current_node.next_element is not None:
            print(f" {current_node.data} -> ")
            current_node = current_node.next_element
        print(f"{current_node.data} -> None")

    def delete_at_head(self):
        if self.is_empty():
            return False
        first_ele = self.get_head()
        self.head_node = first_ele.next_element
        first_ele.next_element = None
        return True

    def delete(self, value):
        if self.is_empty():
            return False
        current_node = self.get_head()
        prev_node = None

        if current_node.data == value:
            self.delete_at_head()
            return True

        while current_node is not None:
            if current_node.data == value:
                prev_node.next_element = current_node.next_element
                current_node.next_element = None
                return True
            prev_node = current_node
            current_node = current_node.next_element
        return False

    def search(self, value):
        if self.is_empty():
            return False
        current_node = self.get_head()
        while current_node is not None:
            if current_node.data == value:
                return True
            current_node = current_node.next_element
        return False
