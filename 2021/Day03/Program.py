from collections import defaultdict

def findMostCommonBit(lines, index):
	print('checking index:', index)
	numLines = len(lines)
	lineSize = len(lines[0])

	ones = [l[index] for l in lines].count('1')
	zeros = [l[index] for l in lines].count('0')

	if ones > zeros:
		return '1'
	elif ones < zeros:
		return '0'
	else:
		return None

print(findMostCommonBit(['101', '010'], 2))

with open('Input') as inFile:
	entries = inFile.read().splitlines()

numEntries = len(entries)
entrySize = len(entries[0])

mostCommonBits = ''.join([findMostCommonBit(entries, i) for i in range(len(entries[0]))])
leastCommonBits = ''.join('1' if x == '0' else '0' for x in mostCommonBits)
gamma = int(mostCommonBits, 2)
epsilon = int(leastCommonBits, 2)

print('Part 1:', gamma * epsilon)

oxygenEntries = entries.copy()
for i in range(entrySize):
	mostCommon = findMostCommonBit(oxygenEntries, i)
	if mostCommon == None:
		mostCommon = '1'
	oxygenEntries = [e for e in oxygenEntries if e[i] == mostCommon]
	print('Round:', i, ' Entries remaining:', len(oxygenEntries))
	if len(oxygenEntries) == 1:
		break

co2Entries = entries.copy()
for i in range(entrySize):
	mostCommon = findMostCommonBit(co2Entries, i)
	leastCommon = '0'
	if mostCommon == '1':
		leastCommon = '0'
	elif mostCommon == '0':
		leastCommon = '1'
	co2Entries = [e for e in co2Entries if e[i] == leastCommon]
	print('Round:', i, ' Entries remaining:', len(co2Entries))
	if len(co2Entries) == 1:
		break

oxygen = int(oxygenEntries[0], 2)
co2 = int(co2Entries[0], 2)

print('Part 2:', oxygen * co2)