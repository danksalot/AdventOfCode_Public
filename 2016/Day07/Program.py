import re

part1Count = 0
part2Count = 0

def part1Match(line):
	return any(a == d and b == c and a != b for a, b, c, d in zip(line, line[1:], line[2:], line[3:]))

def part2Match(outOfBrackets, inBrackets):
	return any(a == c and a != b and b+a+b in inBrackets for a, b, c in zip(outOfBrackets, outOfBrackets[1:], outOfBrackets[2:]))

with open("Input") as inputFile:
	lines = inputFile.readlines()
    
for line in lines:
	line = re.split(r'\[([^\]]+)\]', line)
	parts = ' '.join(line[::2]), ' '.join(line[1::2])
	if part1Match(parts[0]) and not part1Match(parts[1]):
		part1Count += 1

	if part2Match(parts[0], parts[1]):
		part2Count += 1

print "Part 1 answer:", part1Count
print "Part 2 answer:", part2Count