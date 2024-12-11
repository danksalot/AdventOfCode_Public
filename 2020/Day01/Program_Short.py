# Adapted from suggestions in a post here: https://cestlaz.github.io/post/advent-2020-day-01/
from itertools import combinations
from math import prod

with open('Input') as inFile:
	lines = [int(x) for x in inFile.readlines()]

	print('Part 1:', prod([x for x in lines if 2020 - x in lines]))
	print('Part 2:', prod(set([x for x in lines for y in lines if 2020 - (x + y) in lines])))
