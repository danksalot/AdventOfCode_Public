
with open('Input') as inFile:
	lines = [list(map(int, line.strip())) for line in inFile.readlines()]

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)] # N, S, W, E
def findNeighbors(y, x):
	neighbors = [(y+dy, x+dx) for dy, dx in DIRS]
	return [(ny, nx) for ny, nx in neighbors if 0 <= ny < len(lines) and 0 <= nx < len(lines[0]) and lines[ny][nx] == lines[y][x] + 1]

def countReachableNines(y, x):
	neighbors = findNeighbors(y, x)
	reachableNines = set()
	while len(neighbors) > 0:
		ny, nx = neighbors.pop()
		if lines[ny][nx] == 9:
			reachableNines.add((ny, nx))
		else:
			neighbors.extend(findNeighbors(ny, nx))
	return len(reachableNines)

def findDistinctTrails(path):
	y, x = path[-1]
	neighbors = findNeighbors(y, x)
	distinctPaths = set()
	while len(neighbors) > 0:
		ny, nx = neighbors.pop()
		if lines[ny][nx] == 9:
			distinctPaths.add(((y, x), (ny, nx)))
		else:
			paths = findDistinctTrails([(ny, nx)])
			for path in paths:
				distinctPaths.add(((y, x)) + path)
	return distinctPaths

trailheads = {}
for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] == 0:
			trailheads[(y, x)] = 0

print("Part 1:", sum(countReachableNines(y, x) for y, x in trailheads))
print("Part 2:", sum(len(findDistinctTrails([(y, x)])) for y, x in trailheads))
