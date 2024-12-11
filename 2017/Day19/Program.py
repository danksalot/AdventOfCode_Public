directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
grid = []
path = ''
steps = 0

def canMove(position, direction):
	newPos = [position[0] + directions[direction][0], position[1] + directions[direction][1]]
	return grid[newPos[0]][newPos[1]] != ' '

with open('Input') as inFile:
	lines = inFile.readlines()

for line in lines:
	grid.append([x for x in line.rstrip('\n')])

currentPos = [0, grid[0].index('|')]
currentDir = 0
#print 'DOWN' if currentDir == 0 else 'RIGHT' if currentDir == 1 else 'UP' if currentDir == 2 else 'LEFT'

while True:
	steps += 1
	if str.isalpha(grid[currentPos[0]][currentPos[1]]):
		#print 'Found a letter', currentPos, grid[currentPos[0]][currentPos[1]]
		path += grid[currentPos[0]][currentPos[1]]

	if canMove(currentPos, currentDir):
		currentPos = [sum(x) for x in zip(currentPos, directions[currentDir])]
	elif canMove(currentPos, (currentDir + 1) % 4):
		currentDir = (currentDir + 1) % 4
		#print 'DOWN' if currentDir == 0 else 'RIGHT' if currentDir == 1 else 'UP' if currentDir == 2 else 'LEFT'
		currentPos = [sum(x) for x in zip(currentPos, directions[currentDir])]
	elif canMove(currentPos, (currentDir - 1) % 4):
		currentDir = (currentDir - 1) % 4
		#print 'DOWN' if currentDir == 0 else 'RIGHT' if currentDir == 1 else 'UP' if currentDir == 2 else 'LEFT'
		currentPos = [sum(x) for x in zip(currentPos, directions[currentDir])]
	else:
		#print 'No moves available', currentPos
		break;

print 'Letters found along the way:', path
print 'Steps takes:', steps

