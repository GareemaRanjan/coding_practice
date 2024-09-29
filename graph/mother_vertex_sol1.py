"""
Given a directed graph as input, determine a mother vertex within it. A mother vertex in a graph G=(V,E), is vertex V
such that all other vertices in G can be reached by a path from V. Although a graph might feature multiple mother
vertices, your goal is to identify at least one.

edges = [[0, 2, 1], [], [2, 1, 0]]

To find a mother vertex in a given directed graph, we apply a depth-first search (DFS) strategy from each vertex to
confirm if there’s a vertex from which all other vertices are reachable.We start by iteratively performing a depth-first
search (DFS) starting from each vertex in the graph. For each vertex, we call perform_dfs() to see how many vertices can
be reached from it. If the number of vertices reached from the current vertex is equal to the total number of vertices
in the graph, it means that the current vertex can reach all other vertices and, thus, is a mother vertex. We return
this vertex index. If no vertex meets the above condition, we return -1, indicating there’s no mother vertex in the
graph.

We used a helper function, perform_dfs(), to perform a depth-first search starting from a source vertex and count how
many vertices are reachable from this source. It initializes a list vertices_reached to keep track of visited vertices
and a MyStack() stack to manage the DFS traversal. The source vertex is marked as visited and pushed onto the stack.
While the stack is not empty, the algorithm continuously pops a vertex from the stack, and for each of its adjacent
vertices:

If an adjacent vertex hasn’t been visited, it is marked as visited, pushed onto the stack, and the vertices_reached
counter is incremented.

After traversing, the function returns the count of vertices reached plus one (to include the source vertex itself).

The time complexity of this solution is O(V(V+E)), because DFS is performed from each vertex.
------------------------------------------------------------------------------------------------------------------------

"""
from my_stack import MyStack
from Graph import Graph


def dfs(g, s):
    visited = [0] * g.vertices
    result = []
    stack = MyStack()
    stack.push(s)
    while not stack.is_empty():
        vertex = stack.pop()
        if visited[vertex] != 1:
            result.append(vertex)
            current_node = g.array[vertex].get_head()
            while current_node != None:
                stack.push(current_node.data)
                current_node = current_node.next_element
            visited[vertex] = 1
    # print(f"source: {s}, result: {result}")
    return result


def find_mother_vertex(graph):
    if graph.vertices == 0:
        return False
    for i in range(0, graph.vertices):
        if len(dfs(graph, i)) == graph.vertices:
            return i

    return -1


if __name__ == "__main__":
    n = [3, 4, 5, 4, 3]
    edges = [
        [[0, 1], [0, 2], [1, 2]],
        [[2, 3], [3, 2, 1], [3, 0, 2], [2, 1]],
        [[0, 1], [0, 2], [0, 3], [0, 4], [3, 4]],
        [[0, 2, 1], [3, 2, 1], [2, 1, 0]],
        [[2, 0, 1], [1, 2]],
    ]

    for i in range(len(n)):
        print(i + 1, ".\t n = ", n[i], sep="")
        print("\t Edges = ", edges[i], sep="")
        g = Graph(n[i])
        for j in range(len(edges[i])):
            g.add_edge(edges[i][j][0], edges[i][j][1])
        print("\n")
        g.print()
        print("\n\t The mother vertex in this graph is:", find_mother_vertex(g))
        print("-" * 100)
