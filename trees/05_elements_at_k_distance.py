"""
Statement
Given the root node of a binary tree and an integer value k, find all the nodes at a distance of k from the root node.

Solution:
The solution uses depth first search (DFS) to recursively traverse the binary tree and collect the nodes at a distance k
from the root. At each node, the distance k is decremented, and both left and right subtrees are explored. When the
distance reaches 0, the node is added to the result. This process continues until all the nodes at distance k are
explored.

Time complexity

The time complexity of this solution is O(n), where n is the number of nodes in the binary tree. In the worst case,
when k is the maximum depth of the tree, the solution explores all nodes of the binary tree, resulting in the time
complexity of O(n).

Space complexity

The space complexity is O(h), where hvis the height of the binary tree. At each level of recursion, there is a call
stack maintained to keep track of the function calls. Because the depth of the recursion can reach up to the height of
the tree in the worst case, the resulting space complexity is O(h).
#######

k is the same at each level, therefore, we do not use [k]


"""
from BST_Educative import BinarySearchTree


def kth_imp(root, k, elements):
    if root is not None:
        print(f"at {root.data} k={k}")
        if k == 0:
            elements.append(root.data)
            return elements
        k = k - 1
        kth_imp(root.left, k, elements)
        kth_imp(root.right, k, elements)
    return elements


def find_kth_numbers(root, k):
    elements = []
    return kth_imp(root, k, elements)


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
        [18, 15, 13, 19, 5, 14],
        [1, 2, 3, 4, 5, 6],
        [100, 200, 50, 40, 30, 80, 90],
        [10],
        [1, 2],
        [-10, -20, -30, -40, -50, -60, -70],
    ]

    list_of_k = [2, 4, 6, 1, 1, 4]
    y = 1

    for i in range(len(inputs)):
        print(y, ".\tk = ", list_of_k[i], sep="")
        input_tree = BinarySearchTree(inputs[i])
        print("\n\tInput Tree:", sep="")
        display(input_tree.root)

        print(
            "\n\tElements at k distance: ",
            find_kth_numbers(input_tree.root, list_of_k[i]),
            sep="",
        )

        print("-" * 100, "\n")
        y += 1


if __name__ == "__main__":
    main()
