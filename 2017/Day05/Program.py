currentPosition = 0
steps = 0

with open('Input') as inFile:
	instructions = [int(i) for i in inFile]

while currentPosition < len(instructions):
	steps += 1
	newPosition = currentPosition + instructions[currentPosition]

	# Part 1
	# instructions[currentPosition] += 1

	# Part 2
	if (instructions[currentPosition] >= 3):
		instructions[currentPosition] -= 1
	else:
		instructions[currentPosition] += 1

	currentPosition = newPosition

print steps

