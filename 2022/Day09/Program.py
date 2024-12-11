with open('Input') as inFile:
	lines = inFile.read().splitlines()

instructions = []
dirs = { 'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1) }

def followKnot(a, b):
	d1 = a[0] - b[0]
	d2 = a[1] - b[1]
	if abs(d1) < 2 and abs(d2) < 2: # already touching
		return b
	if abs(d1) + abs(d2) > 3: # max diagonal
		return (b[0] + (d1 // 2), b[1] + (d2 // 2))
	elif abs(d1) > abs(d2):
		return (b[0] + (d1 // 2), a[1])
	else:
		return (a[0], b[1] + (d2 // 2))

def processMove(direction, distance):
	for d in range(distance):
		ropeKnots[0] = tuple([sum(tup) for tup in zip(ropeKnots[0], dirs[direction])])
		for i in range(1, len(ropeKnots)):
			ropeKnots[i] = followKnot(ropeKnots[i-1], ropeKnots[i])
		visited[ropeKnots[-1]] = 1

for line in lines:
	parts = line.split(' ')
	instructions.append((parts[0], int(parts[1])))

ropeKnots = [(0,0), (0,0)]
visited = {}

for instruction in instructions:
	processMove(instruction[0], instruction[1])

print('Part 1:', len(visited))

ropeKnots = [(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0)]
visited = {}

for instruction in instructions:
	processMove(instruction[0], instruction[1])

print('Part 2:', len(visited))