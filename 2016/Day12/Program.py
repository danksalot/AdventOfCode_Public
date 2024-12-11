currentInstruction = 0
regs = {"a":0, "b":0, "c":0, "d":0}
# Part 2: regs = {"a":0, "b":0, "c":1, "d":0}

with open("Input") as inputFile:
	lines = inputFile.readlines()
    
while currentInstruction < len(lines):
	parts = lines[currentInstruction].split()
	if parts[0] == "cpy" and parts[1].isdigit():
		regs[parts[2]] = int(parts[1])
	elif parts[0] == "cpy":
		regs[parts[2]] = regs[parts[1]]
	elif parts[0] == "inc":
		regs[parts[1]] += 1
	elif parts[0] == "dec":
		regs[parts[1]] -= 1
	elif parts[0] == "jnz" and ((parts[1].isdigit() and parts[1] != "0") or regs[parts[1]] != 0):
		currentInstruction += int(parts[2])
		continue

	currentInstruction += 1

print regs