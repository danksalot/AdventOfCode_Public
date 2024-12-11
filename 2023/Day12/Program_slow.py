from more_itertools import distinct_permutations
import re
import functools

with open('Input') as inFile:
	lines = [x.strip() for x in inFile.readlines()]

def fitsCondition(springs, condition):
	brokenGroups = re.findall('(#+)', springs)
	return [len(x) for x in brokenGroups] == [int(x) for x in condition]

@functools.lru_cache(maxsize=None)
def getPerms(springs, condition):
	numUnknown = springs.count('?')
	numKnownBroken = springs.count('#')
	numBroken = sum(condition)
	numNeeded = numBroken - numKnownBroken
	permString = '#'*numNeeded + '.'*(numUnknown - numNeeded)
	perms = distinct_permutations(permString)
	return perms

total = 0
for line in lines:
	# print(line)
	parts = line.split(' ')
	springs = parts[0]
	condition = [int(x) for x in parts[1].split(',')]

	for perm in getPerms(springs, condition):
		temp = springs
		for char in perm:
			temp = temp.replace('?', char, 1)

		# print('Testing:', temp, 'against', condition)

		if fitsCondition(temp, condition):
			# print('Fits!')
			total += 1

print('Part 1:', total)

total = 0
for line in lines:
	parts = line.split(' ')
	springs = parts[0]
	springs = springs  + '?' + springs  + '?' + springs  + '?' + springs  + '?' + springs
	condition = [int(x) for x in parts[1].split(',')]
	condition = condition*5

	print('Testing perms of:', springs, 'against', condition)
	for perm in getPerms(springs, condition):
		temp = springs
		for char in perm:
			temp = temp.replace('?', char, 1)

		# print('Testing:', temp, 'against', condition)

		if fitsCondition(temp, condition):
			# print('Fits!')
			total += 1

print('Part 2:', total)
	