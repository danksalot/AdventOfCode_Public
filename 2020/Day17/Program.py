directions = set(
		(x, y, z)
		for x in (-1, 0, 1)
		for y in (-1, 0, 1)
		for z in (-1, 0, 1)
	)
directions.remove((0, 0, 0))
DIRECTIONS = tuple(directions)

def setupGrid(lines):
	return [[[x for x in row] for row in lines]]

def getNeighbors(x, y, z):
	neighbors = [(x + dx, y + dy, z + dz) for dx, dy, dz in DIRECTIONS]
	return [coords for coords in neighbors if 0 <= coords[0] < sizeX and 0 <= coords[1] < sizeY and 0 <= coords[2] < sizeZ]

def calculateNewStatus(neighbors, status):
	if status == '.': return '#' if len([n for n in neighbors if grid[n[2]][n[1]][n[0]] == '#']) == 3 else '.'
	elif status == '#': return '#' if len([n for n in neighbors if grid[n[2]][n[1]][n[0]] == '#']) in [2, 3] else '.'

def increaseGridSize():
	global sizeX
	global sizeY
	global sizeZ
	grid.insert(0, [['.' for i in range(sizeX)] for j in range(sizeY)])
	grid.append([['.' for i in range(sizeX)] for j in range(sizeY)])
	for layer in grid:
		layer.insert(0, ['.' for i in range(sizeX)])
		layer.append(['.' for i in range(sizeX)])
		for row in layer:
			row.insert(0, '.')
			row.append('.')
	sizeZ = len(grid)
	sizeY = len(grid[0])
	sizeX = len(grid[0][0])	

with open('Input') as inFile:
	lines = inFile.read().splitlines()

grid = setupGrid(lines)
sizeZ = len(grid)
sizeY = len(grid[0])
sizeX = len(grid[0][0])

for t in range(6):
	increaseGridSize()
	newGrid = [[[calculateNewStatus(getNeighbors(x, y, z), grid[z][y][x]) for x in range(sizeX)] for y in range(sizeY)] for z in range(sizeZ)]
	grid = newGrid

total = sum(row.count('#') for layer in grid for row in layer)
print('Part 1:', total)