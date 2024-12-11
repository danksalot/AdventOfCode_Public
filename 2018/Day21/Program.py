FUNCTIONS = {
    "addr": lambda reg, a, b: reg[a] + reg[b],
    "addi": lambda reg, a, b: reg[a] + b,
    "mulr": lambda reg, a, b: reg[a] * reg[b],
    "muli": lambda reg, a, b: reg[a] * b,
    "banr": lambda reg, a, b: reg[a] & reg[b],
    "bani": lambda reg, a, b: reg[a] & b,
    "borr": lambda reg, a, b: reg[a] | reg[b],
    "bori": lambda reg, a, b: reg[a] | b,
    "setr": lambda reg, a, b: reg[a],
    "seti": lambda reg, a, b: a,
    "gtir": lambda reg, a, b: 1 if a > reg[b] else 0,
    "gtri": lambda reg, a, b: 1 if reg[a] > b else 0,
    "gtrr": lambda reg, a, b: 1 if reg[a] > reg[b] else 0,
    "eqir": lambda reg, a, b: 1 if a == reg[b] else 0,
    "eqri": lambda reg, a, b: 1 if reg[a] == b else 0,
    "eqrr": lambda reg, a, b: 1 if reg[a] == reg[b] else 0,
}

registers = [0, 0, 0, 0, 0, 0]
ipReg = -1
ip = 0
last = None
found = set()
program = []

with open('Input') as inFile:
	lines = inFile.read().splitlines()

params = lines.pop(0).split()
ipReg = int(params[1])

for line in lines:
	opCode, a, b, c = line.strip().split(" ")
	program.append((opCode, int(a), int(b), int(c)))

while 0 <= ip < len(program):
	if ip == 28:
		if last is None:
			print("Part 1:", registers[3])

		if registers[3] in found:
			print("Part 2:", last)
			exit()

		last = registers[3]
		found.add(last)

	opCode, a, b, c = program[ip]
	registers[ipReg] = ip
	registers[c] = FUNCTIONS[opCode](registers, a, b)
	ip = registers[ipReg] + 1
