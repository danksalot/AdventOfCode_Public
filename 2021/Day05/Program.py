import re

with open('Input') as inFile:
	lines = inFile.read().splitlines()

vents = []

for line in lines:
	parts =[int(x) for x in re.findall('\d+', line)]
	vents.append(parts)

maxX1 = max(x[0] for x in vents)
maxY1 = max(x[1] for x in vents)
maxX2 = max(x[2] for x in vents)
maxY2 = max(x[3] for x in vents)

fieldWidth = max(maxX1, maxX2) + 1
fieldHeight = max(maxY1, maxY2) + 1

field = [[0 for i in range(fieldWidth)] for j in range(fieldHeight)]

# print(field)

for vent in vents:
	x1 = vent[0]
	x2 = vent[2]
	y1 = vent[1]
	y2 = vent[3]

	if x1 == x2 or y1 == y2:
		for y in range(min(y1, y2), max(y1, y2) + 1):
			for x in range(min(x1, x2), max(x1, x2) + 1):
				field[y][x] += 1

	else:
		while x1 != x2:
			field[y1][x1] += 1
			x1 = x1 + 1 if x2 > x1 else x1 - 1
			y1 = y1 + 1 if y2 > y1 else y1 - 1
		field[y1][x1] += 1

count = 0
for row in field:
	for position in row:
		if position >= 2:
			count += 1

print(count)