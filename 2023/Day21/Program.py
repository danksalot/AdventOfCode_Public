with open('Input') as inFile:
	lines = inFile.read().split('\n')

rocks = []
start = None
maxY = len(lines)
maxX = len(lines[0])

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # R, L, D, U

for y in range(maxY):
	for x in range(maxX):
		if lines[y][x] == 'S':
			start = (y, x)
		  
def findNeighbors(pos):
	for direction in directions:
		rockY = (pos[0] + direction[0]) % maxY
		rockX = (pos[1] + direction[1]) % maxX
		neighbor = (pos[0] + direction[0], pos[1] + direction[1])
		if lines[rockY][rockX] != '#':
			yield neighbor

# https://en.wikipedia.org/wiki/Newton_polynomial
# https://www.dcode.fr/newton-interpolating-polynomial
def calcNewtonPolynomial(indicators, lastStep):
	x = lastStep // maxY
	cycle0Val, cycle1Val, cycle2Val = indicators.values()

	# First order slope
	o1slope1 = cycle1Val - cycle0Val
	o1slope2 = cycle2Val - cycle1Val

	# Second order slope
	o2slope1 = o1slope2 - o1slope1

	# return o2slope1 // 2 * (x - 1) * x + (o1slope1 * x) + cycle0Val
	return (o2slope1 // 2 * x ** 2) + ((o1slope1 - o2slope1 // 2) * x) + cycle0Val

def countStepable(start, lastStep):	
	calcIndicators = { start[0] + (i * maxY): None for i in range(3) }
	openSet = set()
	openSet.add(start)
	for step in range(1, lastStep + 1):
		nextOpenSet = set()
		for (y, x) in openSet:
			for neighbor in findNeighbors((y, x)):
				nextOpenSet.add(neighbor)
		openSet = nextOpenSet
		if step in calcIndicators:
			calcIndicators[step] = len(openSet)
			if None not in calcIndicators.values():
				return calcNewtonPolynomial(calcIndicators, lastStep)

	return len(openSet)

print('Part 1:', countStepable(start, 64))
print('Part 2:', countStepable(start, 26501365))