from itertools import cycle
from functools import reduce
import numpy as np

with open('Input') as inFile:
	lines = inFile.readlines()

def extractNode(nodeString):
	name = nodeString[0:3]
	left = nodeString[7:10]
	right = nodeString[12:15]
	return name, [left, right]	

instructions = cycle(lines[0].strip())
nodes = {}
for node in lines[2:]:
	name, paths = extractNode(node)
	nodes[name] = paths

currentNode = 'AAA'
steps = 0
for instruction in instructions:
	steps += 1
	if instruction == 'L':
		currentNode = nodes[currentNode][0]
	elif instruction == 'R':
		currentNode = nodes[currentNode][1]
	if currentNode == 'ZZZ':
		break

print('Part 1:', steps)

currentNodes = [node for node in nodes if node[2] == 'A']
cycleSizes = []
for node in currentNodes:
	steps = 0
	for instruction in instructions:
		steps += 1
		if instruction == 'L':
			node = nodes[node][0]
		elif instruction == 'R':
			node = nodes[node][1]
		if node[2] == 'Z':
			cycleSizes.append(steps)
			break

leastCommonMultiple = reduce(lambda x, y: np.lcm(x, y, dtype=object), cycleSizes)
print('Part 2:', leastCommonMultiple)
