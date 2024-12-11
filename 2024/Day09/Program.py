
with open('Input') as inFile:
	line = list(map(int, inFile.readline().rstrip('\n')))

def expand(condensed):
	fileId = 0
	expanded = []
	for i in range(0, len(condensed), 2):
		for j in range(int(condensed[i])):
			expanded.append(fileId)
		if i < len(condensed) - 1:
			for j in range(int(condensed[i + 1])):
				expanded.append('.')
		fileId += 1
	return expanded

def freeSpaceNaive(fileSystem):
	firstSpace = fileSystem.index('.')
	for i in range(len(fileSystem) - 1, -1, -1):
		if fileSystem[i] != '.' and firstSpace < i:
			fileSystem[firstSpace], fileSystem[i] = fileSystem[i], fileSystem[firstSpace]
			firstSpace = fileSystem.index('.')
	return fileSystem

def findAdequateSpace(fileSystem, fileSize):
	for i in range(len(fileSystem)):
		if all(x == '.' for x in fileSystem[i:i + fileSize]):
			return i
	return -1

def freeSpaceByFile(fileSystem):
	for fileId in range(fileSystem[-1], -1, -1):
		fileSize = fileSystem.count(fileId)
		fileLocation = fileSystem.index(fileId)
		firstAdequateSpace = findAdequateSpace(fileSystem, fileSize)
		if firstAdequateSpace > -1 and firstAdequateSpace < fileLocation:
			fileSystem = fileSystem[:firstAdequateSpace] + [fileId] * fileSize + fileSystem[firstAdequateSpace + fileSize : fileLocation] + ['.'] * fileSize + fileSystem[fileLocation + fileSize:]
	return fileSystem

def calcChecksum(fileSystem):
	total = 0
	for i in range(len(fileSystem)):
		if fileSystem[i] != '.':
			total += i * fileSystem[i]
	return total

print('Part 1:', calcChecksum(freeSpaceNaive(expand(line))))
print('Part 2:', calcChecksum(freeSpaceByFile(expand(line))))
