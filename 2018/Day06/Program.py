import operator
from collections import defaultdict

arraySize = 360
offset = 0
grid = [[-1 for i in range(arraySize)] for j in range(arraySize)]
coords = []
distances = {}
tally = defaultdict(int)
size = 0

with open('Input') as inFile:
	lines = inFile.read().splitlines()

for line in lines:
	parts = line.split(',')
	coords.append([int(parts[0]) + offset, int(parts[1]) + offset])
for x in range(arraySize):
	for y in range(arraySize):
		distances = {}

		for idx, coord in enumerate(coords):
			distances[idx] = abs(y-coord[0]) + abs(x-coord[1])
		
		minKey = min(distances.items(), key=operator.itemgetter(1))[0]
		
		if (sum(x == distances[minKey] for x in distances.values()) == 1):
			grid[x][y] = minKey

		if sum(distances.values()) < 10000:
			size += 1

for x in range(arraySize):
	for y in range(arraySize):
		tally[grid[x][y]] += 1

arraySize = 410
offset = 25
grid = [[-1 for i in range(arraySize)] for j in range(arraySize)]
coords = []
distances = {}
tally2 = defaultdict(int)

for line in lines:
	parts = line.split(',')
	coords.append([int(parts[0]) + offset, int(parts[1]) + offset])
for x in range(arraySize):
	for y in range(arraySize):
		distances = {}

		for idx, coord in enumerate(coords):
			distances[idx] = abs(y-coord[0]) + abs(x-coord[1])
		
		minKey = min(distances.items(), key=operator.itemgetter(1))[0]
		
		if (sum(x == distances[minKey] for x in distances.values()) == 1):
			grid[x][y] = minKey

for x in range(arraySize):
	for y in range(arraySize):
		tally2[grid[x][y]] += 1

print('Part 1:', max([tally[x] for x in tally if tally[x] == tally2[x]]))
print('Part 2:', size)