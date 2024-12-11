def countTrees(lines, stepX, stepY):
	currentX, currentY, treeCount = 0, 0, 0
	width = len(lines[0])

	while currentY < len(lines):
		if lines[currentY][currentX] == '#': treeCount += 1
		currentX = (currentX + stepX) % width
		currentY += stepY

	return treeCount


with open('Input') as inFile:
	lines = inFile.read().splitlines()

	print('Part 1:', countTrees(lines, 3, 1))
	print('Part 2:', (countTrees(lines, 1, 1) * countTrees(lines, 3, 1) * countTrees(lines, 5, 1) * countTrees(lines, 7, 1) * countTrees(lines, 1, 2)))
