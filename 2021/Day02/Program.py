with open('Input') as inFile:
	lines = inFile.read().splitlines()

horizontal = 0
depth = 0

for line in lines:
	parts = line.split()
	if parts[0] == 'forward':
		horizontal += int(parts[1])
	elif parts[0] == 'up':
		depth -= int(parts[1])
	elif parts[0] == 'down':
		depth += int(parts[1])
	else:
		print('Wrong!')

print(horizontal, depth, horizontal * depth)

horizontal = 0
depth = 0
aim = 0

for line in lines:
	parts = line.split()
	if parts[0] == 'forward':
		horizontal += int(parts[1])
		depth += aim * int(parts[1])
	elif parts[0] == 'up':
		aim -= int(parts[1])
	elif parts[0] == 'down':
		aim += int(parts[1])
	else:
		print('Wrong!')

print(horizontal, depth, horizontal * depth)