import operator

deckCount = 50

def calculateScore(playerId):
	deck = players[playerId]
	total = 0
	for i, c in enumerate(deck[::-1]):
		total += (i+1) * int(c)
	return total

def playRound():
	rnd = {}
	for p in players:
		# print(p, 'has deck:', players[p])
		cardPlayed = players[p].pop(0)
		# print(p, 'plays:', cardPlayed)
		rnd[p] = cardPlayed
	winner = max(rnd.items(), key=operator.itemgetter(1))[0]
	# print(winner, 'wins the round!')
	players[winner].extend([x for x in sorted(rnd.values(), reverse=True)])

def checkForWinCondition(gameName):
	for p in players:
		if len(players[p]) == deckCount:
			# print(p, 'wins!')
			print(gameName, p, 'wins with score:', calculateScore(p))
			return True
	return False

with open('Input') as inFile:
	inputPlayers = inFile.read().split("\n\n")

players = {}
for p in inputPlayers:
	deck = p.split("\n")
	players[deck[0][:-1]] = [int(x) for x in deck[1:]]


while checkForWinCondition('Part 1:') == False:
	# print('Playing round')
	playRound()
	# print('After round Player 1:', len(players['Player 1']), 'cards, Player 2:', len(players['Player 2']), 'cards.')

# while checkForWinCondition('Part 2:') == False:
# 	playRoundRecursive()