import sys
sys.setrecursionlimit(10**9)

with open('Input') as inFile:
	lines = inFile.readlines()

grid = [list(x.strip()) for x in lines]

start = (0, 1)
end = (len(grid) - 1, len(grid[-1]) - 2)

def findNeighbors(pos):
	neighbors = []
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # R, L, D, U
	# if grid[pos[0]][pos[1]] == '>': directions = [(0, 1)]
	# elif grid[pos[0]][pos[1]] == '<': directions = [(0, -1)]
	# elif grid[pos[0]][pos[1]] == 'v': directions = [(1, 0)]
	# elif grid[pos[0]][pos[1]] == '^': directions = [(-1, 0)]
	for direction in directions:
		neighbor = (pos[0] + direction[0], pos[1] + direction[1], 1, [])
		if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[neighbor[0]]) and grid[neighbor[0]][neighbor[1]] != '#':
			neighbors.append(neighbor)
	return neighbors

neighborMap = {}
for y in range(len(grid)):
	for x in range(len(grid[y])):
		if grid[y][x] in '.<>^v':
			neighborMap[(y, x)] = findNeighbors((y, x))

numNodes = len(neighborMap) + 1
while len(neighborMap) < numNodes:
	numNodes = len(neighborMap)
	for current in neighborMap:
		neighbors = neighborMap[current]
		if len(neighbors) == 2:
			id1 = (neighbors[0][0], neighbors[0][1])
			id2 = (neighbors[1][0], neighbors[1][1])

			linkFrom1ToCurrent = [l for l in neighborMap[id1] if l[0] == current[0] and l[1] == current[1]][0]
			linkFrom2ToCurrent = [l for l in neighborMap[id2] if l[0] == current[0] and l[1] == current[1]][0]
			distance = linkFrom1ToCurrent[2] + linkFrom2ToCurrent[2]

			neighborMap[id1].remove(linkFrom1ToCurrent)
			neighborMap[id1].append((id2[0], id2[1], distance, linkFrom1ToCurrent[3] + [(current[0], current[1])] + linkFrom2ToCurrent[3]))
			
			neighborMap[id2].remove(linkFrom2ToCurrent)
			neighborMap[id2].append((id1[0], id1[1], distance, linkFrom2ToCurrent[3] + [(current[0], current[1])] + linkFrom1ToCurrent[3]))

			del neighborMap[current]
			break

longestPath = 0
def dfs(start, end, path, distance = 0):
	global longestPath
	if start[0] == end[0] and start[1] == end[1]:
		if distance > longestPath:
			print('New longest path:', distance)
			longestPath = distance
		return
	for neighbor in neighborMap[(start[0], start[1])]:
		if (neighbor[0], neighbor[1]) not in path and not any(intermediate in path for intermediate in neighbor[3]):
			dfs(neighbor, end, path + neighbor[3] + [(neighbor[0], neighbor[1])], distance + neighbor[2])
	return longestPath

# Uncomment lines 15 - 18 for Part 1
dfs(start, end, [start])
print('Part 2:', longestPath)