from math import gcd

X = 0
Y = 1
Z = 2
VelX = 3
VelY = 4
VelZ = 5

initialState = [
	[14, 4, 5, 0, 0, 0],
	[12, 10, 8, 0, 0, 0],
	[1, 7, -10, 0, 0, 0],
	[16, -5, 3, 0, 0, 0]
]

moons = initialState.copy()

def step(moons):
	newMoons = []
	for moon in moons:
		newMoon = moon.copy()
		newMoon[VelX] += sum([1 if moon[X] < m[X] else -1 if moon[X] > m[X] else 0 for m in moons])
		newMoon[VelY] += sum([1 if moon[Y] < m[Y] else -1 if moon[Y] > m[Y] else 0 for m in moons])
		newMoon[VelZ] += sum([1 if moon[Z] < m[Z] else -1 if moon[Z] > m[Z] else 0 for m in moons])
		newMoon[X] += newMoon[VelX]
		newMoon[Y] += newMoon[VelY]
		newMoon[Z] += newMoon[VelZ]
		newMoons.append(newMoon)
	return newMoons.copy()

for i in range(1000):
	moons = step(moons)

totalEnergy = 0
for moon in moons:
	potential = abs(moon[X]) + abs(moon[Y]) + abs(moon[Z])
	kinetic = abs(moon[VelX]) + abs(moon[VelY]) + abs(moon[VelZ])
	totalEnergy += potential * kinetic

print("Part 1:", totalEnergy)

moons = initialState.copy()

timeStep = 0
RepeatX = None
RepeatY = None
RepeatZ = None

while RepeatX == None or RepeatY == None or RepeatZ == None:
	moons = step(moons)
	timeStep += 1

	xkey = ''.join(str(m[VelX]) for m in moons)
	ykey = ''.join(str(m[VelY]) for m in moons)
	zkey = ''.join(str(m[VelZ]) for m in moons)

	if RepeatX == None and xkey == "0000":
		# print("X repeated at", timeStep)
		RepeatX = timeStep * 2
	if RepeatY == None and ykey == "0000":
		# print("Y repeated at", timeStep)
		RepeatY = timeStep * 2
	if RepeatZ == None and zkey == "0000":
		# print("Z repeated at", timeStep)
		RepeatZ = timeStep * 2

def leastCommonMultiple(a):
	lcm = a[0]
	for i in a[1:]:
		numerator = lcm * i
		denominator = gcd(int(lcm), i)
		lcm = numerator / denominator
	return int(lcm)

print("Part 2:", leastCommonMultiple([RepeatX, RepeatY, RepeatZ]))