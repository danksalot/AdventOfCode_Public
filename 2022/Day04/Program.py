with open('Input') as inFile:
	lines = inFile.read().splitlines()

def expand(pair):
	return list(range(pair[0], pair[1]+1))

fullOverlaps = 0
partialOverlaps = 0
for line in lines:
	pair = line.split(',')	
	a = expand([int(x) for x in pair[0].split('-')])
	b = expand([int(x) for x in pair[1].split('-')])

	abOverlaps = len([x for x in a if x in b])
	baOverlaps = len([x for x in b if x in a])
	
	if len(a) == abOverlaps or len(b) == baOverlaps:
		fullOverlaps += 1

	if abOverlaps + baOverlaps > 0:
		partialOverlaps += 1

print("Part 1:", fullOverlaps)
print("Part 2:", partialOverlaps)
