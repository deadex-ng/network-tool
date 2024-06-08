"""Graph class used to represent nodes as an adjacent matrix."""

class Graph:
    def __init__(self):
        self.graph = []
        self.vertices = []
        self.vertices_no = 0

    def add_vertex(self, v: str) -> None:
        """Adds a node to the graph.

        Args:
        v: str. A node to add.
        """
        if v in self.vertices:
            print("Vertex ", v, " already exists")
        else:
            self.vertices.append(v)
            self.vertices_no += 1
            if self.vertices_no > 1:
                for vertex in self.graph:
                    vertex.append(0)
            temp = []
            for i in range(self.vertices_no):
                temp.append(0)
            self.graph.append(temp)

    def add_edge(self, v1: str, v2: str, weight: int) -> None:
        """Adds an edge betweeen two nodes.

        Args:
        v1: str. The start node.
        v2: str. The end node.
        weight: int. The weight between the two nodes.
        """
        if v1 not in self.vertices:
            print("Vertex ", v1, " does not exist.")
        elif v2 not in self.vertices:
            print("Vertex ", v2, " does not exist.")
        else:
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            self.graph[index1][index2] = weight
            self.graph[index2][index1] = weight
    
    def get_graph(self):
        return self.graph