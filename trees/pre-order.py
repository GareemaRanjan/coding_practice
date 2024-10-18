from BinarySearchTree import BinarySearchTree


def preOrderPrint(node):
    if node is not None:  # base condition
        print(node.val)
        preOrderPrint(node.leftChild)
        preOrderPrint(node.rightChild)


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

preOrderPrint(BST.root)
