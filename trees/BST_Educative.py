from queue import Queue
from TreeNode import *


class BinarySearchTree:
    def __init__(self, values):
        self.root = self.createBinaryTree(values)

    def createBinaryTree(self, values):
        if len(values) == 0:
            return None

        # Create the root node of the binary search tree
        root = TreeNode(values[0])

        # Start iterating over the list of values starting from the second value
        for value in values[1:]:
            node = TreeNode(value)
            curr = root
            while True:
                # If the value is less than the current node's value, move to the left child
                if node.data <= curr.data:
                    if curr.left is None:
                        # If the left child is empty, insert the new node here and break the loop
                        curr.left = node
                        break
                    else:
                        # If the left child is not empty, move to the left child and continue the search
                        curr = curr.left
                else:
                    # If the value is greater or equal to the current node's value, move to the right child
                    if curr.right is None:
                        # If the right child is empty, insert the new node here and break the loop
                        curr.right = node
                        break
                    else:
                        # If the right child is not empty, move to the right child and continue the search
                        curr = curr.right

        # Return the root of the binary search tree
        return root
