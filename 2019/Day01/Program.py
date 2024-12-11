with open('Input') as inFile:
	lines = inFile.readlines()

	# Part 1
	sum = 0
	for line in lines:
		temp = int(line) / 3
		sum += int(temp) - 2
	print("Part 1:", sum)

	# Part 2
	sum = 0
	for line in lines:
		temp = int(line) / 3
		fuel = int(temp) - 2

		while (fuel > 0):
			sum += fuel
			temp = int(fuel) / 3
			fuel = int(temp) - 2

	print("Part 2:", sum)