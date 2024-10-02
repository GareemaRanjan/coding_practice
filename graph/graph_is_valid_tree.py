"""
Given an undirected graph containing n nodes labeled from 0 to n−1, determine whether the graph is a valid tree or not.
Return TRUE if the edges of the given graph make up a valid tree, and FALSE otherwise.

A graph is a valid tree when all the nodes are connected and there is no cycle between them.

To check if the graph is a valid tree, we start from the first node and move to adjacent nodes using a depth-first
search. We mark visited nodes and look for cycles by checking if a node has been visited before. If we encounter a
previously visited node that is not the parent, we have found a cycle, indicating the graph is not a tree. If the
depth-first search started from the first node is complete, but some nodes remain unvisited, the graph is not connected,
making it not a tree. If all nodes have been visited and no cycles are found, the graph is a valid tree.

The following are the steps of the algorithm:

-Initialize a visited list to keep track of nodes that will be visited during the traversal of the graph.

-Starting from the first node, start traversing the graph.

-While traversing the adjacent nodes in the graph, mark the current node as visited in the visited list.

-Pick a node and check if the node has been visited before.

    -If a node has not been visited before, continue the traversal from this node.

    -Otherwise, if the node has been visited before a cycle has been found. Return FALSE.

After completing the depth-first search, traverse the visited list and check if the value of any index is FALSE; it
means the graph is disconnected, return FALSE. Otherwise, if all values are TRUE, return TRUE, indicating the graph is
a tree.


The time complexity of this solution is O(V+E), where V is the number of vertices in the graph and E is the number of
edges in the graph. This is because the whole graph is traversed once.

-----------------------------------------------------------------------------------------

### Maintain a copy of visited array. while performing DFs, if all nodes are visited from a node, that means all nodes
can be connected. While performing DFs, check for a cycle as well.
"""


from my_stack import MyStack


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []

        for i in range(vertices):
            # Appending a new LinkedList on each array index
            self.array.append(list())

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].append(destination)

    def print_graph(self):
        for i in range(0, self.vertices):
            print(f"Adjacency Matrix for {i}")
            print(self.array[i])


def check_cycle(g, visited):
    stack = MyStack()
    stack.push(0)
    while not stack.is_empty():
        vertex = stack.pop()
        if visited[vertex] == 1:
            return True
        for i in g.array[vertex]:
            stack.push(i)
        visited[vertex] = 1

    return False


def is_tree(g):
    if g.vertices == 0:
        return False
    visited = [0] * g.vertices

    if check_cycle(g, visited):
        return False

    if any(not i for i in visited):
        return False

    return True


def main():
    n = [3, 4, 5, 5, 6, 1]
    edges = [
        [[0, 1], [0, 2], [1, 2]],
        [[0, 1], [0, 2], [0, 3]],
        [[0, 1], [0, 2], [0, 3], [0, 4], [3, 4]],
        [[0, 1], [0, 2], [0, 3], [3, 4]],
        [[0, 1], [0, 2], [1, 3], [2, 4], [0, 5]],
        [],
    ]

    for i in range(len(n)):
        print(i + 1, ".\t n = ", n[i], sep="")
        print("\t Edges = ", edges[i], sep="")
        g = Graph(n[i])
        for j in range(len(edges[i])):
            g.add_edge(edges[i][j][0], edges[i][j][1])
        print("\n")
        g.print_graph()
        print("\n\t Is the given graph a valid tree:", is_tree(g))
        print("-" * 100)


main()
