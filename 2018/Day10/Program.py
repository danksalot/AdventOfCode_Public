import re

xPos = 0
yPos = 1
hVel = 2
vVel = 3

def PrintGrid(points, time):
	localPoints = []
	for point in points:
		timeAdjustedX = point[xPos] + (point[hVel]*time)
		timeAdjustedY = point[yPos] + (point[vVel]*time)
		localPoints.append([timeAdjustedX, timeAdjustedY])

	hOffset = 0 - min(localPoints, key=lambda p:p[xPos])[xPos]
	vOffset = 0 - min(localPoints, key=lambda p:p[yPos])[yPos]
	length = max(localPoints, key=lambda p:p[xPos])[xPos] + hOffset + 1
	height = max(localPoints, key=lambda p:p[yPos])[yPos] + vOffset + 1
	
	if height < 20:
		print('Checking for message at second ' + str(time) + '...')
		grid = [['.' for x in range(length)] for y in range(height)]
		for point in localPoints:
			grid[point[yPos]+vOffset][point[xPos]+hOffset] = '#'

		for row in grid:
			print(''.join(row))

with open('Input') as inFile:
	points = []
	values = map(lambda s: map(int, re.findall(r'-?\d+', s)), inFile)

	for (x, y, h, v) in values:
		points.append([x, y, h, v])

	for t in range(12000):
		PrintGrid(points, t)