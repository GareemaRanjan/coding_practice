"""
Given a directed graph represented by an adjacency list graph and an integer source, representing the start vertex of
the graph, return a list of integers, result that shows the order of depth-first traversal starting from the specified
source vertex.

To find the depth-first traversal of a given directed graph, we utilize the depth-first search (DFS) method, starting
from the specified source vertex. Explore the graph by traversing each branch as deeply as possible before backtracking.
Begin from the source vertex, and delve deeply into the graph structure by visiting adjacent vertices until we reach a
leaf node or a dead-end. Unlike tree traversal, graph traversal must account for the possibility of cycles. To manage
this, we maintain a record of visited vertices to avoid revisiting them. The process continues until all vertices have
been explored, at which point the traversal order is returned.

Now, let’s look at the algorithm for this approach:

1.Initialize an empty list result to store the traversal order.

2.Determine the total number of vertices in the graph and create a boolean array visited to keep track of visited
vertices. Initialize all entries in the visited array as FALSE.

3.Create an empty stack stack to keep track of the nodes.

4.Push the source vertex onto the stack and mark it as visited by setting the corresponding entry in the visited array
to TRUE.

5.Repeat the following steps until the stack is not empty:

    i.Pop the top vertex from the stack and store it in current_vertex.

    ii.Add current_vertex to the result list.

    iii.Iterate through all neighbors of current_vertex:

        a.If a neighbor has not been visited, push it onto the stack and mark it as visited by setting the corresponding
         entry in the visited array to TRUE.

6.Return the result list containing the DFS traversal order.
"""

from Graph import Graph
from my_stack import MyStack


def dfs_traversal(graph, source):
    result = []
    visited = [0] * graph.vertices
    stack = MyStack()
    stack.push(source)
    while not stack.is_empty():
        vertex = stack.pop()
        if visited[vertex] != 1:
            result.append(vertex)
            current_node = graph.array[vertex].get_head()
            while current_node != None:
                stack.push(current_node.data)
                current_node = current_node.next_element
            visited[vertex] = 1

    print(result)
    return result


if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    dfs_traversal(graph, 0)
