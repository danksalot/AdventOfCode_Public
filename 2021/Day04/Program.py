import re

class Position():
	marked = False
	value = 0

	def __init__(self, value):
		self.value = value
		self.marked = False

	def mark(self):
		self.marked = True

class Board():
	rows = []

	def __init__(self, nums):
		self.rows = []
		boardNums = []
		for q in range(5):
			boardNums.append([int(x) for x in re.findall('\d+', nums[q])])
		for row in boardNums:
			self.rows.append([Position(x) for x in row])
		for column in zip(*boardNums):
			self.rows.append([Position(x) for x in list(column)])

	def printBoard(self):
		print('Printing Board...')
		for row in self.rows[:5]:
			print(' '.join([str(p.value) for p in row]))

	def findMinTurn(self, turns):
		wins = []
		for row in self.rows:
			maxIndex = 0
			lastNum = None		
			for num in row:
				index = turns.index(num.value)
				# print('found', num.value, 'at index', index)
				if index == None:
					continue
				elif index > maxIndex:
					maxIndex = index
					lastNum = turns[index]
			# print('Row', [x.value for x in row], 'won on turn', maxIndex, 'with the winning number', turns[maxIndex])
			wins.append(maxIndex)
		return min(wins)

	def calculateScore(self, turns, finalTurn):
		for turn in turns[0:finalTurn+1]:
			for row in self.rows:
				for position in row:
					if position.value == turn:
						position.marked = True

		unmarkedTotal = 0
		for row in self.rows[0:5]:
			for position in row:
				if position.marked == False:
					unmarkedTotal += position.value

		# print('calculating score', unmarkedTotal, '*', turns[finalTurn], "=", unmarkedTotal * turns[finalTurn])
		return unmarkedTotal * turns[finalTurn]

with open('Input') as inFile:
	lines = inFile.read().splitlines()

inputs = [int(x) for x in lines[0].split(',')]

boards = []

i = 2
while i < len(lines):
	boards.append(Board(lines[i:i+5]))
	i += 6

winningBoardIndex = 1000000
finalTurn = 1000000
for index, board in enumerate(boards):
	winningTurn = board.findMinTurn(inputs)
	if winningTurn is not None: 
		if winningTurn < finalTurn:
			finalTurn = winningTurn
			winningBoardIndex = index

print('Part 1:', boards[winningBoardIndex].calculateScore(inputs, finalTurn))

losingBoardIndex = 1000000
finalTurn = 0
for index, board in enumerate(boards):
	winningTurn = board.findMinTurn(inputs)
	if winningTurn is not None: 
		if winningTurn > finalTurn:
			finalTurn = winningTurn
			losingBoardIndex = index

print('Part 2:', boards[losingBoardIndex].calculateScore(inputs, finalTurn))