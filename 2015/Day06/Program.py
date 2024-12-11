grid = [[[0, 0] for w in range(1000)] for h in range(1000)]

with open("Input") as inputFile:
    lines = inputFile.readlines()
    
for line in lines:
	parts = line.split(' ')
	command = ''
	if len(parts) == 4:
		command = 'toggle'
		firstPair = parts[1].split(',')
		lastPair = parts[3].split(',')
	elif len(parts) == 5:
		command = parts[1]
		firstPair = parts[2].split(',')
		lastPair = parts[4].split(',')

	firstX = int(firstPair[0])
	firstY = int(firstPair[1])
	lastX = int(lastPair[0])
	lastY = int(lastPair[1])

	for y in range(firstY, lastY + 1):
		for x in range(firstX, lastX + 1):
			if command == 'on':
				grid[y][x][0] = 1
				grid[y][x][1] += 1				
			elif command == 'off':
				grid[y][x][0] = 0
				grid[y][x][1] = max(0, grid[y][x][1] - 1)
			elif command == 'toggle':
				grid[y][x][1] += 2
				if grid[y][x][0] == 0:
					grid[y][x][0] = 1
				else:
					grid[y][x][0] = 0

totalOn = 0
totalLevel = 0

for x in range(1000):
	for y in range(1000):
		totalOn += grid[y][x][0]
		totalLevel += grid[y][x][1]

print 'Part 1: ' + str(totalOn)
print 'Part 2: ' + str(totalLevel)
