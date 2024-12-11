import heapq

def getNeighbors(grid, coords):
	y, x = coords
	adjacentNodes = [(y - 1, x),(y + 1, x),(y, x - 1),(y, x + 1)]

	return [
		(grid[newY][newX], (newY, newX)) for newY, newX in adjacentNodes
		if newY >= 0 and newY < len(grid[0]) and newX >= 0 and newX < len(grid)
	]

def dijkstra(grid, start, end):
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
		for edgeCost, next in getNeighbors(grid, cur):
			if next not in visited:
				heapq.heappush(q, (cost + edgeCost, next))

	return visited[end]

grid = []

with open('Input') as inFile:
	lines = inFile.read().splitlines()

for line in lines:
	grid.append([int(x) for x in line])

size = len(grid)
print('Part 1:', dijkstra(grid, (0,0), (size-1,size-1)))

def inc(num, increase):
	for x in range(increase):
		num += 1
		if num == 10:
			num = 1
	return num

largeGrid = []
for row in grid:
	largeGrid.append([x for x in row] + [inc(x,1) for x in row] + [inc(x,2) for x in row] + [inc(x,3) for x in row] + [inc(x,4) for x in row])

for i in range(4*size):
	largeGrid.append([inc(x,1) for x in largeGrid[i]])

largeSize = len(largeGrid)
print('Part 2:', dijkstra(largeGrid, (0,0), (largeSize-1,largeSize-1)))