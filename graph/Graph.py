"""

directed graph - (0,1) is not the same as (1,0)

Graph class consists of two data members:
    The total number of vertices in the graph
    A list of linked lists to store adjacent vertices

We’ve laid down the foundation of our Graph class. The variable vertices contains an integer specifying the total
number of vertices.

The second component is array, which will act as our adjacency list. We simply have to run a loop and create a linked
list for each vertex.

Now, we’ll add two methods to make this class functional:
    print_graph() - Prints the content of the graph
    add_edge() - Connects a source with a destination

------------------------------------------------------------------------------------------------------------------------

### First create a graph specifying the number of nodes - Graph(4)
### Each node will have a linked list
------------------------------------------------------------------------------------------------------------------------

"""
from LinkedList import LinkedList


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []

        for i in range(vertices):
            # Appending a new LinkedList on each array index
            self.array.append(LinkedList())

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_head(destination)
            # print(f"print linkd list when adding {source} --> {destination}")
            # self.array[source].print_list()

            # -------------------------------------------------------------------------------
            # Uncomment the following line for undirected graph
            # self.array[destination].insert_at_head(source)

            # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
            # We would create an edge from destination towards source as well
            # i.e self.list[destination].insertAtHead(source)
            # -------------------------------------------------------------------------------

    def print(self):
        for i in range(0, self.vertices):
            print(f"Adjacency Matrix for {i}")
            self.array[i].print_list()


if __name__ == "__main__":
    graph = Graph(4)

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)

    graph.print()
