from itertools import combinations

numLines = 0
part1Violations = 0
part2Violations = 0

with open('Input') as inFile:
	for line in inFile:
		numLines += 1
		line = line.rstrip()
		words = line.split(' ')

		# Part 1
		for word in words:
			if line.count(word) > 1:
				part1Violations += 1
				break

		# Part 2
		combos = combinations(words, 2)
		for combo in combos:
			if (sorted(combo[0]) == sorted(combo[1])):
				part2Violations += 1
				break

print "Part 1:", numLines - part1Violations
print "Part 2:", numLines - part2Violations