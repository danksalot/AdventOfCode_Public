class Instruction:
	def __init__(self, name, opCode, implementation):
		self.name = name
		self.opCode = opCode
		self.implementation = implementation

	def performAction(self, A, B, C):
		try:
			return self.implementation(A, B, C)
		except:
			return -1

def addr(A, B, C): registers[C] = registers[A] + registers[B]
def addi(A, B, C): registers[C] = registers[A] + B
def mulr(A, B, C): registers[C] = registers[A] * registers[B]
def muli(A, B, C): registers[C] = registers[A] * B
def banr(A, B, C): registers[C] = registers[A] & registers[B]
def bani(A, B, C): registers[C] = registers[A] & B
def borr(A, B, C): registers[C] = registers[A] | registers[B]
def bori(A, B, C): registers[C] = registers[A] | B
def setr(A, B, C): registers[C] = registers[A]
def seti(A, B, C): registers[C] = A
def gtir(A, B, C): registers[C] = 1 if A > registers[B] else 0
def gtri(A, B, C): registers[C] = 1 if registers[A] > B else 0
def gtrr(A, B, C): registers[C] = 1 if registers[A] > registers[B] else 0
def eqir(A, B, C): registers[C] = 1 if A == registers[B] else 0
def eqri(A, B, C): registers[C] = 1 if registers[A] == B else 0
def eqrr(A, B, C): registers[C] = 1 if registers[A] == registers[B] else 0

Instructions = [
	Instruction('addr', 10, addr),
	Instruction('addi',  6, addi),
	Instruction('mulr',  9, mulr),
	Instruction('muli',  0, muli),
	Instruction('banr', 14, banr),
	Instruction('bani',  2, bani),
	Instruction('borr', 11, borr),
	Instruction('bori', 12, bori),
	Instruction('setr', 15, setr),
	Instruction('seti',  1, seti),
	Instruction('gtir',  7, gtir),
	Instruction('gtri',  3, gtri),
	Instruction('gtrr',  4, gtrr),
	Instruction('eqir',  8, eqir),
	Instruction('eqri', 13, eqri),
	Instruction('eqrr',  5, eqrr)
]

with open('Input1') as inFile:
	lines = inFile.read().splitlines()

worksWithThreeOrMore = 0

for i in range(0, len(lines), 4):
	validInstructions = 0
	for instruction in Instructions:
		registers = [int(c) for c in lines[i][9:19].split(', ')]
		params = [int(c) for c in lines[i + 1].split()]
		instruction.performAction(params[1], params[2], params[3])
		validInstructions += registers == [int(c) for c in lines[i + 2][9:19].split(', ')]
	worksWithThreeOrMore += validInstructions >= 3

print('Part 1:', worksWithThreeOrMore)

with open('Input2') as inFile:
	lines = inFile.read().splitlines()

registers = [0, 0, 0, 0]

for line in lines:
	params = [int(c) for c in line.split()]
	instruction = next((i for i in Instructions if i.opCode == params[0]), None)
	instruction.performAction(params[1], params[2], params[3])

print('Part 2:', registers[0])

# Use the following, starting with empty lists on line 89 and 92, and adding the ones you're sure of to figure out the rest
#Omatches = defaultdict(set)
#Imatches = defaultdict(set)
#
#for i in range(0, len(lines), 4):
#	validInstructions = 0
#	lastValidInstruction = None
#	lastValidInstructionOpCode = -1
#	for instruction in [i for i in Instructions if i.name not in ['bori', 'seti', 'mulr', 'bani', 'gtri', 'gtrr', 'muli', 'eqir', 'addr', 'eqrr', 'eqri', 'gtir', 'addi', 'setr', 'banr']]:
#		registers = [int(c) for c in re.findall(r'-?\d+', lines[i])]
#		params = [int(c) for c in re.findall(r'-?\d+', lines[i + 1])]
#		if params[0] not in [0,1,2,3,4,5,6,7,8,9,10,12,13,14,15]:
#			instruction.performAction(params[1], params[2], params[3])
#			worked = registers == [int(c) for c in re.findall(r'-?\d+', lines[i + 2])]
#			if worked:
#				Omatches[params[0]].update([instruction.name])
#				Imatches[instruction.name].update([params[0]])
#				validInstructions += 1
#				lastValidInstruction = instruction
#				lastValidInstructionOpCode = params[0]
#
#	sum3orMore += validInstructions >= 3
#	if validInstructions == 1:
#		print(lastValidInstructionOpCode, lastValidInstruction.name)
#
#print(Omatches)
#print(Imatches)