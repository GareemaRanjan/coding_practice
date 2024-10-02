from Graph import Graph
import random


def count_vertices(edges):
    vertices = 0

    # Flatten the list of edges to count unique vertices
    flat = [num for sublist in edges for num in sublist]

    # Check if there are any vertices in the flattened list
    if len(flat) != 0:
        vertices = max(flat)

    return vertices + 1


def remove_edge(g, s, d):
    g.array[s].delete(d)
    return g


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
        edge = random.choice(edges[i])
        for src, dest in edges[i]:
            g.add_edge(src, dest)
        print("Initial graph: \n")
        g.print()
        print("\nSource: ", edge[0])
        print("Destination: ", edge[1])
        g = remove_edge(g, edge[0], edge[1])
        print("\nGraph after removing the edge: ")
        g.print()
        print("-" * 100)


if __name__ == "__main__":
    main()
