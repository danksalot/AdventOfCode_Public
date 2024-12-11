with open('Input') as inFile:
	lines = inFile.read().splitlines()

readyTime = int(lines[0])
departTime = None
allBuses = lines[1].split(',')
buses = [int(b) for b in allBuses if b != 'x']

for x in range(readyTime, readyTime + 10):
	for bus in buses:
		if x % bus == 0:
			departTime = x
			print('Part 1:', bus * (departTime - readyTime))
			break

step = buses[0]
start = step
schedule = {}
stop = 300000000000000
for x in range(len(allBuses)):
	if allBuses[x].isdigit():
		minute = x
		busName = int(allBuses[x])

		for t1 in range(start, stop, step):
			# print('Searching for', busName, 'starting from', start, 'counting by', step)
			if (t1 + x) % busName == 0:
				start = t1
				for t2 in range(start + step, stop, step):
					# print('Inner searching for', busName, 'starting from', start, 'counting by', step)
					if (t2 + x) % busName == 0:
						step = t2 - t1
						break
				break

print('Part 2:', start)
