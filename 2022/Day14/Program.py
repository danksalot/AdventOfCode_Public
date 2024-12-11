with open('Input') as inFile:
	lines = inFile.read().splitlines()

grid = []
at_rest = 0

def initializeGrid():
	global grid
	grid = [['.' for x in range(0,1000)] for y in range(0,183)]
	
	for line in lines:
		segments = line.split(' -> ')
		for i in range(1, len(segments)):
			x1, y1 = map(int, segments[i-1].split(','))
			x2, y2 = map(int, segments[i].split(','))
			if y1 == y2:
				for x in range(min(x1, x2), max(x1, x2)+1): grid[y1][x] = '#'
			else:
				for y in range(min(y1, y2), max(y1, y2)+1): grid[y][x1] = '#'

def canFall(coords):
	y, x = coords
	if grid[y+1][x] == '.':
		return (y+1, x)
	elif grid[y+1][x-1] == '.':
		return (y+1,x-1)
	elif grid[y+1][x+1] == '.':
		return (y+1,x+1)
	else:
		return None

def drop():
	global at_rest
	coords = (0, 500)
	while coords:		
		result = canFall(coords)
		if result == None:
			grid[coords[0]][coords[1]] = 'o'
			at_rest += 1
			break
		elif result[0] >= len(grid) - 1:
			return True
		else:
			coords = result
	return False

def dropV2():
	global at_rest
	coords = (0, 500)
	while coords:		
		result = canFall(coords)
		if result == None:
			grid[coords[0]][coords[1]] = 'o'
			at_rest += 1
			if coords == (0, 500):				
				return True
			break
		else:
			coords = result
	return False

initializeGrid()
finished = False
while not finished:
	finished = drop()
print('Part 1:', at_rest)

initializeGrid()
at_rest = 0
finished = False
for x in range(0,1000):
	grid[len(grid)-1][x] = '#'
while not finished:
	finished = dropV2()
print('Part 2:', at_rest)

# for y in range(len(grid)):
# 	print(''.join(grid[y][310:690]))

