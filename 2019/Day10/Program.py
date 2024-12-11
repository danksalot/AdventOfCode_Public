import math

asteroids = []
HEIGHT = 0
WIDTH = 0

def greatestCommonDenom(x, y):
	return y if x == 0 else greatestCommonDenom(y % x, x)

def getInViewCountByCoords(x, y):
	asteroid = next((a for a in asteroids if a.x == x and a.y == y), None)
	if asteroid:
		return len(asteroid.getInView())
	else:
		return 0

class Asteroid:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getInView(self):
		detected = set()
		for y in range(HEIGHT):
			for x in range(WIDTH):
				if lines[y][x] == '#' and (y != self.y or x != self.x):
					dy = y - self.y
					dx = x - self.x
					gcd = abs(greatestCommonDenom(dy, dx))
					detected.add((-dy // gcd, dx // gcd))
		return detected

with open('Input') as inFile:
	lines = inFile.readlines()
	HEIGHT = len(lines)
	WIDTH = len(lines[0].rstrip())

for y in range(len(lines[0].rstrip())):
	for x in range(len(lines)):
		if lines[y][x] == "#":
			asteroids.append(Asteroid(x, y))

station = None
stationInViewCount = 0
for asteroid in asteroids:
	count = len(asteroid.getInView())
	if count > stationInViewCount:
		station = asteroid
		stationInViewCount = count

print("Part 1:", stationInViewCount)

candidates = []
for (dy, dx) in station.getInView():
	key = math.atan2(dy, dx)
	if key > math.pi / 2.0:
		key -= 2 * math.pi
	candidates.append((key, (dy, dx)))
candidates = list(reversed(sorted(candidates)))

twoHundredth = candidates[199][1]
targetY = station.y - twoHundredth[0]
targetX = station.x + twoHundredth[1]

while lines[targetY][targetX] != '#':
	targetY -= twoHundredth[0]
	targetX += twoHundredth[1]

print("Part 2:", targetX * 100 + targetY)
