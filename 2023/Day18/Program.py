import re

with open('Input') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
dirMap = { 0: 'R', 1: 'D', 2: 'L', 3: 'U' }

def measurePolygon(sides):
	y, x, perimeter = 0, 0, 0
	corners = []
	for side in sides:
		dir, dist = side[0], int(side[1])
		perimeter += dist
		y += directions[dir][0] * dist
		x += directions[dir][1] * dist
		corners.append((y, x))
	return perimeter, corners

perimeter, corners = measurePolygon([[l.split()[0], l.split()[1]] for l in lines])

minX = min([h[1] for h in corners])
maxX = max([h[1] for h in corners])
minY = min([h[0] for h in corners])
maxY = max([h[0] for h in corners])

def measureArea(alreadyCounted):
	measurementSet = zip(corners, corners[1:])
	shoelaceArea = sum((first[0] + second[0])*(first[1] - second[1]) / 2 for first, second in measurementSet)
	return int(shoelaceArea + (alreadyCounted / 2) + 1)

print('Part 1:', measureArea(perimeter))

sides = []
for line in lines:
	color = re.search(r'#......', line).group()
	dir = dirMap[int(color[-1])]
	dist = int(color[1:-1], 16)
	sides.append([dir, dist])
perimeter, corners = measurePolygon(sides)

minX = min([h[1] for h in corners])
maxX = max([h[1] for h in corners])
minY = min([h[0] for h in corners])
maxY = max([h[0] for h in corners])

print('Part 2:', measureArea(perimeter))
