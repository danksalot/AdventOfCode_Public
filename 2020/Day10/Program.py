with open('Input') as inFile:
	lines = [int(x) for x in inFile.readlines()]

lines.append(0)
lines.append(max(lines) + 3)
lines.sort()

distances = { 1:0, 2:0, 3:0 }
groupsOfOne = { 1:0, 2:0, 3:0, 4:0 }
oneCount = 0

for x in range(1, len(lines)):
	distance = lines[x] - lines[x-1]
	distances[distance] += 1
	if distance == 1:
		oneCount += 1
	if distance == 3 and oneCount != 0:
		groupsOfOne[oneCount] += 1
		oneCount = 0

print('Part 1:', distances[1] * distances[3])

# Groups of 2 1's add 2 options each
# Groups of 3 1's add 4 options each
# Groups of 4 1's add 7 options each
print('Part 2:', (2 ** groupsOfOne[2]) * (4 ** groupsOfOne[3]) * (7 ** groupsOfOne[4]))

