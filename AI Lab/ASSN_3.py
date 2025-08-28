import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#Load binary adjacency matrix
adj_matrix = np.loadtxt("graph.txt", dtype=int)

#Creating graph from adjacency matrix
G = nx.Graph()
rows, cols = adj_matrix.shape
for i in range(rows):
    for j in range(cols):
        if adj_matrix[i][j] == 1:
            G.add_edge(i, j)

#Draw initial graph
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(6, 6))
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
plt.title("Original Graph")
plt.savefig("graph_original.png")
plt.show()

#Find shortest path using BFS (since unweighted)
source, target = 0, 4
path = nx.shortest_path(G, source=source, target=target)
print("Shortest path from {} to {}: {}".format(source, target, path))

# Step 6: Highlight the shortest path on graph
edge_colors = []
for edge in G.edges():
    if (edge[0] in path and edge[1] in path and
        abs(path.index(edge[0]) - path.index(edge[1])) == 1):
        edge_colors.append("red")  # path edges in red
    else:
        edge_colors.append("gray")

plt.figure(figsize=(6, 6))
nx.draw(G, pos, with_labels=True, node_color="lightgreen", edge_color=edge_colors, width=2)
plt.title("Shortest Path Highlighted")
plt.savefig("graph_shortest_path.png")
plt.show()
