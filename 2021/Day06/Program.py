from collections import defaultdict

solvedSums = {}

def countSpawn(numFish, spawnDay, endDay, level):	
	if (numFish,endDay-spawnDay) in solvedSums.keys():
		return solvedSums[(numFish,endDay-spawnDay)]

	total = 0
	for spawn in range(spawnDay, endDay, 7):
		total += numFish
	for newSpawnDay in range(spawnDay + 9, endDay, 7):
		total += countSpawn(numFish, newSpawnDay, endDay, level + 1)

	solvedSums[(numFish,endDay-spawnDay)] = total
	return total

def fishOnDay(gMap, day):
	total = sum(gMap.values())
	for key, value in gMap.items():
		total += countSpawn(value, key, day, 1)
	return total

with open('Input') as inFile:
	lanternfish = [int(x) for x in inFile.read().split(',')]

gestationMap = defaultdict(int)

for i in range(1, max(lanternfish) + 1):
	gestationMap[i] += lanternfish.count(i)

print('Part 1:', fishOnDay(gestationMap, 80))
print('Part 2:', fishOnDay(gestationMap, 256))