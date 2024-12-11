def toggle(line):
	parts = lines[currentInstruction].split()
	if parts[0] == "inc":
		parts[0] = "dec"
	if parts[0] == "dec":
		parts[0] = "inc"
	if parts[0] == "tgl":
		parts[0] = "inc"
	if parts[0] == "jnz":
		parts[0] = "cpy"
	if parts[0] == "cpy":
		parts[0] = "jnz"
	return ''.join(parts)

currentInstruction = 0
regs = {"a":7, "b":0, "c":0, "d":0}
# Part 2: regs = {"a":0, "b":0, "c":1, "d":0}

with open("Input") as inputFile:
	lines = inputFile.readlines()
    
while currentInstruction < len(lines):
	parts = lines[currentInstruction].split()
	print parts
	if parts[0] == "cpy" and parts[1].lstrip("-").isdigit():
		if not parts[2].isdigit():
			regs[parts[2]] = int(parts[1])
	elif parts[0] == "cpy":
		if not parts[2].isdigit():
			regs[parts[2]] = regs[parts[1]]
	elif parts[0] == "inc":
		regs[parts[1]] += 1
	elif parts[0] == "dec":
		regs[parts[1]] -= 1
	elif parts[0] == "jnz" and ((parts[1].isdigit() and parts[1] != "0") or regs[parts[1]] != 0):
		if parts[2].lstrip("-").isdigit():
			currentInstruction += int(parts[2])
		else:
			currentInstruction += regs[parts[2]]
		continue
	elif parts[0] == "tgl":
		instructionIndex = currentInstruction + regs[parts[1]]
		if instructionIndex in range(len(lines)):
			lines[instructionIndex] = toggle(lines[instructionIndex])

	currentInstruction += 1

print regs