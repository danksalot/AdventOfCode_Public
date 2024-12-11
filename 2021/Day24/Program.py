
maxInput = 29989297949519
minInput = 19518121316118

# registers = { 'w':0, 'x':0, 'y':0, 'z':0 }

# def provideInput():
# 	i = 0
# 	inputString = str(currentNum)
# 	while i < len(inputString):
# 		yield int(inputString[i])
# 		i += 1

# def value(v):
# 	try:
# 		return int(v)
# 	except:
# 		return registers[v]

# def operation(opCode, a, b):
# 	global registers
# 	if opCode == 'inp':
# 		registers[a] = next(b)
# 	elif opCode == 'add':
# 		registers[a] = value(a) + value(b)
# 	elif opCode == 'mul':
# 		registers[a] = value(a) * value(b)
# 	elif opCode == 'div':
# 		registers[a] = value(a) // value(b)
# 	elif opCode == 'mod':
# 		registers[a] = value(a) % value(b)
# 	elif opCode == 'eql':
# 		registers[a] = int(value(a) == value(b))

# instructions = []

# with open('Input') as inFile:
# 	lines = inFile.read().splitlines()

# for line in lines:
# 	instructions.append(line.split(' '))

# inp = provideInput()
for i in range(maxInput, 0, -1):
	# print('Testing number', i)
	digits = [int(x) for x in str(i)]
	if (digits[0] + 7) != digits[13]: continue
	if (digits[1] - 8) != digits[12]: continue
	if (digits[2] - 4) != digits[11]: continue
	if (digits[3] + 1) != digits[6]: continue
	if (digits[4] - 7) != digits[5]: continue
	if (digits[7] + 2) != digits[8]: continue
	if (digits[9] + 5) != digits[10]: continue
	print('Part 1:', i)
	break

for i in range(minInput, maxInput + 1):
	# print('Testing number', i)
	digits = [int(x) for x in str(i)]
	if (digits[0] + 7) != digits[13]: continue
	if (digits[1] - 8) != digits[12]: continue
	if (digits[2] - 4) != digits[11]: continue
	if (digits[3] + 1) != digits[6]: continue
	if (digits[4] - 7) != digits[5]: continue
	if (digits[7] + 2) != digits[8]: continue
	if (digits[9] + 5) != digits[10]: continue
	print('Part 2:', i)
	break



	# if str(i).count('0') > 0:
	# 	# print('Skipping number', i)
	# 	continue

	# currentNum = i
	# if currentNum % 999 == 0:
	# 	print('Testing number', currentNum)
	# inp = provideInput()
	# for instruction in instructions:		
	# 	third = inp if len(instruction) < 3 else instruction[2]
	# 	operation(instruction[0], instruction[1], third)
	# if registers['z'] == 0:
	# 	print('Found a valid model number:', currentNum)
	# 	break



