"""
Given a directed graph, check whether the graph contains a cycle and return a boolean value accordingly.

A cycle occurs when you can start at one vertex, follow a path through the edges, and return to the starting vertex.
This means at least one vertex is visited more than once within the same traversal path.

Note: Edges list is interpreted in the following manner:

edges = [[0, 2, 1], [], [2, 1, 0]]

Interpretation:
0:0,2,1
1:None
2:2,1,0

-----------------------------------------------------------------------------------------
##Use DFS. If you encounter any vertex on top of a stack that is already visited, that confirms a cycle.

"""
from my_stack import MyStack
from Graph import Graph


def detect_cycle(graph):
    if graph.vertices == 0:
        return False
    stack = MyStack()
    visited = [0] * graph.vertices
    stack.push(0)
    while not stack.is_empty():
        vertex = stack.pop()
        if visited[vertex] == 1:
            return True
        current_node = graph.array[vertex].get_head()
        visited[vertex] = 1
        while current_node != None:
            stack.push(current_node.data)
            current_node = current_node.next_element

    return False


if __name__ == "__main__":
    edges_list = [
        [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]],
        [[2, 3], [3, 2, 1], [3, 0, 2], [2, 1]],
        [
            [],
            [8, 2],
            [0, 6, 3, 9, 7],
            [6, 7, 9, 5, 8],
            [8, 6, 5],
            [7, 0, 6],
            [7, 9],
            [9],
            [7, 9],
            [0],
        ],
        [[2], [2, 0, 1], [1, 2]],
        [],
    ]
    i = 0
    for i in range(len(edges_list)):
        print(i + 1, "\tEdges = ", edges_list[i], sep="")
        num_vertices = len(edges_list[i])
        g = Graph(num_vertices)
        for index, edges in enumerate(edges_list[i]):
            for node in edges:
                g.add_edge(index, node)
        g.print()
        print("\n\t Output:", detect_cycle(g))
        print("-" * 100)
        i += 1
