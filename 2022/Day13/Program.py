import json
from functools import cmp_to_key

def customCompare(a, b):
	if type(a) is list and type(b) is list:
		for i in range(min(len(a), len(b))):
			result = customCompare(a[i], b[i])
			if result: return result
		if len(a) == len(b): return None
		return len(a) - len(b)
	elif type(a) is list:
		return customCompare(a, [b])
	elif type(b) is list:
		return customCompare([a], b)
	else:
		if a == b: return None
		return a - b

allPackets = []
with open('Input') as inFile:
	for line in inFile.read().splitlines():
		# Only process lines with content
		if line.strip():
			allPackets.append(json.loads(line))

sortedSum = 0
for i in range(0, len(allPackets), 2):
	pair = [allPackets[i], allPackets[i + 1]]
	if pair == sorted(pair, key=cmp_to_key(customCompare)):
		pairIndex = (i // 2) + 1
		sortedSum += pairIndex

print('Part 1:', sortedSum)

dividers = [[[2]],[[6]]]
allPackets.extend(dividers)

decoderKey = 1
for i, packet in enumerate(sorted(allPackets, key=cmp_to_key(customCompare))):
	if packet in dividers:
		decoderKey *= (i + 1)

print('Part 2:', decoderKey)