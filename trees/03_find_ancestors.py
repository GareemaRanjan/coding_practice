"""
Statement:
Given the root node of a binary search tree (BST) and an integer value k, find all the ancestors of the node whose value
is k.

An ancestor of a node in a tree is any node on the path from the root to that node.

Solution:
We can recursively traverse the binary tree. At each node, we check if its value matches the target value, k. If a match
is found, we record the node’s ancestors along the path leading to the target node by appending the current node’s value
to the result list. This process ensures that all ancestors are identified and recorded accurately.

The steps of the algorithm are given below:

- Initialize an empty result list to store the ancestors.
- Check if the current node is NULL, indicating a leaf node or an empty subtree, return FALSE if so.
- If the current node’s value matches the target value k, return TRUE to indicate the target node is found.
- Recursively search for the target node in the left and right subtrees. If found in either subtree, append the current
node’s value to the result list and return TRUE, otherwise, return FALSE.
- Finally, return the result list containing all recorded ancestors of the node k.

Time complexity:

The time complexity of this solution is O(n), where n represents the number of nodes in the binary tree.

Space complexity:

The space complexity of this solution is O(n) because our recursive algorithm uses space on the call stack.


"""
from BST_Educative import BinarySearchTree


def implementation_ancestors(root, val, ancestors):
    if root is not None:
        if val > root.data:
            implementation_ancestors(root.right, val, ancestors)
            ancestors.append(root.data)
        elif val < root.data:
            implementation_ancestors(root.left, val, ancestors)
            ancestors.append(root.data)
        return None


def find_ancestors(root, val):
    ancestors = []
    implementation_ancestors(root, val, ancestors)
    if len(ancestors) == 0:
        ancestors = [-1]
    return ancestors


def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # None.
    if node is None:
        line = "Empty tree!"
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # No child.
    if node.right is None and node.left is None:
        line = str(node.data)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line = x * " " + "/" + (n - x - 1 + u) * " "
        shifted_lines = [line + u * " " for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = str(node.data)
        u = len(s)
        #        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted_lines = [u * " " + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = "%s" % node.data
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


def main():
    inputs = [
        [100, 50, 200, 25, 75, 150, 350],
        [25, 15, 75, 8, 18, 50, 350],
        [350, -100, 450, -175, 125, 375, 500],
        [100],
        [23, 21, 27, 18, 22, 25, 29, 17, 19, 23, 45, 67, 78, 85],
    ]
    k = [75, 8, 125, 100, 85]

    y = 1
    for i in range(len(inputs)):
        input_tree = BinarySearchTree(inputs[i])
        print(y, ".\tInput Tree:", sep="")
        display(input_tree.root)
        print("\n\tk:", k[i])
        print("\n\tThe ancestors are : ", find_ancestors(input_tree.root, k[i]))
        print("-" * 100, "\n")
        y += 1


if __name__ == "__main__":
    main()
