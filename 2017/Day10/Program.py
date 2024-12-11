def listBatch(list, batchSize=1):
	listLength = len(list)
	for i in range(0, listLength, batchSize):
		yield list[i:min(i + batchSize, listLength)]

def crapHashStep(marks, startPosition, length):
	endPosition = (startPosition + length) % len(marks)
	if endPosition >= startPosition:
		marks[startPosition:endPosition] = marks[startPosition:endPosition][::-1]
	else:
		section = marks[startPosition:] + marks[:endPosition]
		reversedSection = section[::-1]
		reversedBeforeWrap = len(marks) - startPosition
		marks[:endPosition] = reversedSection[reversedBeforeWrap:]
		marks[startPosition:] = reversedSection[:reversedBeforeWrap]

	return marks

def crapHash(marks, lengths, passes):
	currentPosition = 0
	skip = 0

	for i in range(passes):
		for length in lengths:
			marks = crapHashStep(marks, currentPosition, length)
			currentPosition = (currentPosition + length + skip) % len(marks)
			skip += 1

	for x in listBatch(marks, 16):
		byte = reduce(lambda x, y: x ^ y, x)
		dense.append(byte)

	return dense

marks = [x for x in range(256)]

with open('Input') as inFile:
	line = inFile.read()
	lengths = map(int, line.split(','))
	lengthOrds = map(ord, line) + [17, 31, 73, 47, 23]

marksPart1 = crapHash(marks[:], lengths, 1)
marksPart2 = crapHash(marks[:], lengthOrds, 64)

print lengthOrds

dense = []

for x in listBatch(marksPart2, 16):
	byte = reduce(lambda x, y: x ^ y, x)
	dense.append(byte)

print dense

print 'Part 1:', marksPart1[0] * marksPart1[1]
print 'Part 2:', ''.join([hex(x)[2:] for x in dense])