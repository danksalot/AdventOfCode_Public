from collections import defaultdict

passages = defaultdict(list)

with open('Input') as inFile:
	lines = inFile.read().splitlines()

for line in lines:
	fr, to = line.split('-')
	if fr not in passages[to]:
		passages[to].append(fr)
	if to not in passages[fr]:
		passages[fr].append(to)

def countPaths(start, end, visited, usedDouble = False):
	visited = visited | {start}

	if start == end:
		return 1	

	numPaths = 0
	for destination in passages[start]:
		newUsedDouble = usedDouble
		if destination.islower() and destination in visited:
			if usedDouble or destination in ['start', 'end']:
				continue
			else:
				newUsedDouble = True

		numPaths += countPaths(destination, end, visited, newUsedDouble)

	return numPaths

print(countPaths('start', 'end', set(), usedDouble = True))
print(countPaths('start', 'end', set()))
