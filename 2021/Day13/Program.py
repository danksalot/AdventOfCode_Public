with open('Input') as inFile:
	lines = inFile.read().splitlines()

grid = [['.'] * 1311 for row in range(895)]
folds = []

def horizontalFold(grid, index):	
	newGrid = [['.'] * len(grid[0]) for row in range(len(grid) - index - 1)]
	for yOffset in range(index + 1):
		for x in range(len(grid[0])):
			if '#' in [grid[index+yOffset][x], grid[index-yOffset][x]]:
				newGrid[index-yOffset][x] = '#'
	return newGrid

def verticalFold(grid, index):	
	newGrid = [['.'] * (len(grid[0]) - index - 1) for row in range(len(grid))]
	for xOffset in range(index + 1):
		for y in range(len(grid)):
			if '#' in [grid[y][index+xOffset], grid[y][index-xOffset]]:
				newGrid[y][index-xOffset] = '#'
	return newGrid

for line in lines:
	if ',' in line:
		x, y = line.split(',')
		grid[int(y)][int(x)] = '#'
	elif 'fold' in line:
		fold, along, instr = line.split(' ')
		axis, index = instr.split('=')
		folds.append((axis, int(index)))

for i in range(len(folds)):
	if folds[i][0] == 'x':
		grid = verticalFold(grid, folds[i][1])
	else:
		grid = horizontalFold(grid, folds[i][1])

	if i == 0:
		count = 0
		for row in grid:
			for spot in row:
				if spot == '#':
					count += 1
		print('Part 1:', count)

print('Part 2:')
for row in grid:
	print(''.join(row))

