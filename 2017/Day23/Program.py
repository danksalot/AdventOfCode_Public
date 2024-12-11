with open('Input') as inFile:
	instructions = map(str.rstrip, inFile.readlines())

def runProgram():
	regs = { 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0 }

	def getValue(v):
		try:
			return int(v)
		except ValueError:
			return regs[v]

	current = 0
	multiplyCount = 0

	while 0 <= current < len(instructions) - 1:
		parts = instructions[current].split()
		if parts[0] == 'set':
			regs[parts[1]] = getValue(parts[2])
		elif parts[0] == 'sub':
			regs[parts[1]] -= getValue(parts[2])
		elif parts[0] == 'mul':
			multiplyCount += 1
			regs[parts[1]] *= getValue(parts[2])
		elif parts[0] == 'jnz':
			if getValue(parts[1]) != 0:
				current += getValue(parts[2])
				continue
		current += 1

	return multiplyCount

print 'Part1:', runProgram()

h = 0
for x in range(109900, 126901, 17):
    for i in range(2, x):
        if x % i == 0:
            h += 1
            break

print 'Part2:', h