from itertools import product

DOWN = 0
LEFT = 1
RIGHT = 2
UP = 3

DIRECTIONS = [
	( 1,  0), #DOWN
	( 0, -1), #LEFT
	( 0,  1), #RIGHT
	( -1, 0)  #UP
]

def printGrid():
	row = ''
	for x in range(minX, maxX + 1):
		row += '+' if x == 500 else '.'
	print(row)

	for y in range(minY, maxY + 1):
		row = ''
		for x in range(minX, maxX + 1):
			row += '#' if (y,x) in clay else '~' if (y,x) in still else '|' if (y,x) in flowing else '.'
		print(row)

def moveDirection(coords, direction):
	return (coords[0] + DIRECTIONS[direction][0], coords[1] + DIRECTIONS[direction][1])

def flowDown(coords, maxY, clay, flowing):
	while coords[0] < maxY:
		nextBlockDown = moveDirection(coords, DOWN)
		if nextBlockDown not in clay:
			flowing.add(nextBlockDown)
			coords = nextBlockDown
		elif nextBlockDown in clay:
			return coords
	return None

def flowOutward(coords, clay, flowing, still):
	temp = set()
	left = flowDirection(coords, LEFT, clay, still, temp)
	right = flowDirection(coords, RIGHT, clay, still, temp)
	if not left and not right:
		still.update(temp)
		if temp in flowing:
			flowing.remove(temp)
	else:
		flowing.update(temp)
	return left, right

def flowDirection(coords, direction, clay, still, temp):
	current = coords
	while current not in clay:
		temp.add(current)
		pos2 = moveDirection(current, DOWN)
		if pos2 not in clay and pos2 not in still:
			return current
		current = moveDirection(current, direction)
	return None

clay, flowing, still, toFall, toSpread = set(), set(), set(), set(), set()

with open('Input') as inFile:
	lines = inFile.read().splitlines()

for line in lines:
	parts = line.split(', ')
	for part in [p for p in parts if p[0] == 'y']:
		coordParts = [int(c) for c in part[2:].split('..')]
		yCoords = range(coordParts[0], coordParts[-1] + 1)
	for part in [p for p in parts if p[0] == 'x']:
		coordParts = [int(c) for c in part[2:].split('..')]
		xCoords = range(coordParts[0], coordParts[-1] + 1)
	clay.update(list(product(yCoords,xCoords)))

minX = min(clay, key=lambda c:c[1])[1] - 1
maxX = max(clay, key=lambda c:c[1])[1] + 1
minY = min(clay, key=lambda c:c[0])[0]
maxY = max(clay, key=lambda c:c[0])[0]

toFall.add((0, 500))
while toFall or toSpread:
	while toFall:
		current = toFall.pop()
		result = flowDown(current, maxY, clay, flowing)
		if result:
			toSpread.add(result)

	while toSpread:
			current = toSpread.pop()
			left, right = flowOutward(current, clay, flowing, still)
			if not right and not left:
				toSpread.add(moveDirection(current, UP))
			else:
				if left:
					toFall.add(left)
				if right:
					toFall.add(right)

#printGrid()
print('Total Water = %d' % len([p for p in (flowing | still) if p[0] >= minY]))
print('Still Water = %d' % len([p for p in still if p[0] >= minY]))

