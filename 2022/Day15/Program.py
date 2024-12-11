with open('Input') as inFile:
	lines = inFile.read().splitlines()

sensors = []
beacons = []
targetRow = 2000000

def manhattanDistance(pos1, pos2):
	disX = abs(pos1[0] - pos2[0])
	disY = abs(pos1[1] - pos2[1])
	return disX + disY

def findAllWithinDistanceOnRow(pos1, dist, tRow):
	result = []
	minX = pos1[1] - dist
	maxX = pos1[1] + dist
	for x in range(minX, maxX + 1):
		if manhattanDistance(pos1, (tRow, x)) <= dist:
			result.append((tRow, x))
	return result

# Parse input
for line in lines:
	parts = line.split(':')
	parts1 = parts[0].split(',')
	parts1a = parts1[0].split('=')
	parts1b = parts1[1].split('=')
	sensorLoc = (int(parts1b[1]), int(parts1a[1]))

	parts2 = parts[1].split(',')
	parts2a = parts2[0].split('=')
	parts2b = parts2[1].split('=')
	beaconLoc = (int(parts2b[1]), int(parts2a[1]))

	dist = manhattanDistance(sensorLoc, beaconLoc)
	sensors.append((sensorLoc, dist))
	beacons.append(beaconLoc)

# Part 1
blockedOnTarget = set()
for sensor in sensors:
	sensorLoc, dist = sensor
	blockedBySensor = findAllWithinDistanceOnRow(sensorLoc, dist, targetRow)
	for position in blockedBySensor:
		if position[0] == targetRow and position not in beacons:
			blockedOnTarget.add(position)
	
print('Part 1:', len(blockedOnTarget))

def calculateTuningFrequency(coords):
	return coords[0] + (coords[1] * 4000000)

def fallsWithin(coords, sensor):
	sensorLoc, dist = sensor
	return manhattanDistance(sensorLoc, coords) <= dist

def getNodesJustOutsideRange(sensor):
	coords, dist = sensor
	for rotationalOffset in range(dist + 1):
		y, x = coords
		yield (y - rotationalOffset, x - dist - 1 + rotationalOffset) # clockwise from left corner
		yield (y + rotationalOffset, x + dist + 1 - rotationalOffset) # clockwise from right corner
		yield (y - dist - 1 + rotationalOffset, x + rotationalOffset) # clockwise from top corner
		yield (y + dist + 1 - rotationalOffset, x - rotationalOffset) # clockwise from bottom corner

maxCoordValue = 4000000

for sensor in sensors:
	candidates = getNodesJustOutsideRange(sensor)
	for cand in candidates:
		if cand[0] < 0 or cand[0] > maxCoordValue or cand[1] < 0 or cand[1] > maxCoordValue:
			continue
		if any(fallsWithin(cand, s) for s in sensors):
			continue

		print('Part 2:', calculateTuningFrequency(cand))
		exit()