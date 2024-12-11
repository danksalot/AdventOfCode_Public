from myIntcode import IntcodeProcessor

SIZE = 50
screen = []

def printScreen():
	global screen
	for row in screen:
		print(''.join(row))

def checkCoords(X, Y):
	firstTime = True
	def fnInput():
		nonlocal firstTime
		returnValue = X if firstTime else Y
		firstTime = False
		return returnValue

	vm1 = IntcodeProcessor(instructions.copy(), 'vm1')
	vm1.debug = False
	vm1.input = fnInput
	vm1.run()
	return '.' if vm1.lastOutput == 0 else '#'

instructions = [int(x) for x in open("Input").read().split(',')]

for y in range(SIZE):
	screen.append([])
	for x in range(SIZE):
		screen[-1].append(checkCoords(x, y))

# printScreen()
total = sum([i.count('#') for i in screen])
print("Part 1:", total)

screen = []
X = 0
for Y in range(99, 100000000):
	while checkCoords(X, Y) == ".":
		X += 1

	result = checkCoords(X+99, Y-99)
	if result == "#":
		print("Part 2:", X * 10000 + Y-99)
		break
