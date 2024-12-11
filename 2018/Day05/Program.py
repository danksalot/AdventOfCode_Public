import re

def triggerReactions(polymer):
	reactionHappened = False
	for i in range(len(polymer) - 1):
		if abs(ord(polymer[i]) - ord(polymer[i+1])) == abs(ord('a') - ord('A')):
		#if (polymer[i] != polymer[i+1]) and (polymer[i].lower() == polymer[i+1].lower()):
			reactionHappened = True
			polymer = polymer[:i] + polymer[i+2:]
			#print('removing character', i, 'of', len(polymer))
			break;
	return (reactionHappened, polymer)


with open('Input') as inFile:
	polymer = inFile.read()
	uniqueChars = set(polymer.lower())
	

part1Polymer = polymer
while True:
	(keepGoing, part1Polymer) = triggerReactions(part1Polymer)
	if not keepGoing:
		break;

shortestLength = len(polymer)

for char in uniqueChars:
	part2Polymer = ''.join([c for c in polymer if c.lower() != char])
	
	while True:
		(keepGoing, part2Polymer) = triggerReactions(part2Polymer)
		if not keepGoing:
			break;

	if len(part2Polymer) < shortestLength:
		shortestLength = len(part2Polymer)

	#print('Removing', char, 'resulted in length of', len(part2Polymer))

print('Part 1:', len(part1Polymer))
print('Part 2:', shortestLength)


