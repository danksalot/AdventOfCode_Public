with open('Input') as inFile:
	lines = [int(x) for x in inFile.readlines()]

increaseCount = 0
previous = 1000000

for line in lines:
	if line > previous:
		increaseCount += 1

	previous = line

print("Part 1: " + str(increaseCount))

increaseCount = 0
previous = 1000000
for i in range(len(lines) - 2):
	total = lines[i] + lines[i+1] + lines[i+2]

	if total > previous:
		increaseCount += 1

	previous = total

print("Part 2: " + str(increaseCount))

print("Part 1:", sum(1 for i in range(len(lines) - 1) if lines[i] < lines[i+1]))
print("Part 2:", sum(1 for i in range(len(lines) - 3) if lines[i] + lines[i+1] + lines[i+2] < lines[i+1] + lines[i+2] + lines[i+3]))