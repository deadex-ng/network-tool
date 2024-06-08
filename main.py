"""The main entry point."""
import pandas as pd
from graph.graph import Graph
from utils.utils import unique

df = pd.read_csv("network.csv")
(rows, cols) = df.shape

nodes_list = []
for i in range(rows):
    start = df.iat[i, 1]
    end = df.iat[i, 2]
    nodes_list.append(start)
    nodes_list.append(end)

graph = Graph()

unique_nodes_list = unique(nodes_list)
for node in unique_nodes_list:
    graph.add_vertex(node)

for i in range(rows):
    start_node = df.iat[i, 1]
    end_node = df.iat[i, 2]
    weight = df.iat[i, 4]
    graph.add_edge(start_node, end_node, weight)

#Show our graph
print(graph.get_graph())