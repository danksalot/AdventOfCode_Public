def PlayGame(numPlayers, lastMarble):
	currentPlayer = 0
	nextMarble = 1
	currentMarbleIndex = 0
	board = [0]
	scores = [0 for x in range(numPlayers)]

	while nextMarble <= lastMarble:
		if nextMarble % 23 == 0:
			scores[currentPlayer] += nextMarble
			currentMarbleIndex = (currentMarbleIndex + len(board) - 7) % len(board)
			otherMarbleScore = board.pop(currentMarbleIndex)
			scores[currentPlayer] += otherMarbleScore
		else:
			if currentMarbleIndex == len(board) - 1:
				currentMarbleIndex = 1
			else:
				currentMarbleIndex += 2
			board.insert(currentMarbleIndex, nextMarble)
		nextMarble += 1
		currentPlayer = (currentPlayer + 1) % numPlayers
	return max(scores)

print('Part 1:', PlayGame(468, 71843))
print('Part 2:', PlayGame(468, 71843 * 100))