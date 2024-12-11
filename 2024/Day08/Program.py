from itertools import combinations

with open('Input') as inFile:
	lines = [line.rstrip() for line in inFile.readlines()]

antennas = dict()
for y in range(len(lines)):
	for x in range(len(lines[y])):
		if lines[y][x] != '.':
			if lines[y][x] in antennas:
				antennas[lines[y][x]].append([y, x])
			else:
				antennas[lines[y][x]] = [[y, x]]

antinodes = set()
for antenna in antennas.values():
	pairs = list(combinations(antenna, 2))
	for pair in pairs:
		ydiff = pair[0][0] - pair[1][0]
		xdiff = pair[0][1] - pair[1][1]
		antinode1 = [pair[0][0] + ydiff, pair[0][1] + xdiff]
		antinode2 = [pair[1][0] - ydiff, pair[1][1] - xdiff]
		if (antinode1[0] >= 0 and antinode1[0] < len(lines)) and (antinode1[1] >= 0 and antinode1[1] < len(lines[0])):
			antinodes.add(tuple(antinode1))
		if (antinode2[0] >= 0 and antinode2[0] < len(lines)) and (antinode2[1] >= 0 and antinode2[1] < len(lines[0])):
			antinodes.add(tuple(antinode2))

print("Part 1:", len(antinodes))

antinodes = set()
for antenna in antennas.values():
	pairs = list(combinations(antenna, 2))
	for pair in pairs:
		antinodes.add(tuple(pair[0]))
		antinodes.add(tuple(pair[1]))

		ydiff = pair[0][0] - pair[1][0]
		xdiff = pair[0][1] - pair[1][1]
		antinode1 = [pair[0][0] + ydiff, pair[0][1] + xdiff]
		antinode2 = [pair[1][0] - ydiff, pair[1][1] - xdiff]

		while (antinode1[0] >= 0 and antinode1[0] < len(lines)) and (antinode1[1] >= 0 and antinode1[1] < len(lines[0])):
			antinodes.add(tuple(antinode1))
			antinode1 = [antinode1[0] + ydiff, antinode1[1] + xdiff]
		while (antinode2[0] >= 0 and antinode2[0] < len(lines)) and (antinode2[1] >= 0 and antinode2[1] < len(lines[0])):
			antinodes.add(tuple(antinode2))
			antinode2 = [antinode2[0] - ydiff, antinode2[1] - xdiff]

print("Part 2:", len(antinodes))
