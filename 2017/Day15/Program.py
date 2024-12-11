def makeGenerator(current, factor, mod):
	for i in range(40000000):
		current = (current * factor) % 2147483647
		if current % mod == 0:
			yield current

def matchGenerators(left, right):
	matches = 0
	while True:	
		valueA = next(left, None)
		valueB = next(right, None)
		if valueA and valueB:
			matches += not ((valueA & 65535) ^ (valueB & 65535))
		else:
			break
	return matches

print 'Part1:', matchGenerators(makeGenerator(699, 16807, 1), makeGenerator(124, 48271, 1))
print 'Part2:', matchGenerators(makeGenerator(699, 16807, 4), makeGenerator(124, 48271, 8))
