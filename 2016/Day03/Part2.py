def IsValidTriangle(sides):
	sides.sort()
	return sides[0] + sides[1] > sides [2]

count = 0

with open("Input") as inputFile:
	lines = inputFile.readlines()

for step in range(0, len(lines), 3):
	group = lines[step:step+3]

	group[0] = map(int, group[0].split())
	group[1] = map(int, group[1].split())
	group[2] = map(int, group[2].split())

	if IsValidTriangle([group[0][0], group[1][0], group[2][0]]):
		count += 1
	if IsValidTriangle([group[0][1], group[1][1], group[2][1]]):
		count += 1
	if IsValidTriangle([group[0][2], group[1][2], group[2][2]]):
		count += 1

print "Valid triangles:", count
