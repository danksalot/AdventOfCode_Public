def calculateSeatId(boardingPass):
	return int(boardingPass.translate(str.maketrans("FBLR", "0101")), 2)

with open('Input') as inFile:
	seatIds = list(map(calculateSeatId, inFile.read().splitlines()))
	
print('Part 1:', max(seatIds))
print('Part 2:', sum(range(min(seatIds), max(seatIds) + 1)) - sum(seatIds))