def getInitialStacks():
	return [
		[],
		['Z','P','M','H','R'],
		['P','C','J','B'],
		['S','N','H','G','L','C','D'],
		['F','T','M','D','Q','S','R','L'],
		['F','S','P','Q','B','T','Z','M'],
		['T','F','S','Z','B','G'],
		['N','R','V'],
		['P','G','L','T','D','V','C','M'],
		['W','Q','N','J','F','M','L']
	]

def moveItems(origin, target, count):
	for i in range(count):
		item = stacks[origin].pop()
		stacks[target].append(item)

def moveItemsV2(origin, target, count):
	items = []
	for i in range(count):
		items.append(stacks[origin].pop())
	stacks[target].extend(items[::-1])

with open('Input') as inFile:
	lines = inFile.read().splitlines()

stacks = getInitialStacks()
for line in lines:
	parts = line.split(' ')
	moveItems(int(parts[3]), int(parts[5]), int(parts[1]))

print('Part 1:', ''.join([stack[-1] for stack in stacks[1:]]))

stacks = getInitialStacks()
for line in lines:
	parts = line.split(' ')
	moveItemsV2(int(parts[3]), int(parts[5]), int(parts[1]))

print('Part 2:', ''.join([stack[-1] for stack in stacks[1:]]))