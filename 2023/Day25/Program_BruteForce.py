from collections import defaultdict
from itertools import combinations
from copy import deepcopy

with open('Input') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

connections = defaultdict(set)
connectionPairs = set()

for line in lines:
	parts = line.split(': ')
	rightparts = parts[1].split(' ')
	for part in rightparts:
		connections[parts[0]].add(part)
		connections[part].add(parts[0])
		connectionPairs.add((min(parts[0], part), max(parts[0], part)))

def findGroups(connections):
	groups = [connections[c].union(set([c])) for c in connections]
	i = 0
	while i < len(groups):
		combined = False
		for component in groups[i]:
			for otherGroup in groups[i+1:]:
				if component in otherGroup:
					combined = True
					groups[i] = groups[i].union(otherGroup)
					groups.remove(otherGroup)
					break
		if not combined:
			i += 1
	return groups	

for pairs in combinations(connectionPairs, 3):
	for pair in pairs:
		a, b = pair
		connections[a].remove(b)
		connections[b].remove(a)

	groups = findGroups(connections)
	if len(groups) == 2:
		print('Part 1:', len(groups[0]) * len(groups[1]))
		exit()

	for pair in pairs:
		a, b = pair
		connections[a].add(b)
		connections[b].add(a)
