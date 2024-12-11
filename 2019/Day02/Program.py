import IntcodeProcessor

with open('Input') as inFile:
	instructions = [int(x) for x in inFile.read().split(',')]

# Part 1
currentInstructionSet = instructions.copy()
currentInstructionSet[1] = 12
currentInstructionSet[2] = 2

IntcodeProcessor.runProgram(currentInstructionSet)
print("Part 1:", currentInstructionSet[0])

# Part 2
TARGET = 19690720

for i in range(100):
	for j in range(100):
		currentInstructionSet = instructions.copy()
		currentInstructionSet[1] = i
		currentInstructionSet[2] = j

		IntcodeProcessor.runProgram(currentInstructionSet)

		if (currentInstructionSet[0] == TARGET):
			print("Part 2:", i * 100 + j)
			exit()
