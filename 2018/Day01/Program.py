total = 0
values = []

with open('Input') as inFile:
	lines = inFile.readlines()
	print('Part 1:', sum(int(line) for line in lines))

	while True:
		for line in lines:
			total += int(line)
			if (total in values):
				print('Part 2:', total)
				exit()
			else:
				values.append(total)
