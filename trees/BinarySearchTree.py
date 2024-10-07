from Node import Node


class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)

    def search(self, val):
        if self.root:
            return self.root.search(val)
        else:
            return False

    def insert_recursive(self, val):
        if self.root:
            return self.root.insert_recursive(val)
        else:
            self.root = Node(val)

    def search_recursive(self, val):
        if self.root:
            return self.root.search_recursive(val)
        else:
            return False
