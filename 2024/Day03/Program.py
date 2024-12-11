import re

with open('Input') as inFile:
	lines = inFile.readlines()

part1Total = 0
part2Total = 0
enabled = True
for line in lines:
	instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
	for instruction in instructions:
		if instruction == 'do()':
			enabled = True
		elif instruction == 'don\'t()':
			enabled = False
		else:
			parts = re.findall(r'\d{1,3}', instruction)
			part1Total += int(parts[0]) * int(parts[1])
			if enabled:
				part2Total += int(parts[0]) * int(parts[1])

print("Part 1:", part1Total)
print("Part 2:", part2Total)
