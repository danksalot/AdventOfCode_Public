deckCount = 50

def calculateScore(deck):
	total = 0
	for i, c in enumerate(deck[::-1]):
		total += (i+1) * int(c)
	return total

def playRoundRecursive(deckA, deckB):
	# print('Playing round:', deckA, deckB)
	rnd = {}
	player1Card = deckA.pop(0)
	player2Card = deckB.pop(0)
	roundWinner = None
	if (len(deckA) >= player1Card and len(deckB) >= player2Card):
		subDeckA = [x for x in deckA][:player1Card]
		subDeckB = [x for x in deckB][:player2Card]
		# print('Recursing:', player1Card, subDeckA, 'vs', player2Card, subDeckB)
		roundWinner, a, b = playGame(subDeckA, subDeckB)
	else:
		if player1Card > player2Card:
			roundWinner = 0
		else:
			roundWinner = 1

	if roundWinner == 0:
		deckA.append(player1Card)
		deckA.append(player2Card)
	else:
		deckB.append(player2Card)
		deckB.append(player1Card)
	return deckA, deckB

def checkForWinCondition(gamelog, deckA, deckB):
	roundKey = ''.join([str(x) for x in deckA] + ['|'] + [str(x) for x in deckB])
	if roundKey in gamelog:
		# print('Loop found!')
		return gamelog, 0
	else:
		gamelog.append(roundKey)
	if len(deckA) == 0:
		return gamelog, 1
	elif len(deckB) == 0:
		return gamelog, 0
	return gamelog, None

def playGame(deckA, deckB):
	gamelog = []
	gamelog, winner = checkForWinCondition(gamelog, deckA, deckB)
	while winner == None:
		deckA, deckB = playRoundRecursive(deckA, deckB)
		gamelog, winner = checkForWinCondition(gamelog, deckA, deckB)
	return winner, deckA, deckB

with open('Input') as inFile:
	inputPlayers = inFile.read().split("\n\n")

deckA = [int(x) for x in inputPlayers[0].split('\n')[1:]]
deckB = [int(x) for x in inputPlayers[1].split('\n')[1:]]

winner, deckA, deckB = playGame(deckA, deckB)
print('Part 2:', calculateScore(deckA if winner == 0 else deckB))