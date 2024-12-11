scores = {}

def calculateScore(grid, x, y, size):
	score = 0
	if (x, y, size-1) in scores:
		score = scores[(x, y, size-1)]
		for yOffset in range(size):
			score += grid[x + size - 1][y + yOffset]
		for xOffset in range(size - 1):
			score += grid[x + xOffset][y + size - 1]
		scores[(x, y, size)] = score
	else:
		for xOffset in range(size):
			for yOffset in range(size):
				score += grid[x + xOffset][y + yOffset]
				scores[(x, y, size)] = score
	return score

serialNum = 8561
grid = [[0 for x in range(300)] for y in range(300)]

for y in range(1, 301):
	for x in range(1, 301):
		grid[x-1][y-1] = ((((x + 10) * y + serialNum) * (x + 10) // 100) % 10) - 5

maxScore = 0
maxIndex = [0, 0, 0]
for size in range(1, 15):
	for y in range(1, 302 - size):
		for x in range(1, 302 - size):
			score = calculateScore(grid, x-1, y-1, size)
			if score > maxScore:
				maxScore = score
				maxIndex = [x, y, size]
	if size == 3:
		print('Part 1:', maxIndex[0:2])

print('Part 2:', maxIndex)
