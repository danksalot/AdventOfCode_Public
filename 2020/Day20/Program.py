import math

def getSides(tileId):
	tile = tiles[tileId]
	top = tile[0]
	bottom = tile[-1]
	left = ''.join([x[0] for x in tile])
	right = ''.join([x[-1] for x in tile])
	return [top, bottom, left, right, top[::-1], bottom[::-1], left[::-1], right[::-1]]

def findMatches(tileId):
	firstSides = getSides(tileId)
	check = [t for t in tiles if t != tileId]

	possibles = []
	for t in check:
		for side in getSides(t):
			if side in firstSides:
				possibles.append(t)

	return set(possibles)

def getImageHashCount(tileId):
	total = 0
	for row in tiles[tileId][1:-1]:
		for x in row:
			if x == '#':
				total += 1
	return total

	# tile = tiles[tileId][1:-1]
	# for row in tile:
	# 	row = row[1:-1]
	# print(sum([1 for x in ]))


with open('Input') as inFile:
	groups = inFile.read().split("\n\n")

tiles = {}

for group in groups:
	parts = group.split('\n')
	tileId = int(parts[0][5:9])
	tiles[tileId] = [x for x in parts[1:]]

matches = {}
for t in tiles:
	matches[t] = findMatches(t)

corners = [x for x in matches if len(matches[x]) == 2]
sides = [x for x in matches if len(matches[x]) == 3]
middles = [x for x in matches if len(matches[x]) == 4]

print(len(corners))
print(len(sides))
print(len(middles))

seaMonsterSize = 15



print('Part 1:', math.prod(corners))


hashCount = sum([getImageHashCount(key) for key in tiles])
print('All hashes:', hashCount)
print('One Seamonster:', hashCount - (seaMonsterSize * 1))
print('Two Seamonsters:', hashCount - (seaMonsterSize * 2))
print('Three Seamonsters:', hashCount - (seaMonsterSize * 3))
print('Four Seamonsters:', hashCount - (seaMonsterSize * 4))
print('Five Seamonsters:', hashCount - (seaMonsterSize * 5))
print('Six Seamonsters:', hashCount - (seaMonsterSize * 6))
print('Seven Seamonsters:', hashCount - (seaMonsterSize * 7))
print('Eight Seamonsters:', hashCount - (seaMonsterSize * 8))
print('Nine Seamonsters:', hashCount - (seaMonsterSize * 9))
print('Ten Seamonsters:', hashCount - (seaMonsterSize * 10))
print('Eleven Seamonsters:', hashCount - (seaMonsterSize * 11))
print('Twelve Seamonsters:', hashCount - (seaMonsterSize * 12))
print('Thirteen Seamonsters:', hashCount - (seaMonsterSize * 13))
print('Fourteen Seamonsters:', hashCount - (seaMonsterSize * 14))
print('Fifteen Seamonsters:', hashCount - (seaMonsterSize * 15))
print('Sixteen Seamonsters:', hashCount - (seaMonsterSize * 16))
print('Seventeen Seamonsters:', hashCount - (seaMonsterSize * 17))
print('Eighteen Seamonsters:', hashCount - (seaMonsterSize * 18))