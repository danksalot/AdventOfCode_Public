from copy import deepcopy

DIRECTIONS = [
	(-1, -1), #UP-LEFT
	(-1,  0), #UP
	(-1,  1), #UP-RIGHT
	( 0, -1), #LEFT
	( 0,  0), #CENTER
	( 0,  1), #RIGHT
	( 1, -1), #DOWN-LEFT
	( 1,  0), #DOWN	
	( 1,  1)  #DOWN-RIGHT
]

with open('Input') as inFile:
	lines = inFile.read().splitlines()

algorithm = [int(x == '#') for x in lines[0]]
grid = []

for line in lines[2:]:
	grid.append([int(x == '#') for x in line])

def expand(grid):
	newGrid = []
	newGrid.append([0] * (len(grid[0]) + 2))
	for row in grid:
		newGrid.append([0] + row + [0])
	newGrid.append([0] * (len(grid[0]) + 2))
	return newGrid

def enhancePixel(grid, y, x):
	neighbors = [(y + dy, x + dx) for dy, dx in DIRECTIONS]
	context = ''
	for neighbor in neighbors:
		if neighbor[0] < 0 or neighbor[0] >= len(grid) or neighbor[1] < 0 or neighbor[1] >= len(grid[0]):
			context += '0'
		else:
			context += str(grid[neighbor[0]][neighbor[1]])

	# context = ''.join([str(grid[neighbor[0]][neighbor[1]]) for neighbor in neighbors])
	# print('Enhancing pixel at y:', y, 'x:', x, 'Context:', context, '(', int(context, 2), ') becomes', algorithm[int(context, 2)])
	return algorithm[int(context, 2)]

def enhance(grid):
	grid = expand(grid)
	newGrid = deepcopy(grid)
	for y in range(len(newGrid)):
		for x in range(len(newGrid[0])):
			newGrid[y][x] = enhancePixel(grid, y, x)
	return newGrid

def countLitPixels(grid):
	count = 0
	for row in grid:
		count += sum([x for x in row])
	return count

def printGrid(grid):
	output = ''
	for row in grid:
		for char in row:
			output += '#' if char else '.'
		output += '\n'
	print(output)

print('\n')
printGrid(grid)
print('Lit Pixels:', countLitPixels(grid), '\n')

grid = enhance(grid)

printGrid(grid)
print('Lit Pixels:', countLitPixels(grid), '\n')

grid = enhance(grid)

printGrid(grid)
print('Part 1:', countLitPixels(grid))