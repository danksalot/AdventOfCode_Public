def distanceToOrigin(point):
	xDistance = abs(point[0])
	yDistance = abs(point[1])
	return xDistance + max(0, (yDistance - xDistance / 2))

with open('Input') as inFile:
	steps = inFile.read().split(',')

directions = {'n':(0, 1), 'ne':(1, 0.5), 'se':(1, -0.5), 's':(0, -1), 'sw':(-1, -0.5), 'nw':(-1, 0.5)}
currentPosition = (0, 0)

maxDistance = 0

for step in steps:
	deltaX, deltaY = directions[step]
	currentPosition = (currentPosition[0] + deltaX, currentPosition[1] + deltaY)
	currentDistance = distanceToOrigin(currentPosition)
	
	if currentDistance > maxDistance:
		maxDistance = currentDistance

print "Ending distance from origin:", distanceToOrigin(currentPosition)
print "Max distance from origin:", maxDistance