from collections import Counter, defaultdict

with open('Input') as inFile:
	lines = inFile.read().splitlines()

pairs = defaultdict(int)
rules = {}
firstChar = lines[0][0]
lastChar = lines[0][-1]

for i in range(len(lines[0]) - 1):
	pairs[lines[0][i:i+2]] += 1

for line in lines[2:]:
	pair, new = line.split(' -> ')
	rules[pair] = new

def scoreAtStep(pairs, rules, step):
	for iteration in range(step):
		newPairs = defaultdict(int)
		for pair in pairs:
			if pair in rules:
				newPairs[pair[0] + rules[pair]] += pairs[pair]
				newPairs[rules[pair] + pair[1]] += pairs[pair]
			else:
				newPairs[pair] += pairs[pair]
		pairs = newPairs.copy()

		occurances = defaultdict(int)
		occurances[firstChar] += 1
		occurances[lastChar] += 1
		for pair in pairs:
			occurances[pair[0]] += pairs[pair]
			occurances[pair[1]] += pairs[pair]

	return int((max(occurances.values()) - min(occurances.values())) / 2)

print('Part 1:', scoreAtStep(pairs, rules, 10))
print('Part 2:', scoreAtStep(pairs, rules, 40))