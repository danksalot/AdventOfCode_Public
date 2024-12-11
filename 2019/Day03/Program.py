
def tracePath(moves):
	currentX = 0
	currentY = 0
	pathLength = 0
	path = {}

	for move in moves:
		code = move[0]
		dist = int(move[1:])

		if code == 'R':
			for i in range(dist):
				pathLength += 1
				currentX += 1
				if (currentX, currentY) not in path:
					path[(currentX, currentY)] = pathLength
		elif code == 'L':
			for i in range(dist):
				pathLength += 1
				currentX -= 1
				if (currentX, currentY) not in path:
					path[(currentX, currentY)] = pathLength
		elif code == 'U':
			for i in range(dist):
				pathLength += 1
				currentY += 1
				if (currentX, currentY) not in path:
					path[(currentX, currentY)] = pathLength
		elif code == 'D':
			for i in range(dist):
				pathLength += 1
				currentY -= 1
				if (currentX, currentY) not in path:
					path[(currentX, currentY)] = pathLength

	return path

with open('Input') as inFile:
	lines = inFile.readlines()

firstPath = tracePath(lines[0].split(','))
secondPath = tracePath(lines[1].split(','))
intersections = set(firstPath) & set(secondPath)

print("Part 1:", min([abs(x) + abs(y) for (x,y) in intersections]))
print("Part 2:", min([firstPath[position] + secondPath[position] for position in intersections]))
