DIRECTIONS = [
    (-1,  0), #UP
    ( 0, -1), #LEFT
    ( 0,  1), #RIGHT
    ( 1,  0), #DOWN
    (-1, -1), #UP-LEFT
    (-1,  1), #UP-RIGHT
    ( 1, -1), #DOWN-LEFT
    ( 1,  1), #DOWN-RIGHT
]

grid = []
flashes = []
size = 10

def getNeighborCoords(y, x):
	neighbors = [(y + dy, x + dx) for dx, dy in DIRECTIONS]
	neighbors = [(y, x) for y, x in neighbors if x >= 0 and x < size and y >= 0 and y < size]
	return neighbors

def flash(y, x):
	# print('Flash', y, x)
	for neighbor in getNeighborCoords(y, x):
		nY = neighbor[0]
		nX = neighbor[1]
		grid[nY][nX] += 1
		if grid[nY][nX] > 9 and (nY, nX) not in flashes:
			# print('Chain - appending to flashes', nY, nX)
			flashes.append((nY, nX))
			# print('Flashes:', flashes)
			#flash(nY, nX)

def step(y, x):
	# print('Step', y, x)
	grid[y][x] += 1
	if grid[y][x] > 9:
		# print('Appending to flashes', y, x)
		flashes.append((y, x))

with open('Input') as inFile:
	lines = inFile.read().splitlines()
	size = len(lines)

for line in lines:
	grid.append([int(x) for x in line])

totalFlashes = 0

# print(grid)
for iteration in range(2000):
	flashes = []
	for y in range(size):
		for x in range(size):
			step(y, x)

	flashIndex = 0
	while flashIndex < len(flashes):
		fl = flashes[flashIndex]
		flash(fl[0], fl[1])
		flashIndex += 1

	for fl in flashes:
		grid[fl[0]][fl[1]] = 0
	totalFlashes += len(flashes)
	# print(grid)

	if iteration == 99:
		print('Part 1:', totalFlashes)

	if len(flashes) == size * size:
		print('Part 2:', iteration + 1)
		break