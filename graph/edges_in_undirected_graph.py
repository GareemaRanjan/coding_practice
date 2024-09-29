"""
Given an n number of nodes in an undirected graph, compute the total number of edges.

This approach iterates over each vertex in the graph and calculates the sum of the lengths of adjacency lists
corresponding to each vertex. The idea is to count the number of connections or edges in the graph. Dividing the final
sum by 2 ensures that each edge is counted only once because, in an undirected graph, each edge is represented twice
(once for each vertex it connects). Therefore, dividing by 2 gives the actual count of edges in the graph. This method
effectively traverses the adjacency list representation of the graph to determine the total number of edges.

The time complexity of the solution is O(v) because of the need to iterate through all vertices and calculate the sum of
the lengths of adjacency lists for each vertex.
------------------------------------------------------------------------------------------------------------------------

##Here, they have changed the graph implementation to a list.That is why the time complexity is O(n).
For linked list, it would increase.
"""


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = [[] for i in range(vertices)]

    def add_edge(self, u, v):
        if v not in self.adjacency[u]:
            self.adjacency[u].append(v)
        if u not in self.adjacency[v]:
            self.adjacency[v].append(u)

    def print_adjacency_list(self):
        for vertex, neighbors in enumerate(self.adjacency):
            print(f"Vertex {vertex}: -> {' -> '.join(map(str, neighbors))}")


def count_edges(graph):
    sum = 0

    # Iterate over each vertex in the graph
    for i in range(graph.vertices):
        sum += len(graph.adjacency[i])

    # Return the total sum of edges divided by 2 (because each edge is counted twice in an undirected graph)
    return sum // 2


# Helper function to count the total number of vertices in the graph
def count_vertices(edges):
    vertices = 0
    flat = [num for sublist in edges for num in sublist]
    if len(flat) != 0:
        vertices = max(flat)

    return vertices + 1


# Driver code
def main():
    edges = [
        [[0, 1], [1, 2]],
        [[0, 1], [0, 3], [1, 2]],
        [[0, 1], [1, 2], [1, 3], [1, 4], [3, 5]],
        [[0, 3], [1, 3], [2, 4], [3, 2]],
        [
            [0, 6],
            [1, 5],
            [1, 4],
            [2, 4],
            [2, 5],
            [2, 6],
            [3, 4],
            [3, 6],
            [4, 5],
            [5, 6],
        ],
    ]

    for i in range(len(edges)):
        vertices = count_vertices(edges[i])
        g = Graph(vertices)
        for src, dest in edges[i]:
            g.add_edge(src, dest)
        print("Edges: ")
        print(edges[i])
        print("\nAdjacency list:")
        g.print_adjacency_list()
        print("\nTotal edges:", count_edges(g))
        print("-" * 100)


if __name__ == "__main__":
    main()
