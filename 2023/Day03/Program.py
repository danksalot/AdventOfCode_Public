import re

with open('Input') as inFile:
	lines = [l.strip() for l in inFile.readlines()]

symbolPositions = []
numPositions = []

def areAdjacent(num, symbol):
	return abs(num[2] - symbol[1]) < 2 and (symbol[0] >= num[0]-1 and symbol[0] <= num[1])

for i, line in enumerate(lines):
	# Find all symbols and numbers in the line [x, y, symbol]
	symbols = re.finditer(r'[^\d\.]', line)
	for symbol in symbols:
		symbolPositions.append([symbol.start(0), i, symbol.group(0)])

	# Find all numbers in the line [startX, endX, y, number]
	nums = re.finditer(r'\d+', line)
	for num in nums:
		numPositions.append([num.start(0), num.end(0), i, int(num.group(0))])

total = 0
for num in numPositions:
	for symbol in symbolPositions:
		if areAdjacent(num, symbol):
			total += num[3]
print('Part 1: ', total)

total = 0
for gear in [g for g in symbolPositions if g[2] == '*']:
	adjacentNums = [num for num in numPositions if areAdjacent(num, gear)]
	if len(adjacentNums) == 2:
		total += adjacentNums[0][3] * adjacentNums[1][3]		
print('Part 2: ', total)