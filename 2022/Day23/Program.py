with open('Input') as inFile:
	lines = inFile.read().splitlines()

elves = []
proposedMoves = []
DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
CHKS = [[[0,1,2],[5,6,7],[0,3,5],[2,4,7]],[[5,6,7],[0,3,5],[2,4,7],[0,1,2]],[[0,3,5],[2,4,7],[0,1,2],[5,6,7]],[[2,4,7],[0,1,2],[5,6,7],[0,3,5]]]

for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] == '#':
			elves.append((y, x))

def makeMoves(elves, moves):
	confirmed = {}
	confirmed.clear()
	for i in range(len(elves)):
		if moves.count(moves[i]) == 1 and moves[i] != elves[i]:
			confirmed[i] = moves[i]
	if len(confirmed.keys()) == 0:
		return True, elves
	for idx in confirmed:
		elves[idx] = confirmed[idx]
	return False, elves

def calcMoves(elves, step):
	moves = []
	for y, x in elves:
		moves.append((y, x))
		neighbors = [(y+dy, x+dx) for dy, dx in DIRS]
		if len(list(set(elves) & set(neighbors))) == 0:
			pass
		else:
			looks = CHKS[step % 4]
			for look in looks:
				if not any([True for i in look if (y+DIRS[i][0], x+DIRS[i][1]) in elves]):
					moves[-1] = (y + DIRS[look[1]][0], x + DIRS[look[1]][1])
					break
	return moves

def getBoardSize(elves):
	minY = min([y for y, x in elves])
	maxY = max([y for y, x in elves])
	minX = min([x for y, x in elves])
	maxX = max([x for y, x in elves])
	return minY, maxY, minX, maxX

def printBoard(elves):
	minY, maxY, minX, maxX = getBoardSize(elves)
	for y in range(minY, maxY+1):
		print(''.join(['#' if (y, x) in elves else '.' for x in range(minX, maxX+1)]))

def countSpaces(elves):
	minY, maxY, minX, maxX = getBoardSize(elves)
	return sum([1 for x in range(minX, maxX+1) for y in range(minY, maxY+1) if (y, x) not in elves])

step = 0
while True:
	proposedMoves = calcMoves(elves, step)
	done, elves = makeMoves(elves, proposedMoves)
	if step + 1 == 10:
		print('Part 1:', countSpaces(elves))
	if done:
		print('Part 2:', step + 1)
		break
	step += 1

