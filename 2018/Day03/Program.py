arraySize = 1100
fabricPart1 = [[0 for i in range(arraySize)] for j in range(arraySize)]
fabricPart2 = [[0 for i in range(arraySize)] for j in range(arraySize)]
count = 0
claims = []
overlaps = []

with open('Input') as inFile:
	lines = inFile.read().splitlines()
	for line in lines:
		parts = line.split()
		claim = int(parts[0][1:])
		claims.append(claim)
		coords = parts[2].split(',')
		size = parts[3].split('x')
		x1 = int(coords[0])
		y1 = int(coords[1][0:-1])
		x2 = x1 + int(size[0])
		y2 = y1 + int(size[1])

		for x in range(x1, x2):
			for y in range(y1, y2):
				fabricPart1[y][x] += 1

		for x in range(x1, x2):
			for y in range(y1, y2):
				if fabricPart2[y][x] != 0:
					overlaps.append(fabricPart2[y][x])
					overlaps.append(claim)
				fabricPart2[y][x] = claim

	for x in fabricPart1:
		count += sum([1 for y in x if y > 1])

print('Part 1:', count)
print('Part 2:', [x for x in claims if x not in overlaps][0])