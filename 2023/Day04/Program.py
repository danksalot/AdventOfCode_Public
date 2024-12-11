import re

with open('Input') as inFile:
	lines = inFile.readlines()

def getNumWinners(winString, haveString):
	winners = re.findall(r'\d+', winString)
	have = re.findall(r'\d+', haveString)
	return len([h for h in have if h in winners])

total = 0
for line in lines:
	parts = line.split(':')[1].split('|')
	numWinners = getNumWinners(parts[0], parts[1])

	if numWinners > 0:
		total += 2 ** (numWinners - 1)

print('Part 1:', total)

numCards = [1] * len(lines)
for i, line in enumerate(lines):
	parts = line.split(':')[1].split('|')
	numWinners = getNumWinners(parts[0], parts[1])
	for x in range(1, numWinners + 1):
		numCards[i + x] += numCards[i]

print('Part 2:', sum(numCards))