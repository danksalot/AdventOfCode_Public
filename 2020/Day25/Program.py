with open('Input') as inFile:
	lines = [int(x) for x in inFile.readlines()]

	for line in lines:
		print(line)