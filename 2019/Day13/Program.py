from myIntcode import IntcodeProcessor
import sys
import os

outCount = 0
instructions = [int(x) for x in open("Input").read().split(',')]
X = None
Y = None
screen = []
tileId = { 0: ' ', 1: '|', 2: '#', 3: '-', 4: 'o'}
inputs = [0,0,0,0,0,0,0,0,1,1,1,1,1,1]
score = 0

clear = lambda: os.system('cls')

def preventOverflow(x, y):
	global screen
	x += 1
	y += 1

	if len(screen) < y:
		for i in range(y - len(screen)):
			screen.append([])

	for row in screen:
		if len(row) < x:
			# print("Increasing columns in row by", x - len(row))
			for i in range(x - len(row)):
				row.append(0)


def processOutput(value):
	global outCount, X, Y, screen, score
	# print("Processing output", value)

	if outCount == 0:
		X = value
	elif outCount == 1:
		Y = value
	elif outCount == 2:
		if X == -1 and Y == 0:
			score = value
			# print('\r\tScore:' + str(value), end='')
			# print("Score:", value)
			pass
		else:
			preventOverflow(X, Y)
			screen[Y][X] = value

	outCount = (outCount + 1) % 3

def localInput():
	global inputs, screen
	printScreen()

	ballIndex = None
	paddleIndex = None

	for row in screen:
		for i in range(len(row)):
			if row[i] == 4:
				ballIndex = i
			elif row[i] == 3:
				paddleIndex = i

	return 0 if paddleIndex == ballIndex else -1 if paddleIndex > ballIndex else 1

vm1 = IntcodeProcessor(instructions.copy(), 'vm1')
vm1.debug = False
vm1.output = processOutput
vm1.run()

def printScreen():
	# print(screen)
	clear()
	sys.stdout.write("\r" + '''
	{row0}
	{row1}
	{row2}
	{row3}
	{row4}
	{row5}
	{row6}
	{row7}
	{row8}
	{row9}
	{row10}
	{row11}
	{row12}
	{row13}
	{row14}
	{row15}
	{row16}
	{row17}
	{row18}
	{row19}
	{row20}
	{row21}
	{row22}
	Score: {playerScore}
	'''.format(
		row0 = ''.join([tileId[x] for x in screen[0]]),
		row1 = ''.join([tileId[x] for x in screen[1]]),
		row2 = ''.join([tileId[x] for x in screen[2]]),
		row3 = ''.join([tileId[x] for x in screen[3]]),
		row4 = ''.join([tileId[x] for x in screen[4]]),
		row5 = ''.join([tileId[x] for x in screen[5]]),
		row6 = ''.join([tileId[x] for x in screen[6]]),
		row7 = ''.join([tileId[x] for x in screen[7]]),
		row8 = ''.join([tileId[x] for x in screen[8]]),
		row9 = ''.join([tileId[x] for x in screen[9]]),
		row10 = ''.join([tileId[x] for x in screen[10]]),
		row11 = ''.join([tileId[x] for x in screen[11]]),
		row12 = ''.join([tileId[x] for x in screen[12]]),
		row13 = ''.join([tileId[x] for x in screen[13]]),
		row14 = ''.join([tileId[x] for x in screen[14]]),
		row15 = ''.join([tileId[x] for x in screen[15]]),
		row16 = ''.join([tileId[x] for x in screen[16]]),
		row17 = ''.join([tileId[x] for x in screen[17]]),
		row18 = ''.join([tileId[x] for x in screen[18]]),
		row19 = ''.join([tileId[x] for x in screen[19]]),
		row20 = ''.join([tileId[x] for x in screen[20]]),
		row21 = ''.join([tileId[x] for x in screen[21]]),
		row22 = ''.join([tileId[x] for x in screen[22]]),
		playerScore = score
		))
	sys.stdout.flush()

	

	# for row in screen:
	# 	# sys.stdout.write("\r" + ''.join([tileId[x] for x in row]))
	# 	# sys.stdout.flush()
	# 	# print(''.join([tileId[x] for x in row]))
	# 	print(len(screen))

print("Part 1:", sum(sum(1 if x == 2 else 0 for x in row) for row in screen))

instructions[0] = 2

vm2 = IntcodeProcessor(instructions.copy(), 'vm2')
vm2.debug = False
vm2.output = processOutput
vm2.input = localInput
vm2.run()

printScreen()