
with open('Input') as inFile:
	lines = [line.rstrip('\n') for line in inFile.readlines()]

count = 0
for y in range(len(lines)):
	for x in range(len(lines[y])):
		# Horizontal backward and forward
		if x < len(lines[y])-3:
			if lines[y][x] == 'X' and lines[y][x+1] == 'M' and lines[y][x+2] == 'A' and lines[y][x+3] == 'S':
				count += 1
			if lines[y][x] == 'S' and lines[y][x+1] == 'A' and lines[y][x+2] == 'M' and lines[y][x+3] == 'X':
				count += 1
		# Vertical backward and forward
		if y < len(lines)-3:
			if lines[y][x] == 'X' and lines[y+1][x] == 'M' and lines[y+2][x] == 'A' and lines[y+3][x] == 'S':
				count += 1
			if lines[y][x] == 'S' and lines[y+1][x] == 'A' and lines[y+2][x] == 'M' and lines[y+3][x] == 'X':
				count += 1
		# Diagonal right and left
		if y < len(lines)-3 and x < len(lines[y])-3:
			if lines[y][x] == 'X' and lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S':
				count += 1
			if lines[y][x] == 'S' and lines[y+1][x+1] == 'A' and lines[y+2][x+2] == 'M' and lines[y+3][x+3] == 'X':
				count += 1
		if y < len(lines)-3 and x > 2:
			if lines[y][x] == 'X' and lines[y+1][x-1] == 'M' and lines[y+2][x-2] == 'A' and lines[y+3][x-3] == 'S':
				count += 1
			if lines[y][x] == 'S' and lines[y+1][x-1] == 'A' and lines[y+2][x-2] == 'M' and lines[y+3][x-3] == 'X':
				count += 1
		
print("Part 1:", count)

count = 0
for y in range(1, len(lines)-1):
	for x in range(1, len(lines[y])-1):
		# Only start checking if the center is an A
		if lines[y][x] == 'A' and (
			# Check the \ diagonal
			(lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S') or
			(lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M')
		) and (
			# Check the / diagonal
			(lines[y+1][x-1] == 'M' and lines[y-1][x+1] == 'S') or
			(lines[y+1][x-1] == 'S' and lines[y-1][x+1] == 'M')
		):
			count += 1

print("Part 2:", count)
