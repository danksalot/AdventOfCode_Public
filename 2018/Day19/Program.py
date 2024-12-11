import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

class Instruction:
	def __init__(self, name, opCode, implementation):
		self.name = name
		self.opCode = opCode
		self.implementation = implementation

	def performAction(self, registers, A, B, C):
		try:
			return self.implementation(registers, A, B, C)
		except:
			return -1

def addr(registers, A, B, C): registers[C] = registers[A] + registers[B]
def addi(registers, A, B, C): registers[C] = registers[A] + B
def mulr(registers, A, B, C): registers[C] = registers[A] * registers[B]
def muli(registers, A, B, C): registers[C] = registers[A] * B
def banr(registers, A, B, C): registers[C] = registers[A] & registers[B]
def bani(registers, A, B, C): registers[C] = registers[A] & B
def borr(registers, A, B, C): registers[C] = registers[A] | registers[B]
def bori(registers, A, B, C): registers[C] = registers[A] | B
def setr(registers, A, B, C): registers[C] = registers[A]
def seti(registers, A, B, C): registers[C] = A
def gtir(registers, A, B, C): registers[C] = 1 if A > registers[B] else 0
def gtri(registers, A, B, C): registers[C] = 1 if registers[A] > B else 0
def gtrr(registers, A, B, C): registers[C] = 1 if registers[A] > registers[B] else 0
def eqir(registers, A, B, C): registers[C] = 1 if A == registers[B] else 0
def eqri(registers, A, B, C): registers[C] = 1 if registers[A] == B else 0
def eqrr(registers, A, B, C): registers[C] = 1 if registers[A] == registers[B] else 0

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

registers = [0, 0, 0, 0, 0, 0]
ipReg = -1
ip = 0

with open('Input') as inFile:
	lines = inFile.read().splitlines()

params = lines.pop(0).split()
ipReg = int(params[1])

while True:
	if not 0 <= ip < len(lines):
		print('Part 1:', registers[0])
		print('Part 2:', int(sum(divisorGenerator(10551267))))
		exit()
	registers[ipReg] = ip
	params = lines[ip].split()
	instruction = next((i for i in Instructions if i.name == params[0]), None)
	instruction.performAction(registers, int(params[1]), int(params[2]), int(params[3]))

	ip = registers[ipReg]
	ip += 1

# After solving part 2, part 1 can be simplified:		
#print('Part 1:', int(sum(divisorGenerator(867))))
#print('Part 2:', int(sum(divisorGenerator(10551267))))