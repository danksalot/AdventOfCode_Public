import networkx as nx

with open('Input') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

G = nx.Graph()

for line in lines:
	parts = line.split(': ')
	rightparts = parts[1].split(' ')
	for part in rightparts:
		G.add_edge(parts[0], part)

G.remove_edges_from(nx.minimum_edge_cut(G))

product = 1
for group in nx.connected_components(G):
	product *= len(group)

print('Part 1:', product)
