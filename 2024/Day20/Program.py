import networkx as nx

with open('Input') as inFile:
	lines = [line.rstrip() for line in inFile.readlines()]

walls = []
start = None
finish = None

for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] == '#':
			walls.append((y, x))
		elif lines[y][x] == 'S':
			start = (y, x)
		elif lines[y][x] == 'E':
			finish = (y, x)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W
def buildGraph(grid, walls) -> nx.Graph:
    graph = nx.Graph()
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if (y, x) not in walls:
                for direction in DIRECTIONS:
                    if (y + direction[0], x + direction[1]) not in walls:
                        graph.add_edge((y, x), (y + direction[0], x + direction[1]), weight=1)    
    return graph

def findCheats(start, end, maxCheatLength):
    graph = buildGraph(lines, walls)
    graphNoWalls = buildGraph(lines, [])
    
    fullPathTime = nx.shortest_path_length(graph, start, end, weight='weight')
    shortestFromStart = nx.single_source_dijkstra_path_length(graph, start, weight='weight')
    shortestFromEnd = nx.single_source_dijkstra_path_length(graph, end, weight='weight')
    
    cheatsFound = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            cheatStart = (y, x)
            if cheatStart not in walls and cheatStart in shortestFromStart:                
                cheatEnds = nx.single_source_dijkstra_path_length(graphNoWalls, cheatStart, cutoff=maxCheatLength)
                for cheatEnd, cheatLength in cheatEnds.items():
                    if (cheatEnd[0], cheatEnd[1]) not in walls:
                        timeUsingCheat = shortestFromStart[cheatStart] + cheatLength + shortestFromEnd[cheatEnd]
                        cheatsFound[(cheatStart, cheatEnd)] = fullPathTime - timeUsingCheat    
    return cheatsFound

cheatsFound = findCheats(start, finish, 2)
print("Part 1:", sum(1 for val in cheatsFound.values() if val >= 100))
cheatsFound = findCheats(start, finish, 20)
print("Part 2:", sum(1 for val in cheatsFound.values() if val >= 100))
