def evaluateRule(ruleId, value):
	rule = rules[ruleId]
	if rule.startswith('"'):
		if not value: return []
		return [value[1:]] if rule[1] == value[0] else []

	possibles = []
	for option in rule.split(' | '):
		newPossibles = [value]
		for rId in option.split(' '):
			newPossibles = [newPoss for currentPossibles in newPossibles for newPoss in evaluateRule(rId, currentPossibles)]
		possibles += newPossibles
	return possibles

with open('Input') as inFile:
	groups = inFile.read().split("\n\n")

rules = dict(map(lambda s : s.split(': '), groups[0].split('\n')))
messages = [x for x in groups[1].split('\n')]

print('Part 1:', sum([1 for message in messages if '' in evaluateRule('0', message)]))

rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

print('Part 2:', sum([1 for message in messages if '' in evaluateRule('0', message)]))


