
with open('Input') as inFile:
	lines = inFile.read().splitlines()

grid = []
for line in lines:
	grid.append([x for x in line])

eastHerd = []
southHerd = []
moves = []
height = len(grid)
width = len(grid[0])

def executeMoves(grid, moves):
	for move in moves:
		y, x, nY, nX, symbol = move
		grid[y][x] = '.'
		grid[nY][nX] = symbol
	return grid

def tryMoveEast(grid, cuke, moves):
	y, x = cuke
	nX = (x + 1) % width
	if grid[y][nX] == '.':
		moves.append((y, x, y, nX, '>'))
	return moves

def tryMoveSouth(grid, cuke, moves):
	y, x = cuke
	nY = (y + 1) % height
	# print('Checking if cuke at', y, x, 'can move South to', nY, x)
	if grid[nY][x] == '.':
		# print('Yes!  Cuke at', y, x, 'can move South to', nY, x)
		moves.append((y, x, nY, x, 'v'))
	return moves

for y in range(height):
	for x in range(width):
		if grid[y][x] == '>':
			eastHerd.append((y, x))
		elif grid[y][x] == 'v':
			southHerd.append((y, x))

print('East Herd')
print(eastHerd)
print('South Herd')
print(southHerd)

for row in grid:
		print(''.join(row))
for i in range(99999):
	numMoves = 0
	moves = []
	for cuke in eastHerd:
		moves = tryMoveEast(grid, cuke, moves)
	numMoves += len(moves)
	grid = executeMoves(grid, moves)
	moves = []
	for cuke in southHerd:
		moves = tryMoveSouth(grid, cuke, moves)
	numMoves += len(moves)
	grid = executeMoves(grid, moves)
	if numMoves == 0:
		print('No cukes moved on step', i + 1)
		break
	else:
		eastHerd = []
		southHerd = []
		for y in range(height):
			for x in range(width):
				if grid[y][x] == '>':
					eastHerd.append((y, x))
				elif grid[y][x] == 'v':
					southHerd.append((y, x))

	print('After step', i + 1)
	for row in grid:
		print(''.join(row))