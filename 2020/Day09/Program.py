def checkIfSum(list, goal):
	for i in range(len(list) - 1):
		for j in range(1, len(list)):
			if (list[i] + list[j]) == goal:
				return True
	return False

with open('Input') as inFile:
	lines = [int(x) for x in inFile.readlines()]

invalidNum = None
for x in range(25, len(lines)):
	if not checkIfSum(lines[x-25:x], lines[x]):
		invalidNum = lines[x]
		break

print('Part 1:', invalidNum)

for x in range(len(lines)):
	total = 0
	offset = 0
	while total < invalidNum:
		total += lines[x + offset]
		offset += 1
	
	if total == invalidNum:
		print('Part 2:', min(lines[x:x + offset]) + max(lines[x:x + offset]))
		break
