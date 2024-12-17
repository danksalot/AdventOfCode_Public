
with open('Input') as inFile:
	lines = [line.rstrip() for line in inFile.readlines()]

registers = {}
instructions = []
pointer = 0
output = []

for line in lines:
    if 'A' in line: registers['A'] = int(line.split()[-1])
    if 'B' in line: registers['B'] = int(line.split()[-1])
    if 'C' in line: registers['C'] = int(line.split()[-1])
    if 'P' in line: instructions = [int(x) for x in line.split(': ')[-1].split(',')]

def getComboOperandValue(operand):
    if 0 <= operand <= 3: return operand
    elif operand == 4: return registers['A']
    elif operand == 5: return registers['B']
    elif operand == 6: return registers['C']
    else: print("Invalid operand value: ", operand)

def adv(operand): registers['A'] = int(registers['A'] / (2 ** getComboOperandValue(operand)))
def bxl(operand): registers['B'] = registers['B'] ^ operand
def bst(operand): registers['B'] = getComboOperandValue(operand) % 8
def jnz(operand): global pointer; pointer = operand - 2 if registers['A'] != 0 else pointer
def bxc(operand): registers['B'] = registers['B'] ^ registers['C']
def out(operand): output.append(getComboOperandValue(operand) % 8)
def bdv(operand): registers['B'] = int(registers['A'] / (2 ** getComboOperandValue(operand)))
def cdv(operand): registers['C'] = int(registers['A'] / (2 ** getComboOperandValue(operand)))

opCodes = {0:adv, 1:bxl, 2:bst, 3:jnz, 4:bxc, 5:out, 6:bdv, 7:cdv }

while pointer < len(instructions):
	instruction = instructions[pointer]
	operand = instructions[pointer + 1]
	opCodes[instruction](operand)
	pointer += 2

print('Part 1:', ','.join(map(str, output)))

for i in range(355435256317, 2251799800000001, 8589934592):
	output.clear()
	pointer = 0
	registers['A'] = i
	registers['B'] = 0
	registers['C'] = 0
	while pointer < len(instructions):
		instruction = instructions[pointer]
		operand = instructions[pointer + 1]
		opCodes[instruction](operand)
		pointer += 2

	if output == instructions:
		print("Part 2:", i)
		break

	# start at output[0:4] and keep adding items using the minimum and step size
	# You can find the minimum and step size between them using the output from this
	# if output[0:14] == instructions[0:14]:
	# 	print(i)
