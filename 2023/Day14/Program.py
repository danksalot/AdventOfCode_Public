with open('Input') as inFile:
	lines = inFile.readlines()

grid = [[x for x in line.strip()] for line in lines]
roundRocks = []
squareRocks = []

def weighGrid():
	global grid
	weight = 0
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == 'O':
				weight += (len(grid) - y)
	return weight

def inBounds(pos):
	return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def tiltGrid(direction):
	global grid
	global roundRocks
	shouldReverse = direction[0] == 1 or direction[1] == 1
	roundRocks.sort(key = lambda x: (x[0], x[1]), reverse = shouldReverse)
	for idx in range(len(roundRocks)):
		newY = roundRocks[idx][0] + direction[0]
		newX = roundRocks[idx][1] + direction[1]

		while inBounds((newY, newX)) and grid[newY][newX] == '.':
			grid[newY][newX] = 'O'
			grid[roundRocks[idx][0]][roundRocks[idx][1]] = '.'
			roundRocks[idx] = (newY, newX)

			newY = roundRocks[idx][0] + direction[0]
			newX = roundRocks[idx][1] + direction[1]

def findCycle(n, minSpin):
	global grid
	weights = []
	for i in range(n):
		tiltGrid((-1, 0))
		tiltGrid((0, -1))
		tiltGrid((1, 0))
		tiltGrid((0, 1))
		if i >= minSpin:
			weights.append(weighGrid())
			if len(weights) % 2 == 0 and weights == weights[:len(weights) // 2] + weights[:len(weights) // 2]:
				return weights[:len(weights) // 2]
		
for y in range(len(grid)):
	for x in range(len(grid[y])):
		if grid[y][x] == 'O':
			roundRocks.append((y, x))
		elif grid[y][x] == '#':
			squareRocks.append((y, x))

tiltGrid((-1, 0))
print('Part 1:', weighGrid())

cycle = findCycle(1000000000, minSpin = 1000)
index = (1000000000 - 1000) % len(cycle) - 1
print('Part 2:', cycle[index])
