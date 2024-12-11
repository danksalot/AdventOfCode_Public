def processNode(line, idx, sumMetadata):
	numChildNodes = int(line[idx])
	idx += 1
	numMetadata = int(line[idx])
	idx += 1
	for j in range(numChildNodes):
		idx, sumMetadata = processNode(line, idx, sumMetadata)
	for k in range(numMetadata):
		sumMetadata += int(line[idx])
		idx += 1
	return idx, sumMetadata

def processNodePart2(line, idx, currentSum):
	numChildNodes = int(line[idx])
	idx += 1
	numMetadata = int(line[idx])
	idx += 1

	if numChildNodes == 0:
		metadataSum = 0
		for l in range(numMetadata):
			metadataSum += int(line[idx])
			idx += 1
		return metadataSum

	childNodes = []
	for j in range(numChildNodes):
		childNodes.append(idx)
		idx, notNeeded = processNode(line, idx, 0)
	for k in range(numMetadata):
		if (int(line[idx]) <= numChildNodes):
			sumFromChild = processNodePart2(line, childNodes[int(line[idx])-1], 0)
			currentSum += sumFromChild			
		idx += 1

	return currentSum


with open('Input') as inFile:
	line = inFile.read().split()

i = 0
sumMetadata = 0
while i < len(line):
	i, sumMetadata = processNode(line, i, sumMetadata)

print('Part 1:', sumMetadata)
print('Part 2:', processNodePart2(line, 0, 0))