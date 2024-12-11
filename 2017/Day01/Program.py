with open('Input') as inFile:
	inputString = inFile.read()

	stringLength = len(inputString)
	halfLength = int(stringLength / 2)
	
	#part1answer = 0
	#part2answer = 0

	# Part 1
	#for i in range(stringLength):
	#	if (inputString[i] == inputString[(i + 1) % (stringLength)]):
	#		part1answer += int(inputString[i])

	# Part 2
	#for i in range(stringLength):
	#	if (inputString[i] == inputString[(i + halfLength) % (stringLength)]):
	#		part2answer += int(inputString[i])

	# Shortened version of correct implementation above
	part1answer = sum(int(inputString[i]) if inputString[i] == inputString[(i + 1) % (stringLength)] else 0 for i in range(stringLength))
	part2answer = sum(int(inputString[i]) if inputString[i] == inputString[(i + halfLength) % (stringLength)] else 0 for i in range(stringLength))

print("Part 1:", part1answer)
print("Part 2:", part2answer)
