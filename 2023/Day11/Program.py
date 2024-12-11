from itertools import combinations

with open('Input') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

emptyRows = [y for y in range(len(lines)) if lines[y].count('#') == 0]
emptyCols = [x for x in range(len(lines[0])) if [lines[y][x] for y in range(len(lines))].count('#') == 0]
galaxies = [(y,x) for y in range(len(lines)) for x in range(len(lines[y])) if lines[y][x] == '#']

def manhattan(a, b, expansionFactor):
	distance = abs(a[0]-b[0]) + abs(a[1]-b[1])
	expansion = sum([1 for y in range(min(a[0], b[0]), max(a[0], b[0])) if y in emptyRows]) 
	expansion += sum([1 for x in range(min(a[1], b[1]), max(a[1], b[1])) if x in emptyCols])
	return (distance - expansion) + (expansion * expansionFactor)

print('Part 1:', sum([manhattan(pair[0], pair[1], 2) for pair in combinations(galaxies, 2)]))
print('Part 2:', sum([manhattan(pair[0], pair[1], 1000000) for pair in combinations(galaxies, 2)]))
