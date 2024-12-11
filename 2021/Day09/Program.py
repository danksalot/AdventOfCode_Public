from math import prod

DIRECTIONS = [
    (-1,  0), #UP
    ( 0, -1), #LEFT
    ( 0,  1), #RIGHT
    ( 1,  0), #DOWN    
]

with open('Input') as inFile:
	lines = inFile.read().splitlines()

cave = []
total = 0
width = len(lines[0])
height = len(lines)
lowPoints = {}

for rowIndex, line in enumerate(lines):
	for colIndex, col in enumerate(line):
		neighbors = [(colIndex + dy, rowIndex + dx) for dx, dy in DIRECTIONS]
		neighbors = [x for x in neighbors if x[0] not in [-1, width] and x[1] not in [-1, height]]
		if all([lines[nx][ny] > col for ny, nx in neighbors]):
			lowPoints[(rowIndex, colIndex)] = 0
			total += int(col) + 1

print('Part 1:', total)

def calcBasinSize(x, y):
	basin = []
	openSet = [(y, x)]
	while len(openSet) > 0:
		# print('OpenSet:', openSet)
		current = openSet.pop()
		basin.append(current)
		# print('Current:', current)
		neighbors = [(current[0] + dy, current[1] + dx) for dx, dy in DIRECTIONS]
		# print('Neighbors:', neighbors)
		neighbors = [x for x in neighbors if x[0] not in [-1, height] and x[1] not in [-1, width]]
		# print('Neighbors:', neighbors)
		neighbors = [x for x in neighbors if x not in basin]
		# print('Neighbors:', neighbors)
		neighbors = [x for x in neighbors if x not in openSet]
		# print('Neighbors:', neighbors)
		neighbors = [x for x in neighbors if lines[x[0]][x[1]] != '9']
		# print('Adding to openSet:', neighbors)
		openSet.extend(neighbors)
	return len(basin)

for lowPoint in lowPoints:
	lowPoints[lowPoint] = calcBasinSize(lowPoint[1], lowPoint[0])

print(prod(sorted(lowPoints.values())[-3:]))