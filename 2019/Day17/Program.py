from myIntcode import IntcodeProcessor
from collections import defaultdict, deque

screen = [""]

def processOutput(value):
	global screen

	if value == 10:
		screen.append("")
	else:
		screen[-1] += str(chr(value))

def sumIntersections():
	global screen

	total = 0
	for y in range(1, len(screen) - 3):
		for x in range(1, len(screen[y]) - 1):		
			if screen[y][x] == "#" and screen[y-1][x] == "#" and screen[y+1][x] == "#" and screen[y][x-1] == "#" and screen[y][x+1] == "#":
				total += x * y
	return total

instructions = [int(x) for x in open("Input").read().split(',')]

vm1 = IntcodeProcessor(instructions.copy(), 'vm1')
vm1.debug = False
vm1.output = processOutput
vm1.run()

# for row in screen:
# 	print(row)

print('Part 1:', sumIntersections())

instructions[0] = 2

screen = [""]

inputString = 'A,A,B,B,C,B,C,B,C,A\n'
inputString += 'L,10,L,10,R,6\n'
inputString += 'R,12,L,12,L,12\n'
inputString += 'L,6,L,10,R,12,R,12\n'
inputString += 'n\n'

Q = deque(ord(x) for x in inputString)
def localInput():
	return Q.popleft()

vm2 = IntcodeProcessor(instructions.copy(), 'vm2')
vm2.debug = False
vm2.output = processOutput
vm2.input = localInput
vm2.run()

# for row in screen:
# 	print(row)

print('Part 2:', vm2.lastOutput)