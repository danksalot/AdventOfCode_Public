with open('Input') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

heading = 2 # 0 = up, 1 = right, 2 = down, 3 = left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # (Y, X)

def followPipe(y, x, steps):
	global heading
	if lines[y][x] == 'F':
		if heading == 0:
			heading = 1
		elif heading == 3:
			heading = 2
	elif lines[y][x] == 'J':
		if heading == 2:
			heading = 3
		elif heading == 1:
			heading = 0
	elif lines[y][x] == '7':
		if heading == 0:
			heading = 3
		elif heading == 1:
			heading = 2
	elif lines[y][x] == 'L':
		if heading == 2:
			heading = 1
		elif heading == 3:
			heading = 0
		
	return y + directions[heading][0], x + directions[heading][1], steps + 1

start = None
for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] == 'S':
			start = (y, x)

grid = [ ['.']*len(lines[0]) for i in range(len(lines)) ]

steps = 0
currentY, currentX, steps = followPipe(start[0], start[1], steps)
grid[start[0]][start[1]] = '|' # Look at the input and determine what symbol this should be to connect to other pipes
while lines[currentY][currentX] != 'S' and steps != 0:
	grid[currentY][currentX] = lines[currentY][currentX]
	currentY, currentX, steps = followPipe(currentY, currentX, steps)	
	
print('Part 1:', steps//2)

def isInterior(y, x):
	return (grid[y][:x].count('|') + grid[y][:x].count('F') + grid[y][:x].count('7')) % 2 == 1

interiorSpaces = 0
for y in range(len(grid)):
	for x in range(len(grid[y])):
		if grid[y][x] == '.' and isInterior(y, x):
			interiorSpaces += 1

print('Part 2:', interiorSpaces)
