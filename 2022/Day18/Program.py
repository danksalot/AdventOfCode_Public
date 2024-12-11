with open('Input') as inFile:
	lines = inFile.read().splitlines()

drops = set()
for line in lines:
	x, y, z = map(int, line.split(','))
	drops.add((x, y, z))

neighborOffsets = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
def countSides(drops):
	exposedSides = 0
	for x, y, z in drops:
		exposedSides += sum([1 if (x+dx, y+dy, z+dz) not in drops else 0 for dx, dy, dz in neighborOffsets])
	return exposedSides

exposedSides = countSides(drops)
print('Part 1:', exposedSides)

def getOpenAirBlocks(start):
	visited = set()
	kyew = set([start])
	while kyew:
		x, y, z = kyew.pop()
		visited.add((x, y, z))
		neighbors = [(x+dx, y+dy, z+dz) for dx, dy, dz in neighborOffsets]
		neighbors = [(x, y, z) for (x, y, z) in neighbors if x >= -1 and x <= 20]
		neighbors = [(x, y, z) for (x, y, z) in neighbors if y >= -1 and y <= 20]
		neighbors = [(x, y, z) for (x, y, z) in neighbors if z >= -1 and z <= 20]
		for newX, newY, newZ in neighbors:			
			if (newX, newY, newZ) not in visited and (newX, newY, newZ) not in drops:
				kyew.add((newX, newY, newZ))				
	return visited

def countSidesP2(drops, openAirBlocks):
	exposedSides = 0
	for x, y, z in drops:
		exposedSides += sum([1 if (x+dx, y+dy, z+dz) in openAirBlocks else 0 for dx, dy, dz in neighborOffsets])
	return exposedSides

openAir = getOpenAirBlocks((20,20,20))
print('Part 2:', countSidesP2(drops, openAir))