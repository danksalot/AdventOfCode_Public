from math import floor

openers = {
	'(':')', 
	'[':']', 
	'{':'}', 
	'<':'>'
}

closerValues = {')':1, ']':2, '}':3, '>':4}

corruptionFound = {')':0, ']':0, '}':0, '>':0}
incompleteLineScores = []

with open('Input') as inFile:
	lines = inFile.read().splitlines()

for line in lines:
	workingSet = []
	corrupt = False
	for char in line:
		if char in openers:
			workingSet.append(char)
			# print('Found opener:', char, 'WorkingSet:', workingSet)			
		else:
			matchingOpener = workingSet.pop()
			# print('Found closer:', char, 'matching with:', matchingOpener, 'WorkingSet:', workingSet)
			if openers[matchingOpener] != char:	
				# print('Found corruption!', char, 'did not match', matchingOpener)
				corruptionFound[char] += 1
				corrupt = True
				break
	if not corrupt:
		# print('Found incomplete line')
		score = 0
		while len(workingSet) > 0:
			unmatchedOpener = workingSet.pop()
			score *= 5
			score += closerValues[openers[unmatchedOpener]]
		incompleteLineScores.append(score)

total = corruptionFound[')'] * 3
total += corruptionFound[']'] * 57
total += corruptionFound['}'] * 1197
total += corruptionFound['>'] * 25137

print('Part 1:', total)
print('Part 2:', sorted(incompleteLineScores)[floor(len(incompleteLineScores)/2)])