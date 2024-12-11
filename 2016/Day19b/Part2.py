def getElimenatedIndex(currentIndex):
	print seats[currentIndex], "takes out", seats[(currentIndex + len(seats) / 2) % len(seats)]
	return (currentIndex + len(seats) / 2) % len(seats)

numSeats = 6

seats = [x for x in range(1, numSeats+1)]

while len(seats) > 1:
	print len(seats), "seats left"
	for idx, out in enumerate(seats):
		del seats[getElimenatedIndex(idx)]

print seats