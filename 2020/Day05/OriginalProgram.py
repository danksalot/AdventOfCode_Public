def findRow(boardingPass):
	lower, upper = 0, 127
	for direction in boardingPass[:7]:
		midpoint = lower + ((upper - lower) // 2)
		lower = midpoint + 1 if direction == 'B' else lower
		upper = upper if direction == 'B' else midpoint
	return lower

def findColumn(boardingPass):
	lower, upper = 0, 7
	for direction in boardingPass[7:]:
		midpoint = lower + ((upper - lower) // 2)
		lower = midpoint + 1 if direction == 'R' else lower
		upper = upper if direction == 'R' else midpoint
	return lower

with open('Input') as inFile:
	boardingPasses = inFile.read().splitlines()

seatIds = []

for boardingPass in boardingPasses:
	row = findRow(boardingPass)
	column = findColumn(boardingPass)
	seatId = (row * 8) + column
	seatIds.append(seatId)

print('Part 1:', max(seatIds))
print('Part 2:', sum(range(min(seatIds), max(seatIds) + 1)) - sum(seatIds))
