directions = [[1, 0], [0, 1], [-1, 0], [0, -1]] # DOWN, RIGHT, UP, LEFT
extraLayers = 200

with open('Input') as inFile:
	lines = map(str.rstrip, inFile.readlines())

################################################
## PART 1
################################################

grid = []
counter = 0
currentDir = 2
currentPos = [12 + extraLayers, 12 + extraLayers]

# Setup the grid
for i in range(extraLayers):
	grid.append(['.'] * (2 * extraLayers + 25))

for line in lines:
	gridLine = ['.'] * extraLayers
	gridLine += [x for x in list(line)]
	gridLine += ['.'] * extraLayers
	grid.append(gridLine)

for i in range(extraLayers):
	grid.append(['.'] * (2 * extraLayers + 25))

# Perform iterations
for i in range(10000):
	if grid[currentPos[0]][currentPos[1]] == '#':
		currentDir = (currentDir - 1) % 4
		grid[currentPos[0]][currentPos[1]] = '.'
	elif grid[currentPos[0]][currentPos[1]] == '.':
		counter += 1
		currentDir = (currentDir + 1) % 4
		grid[currentPos[0]][currentPos[1]] = '#'

	newY = currentPos[0] + directions[currentDir][0]
	newX = currentPos[1] + directions[currentDir][1]
	currentPos = [newY, newX]

print 'Part1:', counter

################################################
## PART 2
################################################

grid = []
counter = 0
currentDir = 2
currentPos = [12 + extraLayers, 12 + extraLayers]

# Setup the grid
for i in range(extraLayers):
	grid.append(['.'] * (2 * extraLayers + 25))

for line in lines:
	gridLine = ['.'] * extraLayers
	gridLine += [x for x in list(line)]
	gridLine += ['.'] * extraLayers
	grid.append(gridLine)

for i in range(extraLayers):
	grid.append(['.'] * (2 * extraLayers + 25))

# Perform iterations
for i in range(10000000):
	if grid[currentPos[0]][currentPos[1]] == '#':
		currentDir = (currentDir - 1) % 4
		grid[currentPos[0]][currentPos[1]] = 'F'
	elif grid[currentPos[0]][currentPos[1]] == '.':
		currentDir = (currentDir + 1) % 4
		grid[currentPos[0]][currentPos[1]] = 'W'
	elif grid[currentPos[0]][currentPos[1]] == 'W':
		counter += 1
		grid[currentPos[0]][currentPos[1]] = '#'
	elif grid[currentPos[0]][currentPos[1]] == 'F':
		currentDir = (currentDir + 2) % 4
		grid[currentPos[0]][currentPos[1]] = '.'

	newY = currentPos[0] + directions[currentDir][0]
	newX = currentPos[1] + directions[currentDir][1]
	currentPos = [newY, newX]

print 'Part2:', counter