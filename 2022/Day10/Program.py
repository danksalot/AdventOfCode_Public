with open('Input') as inFile:
	lines = inFile.read().splitlines()

def clockTick():
	global signalSum, instr
	instr += 1
	if instr in [20, 60, 100, 140, 180, 220]:
		signalSum += (instr * x)
	if instr in [1, 41, 81, 121, 161, 201]:
		display.append([])
	if x >= ((instr-1)%40) - 1 and x <= ((instr-1)%40) + 1:
		display[-1].append('#')
	else:
		display[-1].append('.')

instr = 0
x = 1
signalSum = 0
display = []

for line in lines:
	parts = line.split(' ')
	if parts[0] == 'noop':
		clockTick()
	else:
		clockTick()
		clockTick()
		x += int(parts[1])

print('Part 1:', signalSum)

print('Part 2:')
for row in display:
	print(''.join(row))