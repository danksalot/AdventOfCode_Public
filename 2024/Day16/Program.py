
import heapq

with open('Input') as inFile:
	lines = [line.rstrip() for line in inFile.readlines()]

walls = []
start = None
finish = None

for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] == '#':
			walls.append((y, x))
		elif lines[y][x] == 'S':
			start = (y, x, 1)
		elif lines[y][x] == 'E':
			finish = (y, x)

DIRECTIONS = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
def getNeighbors(position):
	y, x, heading = position
	adjacentNodes = [(1000, (y, x, (heading + 1) % 4)), (1000, (y, x, (heading - 1) % 4))]
	if (y + DIRECTIONS[heading][0], x + DIRECTIONS[heading][1]) not in walls:
		adjacentNodes.append((1, (y + DIRECTIONS[heading][0], x + DIRECTIONS[heading][1], heading)))
	return adjacentNodes

def dijkstra(start, end):
	visited = {}
	q = []
	heapq.heappush(q, (0, start))

	while q:
		cost, cur = heapq.heappop(q)
		if cur in visited:
			continue
		visited[cur] = cost
		if cur[0] == end[0] and cur[1] == end[1] and (len(end) == 2 or cur[2] == end[2]):
			continue
		for edgeCost, next in getNeighbors(cur):
			if next not in visited or visited[next] > cost + edgeCost:
				heapq.heappush(q, (cost + edgeCost, next))

	best = [val for key, val in visited.items() if key[0] == end[0] and key[1] == end[1] and (len(end) == 2 or key[2] == end[2])][0]
	return best, {k: v for k, v in visited.items() if v <= best}

best, forward = dijkstra(start, finish)
print("Part 1:", best)

backward = []
best0, backward0 = dijkstra((finish[0], finish[1], 0), start)
if best0 == best:
	backward.append(backward0)

best1, backward1 = dijkstra((finish[0], finish[1], 1), start)
if best1 == best:
	backward.append(backward1)

best2, backward2 = dijkstra((finish[0], finish[1], 2), start)
if best2 == best:
	backward.append(backward2)

best3, backward3 = dijkstra((finish[0], finish[1], 3), start)
if best3 == best:
	backward.append(backward3)

# Reverse direction since these are backward
backward = {(k[0], k[1], (k[2] + 2) % 4): v for k, v in backward[0].items()}

goodSeats = set()
for y in range(len(lines)):
	for x in range(len(lines[y])):
		for heading in range(4):
			if (y, x, heading) in forward and (y, x, heading) in backward and forward[(y, x, heading)] + backward[(y, x, heading)] == best:
				goodSeats.add((y, x))
print("Part 2:", len(goodSeats))
