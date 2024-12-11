instructionSet = []
instructionPointer = 0
inputValue = 0

def getParameters(numParams):
	global instructionSet
	global instructionPointer

	index = -3
	opCodeValue = "0000" + str(instructionSet[instructionPointer])
	
	params = []
	for i in range(1, numParams + 1):
		mode = opCodeValue[index] if abs(index) <= len(opCodeValue) else 0
		index -= 1
		params.append(instructionSet[instructionSet[instructionPointer + i]] if mode == "0" else instructionSet[instructionPointer + i])
	
	return params

def setValue(index, value):
	global instructionSet
	instructionSet[index] = value

def add():
	global instructionSet
	global instructionPointer

	left, right = getParameters(2)
	resultIndex = instructionSet[instructionPointer + 3]
	instructionSet[resultIndex] = left + right
	instructionPointer += 4

def mult():
	global instructionSet
	global instructionPointer

	left, right = getParameters(2)
	resultIndex = instructionSet[instructionPointer + 3]
	instructionSet[resultIndex] = left * right
	instructionPointer += 4

def save():
	global instructionSet
	global instructionPointer

	resultIndex = instructionSet[instructionPointer + 1]
	instructionSet[resultIndex] = inputValue
	instructionPointer += 2

def out():
	global instructionSet
	global instructionPointer

	resultValue = getParameters(1)[0]
	print("Output:", resultValue)
	instructionPointer += 2

def jit():
	global instructionSet
	global instructionPointer

	left, target = getParameters(2)
	if left != 0:
		instructionPointer = target
	else:
		instructionPointer += 3

def jnt():
	global instructionSet
	global instructionPointer

	left, target = getParameters(2)
	if left == 0:
		instructionPointer = target
	else:
		instructionPointer += 3

def lt():
	global instructionSet
	global instructionPointer

	left, right = getParameters(2)
	resultIndex = instructionSet[instructionPointer + 3]
	instructionSet[resultIndex] = 1 if left < right else 0
	instructionPointer += 4

def eq():
	global instructionSet
	global instructionPointer

	left, right = getParameters(2)
	resultIndex = instructionSet[instructionPointer + 3]
	instructionSet[resultIndex] = 1 if left == right else 0
	instructionPointer += 4

def processInstruction():
	global instructionSet
	global instructionPointer

	switcher = {
		1: lambda: add(),
		2: lambda: mult(),
		3: lambda: save(),
		4: lambda: out(),
		5: lambda: jit(),
		6: lambda: jnt(),
		7: lambda: lt(),
		8: lambda: eq(),
		99: lambda: -1,
	}

	opCode = int(str(instructionSet[instructionPointer])[-2:])
	func = switcher.get(opCode, lambda: "nothing")
	return func()

def setInput(value):
	global inputValue
	inputValue = value

def runProgram(instructions):
	global instructionSet
	global instructionPointer

	instructionSet = instructions
	instructionPointer = 0

	keepGoing = 0
	while keepGoing != -1:
		keepGoing = processInstruction()
