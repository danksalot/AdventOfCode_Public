with open('Input') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

knownArrangements = {}
def getNumArrangements(springs, condition):
	if len(condition) == 0:
		# We've reached the end of the condition, so count 1 if we've found all the broken springs
		return springs.count('#') == 0
	
	if (springs, tuple(condition)) in knownArrangements:
		return knownArrangements[(springs, tuple(condition))]

	spaceNeededAfterCurrentGroup = sum(condition[1:]) + (len(condition) - 1)
	currentGroupLength = condition[0]
	maxWorking = len(springs) - spaceNeededAfterCurrentGroup - currentGroupLength
	
	numArrangements = 0
	for numWorking in range(maxWorking + 1):
		temp = '.' * numWorking + '#' * currentGroupLength + '.'
		matchesPattern = True
		for i in range(min(len(temp), len(springs))):
			if temp[i] != springs[i] and springs[i] != '?':
				matchesPattern = False
		if matchesPattern:
			numArrangements += getNumArrangements(springs[len(temp):], condition[1:])

	knownArrangements[(springs, tuple(condition))] = numArrangements
	return numArrangements

total = 0
for line in lines:
	parts = line.split(' ')
	springs = parts[0]
	condition = [int(x) for x in parts[1].split(',')]

	total += getNumArrangements(springs, condition)

print('Part 1:', total)

total = 0
for line in lines:
	parts = line.split(' ')
	springs = parts[0]
	springs = springs  + '?' + springs  + '?' + springs  + '?' + springs  + '?' + springs
	condition = [int(x) for x in parts[1].split(',')]
	condition = condition*5

	total += getNumArrangements(springs, condition)

print('Part 2:', total)
	