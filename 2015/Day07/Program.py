import BitwiseOps as bg

gates = []

with open("Input") as inputFile:
    lines = inputFile.readlines()
    
for line in lines:
	parts = line.split()
	if(len(parts) == 3): # ASSIGNMENT
		gates.append([bg.Assignment(parts[0]), parts[-1]])
	elif(len(parts) == 4): # NOT
		gates.append([bg.NotGate(parts[1]), parts[-1]])
	elif(parts[1] == 'AND'): # AND
		gates.append([bg.AndGate(parts[0], parts[2]), parts[-1]])
	elif(parts[1] == 'OR'): # OR
		gates.append([bg.OrGate(parts[0], parts[2]), parts[-1]])
	elif(parts[1] == 'RSHIFT'): # RSHIFT
		gates.append([bg.RShift(parts[0], parts[2]), parts[-1]])
	elif(parts[1] == 'LSHIFT'): # LSHIFT
		gates.append([bg.LShift(parts[0], parts[2]), parts[-1]])

while len(gates) > 0:
	for g in gates:
		result = g[0].result();
		if (result != None):
			bg.Resolve(result, g[1])
			gates.remove(g)

part1Answer = bg.wires['a']
print('Part 1: ', part1Answer)

bg.Reset()

bg.Resolve(part1Answer, 'b')

for line in lines:
	parts = line.split()
	
	if(len(parts) == 3 and parts[-1] != 'b'): # ASSIGNMENT
		gates.append([bg.Assignment(parts[0]), parts[-1]])
	elif(len(parts) == 4): # NOT
		gates.append([bg.NotGate(parts[1]), parts[-1]])
	elif(parts[1] == 'AND'): # AND
		gates.append([bg.AndGate(parts[0], parts[2]), parts[-1]])
	elif(parts[1] == 'OR'): # OR
		gates.append([bg.OrGate(parts[0], parts[2]), parts[-1]])
	elif(parts[1] == 'RSHIFT'): # RSHIFT
		gates.append([bg.RShift(parts[0], parts[2]), parts[-1]])
	elif(parts[1] == 'LSHIFT'): # LSHIFT
		gates.append([bg.LShift(parts[0], parts[2]), parts[-1]])

while len(gates) > 0:
	for g in gates:
		result = g[0].result();
		if (result != None):
			bg.Resolve(result, g[1])
			gates.remove(g)

part2Answer = bg.wires['a']
print('Part 2: ', part2Answer)
