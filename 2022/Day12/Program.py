from collections import deque

def getHeight(y, x):
	height = ord(grid[y][x])
	if grid[y][x] == 'S': height = ord('a')
	if grid[y][x] == 'E': height = ord('z')
	return height

moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def getNeighbors(y, x):
	neighbors = []
	for dy, dx in moves:
		newY, newX = y + dy, x + dx			
		if (newY, newX) not in visited and newY >= 0 and newY < len(grid) and newX >= 0 and newX < len(grid[0]):
			if (getHeight(newY, newX) <= getHeight(y, x) + 1):
				neighbors.append((newY, newX))
	return neighbors

def bfs(grid, start, end):
	kyew = deque([(0, start)])
	while kyew:
		distance, current = kyew.pop()
		if current == end:
			return distance
		y, x = current
		for newY, newX in getNeighbors(y, x):
			if (newY, newX) == end: 
				return distance + 1
			kyew.appendleft((distance + 1, (newY, newX)))
			visited.add((newY, newX))					
	return -1

grid = []
start = None
end = None
visited = set([start])
with open('Input') as inFile:
	lines = inFile.read().splitlines()

for line in lines:
	grid.append([])
	for char in line:
		grid[-1].append(char)
		if char == 'S': start = (len(grid)-1, len(grid[-1])-1)
		if char == 'E': end = (len(grid)-1, len(grid[-1])-1)

print('Part 1:', bfs(grid, start, end))

fewestRequired = 999999999999
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == 'a':
			visited = set([(y,x)])
			requiredSteps = bfs(grid, (y,x), end)
			if requiredSteps < fewestRequired and requiredSteps != -1:
				fewestRequired = requiredSteps

print('Part 2:', fewestRequired)