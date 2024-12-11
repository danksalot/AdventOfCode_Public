from itertools import cycle

cups = [9, 1, 6, 4, 3, 8, 2, 7, 5]  # INPUT VALUES
# cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]  # TEST VALUES
positions = cycle(range(10))



def takeTurn():
	global cups
	cIdx = next(positions)
	print('Cups:', cups)

	# turnList = cups[cIdx:] + cups[0:cIdx]
	# print('TurnList:', turnList)

	current = cups[0]
	print('Current cup:', current)

	takenOut = [cups.pop(1), cups.pop(1), cups.pop(1)]
	print('Pick up:', takenOut)




	destination = current - 1
	if destination == 0: destination = 9
	while destination in takenOut:
		destination -= 1
		if destination == 0: destination = 9

	print('Destination:', destination)

	destinationIdx = cups.index(destination)

	# print('DestinationIdx',destinationIdx)

	cups.insert(destinationIdx + 1, takenOut[2])
	cups.insert(destinationIdx + 1, takenOut[1])
	cups.insert(destinationIdx + 1, takenOut[0])

	cups = cups[1:] + cups[:1]





for x in range(1, 101):
	print('\nTurn', x)
	takeTurn()


print(cups)


# 32849765