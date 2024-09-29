"""
Given a directed graph as input, determine a mother vertex within it. A mother vertex in a graph G=(V,E), is vertex V
such that all other vertices in G can be reached by a path from V. Although a graph might feature multiple mother
vertices, your goal is to identify at least one.

edges = [[0, 2, 1], [], [2, 1, 0]]

************************ Kosaraju’s strongly connected component algorithm *************************

This solution also uses a modified DFS approach named Kosaraju’s strongly connected component algorithm to find the
mother vertex in the graph. The key insight is the last visited vertex in this sequence, last_v, which likely has paths
to all other vertices due to its reachability in the DFS order. The solution is divided in two key phases:

Phase 1: Identifying a candidate

    1.Initialize a visited list to keep track of explored nodes, ensuring no node is visited more than once during the
    search.

    2.Iterate through each vertex in the graph. For vertices not yet visited, perform DFS starting from that vertex.
    This step is crucial for identifying a candidate mother vertex.

    3.During DFS, mark each visited node as TRUE in the visited list to prevent revisitation. The DFS continues until it
     reaches a node with no unvisited adjacent nodes.

    4.The last vertex visited in this complete traversal, last_v, becomes a candidate for the mother vertex.

Phase 2: Validating the candidate

    1.Reset the visited list to ensure a fresh start for validation.

    2.Perform DFS starting from the candidate mother vertex, last_v, to see if all other vertices can be reached from
    it.

    3.After this second DFS, check the visited list. If any vertex remains unvisited (FALSE in the visited list), then
    last_v cannot reach all vertices, and thus, there is no mother vertex in the graph (indicated by returning -1).

    4.If all vertices are visited in this phase, then last_v is confirmed as the mother vertex and is returned by the
    function.

The time complexity of this solution is O(V+E).


------------------------------------------------------------------------------------------------------------------------
###### The key observation is that the last vertex in a complete DFS traversal (last_v) is a candidate for the mother
vertex. This is because, in the DFS, this vertex likely has paths leading to all other nodes, given that it is the last
node finished in the exploration of the graph.

Why? If a vertex is visited last in a DFS traversal, it suggests that all other vertices have already been explored
through some path that connects them to this vertex, making it a good candidate to be a mother vertex.


"""
from my_stack import MyStack
from Graph import Graph


def dfs(g, s, visited):
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
    visited = [0] * graph.vertices
    last_v = 0
    for vertex in range(0, graph.vertices):
        if visited[vertex] == 0:
            dfs(graph, vertex, visited)
            last_v = vertex

    visited = [0] * graph.vertices
    dfs(graph, last_v, visited)
    if any(not i for i in visited):
        return -1
    else:
        return last_v


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
