import re
from z3 import If, Int, Optimize

bots = []
ranges = {}

class Bot:
	def __init__(self, x, y, z, r):
		self.Coords = (x, y, z)
		self.Radius = r

	def distanceFrom(self, coords):
		x1, y1, z1 = coords
		x2, y2, z2 = self.Coords
		return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

	def canReachPoint(self, x, y, z):
		return self.distanceFrom((x, y, z)) <= self.Radius

with open('Input') as inFile:
	lines = inFile.read().splitlines()

for (x, y, z, r) in map(lambda s: map(int, re.findall(r'-?\d+', s)), lines):
	bots.append(Bot(x, y, z, r))

maxBot = max(bots, key=lambda b:b.Radius)
inRange = sum(b.distanceFrom(maxBot.Coords) <= maxBot.Radius for b in bots)

print('Part 1:', inRange)

def abs(x):
  return If(x >= 0, x, -x)

def manhattan3d(start, finish):
	sX, sY, sZ = start
	fX, fY, fZ = finish
	return abs(sX - fX) + abs(sY - fY) + abs(sZ - fZ)

x = Int('x')
y = Int('y')
z = Int('z')
counts = [Int('count_' + str(i)) for i in range(len(bots))]
numInRange = Int('num')
distanceFromOrigin = Int('dist')

o = Optimize()
o.add([counts[i] == bots[i].canReachPoint(x, y, z) for i in range(len(bots))])
o.add(numInRange == sum(counts))
o.add(distanceFromOrigin == abs(x) + abs(y) + abs(z))
o.maximize(numInRange)
heuristic = o.minimize(distanceFromOrigin)

o.check()
print("Part 2:", o.lower(heuristic))
