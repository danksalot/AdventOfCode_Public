
with open('Input') as inFile:
	lines = [line.strip() for line in inFile.readlines()]

roomWidth = 101
roomHeigt = 103
robots = []
for line in lines:
	parts = line.split(' v')
	position = parts[0].split('=')[1].split(',')
	velocity = parts[1].split('=')[1].split(',')
	robots.append([int(position[1]), int(position[0]), int(velocity[1]), int(velocity[0])])

def move(robots):
	for robot in robots:
		robot[0] = (robot[0] + robot[2]) % roomHeigt
		robot[1] = (robot[1] + robot[3]) % roomWidth
	return robots

def moveIterations(iterations, robots):
	for i in range(iterations):
		robots = move(robots)
	return robots

def printRobots(robots):
	for i in range(roomHeigt):
		for j in range(roomWidth):
			numRobots = sum(1 for robot in robots if robot[0] == i and robot[1] == j)
			if numRobots > 0:
				print(numRobots, end='')
			else:
				print('.', end='')
		print()
	print('\n')

def calcSafetyScore(robots):
	horizontalDivider = roomHeigt // 2
	verticalDivider = roomWidth // 2
	q1Robots = sum(1 for robot in robots if robot[0] < horizontalDivider and robot[1] < verticalDivider)
	q2Robots = sum(1 for robot in robots if robot[0] < horizontalDivider and robot[1] > verticalDivider)
	q3Robots = sum(1 for robot in robots if robot[0] > horizontalDivider and robot[1] < verticalDivider)
	q4Robots = sum(1 for robot in robots if robot[0] > horizontalDivider and robot[1] > verticalDivider)
	return q1Robots * q2Robots * q3Robots * q4Robots

robots = moveIterations(100, robots)
print("Part 1:", calcSafetyScore(robots))

for i in range(101, 10000):
	robots = move(robots)
	robotPositions = [(robot[0], robot[1]) for robot in robots]
	if len(robotPositions) == len(set(robotPositions)):
		# printRobots(robots)
		print('Part 2:', i)
		break
