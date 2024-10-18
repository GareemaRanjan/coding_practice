from BinarySearchTree import BinarySearchTree


def postOrderPrint(node):
    if node is not None:  # base condition
        postOrderPrint(node.leftChild)
        postOrderPrint(node.rightChild)
        print(node.val)


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

postOrderPrint(BST.root)
