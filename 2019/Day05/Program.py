import IntcodeProcessor

with open('Input') as inFile:
	instructions = [int(x) for x in inFile.read().split(',')]

print("Part 1:")
IntcodeProcessor.setInput(1)
IntcodeProcessor.runProgram(instructions.copy())

print("\nPart 2:")
IntcodeProcessor.setInput(5)
IntcodeProcessor.runProgram(instructions.copy())
