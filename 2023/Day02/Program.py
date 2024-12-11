import re

with open('Input') as inFile:
	lines = inFile.readlines()

total = 0
totalPower = 0

for line in lines:
	maxReds = max([int(r) for r in re.findall(r'(\d+) red', line)])
	maxGreens = max([int(g) for g in re.findall(r'(\d+) green', line)])
	maxBlues = max([int(b) for b in re.findall(r'(\d+) blue', line)])

	if maxReds <= 12 and maxGreens <= 13 and maxBlues <= 14: 
		total += int(re.findall(r'(\d+)', line)[0])	
	totalPower += maxReds * maxGreens * maxBlues
	
print('Part 1: ', total)
print('Part 2: ', totalPower)