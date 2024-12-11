from copy import deepcopy

with open('Input') as inFile:
	lines = [l.strip() for l in inFile.readlines()]

def isSupported(brick, allCubes):
	x1, y1, z1, x2, y2, z2, id = brick
	below = z1 - 1
	if below == 0:
		return True
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			if (x, y, below) in allCubes:
				return True
	return False

def fallOnce(bricks):
	changed = False
	newBricks = []
	allCubes = set()
	for (x1, y1, z1, x2, y2, z2, id) in bricks:
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				allCubes.add((x, y, z2))

	for brick in bricks:
		x1, y1, z1, x2, y2, z2, id = brick
		if not isSupported(brick, allCubes):
			changed = True
			newBricks.append((x1, y1, z1 - 1, x2, y2, z2 - 1, id))
		else:
			newBricks.append(brick)
	return newBricks, changed

bricks = []
for i in range(len(lines)):
	line = lines[i].replace('~', ',')
	coords = [int(c) for c in line.split(',')]
	bricks.append(tuple(coords + [i]))

changed = True
while changed:
	bricks = sorted(bricks, key=lambda b: b[2])
	bricks, changed = fallOnce(bricks)

def safeToRemove(brick, bricks):
	bricksCopy = deepcopy(bricks)
	bricksCopy.remove(brick)
	_, changed = fallOnce(bricksCopy)
	return not changed

safeToRemove = [b for b in bricks if safeToRemove(b, bricks)]
print('Part 1:', len(safeToRemove))

sum = 0
for brick in [b for b in bricks if b not in safeToRemove]:
	test = deepcopy(bricks)
	test.remove(brick)
	changed = True
	while changed:
		test, changed = fallOnce(test)

	allDiff = set(bricks).symmetric_difference(test)
	sum += len(allDiff) // 2

print('Part 2:', sum)

