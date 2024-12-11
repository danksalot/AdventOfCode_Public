from itertools import cycle

with open('testInput') as inFile:
	inputLine = inFile.read()

class Rock:
	Type = 'X'
	Coords = []
	Stopped = False

	def __init__(self, type, height):
		self.Type = type
		if type == '-': 
			self.Coords = [(height, 3), (height, 4), (height, 5), (height, 6)]
		elif type == '+':
			self.Coords = [(height + 2, 4), (height + 1, 3), (height + 1, 4), (height + 1, 5), (height, 4)]
		elif type == 'L':
			self.Coords = [(height + 2, 5), (height + 1, 5), (height, 3), (height, 4), (height, 5)]
		elif type == 'l':
			self.Coords = [(height + 3, 3), (height + 2, 3), (height + 1, 3), (height, 3)]
		elif type == 'o':
			self.Coords = [(height + 1, 3), (height + 1, 4), (height, 3), (height, 4)]

	def fall(self, obstructions):
		if any((y-1, x) in obstructions for y, x in self.Coords):
			self.Stopped = True
			return False
		for i in range(len(self.Coords)):
			self.Coords[i] = (self.Coords[i][0] - 1, self.Coords[i][1])
		return True

	def push(self, dx, obstructions):
		if any((y, x+dx) in obstructions for y, x in self.Coords):
			return False
		for i in range(len(self.Coords)):
			self.Coords[i] = (self.Coords[i][0], self.Coords[i][1] + dx)
		return True

def getCurrentHeight(obstructions):
	return max([y for y, x in obstructions if x > 0 and x < 8])

def printBoard(obstructions, rock, height = -1):
	upperBound = max(y for y, x in rock.Coords + list(obstructions))
	lowerBound = max(-1, upperBound - height)
	for y in range(upperBound, lowerBound, -1):
		print(''.join(['@' if (y, x) in rock.Coords and not rock.Stopped else '.' if (y, x) not in obstructions else '#' for x in range(9)]))
	print('\n\n')


windSpeed = {'<': -1, '>': 1}
wind = cycle(inputLine)
rockTypes = cycle('-+Llo')

obstructions = set()
# Add floor to obstructions
for i in range(9):
	obstructions.add((0, i))

# Add walls to obstructions
def extendWalls(obstructions):
	height = getCurrentHeight(obstructions)
	for i in range(height, height + 8):
		obstructions.add((i, 0))
		obstructions.add((i, 8))
	return obstructions

for i in range(10):
	falling = True
	rock = Rock(next(rockTypes), getCurrentHeight(obstructions) + 4)
	obstructions = extendWalls(obstructions)
	while falling:
		printBoard(obstructions, rock, 15)
		rock.push(windSpeed[next(wind)], obstructions)
		printBoard(obstructions, rock, 15)
		falling = rock.fall(obstructions)		

	for x in rock.Coords:
		obstructions.add(x)

	# printBoard(obstructions, rock)

print('Part 1:', getCurrentHeight(obstructions))



# # Reset
# windIndex = 0
# rockIndex = 0
# rockTypeString = '-+Llo'

# obstructions = set()
# # Add floor to obstructions
# for i in range(9):
# 	obstructions.add((0, i))



# for i in range(1000000000000):
# 	if i % 1720 == 1440:
# 		print('Rock number:', i, 'Current height:', getCurrentHeight(obstructions))

# 	falling = True
# 	rock = Rock(rockTypeString[rockIndex], getCurrentHeight(obstructions) + 4)

# 	# if windIndex == 0:
# 	# 	print('Step:', i, 'rockIndex:', rockIndex, 'windIndex:', windIndex, 'height:', getCurrentHeight(obstructions))

# 	obstructions = extendWalls(obstructions)

	


	
	
# 	# printBoard(obstructions, rock, 15)
# 	while falling:
# 		# if rockIndex == 0 and windIndex == 0:
# 		# 	printBoard(obstructions, rock, 15)
# 		# 	print('Rock number:', i, 'Current height:', getCurrentHeight(obstructions))

# 		dx = windSpeed[inputLine[windIndex]]
# 		windIndex = (windIndex + 1) % len(inputLine)

		

# 		rock.push(dx, obstructions)
# 		# printBoard(obstructions, rock)
# 		falling = rock.fall(obstructions)
# 	rockIndex = (rockIndex + 1) % len(rockTypeString)		

# 	for x in rock.Coords:
# 		obstructions.add(x)




print('Part 2:', (581395348 * 2729) + 2229)