numSeats = 3014603

seats = [x for x in range(1, numSeats + 1)]

while len(seats) > 1:
	if len(seats) & 1:
		seats = seats[2::2]
	else:
		seats = seats[::2]

print "Winning seat:", seats[0]