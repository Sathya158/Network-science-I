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

with open("adjacency_matrix.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([""] + nodes) 
    for i, row in enumerate(adj_matrix.tolist()): 
        writer.writerow([nodes[i]] + row)

degrees = dict(G.degree())
degree_values = list(degrees.values())

print(f"\nMin degree: {min(degree_values)}")
print(f"Max degree: {max(degree_values)}")
print(f"Mean degree: {sum(degree_values)/len(degree_values):.2f}")

# --- Frequency & Relative Frequency ---
frequency = Counter(degree_values)
print(f"\nFrequency of degrees: {frequency}")
relative_frequency = {deg: freq/len(G) for deg, freq in frequency.items()}
print(f"Relative frequency of degrees: {relative_frequency}")

# --- Histogram ---
plt.figure(figsize=(8, 6))
bars = plt.bar(frequency.keys(), frequency.values(), color='red', edgecolor='yellow')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, f'{int(height)}',
             ha='center', va='bottom', fontsize=10)

plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.title("Histogram of Node Degrees")
plt.xticks(list(frequency.keys()))
plt.show()
