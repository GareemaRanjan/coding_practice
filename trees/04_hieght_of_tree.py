"""
Statement:
Given the root of a binary search tree, return the height of the tree. The height of the tree is the length of the
longest path from the root node to any leaf node in the tree.

Note: The height of an empty tree is 0, whereas the height of a tree with a single node is 1.

Solution:
To find the height of a given binary search tree, we utilize the depth-first search (DFS) method, starting from the
root node of the tree. By traversing the tree recursively, we explore each node’s left and right subtrees to reach
the farthest leaf node. Leveraging the preorder traversal method, we first visit the root node, followed by its left
child and then its right child. At each node, we record its height. Finally, we return the maximum height among the
left and right subtrees, incremented by one to account for the root node’s height.

We will follow this algorithm to reach the solution:

1. Start from the root node and check whether it exists. If the root node does not exist, return 0.

2. Otherwise, recursively perform the following steps:

    i. Visit the left child of the current node and calculate its height by recursively calling the function to find
    the height of the left subtree.

    ii. Explore and calculate the height of the right child by recursively calling the function to find the height of
    the right subtree.

    iii. Take the maximum of both heights obtained in the above steps, then add 1 to account for the current node.

3. At the end, return this calculated height of the tree.


Time complexity:

The time complexity of the solution above is O(n), where n is the number of nodes in the given binary search tree.



Space complexity:

The space complexity of this solution is O(h), where h is the height of the given tree. The space complexity of the
solution above is determined by the recursion stack space used during the depth-first traversal of the tree. In the
worst case, where we have a completely unbalanced binary search tree, the recursion stack can grow as large as the
height of the tree. However, in the average-case and best-case scenarios where we have a balanced tree, the height of
the tree is logarithmic in terms of the number of nodes, i.e., O(logn). Therefore, in such cases, the recursion stack
would also be logarithmic, leading to a space complexity of O(logn).

####
K-th Largest Problem: We passed k as a list ([k]) because we needed to update k across recursive calls (global mutable
state).
Height Calculation Problem: Each subtree’s height is computed independently and returned up the recursion chain.
There's no need for a global mutable state, so passing height as a list is unnecessary.

K-th Max Problem:

The goal was to track how many nodes we had visited.
Decrementing k with each node we visited was necessary to determine when we had reached the k-th largest element.
We passed k as a list ([k]) because we needed to update and carry forward that decrementing state across the entire
recursion.

Height Problem:

The goal here is not to track a shared counter like k, but rather to calculate the height of the tree recursively by
considering the heights of the left and right subtrees.
We don’t need to track or share state like k across recursive calls. Instead, we are simply returning a computed
result (height) from each subtree up to the parent node.
At each level, we accumulate the height by taking the maximum of the left and right subtree heights and adding 1
(for the current node).
Each call independently computes height.

"""
from BST_Educative import BinarySearchTree


def implementation(root):
    if root is None:
        return 0

    height_l = implementation(root.left)
    print(f"Height of left subtree of {root.data} = {height_l}")
    height_r = implementation(root.right)
    print(f"Height of right subtree of {root.data} = {height_r}")

    current_height = max(height_l, height_r) + 1
    print(f"Final height at node {root.data} = {current_height}")

    return current_height


def find_height(root):
    return implementation(root)


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
    y = 1
    for i in range(len(inputs)):
        input_tree = BinarySearchTree(inputs[i])
        print(y, ".\tGiven Tree:", sep="")
        display(input_tree.root)
        print("\n\tHeight of the Tree: ", find_height(input_tree.root))
        print("-" * 100, "\n")
        y += 1


if __name__ == "__main__":
    main()
