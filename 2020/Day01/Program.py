from itertools import combinations
from math import prod

with open('Input') as inFile:
	lines = [int(x) for x in inFile.readlines()]

for c in combinations(lines, 2):
	if sum(c) == 2020: print('Part 1:', prod(c))

for c in combinations(lines, 3):
	if sum(c) == 2020: print('Part 2:', prod(c))
