with open('Input') as inFile:
	lines = inFile.read().splitlines()

trees = []
visible = {}

for line in lines:
	trees.append([int(x) for x in line])

def addIfVisible(highest, y, x):
	if trees[y][x] > highest:
		visible[(y,x)] = 1
		return trees[y][x]
	return highest

def addVisibleForRow(innerRange, horizontal):
	for a in range(0, len(trees)):
		highest = -1
		for b in innerRange:
			highest = addIfVisible(highest, a, b) if horizontal else addIfVisible(highest, b, a)

addVisibleForRow(range(0, len(trees[0])), horizontal=True)         # left to right
addVisibleForRow(range(len(trees[0])-1, -1, -1), horizontal=True)  # right to left
addVisibleForRow(range(0, len(trees[0])), horizontal=False)        # top to bottom
addVisibleForRow(range(len(trees[0])-1, -1, -1), horizontal=False) # bottom to top

print('Part 1:', len(visible))

def measureHorizontal(aRange, x, minHeight):
	score = 0
	for newY in aRange:
		score += 1
		if trees[newY][x] >= minHeight:
			break
	return score

def measureVertical(aRange, y, minHeight):
	score = 0
	for newX in aRange:
		score += 1
		if trees[y][newX] >= minHeight:
			break
	return score

def measureScore(y, x):
	upScore = measureHorizontal(range(y-1, -1, -1), x, trees[y][x])
	downScore = measureHorizontal(range(y+1, len(trees)), x, trees[y][x])
	leftScore = measureVertical(range(x-1, -1, -1), y, trees[y][x])
	rightScore = measureVertical(range(x+1, len(trees)), y, trees[y][x])
	return upScore * downScore * leftScore * rightScore

print('Part 2:', max([measureScore(y, x) for y in range(len(trees)) for x in range(len(trees))]))