import networkx as nx

with open('Input') as inFile:
	lines = inFile.read().splitlines()

timelimit = 30
G = nx.Graph()
flowRates = {}
shortestPaths = {}

for line in lines:
	parts = line.split(';')
	name = parts[0].split(' ')[1]
	rate = int(parts[0].split('=')[-1])
	parts2 = parts[1].split("valve ")
	if "valves" in parts[1]:
		parts2 = parts[1].split("valves ")
	tunnels = parts2[-1].split(', ')

	if rate > 0:
		flowRates[name] = rate
	for tunnel in tunnels:
		G.add_edges_from([(name, tunnel)])

# Pre-calculate the shortest paths between all valves with positive flow
shortestPaths['AA'] = { other:len(nx.shortest_path(G, 'AA', other)) for other in flowRates }
for valve in flowRates:
	shortestPaths[valve] = { other:len(nx.shortest_path(G, valve, other)) for other in flowRates if other != valve }

partialPaths = []
def getMaxFlow(loc, currentFlow, currentTime, visited, timeLimit, storePartialPaths):
	# Store partial paths that are around the middle
	if storePartialPaths and currentTime > (timeLimit / 2) - 5 and currentTime < (timeLimit / 2) + 5:
		partialPaths.append([currentFlow, visited])

	childMaxFlows = []
	for child in [x for x in flowRates if x != loc]:
		timeWhenReached = currentTime + shortestPaths[loc][child]
		if timeWhenReached <= timeLimit and child not in visited:
			newScore = currentFlow + (flowRates[child] * (timeLimit - timeWhenReached))
			childMaxFlows.append(getMaxFlow(child, newScore, timeWhenReached, visited + [child], timeLimit, storePartialPaths))
	
	if childMaxFlows:
		return max(childMaxFlows)
	else:
		return currentFlow

print('Part 1:', getMaxFlow('AA', 0, 0, [], timelimit, False))

# Generate partial paths
getMaxFlow('AA', 0, 0, [], timelimit-4, True)
# Look for a best second half to all partial paths
maxFlow = 0
for partialPath in partialPaths:
    combinedFlow = getMaxFlow('AA', partialPath[0], 0, partialPath[1], timelimit-4, False)
    if combinedFlow > maxFlow:
        maxFlow = combinedFlow
print('Part 2:', maxFlow)


