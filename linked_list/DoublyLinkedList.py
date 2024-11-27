class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None


class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None  # Keep track of the last
