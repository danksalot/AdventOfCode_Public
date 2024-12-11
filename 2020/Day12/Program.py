def part1Action(op, x, y, facing):
	if op.startswith('N'):
		y += int(op[1:])
	if op.startswith('S'):
		y -= int(op[1:])
	if op.startswith('E'):
		x += int(op[1:])
	if op.startswith('W'):
		x -= int(op[1:])
	if op.startswith('R'):
		facing = (facing + int(op[1:])) % 360
	if op.startswith('L'):
		facing = (facing - int(op[1:])) % 360
	if op.startswith('F'):
		if facing == 0: op = op.replace('F','E')
		if facing == 90: op = op.replace('F','S')
		if facing == 180: op = op.replace('F','W')
		if facing == 270: op = op.replace('F','N')
		return part1Action(op, x, y, facing)
	return x, y, facing

def part2Action(op, x, y, wx, wy):
	if op.startswith('L'): return part2Action('R' + str(360 - int(op[1:])), x, y, wx, wy)
	if op.startswith('N'): wy += int(op[1:])
	if op.startswith('S'): wy -= int(op[1:])
	if op.startswith('E'): wx += int(op[1:])
	if op.startswith('W'): wx -= int(op[1:])
	if op.startswith('R'):
		for i in range(int(int(op[1:])/90)):
			newWY = ((wx - x) * -1 if wx > x else x - wx)
			newWX = (wy - y if wy > y else (y - wy) * -1)

			wx = x + newWX
			wy = y + newWY	
	if op.startswith('F'):
		xdist = wx - x
		ydist = wy - y
		for i in range(int(op[1:])):
			x += xdist
			wx += xdist
			y += ydist
			wy += ydist
	return x, y, wx, wy

with open('Input') as inFile:
	lines = inFile.read().splitlines()

x = y = facing = 0
for line in lines:
	x, y, facing = part1Action(line, x, y, facing)

print('Part 1:', abs(x) + abs(y))

x = y = 0
wx = 10
wy = 1
for line in lines:
	x, y, wx, wy = part2Action(line, x, y, wx, wy)

print('Part 2:', abs(x) + abs(y))