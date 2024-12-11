def IsValidTriangle(line):
	sides = map(int, line.split())
	sides.sort()
	return sides[0] + sides[1] > sides [2]

count = 0

with open("Input") as inputFile:
	lines = inputFile.readlines()
    
for line in lines:
	if IsValidTriangle(line):
		count += 1

print "Valid triangles:", count
