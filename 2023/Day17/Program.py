import heapq

with open('Input') as inFile:
	grid = [[int(x) for x in y.strip()] for y in inFile.readlines()]
	
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Right, Down, Left, Up
minStraightPath = 0
maxStraightPath = 3

def getNeighbors(y, x, heading, stepsInHeading):
	neighbors = []
	for newHeading, dir in enumerate(directions):
		newY = y + dir[0]
		newX = x + dir[1]
		if max(heading, newHeading) - min(heading, newHeading) == 2: # can't turn around
			continue
		if 0 <= newY < len(grid) and 0 <= newX < len(grid[0]): # stay in bounds
			if newHeading != heading and stepsInHeading >= minStraightPath: # if turning
				neighbors.append((newY, newX, newHeading, 1))
			elif newHeading == heading and stepsInHeading < maxStraightPath: # if going straight
				neighbors.append((newY, newX, newHeading, stepsInHeading + 1))
	return neighbors
	
def findShortestPath(start, end):
	visited = {}
	queue = [(0, start[0], start[1], 0, 0, [])]
	while queue:
		dist, y, x, heading, stepsInHeading, prev = heapq.heappop(queue)
		if (y, x) == end and stepsInHeading >= minStraightPath:
			return dist
		if (y, x, heading, stepsInHeading) in visited:
			continue
		visited[(y, x, heading, stepsInHeading)] = dist
		for neighbor in getNeighbors(y, x, heading, stepsInHeading):
			if neighbor not in visited:
				newDist = dist + grid[neighbor[0]][neighbor[1]]
				heapq.heappush(queue, (newDist, neighbor[0], neighbor[1], neighbor[2], neighbor[3], prev + [(y, x)]))

start = (0, 0)
end = (len(grid) - 1, len(grid[0]) - 1)

print('Part 1:', findShortestPath(start, end))
minStraightPath = 4
maxStraightPath = 10
print('Part 2:', findShortestPath(start, end))
