class Marble:
	def __init__(self, value):
		self.value = value
		self.next = self
		self.prev = self

def PlayMarble(currentMarble, nextMarble):
	if nextMarble.value % 23 == 0:
		removed = currentMarble.prev.prev.prev.prev.prev.prev.prev
		removed.prev.next = removed.next
		removed.next.prev = removed.prev
		return removed.next, removed.value + nextMarble.value
	else:
		oneAway = currentMarble.next
		twoAway = currentMarble.next.next
		nextMarble.next = twoAway
		nextMarble.prev = oneAway
		oneAway.next = nextMarble
		twoAway.prev = nextMarble
		return nextMarble, 0

def PlayGame(numPlayers, numMarbles):
	currentPlayer = 0
	nextMarble = 1
	scores = [0 for x in range(numPlayers)]
	currentMarble = Marble(0)

	while nextMarble != numMarbles:
		currentMarble, score = PlayMarble(currentMarble, Marble(nextMarble))
		scores[currentPlayer] += score
		currentPlayer = (currentPlayer + 1) % numPlayers
		nextMarble += 1

	return max(scores)

print('Part 1:', PlayGame(468, 71843))
print('Part 2:', PlayGame(468, 71843 * 100))