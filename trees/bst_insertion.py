from Node import Node
from BinarySearchTree import BinarySearchTree

import random


def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.rightChild is None and node.leftChild is None:
        line = "%s" % node.val
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.rightChild is None:
        lines, n, p, x = _display_aux(node.leftChild)
        s = "%s" % node.val
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line = x * " " + "/" + (n - x - 1 + u) * " "
        shifted_lines = [line + u * " " for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.leftChild is None:
        lines, n, p, x = _display_aux(node.rightChild)
        s = "%s" % node.val
        u = len(s)
        first_line = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted_lines = [u * " " + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.leftChild)
    right, m, q, y = _display_aux(node.rightChild)
    s = "%s" % node.val
    u = len(s)
    first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
    second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
    if p < q:
        left += [n * " "] * (q - p)
    elif q < p:
        right += [m * " "] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


BST = BinarySearchTree(50)
BST.insert(50)
BST.insert_recursive(8)
for _ in range(10):
    ele = random.randint(0, 100)
    print("Inserting " + str(ele) + ":")
    BST.insert(ele)
    display(BST.root)
    print("\n")

for _ in range(5):
    ele = random.randint(0, 100)
    print("Inserting " + str(ele) + ":")
    BST.insert_recursive(ele)
    display(BST.root)
    print("\n")

BST.insert(50)
BST.insert_recursive(8)
