import networkx as nx
import csv
from collections import Counter
import matplotlib.pyplot as plt 

edges = []
with open("KarateClub.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        u, v = row[0].split(";")
        u, v = u.strip(), v.strip()
        edges.append((u, v))

G = nx.Graph()
G.add_edges_from(edges)

for node, neighbors in G.adjacency():
    print(f"{node}: {list(neighbors.keys())}")

nodes = sorted(G.nodes(), key=int)
adj_matrix = nx.to_numpy_array(G, nodelist=nodes, dtype=int)
print("\nAdjacency Matrix:")
for row in adj_matrix:
    print(" ".join(str(val) for val in row))

#shortst path 
unweighted_path = dict(nx.all_pairs_shortest_path_length(G))
print(unweighted_path)


#Mean distance
mean_dist = nx.average_shortest_path_length(G)
print(f"\nMean distance: {mean_dist:.2f}")


#Diameter
d = nx.diameter(G)
print(f"Diameter: {d}")

#closeness centrality
cl_cent = nx.closeness_centrality(G)
print(f"\ncloseness centrality: {cl_cent}")

with open("adjacency_matrix.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Node", "ClosenessCentrality"])
    for node, centrality in cl_cent.items():
        writer.writerow([node, centrality])

