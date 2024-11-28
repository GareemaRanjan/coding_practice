"""
Given a list representing a max heap, convert this into a min heap.

Solution
In this solution, we convert a given max_heap into a min heap. We achieve this by adjusting the positions of elements
within the heap to meet the criteria of a min heap, where each parent node is smaller than its child nodes. This process
starts from the halfway point of the heap, typically where the last nonleaf node is found, and iteratively applies the
min heap criteria up to the root node.

The adjustment involves comparing each node with its children to identify the smallest among them. We determine the left
and right children of a node using the following formulas:

left=index∗2+1

right=index∗2+2

Here are the steps for the comparison:

    Check whether the node does not have the smallest value among its children.

        - If the value of the left child is smaller, then swap the node with the left child.

        - Otherwise, swap the node with the right child.

    Apply the above step recursively to ensure the entire subtree rooted at the swapped node satisfies the min heap
    property.

Continue this process until all the nodes, from the last nonleaf node up to the root, have been checked and adjusted to
meet the criteria of a min heap.

Time complexity

The time complexity of this solution is O(n), where n is the number of elements in the max heap. This is because each
element in the max heap is visited and possibly swapped down the heap hierarchy during the heapification process.

Space complexity

The space complexity of this solution is O(1), as each recursive call is resolved before the next one begins. Therefore,
the space remains constant.

"""


# Function to heapify the subtree rooted at the given index
def min_heapify(max_heap, index):
    # Calculate the left and right child indices
    left = index * 2 + 1
    right = (index * 2) + 2
    smallest = index

    # Check if the left child is within the heap bounds and smaller than the current smallest
    if len(max_heap) > left and max_heap[smallest] > max_heap[left]:
        smallest = left

    # Check if the right child is within the heap bounds and smaller than the current smallest
    if len(max_heap) > right and max_heap[smallest] > max_heap[right]:
        smallest = right

    # Swap the smallest element with the current index if needed, and recursively min heapify
    if smallest != index:
        tmp = max_heap[smallest]
        max_heap[smallest] = max_heap[index]
        max_heap[index] = tmp
        min_heapify(max_heap, smallest)

    return max_heap


# Function to convert the given max heap into a min heap
def convert_max(max_heap):
    # Convert the max heap into a min heap using min_heapify starting from the last nonleaf node
    for i in range((len(max_heap)) // 2, -1, -1):
        max_heap = min_heapify(max_heap, i)
    return max_heap


# Driver code
def main():
    max_heaps = [
        [9, 4, 7, 1, -2, 6, 5],
        [468, 397, 361, 336, 324, 318],
        [1000, 800, 500, -900, -1000],
        [5, 4, 3, 2, 1],
        [[10, 9, 6, 2, -3, -12, -14]],
    ]

    for i in range(len(max_heaps)):
        print(i + 1, ".", "\tGiven Max heap: ", max_heaps[i])
        print("\tConverted Min heap: ", convert_max(max_heaps[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()
