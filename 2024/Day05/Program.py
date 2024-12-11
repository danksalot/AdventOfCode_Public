
with open('Input') as inFile:
	lines = [line.rstrip('\n') for line in inFile.readlines()]

rules = [list(map(int, line.split('|'))) for line in lines if '|' in line]
updates = [list(map(int, line.split(','))) for line in lines if ',' in line]

def findBrokenRule(update):
	for i in range(len(update)):
		brokenRules = [r for r in rules if r[1] == update[i] and r[0] in update[i:]]
		if brokenRules:
			return brokenRules[0]
	return None

def fixUpdate(update):
	ruleBroken = findBrokenRule(update)
	while ruleBroken:
		a, b = update.index(ruleBroken[0]), update.index(ruleBroken[1])
		update[b], update[a] = update[a], update[b]
		ruleBroken = findBrokenRule(update)
	return update

print("Part 1:", sum(update[len(update)//2] for update in updates if findBrokenRule(update) is None))
print("Part 2:", sum(fixUpdate(update)[len(update)//2] for update in updates if findBrokenRule(update)))
