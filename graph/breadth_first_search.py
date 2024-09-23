"""
Given a directed graph represented as an adjacency list, graph, and an integer, source, which is the starting
vertex number, return an array of integers, result, that contains the order of the graph’s breadth-first traversal
starting from the source vertex.

To find the breadth-first traversal of a given directed graph, we utilize the breadth-first search (BFS) method, starting
from the specified source vertex. This approach ensures that all vertices at the same level (breadth) are visited
before proceeding to vertices at the next level. Starting from the source vertex, BFS explores its immediate neighbors
first, expanding outward level by level. Unlike tree traversal, graph traversal must account for the possibility of
cycles. To manage this, we maintain a record of visited vertices to avoid revisiting them. The process continues until
all vertices have been explored, at which point the order of traversal is returned.


We will follow this algorithm to reach the solution:

1.Initialize a queue and an integer array, result to store the order of traversal.

2.Keep track of the visited vertices with the help of visited array. If a vertex has been visited, we mark it as TRUE in
the visited array.

3.Enqueue the source vertex, and mark it as visited.

4.Keep on repeating the following steps until the queue is not empty:

    i.Dequeue the vertex, and add it to the result array. Also, check if its neighboring vertices are visited or not.

    ii.If they are not visited, enqueue them and mark them as visited.

5.Return the result array, which contains the breadth-first traversal order of the graph starting from the source
vertex.

"""




from Graph import Graph
from my_queue import MyQueue

def bfs_traversal(graph, source):
    queue = MyQueue()
    queue.enqueue(source)
    result = []
    visited = [0]*graph.vertices
    while not queue.is_empty():
        vertex = queue.dequeue()
        print(f"vertex: {vertex}")
        if visited[vertex] == 0:
            current_node = graph.array[vertex].get_head()
            while current_node != None:
                queue.enqueue(current_node.data)
                current_node = current_node.next_element
            visited[vertex] = 1
            result.append(vertex)
        print(f"Queue {queue.queue_list}")
    print(result)
    return result


if __name__ == '__main__':
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    bfs_traversal(graph, 0)