import re
from copy import deepcopy
from functools import reduce
import operator

with open('Input') as inFile:
	lines = inFile.read().split('\n\n')

class Part:
	x, m, a, s = 0, 0, 0, 0
	def __init__(self, x=0, m=0, a=0, s=0):
		self.x = int(x)
		self.m = int(m)
		self.a = int(a)
		self.s = int(s)

	def print(self):
		print('x:', self.x, 'm:', self.m, 'a:', self.a, 's:', self.s)

class Condition:
	test = None
	testCategory = None
	testOp = None
	testValue = None
	destination = None

	def __init__(self, conditionString):
		parts = conditionString.split(':')
		if len(parts) == 1:
			self.destination = conditionString
		else:
			self.test, self.destination = conditionString.split(':')
			self.testCategory = self.test[0]
			self.testOp = self.test[1]
			self.testValue = int(self.test[2:])

	def cEval(self, part):
		if self.test is None:
			return self.destination
		evalString = 'part.' + self.test
		if eval(evalString):
			return self.destination
		return None

class Rule:
	conditions = []
	
	def __init__(self, ruleString):
		self.conditions = []
		for conditionString in ruleString.split(','):
			self.conditions.append(Condition(conditionString))

	def rEval(self, part):
		for condition in self.conditions:
			result = condition.cEval(part)
			if result is not None:
				return result
			
	def print(self):
		print('Rule:')
		for condition in self.conditions:
			print('\t', condition.test, condition.destination)

rules = {}
parts = []

for r in lines[0].split('\n'):
	ruleparts = r.split('{')
	rules[ruleparts[0]] = Rule(ruleparts[1][:-1])

for p in lines[1].split('\n'):
	values = re.findall(r'\d+', p)
	parts.append(Part(*values))

total = 0
# acceptedPaths = set()
for part in parts:
	ruleIds = ['in']
	while True:	
		result = rules[ruleIds[-1]].rEval(part)
		if result == 'A':
			total += (part.x + part.m + part.a + part.s)
			# acceptedPaths.add(tuple(ruleIds))	
			break
		elif result == 'R':
			break
		else:
			ruleIds.append(result)

print('Part 1:', total)
# for p in acceptedPaths:
# 	print(p)

def countCombinations(ranges, ruleId):
	if ruleId == 'A':
		combinations = (ranges['x'][1] - ranges['x'][0] + 1)
		combinations *= (ranges['m'][1] - ranges['m'][0] + 1)
		combinations *= (ranges['a'][1] - ranges['a'][0] + 1)
		combinations *= (ranges['s'][1] - ranges['s'][0] + 1)
		return combinations
	if ruleId == 'R':
		return 0
	combinations = 0
	filteredRanges = deepcopy(ranges)
	for cond in rules[ruleId].conditions:
		if cond.test is None:
			combinations += countCombinations(filteredRanges, cond.destination)
		else:
			currentMin = filteredRanges[cond.testCategory][0]
			currentMax = filteredRanges[cond.testCategory][1]
			if cond.testValue >= currentMin and cond.testValue <= currentMax:
				if cond.testOp == '>':					
					filteredRanges[cond.testCategory] = (currentMin, cond.testValue)
					stillToTestRanges = deepcopy(filteredRanges)
					stillToTestRanges[cond.testCategory] = (cond.testValue + 1, currentMax)
					combinations += countCombinations(stillToTestRanges, cond.destination)
				if cond.testOp == '<':					
					filteredRanges[cond.testCategory] = (cond.testValue, currentMax)
					stillToTestRanges = deepcopy(filteredRanges)
					stillToTestRanges[cond.testCategory] = (currentMin, cond.testValue - 1)
					combinations += countCombinations(stillToTestRanges, cond.destination)
	return combinations

startingRanges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
print("Part 2:", countCombinations(startingRanges, 'in'))

