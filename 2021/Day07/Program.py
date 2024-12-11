from math import floor

with open('Input') as inFile:
	crabs = [int(x) for x in inFile.read().split(',')]

minPosition = min(crabs)
maxPosition = max(crabs)
minFuelSpent = 10000000

for pos in range(minPosition, maxPosition):
	fuelSpent = 0
	for crab in crabs:
		fuelSpent += abs(pos - crab)
	if fuelSpent < minFuelSpent:
		minFuelSpent = fuelSpent

print('Part 1:', minFuelSpent)

minPosition = min(crabs)
maxPosition = max(crabs)
minFuelSpent = 1000000000000

for pos in range(minPosition, maxPosition):
	fuelSpent = 0
	for crab in crabs:
		distance = abs(pos - crab)
		fuelSpent += floor(((distance ** 2) + distance) / 2)
	if fuelSpent < minFuelSpent:
		minFuelSpent = fuelSpent

print('Part 2:', minFuelSpent)