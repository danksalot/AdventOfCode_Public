import re

with open('Input') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

directions = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
holes = {}
holes[(0, 0)] = 'R'
heading = 'U'
y = 0
x = 0

def dig(dir, dist):
	global y, x, heading, holes
	if heading + dir in ['UL', 'RD']: holes[(y, x)] = '7'
	if heading + dir in ['UR', 'LD']: holes[(y, x)] = 'F'
	if heading + dir in ['DL', 'RU']: holes[(y, x)] = 'J'
	if heading + dir in ['DR', 'LU']: holes[(y, x)] = 'L'
	heading = dir
	for i in range(dist):
		y += directions[dir][0]
		x += directions[dir][1]
		holes[(y, x)] = dir

for line in lines:
	digits = re.search(r'\d+', line).group()
	dig(line[0], int(digits))

minX = min([h[1] for h in holes])
maxX = max([h[1] for h in holes])
minY = min([h[0] for h in holes])
maxY = max([h[0] for h in holes])

def isInterior(y, x):
	bordersLeft = [1 for h in holes if h[0] == y and h[1] < x and holes[h] in 'UDF7']
	return len(bordersLeft) % 2 == 1
				
total = 0		
for y in range(minY, maxY+1):
	for x in range(minX, maxX+1):
		if (y, x) in holes or isInterior(y, x):
			total += 1

print('Part 1:', total)
