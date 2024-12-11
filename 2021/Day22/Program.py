STATE = 0
XCOORDS = 1
YCOORDS = 2
ZCOORDS = 3

with open('Input') as inFile:
	lines = inFile.read().splitlines()

instructions = []
xRange = set()
yRange = set()
zRange = set()

for line in lines:
	state, combinedCoords = line.split(' ')
	coords = combinedCoords.split(',')
	xCoords = [int(x) for x in coords[0][2:].split('..')]
	yCoords = [int(x) for x in coords[1][2:].split('..')]
	zCoords = [int(x) for x in coords[2][2:].split('..')]
	instructions.append([state, xCoords, yCoords, zCoords])
	if state == 'on':
		xRange |= set(range(xCoords[0], xCoords[1]+1))
		yRange |= set(range(yCoords[0], yCoords[1]+1))
		zRange |= set(range(zCoords[0], zCoords[1]+1))

onCuboids = set()

for i in instructions[:20]:
	# print(i)
	newStateCuboids = set()
	for x in range(i[XCOORDS][0], i[XCOORDS][1]+1):
		for y in range(i[YCOORDS][0], i[YCOORDS][1]+1):
			for z in range(i[ZCOORDS][0], i[ZCOORDS][1]+1):
				newStateCuboids.add((x, y, z))
	if i[STATE] == 'on':
		# print('Turning on cuboids:', len(newStateCuboids), newStateCuboids)
		onCuboids |= newStateCuboids
		# print('Total on cuboids:', len(onCuboids))
	else:
		# print('Turning off cuboids:', len(newStateCuboids), newStateCuboids)
		onCuboids -= newStateCuboids
		# print('Total on cuboids:', len(onCuboids))

print('Part 1:', len(onCuboids))

def findOverlaps(first, second):
	low = max(first[0], second[0])
	high = min(first[-1], second[-1])

	if high < low:
		return []

	return [low, high]

def countUniqueOnCubioids(instruction, followingInstructions):
	state, xCoords, yCoords, zCoords = instruction

	count = (xCoords[1] - xCoords[0] + 1) * (yCoords[1] - yCoords[0] + 1) * (zCoords[1] - zCoords[0] + 1)
	# print('Setting count to:', count)
	overlaps = []

	for i in followingInstructions:
		xOverlaps = findOverlaps(xCoords, i[XCOORDS])
		yOverlaps = findOverlaps(yCoords, i[YCOORDS])
		zOverlaps = findOverlaps(zCoords, i[ZCOORDS])

		if len(xOverlaps) * len(yOverlaps) * len(zOverlaps) == 0:
			continue

		overlaps.append((i[STATE], xOverlaps, yOverlaps, zOverlaps))

	for i in range(len(overlaps)):
		alteredLater = countUniqueOnCubioids(overlaps[i], overlaps[i+1:])
		# print('Removing', alteredLater, 'because they are altered later')
		count -= alteredLater

	return count

onCuboidCount = 0

for i in range(len(instructions)):
	if instructions[i][STATE] == 'off':
		continue
	onCuboidCount += countUniqueOnCubioids(instructions[i], instructions[i+1:])			

print('Part 2:', onCuboidCount)
