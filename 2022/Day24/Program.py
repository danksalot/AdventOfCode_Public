with open('Input') as inFile:
	lines = inFile.read().splitlines()

walls = []
blizzards = []
wraps = {}
DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]

for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] == '#':
			walls.append((y, x))
		elif lines[y][x] in '<>^v':
			blizzards.append((y, x, lines[y][x]))

for x in range(len(lines[0])):
	wraps[(0, x, '^')] = (len(lines)-2, x, '^')
	wraps[(len(lines)-1, x, 'v')] = (0+1, x, 'v')
for y in range(len(lines)):
	wraps[(y, 0, '<')] = (y, len(lines[0])-2, '<')
	wraps[(y, len(lines[0])-1, '>')] = (y, 0+1, '>')

def calcBlizzardMoves(blizzards):
	global wraps
	newB = []
	for blizzard in blizzards:
		y, x, d = blizzard
		dy, dx = DIRS['<>^v'.index(d)]
		newLoc = (y+dy, x+dx, d)
		if newLoc in wraps:
			newLoc = wraps[newLoc]
		newB.append(newLoc)
	return newB

def getPossibleMoves(loc, blizzards):
	y, x = loc
	candidates = [(y+dy, x+dx) for dy, dx in MOVES if 0<=y+dy<len(lines) and (y+dy, x+dx) not in walls]
	candidates = [c for c in candidates if c not in [(y, x) for y, x, d in blizzards]]	
	return candidates

def search(start, end, step, blizzards):
	currentSet = [start]
	while len(currentSet) > 0:
		print('Working on step:', step, 'openSet:', len(currentSet))
		nextSet = []
		blizzards = calcBlizzardMoves(blizzards)
		for candidate in currentSet:	
			for nextMove in getPossibleMoves(candidate, blizzards):
				if nextMove == end:
					return step+1, blizzards
				if (nextMove[0], nextMove[1]) not in nextSet:
					nextSet.append((nextMove[0], nextMove[1]))
		currentSet = nextSet
		step += 1

start = (0, 1)
end = (len(lines)-1, len(lines[0])-2)
steps, blizzards = search(start, end, 0, blizzards)
print('Part 1:', steps)

steps, blizzards = search(end, start, steps, blizzards)
steps, blizzards = search(start, end, steps, blizzards)
print('Part 2:', steps)


