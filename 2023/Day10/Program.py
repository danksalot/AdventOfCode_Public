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

# Create an expanded grid where & is added above and to the right of each space
# Replace the & with a pipe if needed to connect to a pipe above or to the right
expandedGrid = []
for y in range(len(grid)):
	expandedGrid.append(['&']*(len(grid[0])*2))
	expandedGrid.append([])
	for x in range(len(grid[y])):
		spaceValue = grid[y][x]
		expandedGrid[-1].append(spaceValue)
		expandedGrid[-1].append('&')
		if spaceValue in ['|','L', 'J']:
			expandedGrid[-2][x*2] = '|'
		if spaceValue in ['-', 'F', 'L']:
			expandedGrid[-1][-1] = '-'

def isExterior(y, x):
	if y == 0 or y == len(expandedGrid)-1 or x == 0 or x == len(expandedGrid[y])-1:
		return True
	
	for direction in directions:
		if expandedGrid[y+direction[0]][x+direction[1]] == '0':
			return True
		
	return False

# Replace all '&' and '.' with 0 if they are on the exterior of the grid
keepGoing = True
while keepGoing == True:
	keepGoing = False
	for y in range(len(expandedGrid)):
		for x in range(len(expandedGrid[y])):
			if expandedGrid[y][x] in ['&', '.'] and isExterior(y, x):
				expandedGrid[y][x] = '0'
				keepGoing = True

# All of the remaining '.' are interior spaces
print('Part 2:', sum([x.count('.') for x in expandedGrid]))
