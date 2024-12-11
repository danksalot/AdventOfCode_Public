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

	return marks

marks = [x for x in range(256)]
hashLengths = []

for i in range(128):
	hashLengths.append(map(ord, 'jxqlasbh-' + str(i)) + [17, 31, 73, 47, 23])

temp = []

for i in range(128):
	temp.append(crapHash(marks[:], hashLengths[i], 64))

dense = []
bits = []

for i in range(128):
	dense.append('')
	for x in listBatch(temp[i], 16):
		byte = reduce(lambda x, y: x ^ y, x)
		dense[i] += ''.join([hex(byte)[2:]]).zfill(2)

for i in range(128):
	bits.append([])
	for h in ''.join(dense[i]):
		bits[i].append(bin(int(h, 16))[2:].zfill(4))

counter = 0

for i in range(128):
	for b in bits[i]:
			count = b.count('1')
			print counter, i, b, 'contains', count, 'used squares'
			counter += count

print counter

print sum(sum(b.count('1') for b in bits[i]) for i in range(128))

