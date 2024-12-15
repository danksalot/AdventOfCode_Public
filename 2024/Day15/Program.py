
with open('Input') as inFile:
	lines = inFile.read().split('\n\n')
	
moves = ''.join(lines[1].split('\n'))
grid = lines[0].split('\n')

DIRECTIONS = {'^': [-1, 0], 'v': [1, 0], '<': [0, -1], '>': [0, 1]}

walls = []
boxes = []
twoWideBoxes = []
freeSpaces = []
robot = []

for y in range(len(grid)):
	for x in range(len(grid[y])):
		if grid[y][x] == '#':
			walls.append([y, x])
		elif grid[y][x] == 'O':
			boxes.append([y, x])
		elif grid[y][x] == '.':
			freeSpaces.append([y, x])
		elif grid[y][x] == '@':
			robot = [y, x]

def moveRobot(move):
	global robot
	boxesToPush = []
	direction = DIRECTIONS[move]
	newPos = [robot[0] + direction[0], robot[1] + direction[1]]
	canMove = False
	while newPos not in walls:
		if newPos in boxes:
			boxesToPush.append(boxes.index(newPos))
			newPos = [newPos[0] + direction[0], newPos[1] + direction[1]]
		else:
			canMove = True
			break
	if canMove:
		robot = [robot[0] + direction[0], robot[1] + direction[1]]
		for boxIdx in boxesToPush:
			boxes[boxIdx] = [boxes[boxIdx][0] + direction[0], boxes[boxIdx][1] + direction[1]]

def drawGrid(gridToDraw):
	for y in range(len(gridToDraw)):
		for x in range(len(gridToDraw[y])):
			if [y, x] in walls:
				print('#', end='')
			elif [y, x] in boxes:
				print('O', end='')
			elif [y, x] in twoWideBoxes:
				print('[', end='')
			elif [y, x-1] in twoWideBoxes:
				print(']', end='')
			elif [y, x] == robot:
				print('@', end='')			
			else:
				print('.', end='')
		print()

def calcGPSTotal():
	total = 0
	for box in boxes:
		total += (100 * box[0]) + box[1]
	for box in twoWideBoxes:
		total += (100 * box[0]) + box[1]
	return total

for move in moves:
	moveRobot(move)
	# drawGrid()
	# print()

drawGrid(grid)

print("Part 1:", calcGPSTotal())

grid = lines[0].split('\n')
expandedGrid = []
for row in grid:
	expandedGrid.append(row.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.'))

walls = []
boxes = []
twoWideBoxes = []
freeSpaces = []
robot = []

for y in range(len(expandedGrid)):
	for x in range(len(expandedGrid[y])):
		if expandedGrid[y][x] == '#':
			walls.append([y, x])
		elif expandedGrid[y][x] == '[':
			twoWideBoxes.append([y, x])
		elif expandedGrid[y][x] == '.':
			freeSpaces.append([y, x])
		elif expandedGrid[y][x] == '@':
			robot = [y, x]

def moveRobotExpanded(move):
	global robot
	boxesToPush = []
	direction = DIRECTIONS[move]
	newPositions = [[robot[0] + direction[0], robot[1] + direction[1]]]
	canMove = False
	while not any (pos in walls for pos in newPositions):
		newBoxesBeingPushed = False
		for i in range(len(newPositions)):
			boxIdx = twoWideBoxes.index(newPositions[i]) if newPositions[i] in twoWideBoxes else -1
			if boxIdx != -1 and boxIdx not in boxesToPush:
				boxesToPush.append(twoWideBoxes.index(newPositions[i]))
				newPositions.append([newPositions[i][0] + direction[0], newPositions[i][1] + direction[1]])
				newPositions.append([newPositions[i][0] + direction[0], newPositions[i][1] + direction[1] + 1])
				newBoxesBeingPushed = True
			boxIdx = twoWideBoxes.index([newPositions[i][0], newPositions[i][1] - 1]) if [newPositions[i][0], newPositions[i][1] - 1] in twoWideBoxes else -1
			if boxIdx != -1 and boxIdx not in boxesToPush:
				boxesToPush.append(twoWideBoxes.index([newPositions[i][0], newPositions[i][1] - 1]))
				newPositions.append([newPositions[i][0] + direction[0], newPositions[i][1] + direction[1] - 1])
				newPositions.append([newPositions[i][0] + direction[0], newPositions[i][1] + direction[1]])
				newBoxesBeingPushed = True
		if not newBoxesBeingPushed:
			canMove = True
			break

	if canMove:
		robot = [robot[0] + direction[0], robot[1] + direction[1]]
		for boxIdx in boxesToPush:
			twoWideBoxes[boxIdx] = [twoWideBoxes[boxIdx][0] + direction[0], twoWideBoxes[boxIdx][1] + direction[1]]

drawGrid(expandedGrid)

for move in moves:
	# print('Move:', move)
	moveRobotExpanded(move)
	# drawGrid(expandedGrid)
	# print()

print("Part 2:", calcGPSTotal())
