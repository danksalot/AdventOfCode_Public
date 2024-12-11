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

size = 50

def getNeighbors(y, x):
	neighbors = [(y + dy, x + dx) for dy, dx in DIRECTIONS]
	return [coords for coords in neighbors if 0 <= coords[0] < size and 0 <= coords[1] < size]

def printGrid():
	for i in range(size):
		print(''.join(grid[i]))

def setupGrid(lines):
	grid = []
	for line in lines:
		temp = []
		for char in line:
			temp.append(char)
		grid.append(temp)
	return grid

def runForMinutes(lines, numMinutes):
	grid = setupGrid(lines)
	for i in range(numMinutes):
		newGrid = [[0 for x in range(size)] for y in range(size)]
		for y in range(size):
			for x in range(size):
				neighbors = getNeighbors(y, x)
				if grid[y][x] == '.':
					newGrid[y][x] = '|' if len([n for n in neighbors if grid[n[0]][n[1]] == '|']) >= 3 else '.'
				elif grid[y][x] == '|':
					newGrid[y][x] = '#' if len([n for n in neighbors if grid[n[0]][n[1]] == '#']) >= 3 else '|'
				elif grid[y][x] == '#':
					newGrid[y][x] = '#' if any([n for n in neighbors if grid[n[0]][n[1]] == '#']) and any([n for n in neighbors if grid[n[0]][n[1]] == '|']) else '.'
		grid = newGrid
		#printGrid()
		#print('Score:', sum(g.count('|') for g in grid) * sum(g.count('#') for g in grid), 'i:', i)
	return sum(g.count('|') for g in grid) * sum(g.count('#') for g in grid)


with open('Input') as inFile:
	lines = inFile.read().splitlines()

print('Part 1:', runForMinutes(lines, 10))

# Running the above algorithm and printing out the scores, I found that a 28-minute pattern emerged starting at minute 582.
afterPatternStarts = 1000000000 - 582
stepsIntoPattern = afterPatternStarts % 28
minStepWithSameScore = 582 + stepsIntoPattern

print('Part 2:', runForMinutes(lines, minStepWithSameScore))