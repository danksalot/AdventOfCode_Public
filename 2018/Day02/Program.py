from collections import Counter
from itertools import combinations
from difflib import ndiff

exactlyTwo = 0
exactlyThree = 0

with open('Input') as inFile:
	lines = inFile.read().splitlines()
	for line in lines:
		counts = Counter(line)
		exactlyTwo += 1 if 2 in counts.values() else 0
		exactlyThree += 1 if 3 in counts.values() else 0

	print('Part 1:', (exactlyTwo * exactlyThree))

	for pair in combinations(lines, 2):
		numDiffs = len([d for d in ndiff(pair[0], pair[1]) if d[0] != ' '])
		if (numDiffs == 2):  # 2 diffs - one letter removed and one added
			print('Part 2:', ''.join([d.strip() for d in ndiff(pair[0], pair[1]) if d[0] == ' ']))
			exit()
