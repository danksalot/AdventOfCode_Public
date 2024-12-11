def rotate(l, n):
    return l[n:] + l[:n]

def createRectangle(grid, y, x):
	for i in range(x):
		for j in range(y):
			grid[i][j] = 1
	return grid

def rotateRow(grid, index, distance):
	grid[index] = rotate(grid[index], -distance)
	return grid

def rotateColumn(grid, index, distance):
	rotated = zip(*grid[::-1])
	rotated[index] = rotate(rotated[index], distance)
	rotated = zip(*rotated[::-1])
	rotated = zip(*rotated[::-1])
	grid = [list(a) for a in zip(*rotated[::-1])] 
	return grid

grid = [[0 for x in range(50)] for y in range(6)]

with open("Input") as inputFile:
	lines = inputFile.readlines()
    
for line in lines:
	parts = line.split()
	if parts[0] == "rect":
		dimensions = parts[1].split('x')
		grid = createRectangle(grid, int(dimensions[0]), int(dimensions[1]))
	elif parts[0] == "rotate":
		if parts[1] == "row":
			grid = rotateRow(grid, int(parts[2][2:]), int(parts[4]))
		else:
			grid = rotateColumn(grid, int(parts[2][2:]), int(parts[4]))

print "Number of pixels lit:", sum(sum(x) for x in grid), "\n"
print '\n'.join(''.join('#' if p else ' '  for p in row) for row in grid)
