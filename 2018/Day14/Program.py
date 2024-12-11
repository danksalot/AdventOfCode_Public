numRecipies = '824501'

elves = [0, 1]

scores = '37'

while numRecipies not in scores[-7:]:
	scores += str(int(scores[elves[0]]) + int(scores[elves[1]]))
	elves[0] = (elves[0] + int(scores[elves[0]]) + 1) % len(scores)
	elves[1] = (elves[1] + int(scores[elves[1]]) + 1) % len(scores)

print('Part 1:', scores[int(numRecipies):int(numRecipies)+10])
print('Part 2:', scores.index(numRecipies))
