def add(position, instructionSet): 
	left = instructionSet[position + 1]
	right = instructionSet[position + 2]
	result = instructionSet[position + 3]
	instructionSet[result] = instructionSet[left] + instructionSet[right]
	return 4

def mult(position, instructionSet):
	left = instructionSet[position + 1]
	right = instructionSet[position + 2]
	result = instructionSet[position + 3]
	instructionSet[result] = instructionSet[left] * instructionSet[right]
	return 4

def processInstruction(position, instructionSet):
	switcher = {
		1: lambda: add(position, instructionSet),
		2: lambda: mult(position, instructionSet),
		99: lambda: -1,
	}
	func = switcher.get(instructionSet[position], lambda: "nothing")
	return func()

def runProgram(instructionSet):
	instructionPointer = 0
	step = 0

	while (step != -1):
		instructionPointer += step
		step = processInstruction(instructionPointer, instructionSet)