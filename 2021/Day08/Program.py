import itertools

digitDefs = {'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4, 'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}

class Display:
	sample = []
	output = []

	def __init__(self, pattern):
		parts = pattern.split(' | ')
		self.sample = parts[0].split(' ')
		self.output = parts[1].split(' ')

with open('Input') as inFile:
	patterns = inFile.read().splitlines()

displays = []

count = 0
for pattern in patterns:
	current = Display(pattern)
	displays.append(current)
	count += sum(1 for d in current.output if len(d) in [2,3,4,7])

print('Part 1:', count)

count = 0
for display in displays:
	for permutation in itertools.permutations('abcdefg'):
		wireMap = {a:b for a,b in zip(permutation, 'abcdefg')}
		decodedSample = [''.join(wireMap[seg] for seg in digit) for digit in display.sample]
		decodedOutput = [''.join(wireMap[seg] for seg in digit) for digit in display.output]
		if all(''.join(sorted(digit)) in digitDefs for digit in decodedSample):
			decodedOutput = [''.join(sorted(x)) for x in decodedOutput]
			count += int(''.join(str(digitDefs[x]) for x in decodedOutput))
			break

print(count)