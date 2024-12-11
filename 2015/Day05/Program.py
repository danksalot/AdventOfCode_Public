import re

part1Count = 0
part2Count = 0

with open("Input") as inputFile:
    lines = inputFile.readlines()
    
for line in lines:
	if 3 <= sum(line.count(x) for x in ("a", "e", "i", "o", "u")):
		if re.match(r'.*(.)\1.*', line) != None:
			if 0 == sum(line.count(x) for x in ("ab", "cd", "pq", "xy")):
				part1Count += 1

for line in lines:
	if re.match(r'.*(.)(.).*\1\2.*', line) != None:
		if re.match(r'.*(.)(.)\1.*', line) != None:
			part2Count += 1

print "Part1 Count:", part1Count
print "Part2 Count:", part2Count
