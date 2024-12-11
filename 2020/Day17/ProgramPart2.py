directions = set(
	(x, y, z, w)
	for x in (-1, 0, 1)
	for y in (-1, 0, 1)
	for z in (-1, 0, 1)
	for w in (-1, 0, 1)
)
directions.remove((0, 0, 0, 0))
DIRECTIONS = tuple(directions)

def setupGrid(lines):
	return [[[[x for x in row] for row in lines]]]

def getNeighbors(x, y, z, w):
	neighbors = [(x + dx, y + dy, z + dz, w + dw) for dx, dy, dz, dw in DIRECTIONS]
	return [coords for coords in neighbors if 0 <= coords[0] < sizeX and 0 <= coords[1] < sizeY and 0 <= coords[2] < sizeZ and 0 <= coords[3] < sizeW]

def calculateNewStatus(neighbors, status):
	if status == '.': return '#' if len([n for n in neighbors if grid[n[3]][n[2]][n[1]][n[0]] == '#']) == 3 else '.'
	elif status == '#': return '#' if len([n for n in neighbors if grid[n[3]][n[2]][n[1]][n[0]] == '#']) in [2, 3] else '.'

def increaseGridSize():
	global sizeX
	global sizeY
	global sizeZ
	global sizeW
	grid.insert(0, [[['.' for i in range(sizeX)] for j in range(sizeY)] for j in range(sizeZ)])
	grid.append([[['.' for i in range(sizeX)] for j in range(sizeY)] for j in range(sizeZ)])
	for time in grid:
		time.insert(0, [['.' for i in range(sizeX)] for j in range(sizeY)])
		time.append([['.' for i in range(sizeX)] for j in range(sizeY)])
		for layer in time:
			layer.insert(0, ['.' for i in range(sizeX)])
			layer.append(['.' for i in range(sizeX)])
			for row in layer:
				row.insert(0, '.')
				row.append('.')
	sizeW = len(grid)
	sizeZ = len(grid[0])
	sizeY = len(grid[0][0])
	sizeX = len(grid[0][0][0])	

with open('Input') as inFile:
	lines = inFile.read().splitlines()

grid = setupGrid(lines)
sizeW = len(grid)
sizeZ = len(grid[0])
sizeY = len(grid[0][0])
sizeX = len(grid[0][0][0])

for t in range(6):
	increaseGridSize()
	newGrid = [[[[calculateNewStatus(getNeighbors(x, y, z, w), grid[w][z][y][x]) for x in range(sizeX)] for y in range(sizeY)] for z in range(sizeZ)] for w in range(sizeW)]
	grid = newGrid

total = sum(row.count('#') for time in grid for layer in time for row in layer)
print('Part 2:', total)