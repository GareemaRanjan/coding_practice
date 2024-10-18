# Deleting a Node in a Binary Search Tree (BST)

# General Steps:
# 1. Search for the node to be deleted.
# 2. Once found, delete the node based on the specific case.

# We have 6 main cases to consider for deletion in a BST:

################################################################################
# Case 1: Deleting from an empty tree
################################################################################
# Explanation:
# - If the BST is empty, there is nothing to delete.
# - An empty tree is represented by 'None' (i.e., root is None).
# - Attempting to delete in an empty tree results in no action.
#
# Graph Example:
# (No tree exists)
#
# Before deletion:
#   [empty]
# After deletion:
#   [empty]
################################################################################


################################################################################
# Case 2: Deleting a leaf node (a node with no children)
################################################################################
# Explanation:
# - A leaf node is a node with no children, meaning both left and right children are 'None'.
# - To delete a leaf node, you simply remove the node by setting its parent's corresponding
#   pointer (left or right) to 'None'.
# - The rest of the tree remains unaffected.
#
# Graph Example:
# Tree before deletion:
#        50
#       /  \
#     30    70
#           /
#         60   <-- Leaf node to be deleted
#
# - In this tree, node 60 is a leaf node (no children).
# - To delete node 60, we set the right child of node 70 to 'None'.
#
# Tree after deleting node 60:
#        50
#       /  \
#     30    70
#           [empty]  <-- Node 60 has been removed, so 70 now has no right child.
################################################################################


################################################################################
# Case 3: Deleting a node with one child only
################################################################################
# Explanation:
# - When a node has only one child, you replace the node with its child.
# - This ensures the subtree remains connected to the parent of the deleted node.

################################################################################
# Case 3a: Deleting a node with only a right child
################################################################################
# - If a node has only a right child, you replace the node with its right child.
# - The right child "takes the place" of the deleted node in the tree.
#
# Graph Example:
# Tree before deletion:
#        50
#       /  \
#     30    70
#             \
#             80   <-- Node 70 has only a right child (80).
#
# - To delete node 70, we replace it with its right child (80).
#
# Tree after deleting node 70:
#        50
#       /  \
#     30    80  <-- 80 takes the place of 70.
################################################################################


################################################################################
# Case 3b: Deleting a node with only a left child
################################################################################
# - If a node has only a left child, you replace the node with its left child.
# - The left child "takes the place" of the deleted node in the tree.
#
# Graph Example:
# Tree before deletion:
#        50
#       /  \
#     30    70
#           /
#         60   <-- Node 70 has only a left child (60).
#
# - To delete node 70, we replace it with its left child (60).
#
# Tree after deleting node 70:
#        50
#       /  \
#     30    60  <-- 60 takes the place of 70.
################################################################################


################################################################################
# Case 4: Deleting a node with two children
################################################################################
# Explanation:
# - If a node has two children, you need to be more careful when deleting it.
# - The standard approach is to find the node's **inorder successor** or **inorder predecessor**.
# - The inorder successor is the smallest node in the node's right subtree (i.e., the leftmost
#   node in the right subtree).
# - You replace the value of the node to be deleted with the value of the inorder successor,
#   then delete the inorder successor (which will be a simpler case as it will have at most
#   one child).
#
# Graph Example:
# Tree before deletion:
#        50
#       /  \
#     30    70
#         /   \
#       60    80
#
# - To delete node 70, which has two children (60 and 80):
#   1. Find the inorder successor of 70, which is node 80 (smallest node in the right subtree).
#   2. Replace node 70's value with 80's value.
#   3. Now delete node 80, which is a simpler case (leaf or node with one child).
#
# Tree after deleting node 70:
#        50
#       /  \
#     30    80
#         /
#       60   <-- 80 takes the place of 70, and the tree remains valid.
################################################################################


# Summary of Steps for Deletion:
# - Always search for the node first.
# - Depending on the number of children the node has, perform the appropriate operation.
# - If it's a leaf node, just remove it.
# - If it has one child, replace the node with the child.
# - If it has two children, find the inorder successor (or predecessor), swap values, and
#   delete the successor (which will be a simpler case).


class Node:
    def __init__(self, value):
        self.val = value
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
        current = self
        parent = None
        while current:
            # Before moving current down the tree, we set parent to the current node. This keeps track of the parent
            # of the next node we are going to check.
            parent = current
            if val > current.val:
                current = current.rightChild
            else:
                current = current.leftChild

        if val < parent.val:
            parent.leftChild = Node(val)
        elif val > parent.val:
            parent.rightChild = Node(val)

    def insert_recursive(self, val):
        """
        The first thing to note in recursion is that you need a base case (where the recursion stops) and a recursive
        call (where the function calls itself to solve a subproblem).

        In this function:

        - The base case happens when the current node (self) doesn't have a child (either left or right), and we insert
        the new value at this position.
        - The recursive call happens when the current node has a child, and we call insert_recursive again on that
        child.
        """
        if val < self.val:
            if self.leftChild:
                self.leftChild.insert(val)
            else:
                self.leftChild = Node(val)
                return
        elif val > self.val:
            if self.rightChild:
                self.rightChild.insert(val)
            else:
                self.rightChild = Node(val)
                return
        else:
            return

    def search(self, val):
        current = self
        while current is not None:
            if val > current.val:
                current = current.rightChild
            elif val < current.val:
                current = current.rightChild
            else:
                return True
        return False

    def search_recursive(self, val):
        if val > self.val:
            if self.rightChild:
                return self.rightChild.search_recursive(val)
            else:
                return False
        elif val < self.val:
            if self.leftChild:
                return self.leftChild.search_recursie(val)
            else:
                return False
        # This is the base case. If val == self.val (i.e., the value of the current node is equal to the value you're
        # searching for), the function returns True, meaning that the value has been found.
        else:
            return True

    def delete(self, val):
        if val < self.val:
            if self.leftChild:
                self.leftChild = self.leftChild.delete(val)
            else:
                print(f"value not found")
                return self
        elif val > self.val:
            if self.rightChild:
                self.rightChild = self.rightChild.delete(val)
            else:
                print(f"value not found")
                return self
        else:
            if not self.leftChild and not self.rightChild:
                self = None
                return None
            elif not self.leftChild:
                tmp = self.rightChild
                self.leftChild = None
                return tmp
            elif not self.rightChild:
                tmp = self.leftChild
                self.rightChild = None
                return tmp
            else:
                # 1. From the given node to be deleted, find either the node with the smallest value in the right
                # sub-tree or the node with the largest value in the left sub-tree. Suppose you want to find the
                # smallest value in the right sub-tree; you do this by moving on to every node’s left child until
                # the last left child is reached.
                #
                # 2. Replace the node to be deleted with the node found (the smallest node in the right sub-tree or the
                # largest node in the left sub-tree).
                #
                # 3. Finally, delete the node found (the smallest in the right sub-tree).

                #  Q. In the delete function, why are we only looking in the right-subtree for the smallest value
                #  in the node-with-two-children case?
                #
                #  A. Because that node is one of the nodes that can replace the node to be deleted and still keep
                #  the BST properties
                #

                current = self.rightChild

                while current.leftChild is not None:
                    current = current.leftChild
                self.val = current.val
                current.val = val
                self.rightChild = self.rightChild.delete(val)

        return self
