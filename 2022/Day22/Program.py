with open('Input') as inFile:
	lines = inFile.read().splitlines()

with open('Input2') as inFile:
	instructions = inFile.read().replace('R', ' R ').replace('L', ' L ').split(' ')

walls = []
spaces = []
wraps = {}
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DEGS = { 'R': 1, 'L': -1}
height = len(lines)
width = max([len(x) for x in lines])

for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] == '#':
			walls.append((y, x))
		elif lines[y][x] == '.':
			spaces.append((y, x))

def initializeWraps(walls, spaces, wraps, height, width):
	allMap = walls + spaces
	wraps.clear()
	
	# Horizontal
	for curY in range(height):
		leftBorder = min([x for y, x in allMap if y == curY])
		rightBorder = max([x for y, x in allMap if y == curY])
		if lines[curY][leftBorder] == '.' and lines[curY][rightBorder] == '.':
			wraps[(curY, leftBorder-1, 2)] = (curY, rightBorder, 2)
			wraps[(curY, rightBorder+1, 0)] = (curY, leftBorder, 0)

	# Vertical
	for curX in range(width):
		topBorder = min([y for y, x in allMap if x == curX])
		bottomBorder = max([y for y, x in allMap if x == curX])
		if lines[topBorder][curX] == '.' and lines[bottomBorder][curX] == '.':
			wraps[(topBorder-1, curX, 3)] = (bottomBorder, curX, 3)
			wraps[(bottomBorder+1, curX, 1)] = (topBorder, curX, 1)

def initializeWrapsV2(walls, spaces, wraps, height, width):
	allMap = walls + spaces
	wraps.clear()

	# Faces
	#  12
	#  3
	# 45
	# 6

	# Face 1 -> Face 4
	curX = 50
	newX = 0
	for curY in range(50):		
		newY = 149 - curY
		if lines[curY][curX] == '.' and lines[newY][newX] == '.':
			wraps[(curY, curX-1, 2)] = (newY, newX, 0)
			wraps[(newY, newX-1, 2)] = (curY, curX, 0)

	# Face 1 -> Face 6
	curY = 0
	newX = 0
	for curX in range(50, 100):		
		newY = curX + 100
		if lines[curY][curX] == '.' and lines[newY][newX] == '.':
			wraps[(curY-1, curX, 3)] = (newY, newX, 0)
			wraps[(newY, newX-1, 2)] = (curY, curX, 1)	

	# Face 2 -> Face 5
	curX = 149
	newX = 99
	for curY in range(50):		
		newY = 149 - curY
		if lines[curY][curX] == '.' and lines[newY][newX] == '.':
			wraps[(curY, curX+1, 0)] = (newY, newX, 2)
			wraps[(newY, newX+1, 0)] = (curY, curX, 2)

	# Face 2 -> Face 6
	curY = 0
	newY = 199
	for curX in range(100, 150):		
		newX = curX - 100
		if lines[curY][curX] == '.' and lines[newY][newX] == '.':
			wraps[(curY-1, curX, 3)] = (newY, newX, 3)
			wraps[(newY+1, newX, 1)] = (curY, curX, 1)

	# Face 3 -> Face 2
	curX = 99
	newY = 49
	for curY in range(50, 100):		
		newX = curY + 50
		if lines[curY][curX] == '.' and lines[newY][newX] == '.':
			wraps[(curY, curX+1, 0)] = (newY, newX, 3)
			wraps[(newY+1, newX, 1)] = (curY, curX, 2)

	# Face 3 -> Face 4
	curX = 50
	newY = 100
	for curY in range(50, 100):		
		newX = curY - 50
		if lines[curY][curX] == '.' and lines[newY][newX] == '.':
			wraps[(curY, curX-1, 2)] = (newY, newX, 1)
			wraps[(newY-1, newX, 3)] = (curY, curX, 0)

	# Face 5 -> Face 6
	curY = 149
	newX = 49
	for curX in range(50, 100):		
		newY = curX + 100
		if lines[curY][curX] == '.' and lines[newY][newX] == '.':
			wraps[(curY+1, curX, 1)] = (newY, newX, 2)
			wraps[(newY, newX+1, 0)] = (curY, curX, 3)

def calculatePassword(pos):
	y, x, h = pos
	return ((y+1) * 1000) + ((x+1) * 4) + h

def turn(pos, rotation):
	y, x, h = pos
	newHeading = (h + rotation) % 4
	return (y, x, newHeading)

def calcNewPosition(pos):
	global spaces, walls, wraps
	y, x, h = pos
	dy, dx = DIRS[h]
	newPosition = (y+dy, x+dx)
	newPositionWithHeading = (y+dy, x+dx, h)
	if newPosition in spaces:
		return newPositionWithHeading
	elif newPositionWithHeading in wraps:
		newY, newX, newHeading = wraps[newPositionWithHeading]
		return wraps[newPositionWithHeading]
	else:
		return (y, x, h)

def move(pos, numSteps):
	y, x, h = pos
	for i in range(numSteps):
		y, x, h = calcNewPosition((y, x, h))
	return (y, x, h)

initializeWraps(walls, spaces, wraps, height, width)
pos = (0, min([x for y, x in spaces if y == 0]), 0)
for instr in instructions:	
	if instr.isdigit():
		pos = move(pos, int(instr))
	else:
		pos = turn(pos, DEGS[instr])
print('Part 1:', calculatePassword(pos))

initializeWrapsV2(walls, spaces, wraps, height, width)
pos = (0, min([x for y, x in spaces if y == 0]), 0)
for instr in instructions:	
	if instr.isdigit():
		pos = move(pos, int(instr))
	else:
		pos = turn(pos, DEGS[instr])
print('Part 2:', calculatePassword(pos))