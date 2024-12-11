from collections import defaultdict

with open('Input') as inFile:
	groups = []
	for line in inFile.read().split('\n\n'):
		tempGroup = defaultdict(int)
		forms = line.split('\n')
		for form in forms:
			tempGroup['count'] += 1
			for question in form:
				tempGroup[question] += 1
		groups.append(tempGroup)

print('Part 1:', sum([len(set([key for key in group if key != 'count'])) for group in groups]))
print('Part 2:', sum([sum([1 for key in group if group[key] == group['count'] and key != 'count']) for group in groups]))
