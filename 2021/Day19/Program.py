from collections import defaultdict
from itertools import permutations

def manhattanDistance(pos1, pos2):
	disX = abs(pos1[0] - pos2[0])
	disY = abs(pos1[1] - pos2[1])
	disZ = abs(pos1[2] - pos2[2])
	return disX + disY + disZ

def subractCoords(pos1, pos2):
	return (pos1[0] - pos2[0], pos1[1] - pos2[1], pos1[2] - pos2[2])

def addCoords(pos1, pos2):
	return (pos1[0] + pos2[0], pos1[1] + pos2[1], pos1[2] + pos2[2])

posNegs = [
	[ 1,  1,  1],
	[-1,  1,  1],
	[ 1, -1,  1],
	[ 1,  1, -1],
	[-1, -1,  1],
	[-1,  1, -1],
	[ 1, -1, -1],
	[-1, -1, -1],
]

def getPermutations():
	perms = []
	for position in permutations([0, 1, 2]):
		for posNeg in posNegs:
			perms.append((position, posNeg))
	return perms

def applyPermutation(perm, coords):
	pos, posNeg = perm
	return (coords[pos[0]] * posNeg[0], coords[pos[1]] * posNeg[1], coords[pos[2]] * posNeg[2])

with open('Input') as inFile:
	lines = inFile.read().splitlines()

scanners = {}
scannerPositions = {}

for line in lines:
	if 'scanner' in line:
		current = int(line.split(' ')[2])
		scanners[current] = []
	elif len(line.split(',')) == 3:
		parts = line.split(',')
		scanners[current].append((int(parts[0]), int(parts[1]), int(parts[2])))

knownBeacons = set(scanners[0])
tested = defaultdict(set)

def overlapsKnown(scannerId):
	global knownBeacons
	for perm in getPermutations():
		currentSet = [applyPermutation(perm, coords) for coords in scanners[scannerId]]

		testSet = knownBeacons - tested[scannerId]
		for current in currentSet:
			for test in testSet:
				scannerPoition = subractCoords(test, current)
				tried = set(map(lambda z: addCoords(z, scannerPoition), currentSet))
				if len(tried & knownBeacons) >= 12:
					knownBeacons |= tried
					scannerPositions[scannerId] = scannerPoition
					return True

	tested[scannerId] |= testSet
	return False

unmappedScanners = [x for x in scanners.keys()]

while unmappedScanners:
	print('Unmapped Scanners:', len(unmappedScanners))
	for scanner in unmappedScanners:
		if overlapsKnown(scanner):
			unmappedScanners.remove(scanner)
			break

print('Part 1:', len(knownBeacons))

farthest = 0
for a in scannerPositions.values():
	for b in scannerPositions.values():
		dist = manhattanDistance(a, b)
		if dist > farthest:
			farthest = dist

print('Part 2:', farthest)