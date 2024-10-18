"""
Statement:
Given the root node of a binary search tree (BST), find and return the minimum value present in the BST.

Constraints:
Let n be the number of nodes in the binary search tree.
0 ≤ n ≤ 500
-10^4 ≤ Node.data ≤ 10^4

Recursive approach:
1. Start with a base case to check if the root is NULL. If the root is NULL, it means the tree is empty, so return None.
2. The next base case is to check if the root has no left child (root.left is NULL). If so, the root itself is the
 minimum value in the tree, so return root.data.
3. If the current root has a left child, make a recursive call on the left child using find_min(root.left). This call
traverses down the left subtree until it reaches a node with no left child (a leaf node).
4. The minimum value found in that leaf node will be propagated back up, step by step, until the original call receives
the smallest value from the entire BST.

Complexity analysis:

Time complexity:
- The time complexity of this solution is O(h), where h is the height of the binary search tree.
- In a balanced BST, h = log(n), where n is the number of nodes. Therefore, time complexity becomes O(log(n)).
- In the worst case (left-skewed tree), h = n, so the time complexity becomes O(n).

Space complexity:
- The space complexity is O(h), where h is the height of the tree.
- In a balanced BST, space complexity becomes O(log(n)) due to the recursive call stack.
- In the worst case (left-skewed tree), the space complexity becomes O(n) due to the recursive call stack.
"""

from BST_Educative import BinarySearchTree


def find_min(root):
    if root.left is not None:
        return find_min(root.left)
    else:
        return root.data


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
        print(y, ".\tInput Tree:", sep="")
        display(input_tree.root)
        print("\n\tSmallest element: ", find_min(input_tree.root))
        print("-" * 100, "\n")
        y += 1


if __name__ == "__main__":
    main()
