
with open('Input') as inFile:
	lines = [line.rstrip('\n') for line in inFile.readlines()]

def runSimulation(guard, guardDir, obstacles):
	DIRS = [(-1,0), (0,1), (1,0), (0,-1)] # UP, RIGHT, DOWN, LEFT
	path = {tuple([guard[0], guard[1], guardDir])}
	while True:
		# Detect obstacle
		newPos = [guard[0]+DIRS[guardDir][0], guard[1]+DIRS[guardDir][1]]		
		if newPos in obstacles:
			guardDir = (guardDir + 1) % 4
			continue

		# Detect loop
		if (newPos[0], newPos[1], guardDir) in path:
			return None
		
		# Move guard
		guard = newPos
		path.add(tuple([guard[0], guard[1], guardDir]))

		# Detect finish condition
		if guard[0] in [0, len(lines)] or guard[1] in [0, len(lines[0])]:
			break

	return len({tuple([position[0], position[1]]) for position in path})

guard = None
obstacles = []
for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] == '^':
			guard = [y,x]
		elif lines[y][x] == '#':
			obstacles.append([y,x])

print("Part 1:", runSimulation(guard, 0, obstacles))

numNewObstacles = 0
for y in range(len(lines)):
	for x in range(len(lines[y])):
		if [y,x] in obstacles:
			continue
		result = runSimulation(guard, 0, obstacles + [[y,x]])
		if result is None:
			numNewObstacles += 1
			print('New loop found in row ' + str(y) + '.  Found so far:', numNewObstacles)

print('Part 2:', numNewObstacles)