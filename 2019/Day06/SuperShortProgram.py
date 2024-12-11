import networkx as nx

graph = nx.Graph(x.split(")") for x in open('Input').read().split('\n'))
print("Part 1:", sum(nx.shortest_path_length(graph, x, "COM") for x in graph.nodes))
print("Part 2:", nx.shortest_path_length(graph, "YOU", "SAN") - 2)
