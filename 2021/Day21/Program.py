from collections import defaultdict

positions = [7, 3]
scores = [0, 0]

previousDieRoll = 0
rollCount = 0

def roll(playerId):
	global rollCount, previousDieRoll
	moves = (previousDieRoll * 3) + 6
	previousDieRoll = previousDieRoll + 3
	rollCount += 3
	for i in range(moves):
		positions[playerId] += 1
		if positions[playerId] == 11:
			positions[playerId] = 1
	scores[playerId] += positions[playerId]

currentPlayerId = 0
while max(scores) < 1000:
	roll(currentPlayerId)
	currentPlayerId = (currentPlayerId + 1) % 2

print('Part 1:', min(scores) * rollCount)

positions = [7, 3]
scores = [0, 0]
currentPlayerId = 0

universes = defaultdict(int)
universes[tuple(positions), tuple(scores), currentPlayerId] = 1
wins = [0, 0]
while universes:
	positions, scores, currentPlayerId = min(universes.keys(), key=lambda x:x[1][0]+x[1][1])
	count = universes.pop((positions, scores, currentPlayerId))
	for i in range(1,4):
		for j in range(1,4):
			for k in range(1,4):
				tempPositions = [x for x in positions]
				tempPositions[currentPlayerId] = (tempPositions[currentPlayerId] + i + j + k - 1) % 10 + 1
				tempScores = [x for x in scores]
				tempScores[currentPlayerId] += tempPositions[currentPlayerId]
				if tempScores[currentPlayerId] >= 21:
					# print('Adding', count, 'wins for player', currentPlayerId)
					wins[currentPlayerId] += count
				else:
					# print('Adding', count, 'new universes with positions', tempPositions, 'scores', tempScores, 'and current player', currentPlayerId)
					universes[tuple(tempPositions), tuple(tempScores), 1-currentPlayerId] += count

print('Part 2:', max(wins))