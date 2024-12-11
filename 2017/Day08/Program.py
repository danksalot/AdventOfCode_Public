maxValue = 0

with open('Input') as inFile:
	lines = [x.split() for x in inFile.readlines()]

registers = { line[0] : 0 for line in lines}

for line in lines:
	if eval(str(registers[line[4]]) + line[5] + line[6]):
		if line[1] == 'inc':
			registers[line[0]] += int(line[2])
		elif line[1] == 'dec':
			registers[line[0]] -= int(line[2])
		
		if (registers[line[0]] > maxValue):
			maxValue = registers[line[0]]

maxRegister = max(registers, key=registers.get)
print "Max register: {", maxRegister, ":", registers[maxRegister], "}"
print "Max value reached during the process:", maxValue