from Graph import Graph
from my_queue import MyQueue


def check_path(g, s, d):
    visited = [0] * g.vertices
    print(s, d)
    queue = MyQueue()
    queue.enqueue(s)

    while not queue.is_empty():
        vertex = queue.dequeue()
        if vertex == d:
            return True
        if visited[vertex] != 1:
            current_node = g.array[vertex].get_head()
            while not current_node is None:
                queue.enqueue(current_node.data)
                current_node = current_node.next_element
            visited[vertex] = 1
    return False


def main():
    n = [3, 4, 6, 5, 7]
    edges = [
        [[0, 1], [1, 2]],
        [[0, 1], [0, 3]],
        [[0, 1], [1, 2], [1, 3], [1, 4], [3, 5]],
        [[0, 3], [1, 3], [2, 4]],
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
    sources = [2, 0, 0, 3, 5]
    destinations = [0, 2, 5, 4, 3]

    for i in range(len(n)):
        print(i + 1, ".\t n = ", n[i], sep="")
        print("\t Edges = ", edges[i], sep="")
        g = Graph(n[i])
        for j in range(len(edges[i])):
            g.add_edge(edges[i][j][0], edges[i][j][1])
            g.add_edge(edges[i][j][1], edges[i][j][0])
        print("\n")
        g.print()
        print(
            f"\n\t Path exists between {sources[i], destinations[i]}:",
            check_path(g, sources[i], destinations[i]),
        )
        print("-" * 100)


if __name__ == "__main__":
    main()
