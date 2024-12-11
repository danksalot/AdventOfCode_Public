with open('Input') as inFile:
	lines = inFile.read().splitlines()

memory = {}
mask = 'X' * 36
for line in lines:
	parts = line.split()
	if parts[0] == 'mask':
		mask = parts[2]
	elif parts[0].startswith('mem'):
		address = parts[0][4:-1]
		value = format(int(parts[2]), '#038b').replace('0b', '')
		value = ''.join(list(map(lambda xy: xy[0] if xy[0] != 'X' else xy[1], zip(mask, value))))
		memory[address] = value

total = sum([int(memory[key], 2) for key in memory])
print('Part 1:', total)



def addFloats(value):
	result = [value]
	for f in floats:
		new = []
		for i in range(len(result)):
			current = list(result[i])
			temp = list(result[i])
			current[f] = '0'
			temp[f] = '1'
			new.append(''.join(current))
			new.append(''.join(temp))
		result = new
	return result

memory = {}
mask = '0' * 36
floats = []
for line in lines:
	parts = line.split()
	if parts[0] == 'mask':
		mask = parts[2]
		floats = []
		for i, x in enumerate(mask):
			if x == 'X':
				floats.append(i)
	elif parts[0].startswith('mem'):
		value = parts[2]
		address = format(int(parts[0][4:-1]), '#038b').replace('0b', '')
		address = ''.join(list(map(lambda xy: '1' if xy[0] == '1' else xy[1], zip(mask, address))))
		addresses = addFloats(address)
		for a in list(addresses):
			memory[a] = value

total = sum([int(memory[key]) for key in memory])
print('Part 2:', total)
