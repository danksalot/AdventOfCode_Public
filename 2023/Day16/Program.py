with open('Input') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Right, Down, Left, Up
mirrors = []
splitters = []
openSpace = []

for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] in ['/', '\\']:
			mirrors.append([(y, x), lines[y][x]])
		elif lines[y][x] in ['|', '-']:
			splitters.append([(y, x), lines[y][x]])
		else:
			openSpace.append((y, x))

def isOutOfBounds(y, x):
	return y < 0 or y >= len(lines) or x < 0 or x >= len(lines[y])

def followBeam(y, x, dir):
	dy, dx = directions[dir]
	return (y + dy, x + dx, dir)

def countBeamActivation(beam):
	openSet = [beam]
	activated = set()
	alreadyProcessed = set()
	while openSet:
		newBeams = []
		for beam in openSet:
			y = beam[0]
			x = beam[1]
			dir = beam[2]
			if isOutOfBounds(y, x) or beam in alreadyProcessed:
				continue
			activated.add((y, x))
			alreadyProcessed.add(beam)
			if ((y, x)) in openSpace:
				newBeams.append(followBeam(y, x, dir))
			if [(y, x), '/'] in mirrors:
				if dir == 0:
					newBeams.append(followBeam(y, x, 3))
				elif dir == 1:
					newBeams.append(followBeam(y, x, 2))
				elif dir == 2:
					newBeams.append(followBeam(y, x, 1))
				else:
					newBeams.append(followBeam(y, x, 0))
			elif [(y, x), '\\'] in mirrors:
				if dir == 0:
					newBeams.append(followBeam(y, x, 1))
				elif dir == 1:
					newBeams.append(followBeam(y, x, 0))
				elif dir == 2:
					newBeams.append(followBeam(y, x, 3))
				else:
					newBeams.append(followBeam(y, x, 2))
			elif [(y, x), '|'] in splitters:
				if dir in [0, 2]:
					newBeams.append(followBeam(y, x, 1))
					newBeams.append(followBeam(y, x, 3))
				else:
					newBeams.append(followBeam(y, x, dir))
			elif [(y, x), '-'] in splitters:
				if dir in [1, 3]:
					newBeams.append(followBeam(y, x, 0))
					newBeams.append(followBeam(y, x, 2))
				else:
					newBeams.append(followBeam(y, x, dir))
		openSet = newBeams
	return len(activated)


print('Part 1:', countBeamActivation((0, 0, 0)))

best = 0
for i in range(len(lines)):
	localBest = max(
		countBeamActivation((i, 0, 0)), 
		countBeamActivation((i, len(lines[0]) - 1, 2)), 
		countBeamActivation((0, i, 1)), 
		countBeamActivation((len(lines) - 1, i, 3)))
	if localBest > best:
		best = localBest

print('Part 2:', best)
