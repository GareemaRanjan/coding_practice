"""
Statement
Given the root node of a binary search tree and an integer value k, return the Kth maximum value in the tree.

Solution:
For this solution, we will recursively perform the inorder traversal (right subtree, root, left subtree) on the binary
search tree. We will use the inorder traversal to get elements in sorted order.

While performing the inorder traversal on the tree, decrement kby 1, indicating the number of maximum elements that
still need to be found. After decrementing k, we check whether the value of k has reached 0. If it is 0, we return the
current node, indicating the node having the k th maximum element. If not, continue the traversal.

This approach ensures that we traverse the tree in a depth-first manner while appropriately updating k and
effectively finding the k th maximum element.
Time complexity

The time complexity of this solution is O(n), where n represents the number of nodes in the binary tree.

Space complexity

The space complexity of this solution is O(n) because our recursive algorithm uses space on the call stack.
#######

# - We are performing a reverse in-order traversal (right -> root -> left)
# - Start by checking the right subtree first since it contains the largest elements in a BST
# - If the k-th largest element is found in the right subtree, return it immediately
# - Process the current node (after the right subtree) and decrement k
# - Forn recursion, pass k as a list to maintain call be reference. Otherwise, new values of k will not be passed
# - When k becomes 0, it means the current node is the k-th largest element, so return it
# - If the k-th largest element is not found yet, continue by checking the left subtree
# - If the result is found in the left subtree, return it, otherwise return None
# - Always propagate the result up through the recursive calls to avoid unnecessary traversal
# - Debugging print statements help to track the recursion flow and understand when values are found or missed


"""
from BST_Educative import BinarySearchTree


def implementation(root, k):
    # print(f"root value {root}")
    if root:
        print(f"Root is not none ${root.data}")

        print(f"going to root right ${root.data}")
        res = implementation(root.right, k)
        if res is not None:
            print(f"found res={res} at {root.data}")
            return res
        else:
            print(f"Res was None at {root.data}")

        print(root.data, k)
        if k[0] > 0:
            k[0] = k[0] - 1
            print(f"Reducing k for {root.data} to {k[0]}")
        if k[0] == 0:
            print(f"Found value, returning {root.data}")
            return root.data
        print(f"Found nothing, so now checking left of {root.data}")
        resl = implementation(root.left, k)
        print(f"found resl val {resl} at {root.data}")

        if resl is not None:
            print(f"found non none resl val {resl} at {root.data}")
            return resl
        else:
            print(f"found none resl val {resl} at {root.data}")
            return None


def find_kth_max(root, k):
    return implementation(root, [k])


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

    list_of_k = [3, 4, 6, 1, 1, 4]
    y = 1

    for i in range(len(inputs)):
        print(y, ".\tk = ", list_of_k[i], sep="")
        input_tree = BinarySearchTree(inputs[i])
        print("\n\tInput Tree:", sep="")
        display(input_tree.root)

        print(
            "\n\tKth Maximum Element: ",
            find_kth_max(input_tree.root, list_of_k[i]),
            sep="",
        )

        print("-" * 100, "\n")
        y += 1


if __name__ == "__main__":
    main()
