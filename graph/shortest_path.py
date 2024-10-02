"""
Given a directed graph of n nodes and two vertices, src and dest, return the length of the shortest path between src and
 dest. The shortest path will contain the minimum number of edges.

If no path exists between src and dest, return -1.

The solution employs the Breadth-First Search (BFS) algorithm to traverse the graph, starting from the source node.
It utilizes a Queue data structure to facilitate the BFS process, calculating the distance from the source node to each
of its neighbors. This distance is invariably the shortest since each node is visited exactly once. Upon encountering
the destination node, the algorithm returns the calculated distance. If the destination node is not found, it returns
-1.

"""

from my_queue import MyQueue


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


def find_min(g, s, d):
    print("***" * 30)
    visited = [0] * g.vertices
    dist = [0] * g.vertices
    queue = MyQueue()
    queue.enqueue(s)
    while not queue.is_empty():
        vertex = queue.dequeue()
        print(f"vertex = {vertex}")
        if vertex == d:
            return dist[vertex]

        if visited[vertex] == 0:
            for i in g.array[vertex]:
                if (
                    i not in queue.queue_list
                ):  # this check is essential we are counting distance based on which element is queued
                    dist[i] = dist[vertex] + 1
                    queue.enqueue(i)
        visited[vertex] = 1

        print("\t" + str(queue.queue_list))
        print("\tdist- " + str(dist))

    return -1


def main():
    inputs = [
        [[0, 1], [1, 2]],
        [[1, 2], [2, 4], [1, 4], [4, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 4], [2, 4]],
        [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
    ]

    src = [0, 1, 0, 0, 1]
    dest = [2, 3, 4, 6, 3]

    for i in range(len(inputs)):
        g = Graph(len(inputs[i]) + 1)
        for j in range(len(inputs[i])):
            g.add_edge(inputs[i][j][0], inputs[i][j][1])
        print("\tGraph:")
        g.print_graph()
        print("\n\tsrc: ", src[i], sep="")
        print("\tdest: ", dest[i], sep="")
        print("\n\tResult: ", find_min(g, src[i], dest[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
