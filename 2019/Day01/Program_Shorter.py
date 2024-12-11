def calcFuel(weight): return weight // 3 - 2
def calcCompounding(weight): return weight // 3 - 2 + calcCompounding(weight // 3 - 2) if (weight // 3 - 2) > 0 else 0

with open('Input') as inFile:
	lines = inFile.readlines()

	print("Part 1:", sum(map(calcFuel, (int(line) for line in lines))))
	print("Part 2:", sum(map(calcCompounding, (int(line) for line in lines))))