from itertools import product

with open('Input') as inFile:
	lines = inFile.readlines()

def add(a, b): return a + b
def multiply(a, b): return a * b
def concatenate(a, b): return int(str(a) + str(b))

def canBeTrue(testValue, operands):
	for p in product(OPERATIONS, repeat=len(operands) - 1):
		result = operands[0]
		for i in range(1, len(operands)):
			result = p[i - 1](result, operands[i])
		if result == testValue:
			return True
	return False

equations = []
for line in lines:
	testValue, operands = line.split(": ")
	testValue = int(testValue)
	operands = list(map(int, operands.split(" ")))
	equations.append((testValue, operands))

OPERATIONS = [add, multiply]
print("Part 1:", sum(eq[0] for eq in equations if canBeTrue(eq[0], eq[1])))

OPERATIONS = [add, multiply, concatenate]
print("Part 2:", sum(eq[0] for eq in equations if canBeTrue(eq[0], eq[1])))
