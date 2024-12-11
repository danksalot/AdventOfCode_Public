def pruneDeadEnds(grid, side):
	walls = sum(map(sum, grid))
	while True:
		grid = prune(grid, side)
		if walls != sum(map(sum, grid)):
			walls = sum(map(sum, grid))
		else:
			break

def prune(grid, side):
	for x in range(1, side-1):
		for y in range(1, side-1):
			if grid[y][x] == 0 and \
				(grid[y-1][x] == 1 and grid[y+1][x] == 1 and grid[y][x-1] == 1) or \
				(grid[y-1][x] == 1 and grid[y+1][x] == 1 and grid[y][x+1] == 1) or \
				(grid[y-1][x] == 1 and grid[y][x-1] == 1 and grid[y][x+1] == 1) or \
				(grid[y+1][x] == 1 and grid[y][x-1] == 1 and grid[y][x+1] == 1):
			   		grid[y][x] = 1
					
	return grid


side = 50
grid = [[0 for x in range(side)] for y in range(side)]

for x in range(side):
	for y in range(side):
		grid[y][x] = (bin)(x*x + 3*x + 2*x*y + y + y*y + 1358)[2:].count('1') % 2

print '\n'.join(''.join(' ' if p else 'O'  for p in row) for row in grid)

pruneDeadEnds(grid, side)

print "\nPruned:"
print '\n'.join(''.join('#' if p else ' '  for p in row) for row in grid)
