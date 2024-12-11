DIRECTIONS = [
	(-1,  0), #UP
	( 0,  1), #RIGHT
	( 1,  0), #DOWN
	( 0, -1), #LEFT
]

class Cart:
	def __init__(self, coords, direction, turn):
		self.coords = coords
		self.direction = direction
		self.turn = turn

	def Move(self):
		newY = self.coords[0] + DIRECTIONS[self.direction][0]
		newX = self.coords[1] + DIRECTIONS[self.direction][1]
		self.coords = (newY,newX)
		return newY, newX

	def MakeTurn(self, path):
		if path == '\\':
			if self.direction in (1, 3):
				self.direction = (self.direction + 1) % 4
			else:
				self.direction = (self.direction - 1) % 4
		elif path == '/':
			if self.direction in (1, 3):
				self.direction = (self.direction - 1) % 4
			else:
				self.direction = (self.direction + 1) % 4
		elif path == '+':
			self.direction = (self.direction - 1 + self.turn) % 4
			self.turn = (self.turn + 1) % 3

	def FormatCoords(self):
		return str(self.coords[1]) + ',' + str(self.coords[0])

def ToDirection(char):
	direction = None
	if char == '^':
		direction = 0
	elif char == '>':
		direction = 1
	elif char == 'v':
		direction = 2
	elif char == '<':
		direction = 3
	return direction

def ProcessTick(grid, cartsBeforeMoving):
	cartsBeforeMoving = sorted(cartsBeforeMoving, key=lambda x: (x.coords[0], x.coords[1]))
	cartsAfterMoving = []
	crashedCarts = []
	crashes = []
	while cartsBeforeMoving:
		currentCart = cartsBeforeMoving.pop(0)
		newY, newX = currentCart.Move()
		if any(c.coords == currentCart.coords for c in cartsAfterMoving) or any(c.coords == currentCart.coords for c in cartsBeforeMoving):
			crashes.append(currentCart)
			cartsAfterMoving = [c for c in cartsAfterMoving if c.coords != currentCart.coords]
			cartsBeforeMoving = [c for c in cartsBeforeMoving if c.coords != currentCart.coords]
			crashedCarts.append(currentCart)
			continue
		currentCart.MakeTurn(grid[newY][newX])
		cartsAfterMoving.append(currentCart)
	return crashes, cartsAfterMoving

with open('Input') as inFile:
	lines = inFile.read().splitlines()

grid = [[c for c in line] for line in lines]
carts = []

size = len(grid)
for y in range(size):
	for x in range(size):
		if grid[y][x] in '<>^v':
			carts.append(Cart((y,x), ToDirection(grid[y][x]), 0))
			grid[y][x] = '-' if grid[y][x] in '<>' else '|'

allClear = True
while True:
	crashes, carts = ProcessTick(grid, carts)

	if allClear and len(crashes) > 0:
		print('Part 1: ' + crashes[0].FormatCoords())
		allClear = False

	if (len(carts) == 1):
		print('Part 2: ' + carts[0].FormatCoords())
		exit()