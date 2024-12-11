from collections import defaultdict

with open('Input') as inFile:
	lines = inFile.read().splitlines()

folderSizes = defaultdict(int)
currentLoc = ['/']

def getDirectoryPath(depth):
	if depth == 0: return '/'
	return ('/'.join(currentLoc[0:depth+1]))[1:]

def processCdCommand(arg):
	if arg == '..':
		currentLoc.pop()
	else:
		currentLoc.append(arg)

def processContent(a, b):
	if a.isdigit():
		for depth in range(len(currentLoc)):
			folderSizes[getDirectoryPath(depth)] += int(a)

for line in lines[1:]:
	parts = line.split(' ')
	if parts[0] == '$':
		if parts[1] == 'cd':
			processCdCommand(parts[2])
	else:
		processContent(parts[0], parts[1])

print("Part 1:", sum([x for x in folderSizes.values() if x <= 100000]))

unusedSpace = 70000000 - folderSizes['/']
needToFree = 30000000 - unusedSpace
print('Part 2:', min([x for x in folderSizes.values() if x > needToFree]))