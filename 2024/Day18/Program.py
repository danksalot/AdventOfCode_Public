import heapq

with open('Input') as inFile:
	lines = [line.rstrip() for line in inFile.readlines()]

size = 70
nanoseconds = 1024
bytes = []
grid = [['.' for i in range(size + 1)] for j in range(size + 1)]
for line in lines:
	bytes.append((int(line.split(',')[1]), int(line.split(',')[0])))

for step in range(nanoseconds):
	y, x = bytes[step]
	grid[y][x] = '#'
	
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W
def getNeighbors(position):
	y, x = position
	adjacentNodes = []
	for direction in DIRECTIONS:
		if 0 <= y + direction[0] <= size and 0 <= x + direction[1] <= size:
			if grid[y + direction[0]][x + direction[1]] == '.':
				adjacentNodes.append((y + direction[0], x + direction[1]))
	return adjacentNodes

def dijkstra(start, end):
	visited = {}
	q = []
	heapq.heappush(q, (0, start))

	while q:
		cost, cur = heapq.heappop(q)
		if cur in visited:
			continue
		visited[cur] = cost
		if cur == end:
			break		
		for next in getNeighbors(cur):
			heapq.heappush(q, (cost + 1, next))
	return visited[end] if end in visited else None

print("Part 1:", dijkstra((0, 0), (size, size)))

for i in range(nanoseconds + 1, len(bytes) + 1):
	y, x = bytes[i]
	grid[y][x] = '#'
	shortest = dijkstra((0, 0), (size, size))
	if shortest == None:
		print("Part 2: " + str(x) + ',' + str(y))
		break
