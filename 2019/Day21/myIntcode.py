from collections import defaultdict

class IntcodeProcessor:
	def __init__(self, instructions, label):
		self.label = label
		self.debug = False
		self.suppressOutput = True
		self.input = lambda: input(">> ")
		self.lastOutput = None
		self.instructionPointer = 0
		self.relativeBase = 0
		self.memory = defaultdict(int)
		for i, v in enumerate(instructions):
			self.memory[i] = v
		self.OPERATIONS = {
			1: self.add,
			2: self.mult,
			3: self.store,
			4: self.out,
			5: self.jit,
			6: self.jnt,
			7: self.lt,
			8: self.eq,
			9: self.setRel
		}

	def output(self, message):
		if not self.suppressOutput:
			print(message)

	def printDebug(self, message):
		if self.debug:
			print(message)

	def run(self):
		self.printDebug("Starting program")
		opCode = self.memory[self.instructionPointer] % 100
		while opCode != 99:
			self.processInstruction(opCode)
			opCode = self.memory[self.instructionPointer] % 100

	def processInstruction(self, opCode):
		self.printDebug(str(self.instructionPointer) + ": Running op: " + str(self.memory[self.instructionPointer]) + " - " + str(opCode))
		op = self.OPERATIONS[opCode]
		op()

	def getArgValues(self, numInputs, includeOutput):
		op = self.memory[self.instructionPointer]
		self.instructionPointer += 1
		argValues = []
		target = None
		
		# Get values for input args
		for i in range(numInputs):
			mode = (op // (10 ** (2 + i))) % 10
			if mode == 0:
				argValues.append(self.memory[self.memory[self.instructionPointer]])
			elif mode == 1:
				argValues.append(self.memory[self.instructionPointer])
			elif mode == 2:
				argValues.append(self.memory[self.memory[self.instructionPointer] + self.relativeBase])
			self.instructionPointer += 1
		
		# Get address for output arg
		if includeOutput:
			mode = (op // (10 ** (2 + numInputs))) % 10
			if mode == 0:
				target = self.memory[self.instructionPointer]
			elif mode == 2:
				target = self.memory[self.instructionPointer] + self.relativeBase
			self.instructionPointer += 1
		
		self.printDebug("Got arg values " + str(argValues) + " and target " + str(target))
		return argValues, target

	def add(self):
		args, target = self.getArgValues(2, True)
		self.printDebug("ADD: Adding: memory[" + str(target) + "] = " + str(args[0]) + " + " + str(args[1]))
		self.memory[target] = args[0] + args[1]

	def mult(self):
		args, target = self.getArgValues(2, True)
		self.printDebug("MULT: Multiplying: memory[" + str(target) + "] = " + str(args[0]) + " * " + str(args[1]))
		self.memory[target] = args[0] * args[1]

	def store(self):
		self.printDebug("STORE: Attempting to get arg values")
		args, target = self.getArgValues(0, True)
		value = self.input()
		self.printDebug("STORE: Saving " + str(value) + " to memory[" + str(target) + "]")
		self.memory[target] = int(value)

	def out(self):
		args, target = self.getArgValues(1, False)
		self.printDebug("OUT: Outputting value " + str(args[0]))
		self.lastOutput = args[0]
		self.output(args[0])

	def jit(self):
		args, target = self.getArgValues(2, False)
		self.printDebug("JIT: evaluating " + str(args[0]) + " and jumping to " + str(args[1]) + " : " + str(args[0] != 0))
		if args[0] != 0: self.instructionPointer = args[1]

	def jnt(self):
		args, target = self.getArgValues(2, False)
		self.printDebug("JNT: evaluating " + str(args[0]) + " and jumping to " + str(args[1]) + " : " + str(args[0] == 0))
		if args[0] == 0: self.instructionPointer = args[1]

	def lt(self):
		args, target = self.getArgValues(2, True)
		self.printDebug("LT: memory[" + str(target) + "] = " + str(args[0]) + " < " + str(args[1]))
		self.memory[target] = int(args[0] < args[1])

	def eq(self):
		args, target = self.getArgValues(2, True)
		self.printDebug("EQ: memory[" + str(target) + "] = " + str(args[0]) + " == " + str(args[1]))
		self.memory[target] = int(args[0] == args[1])

	def setRel(self):
		args, target = self.getArgValues(1, False)
		self.printDebug("SETREL: setting relativeBase to " + str(args[0]))
		self.relativeBase += args[0]