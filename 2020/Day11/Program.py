DIRECTIONS = [
	(-1,  0), #UP
	( 0, -1), #LEFT
	( 0,  1), #RIGHT
	( 1,  0), #DOWN	
	(-1, -1), #UP-LEFT
	(-1,  1), #UP-RIGHT
	( 1, -1), #DOWN-LEFT
	( 1,  1)  #DOWN-RIGHT
]

def setupGrid(lines):
	return [[x for x in row] for row in lines]

def getNeighborsPart1(y, x):
	neighbors = [(y + dy, x + dx) for dy, dx in DIRECTIONS]
	return [coords for coords in neighbors if 0 <= coords[0] < sizeY and 0 <= coords[1] < sizeX]

def getNeighborsPart2(y, x):
	neighbors = []
	for dy, dx in DIRECTIONS:
		newY = y + dy
		newX = x + dx
		while 0 <= newY < sizeY and 0 <= newX < sizeX and grid[newY][newX] == '.':
			newY = newY + dy
			newX = newX + dx
		if 0 <= newY < sizeY and 0 <= newX < sizeX:
			neighbors.append((newY, newX))
	return neighbors

def calculateNewSeatStatus(neighbors, seatStatus, tolerance):
	if seatStatus == '.': return '.'
	elif seatStatus == 'L': return '#' if len([n for n in neighbors if grid[n[0]][n[1]] == '#']) == 0 else 'L'
	elif seatStatus == '#': return 'L' if len([n for n in neighbors if grid[n[0]][n[1]] == '#']) >= tolerance else '#'

with open('Input') as inFile:
	lines = inFile.read().splitlines()

grid = setupGrid(lines)
sizeY = len(grid)
sizeX = len(grid[0])
while True:
	newGrid = [[calculateNewSeatStatus(getNeighborsPart1(y, x), grid[y][x], 4) for x in range(sizeX)] for y in range(sizeY)]
	if grid == newGrid: break
	grid = newGrid
print('Part 1:', sum(g.count('#') for g in grid))

grid = setupGrid(lines)
while True:
	newGrid = [[calculateNewSeatStatus(getNeighborsPart2(y, x), grid[y][x], 5) for x in range(sizeX)] for y in range(sizeY)]
	if grid == newGrid: break
	grid = newGrid
print('Part 2:', sum(g.count('#') for g in grid))