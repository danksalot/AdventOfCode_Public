with open('Input') as inFile:
	lines = inFile.read().splitlines()

def getPriority(item):
	if item.isupper():
		return (ord(item)-38)
	else:
		return (ord(item)-96)

errorSum = 0
for line in lines:
	size = int(len(line)/2)	
	for item in line[0:size]:
		if item in line[size:]:	
			errorSum += getPriority(item)
			break

print('Part 1:', errorSum)

badgeSum = 0
for index in range(0, len(lines), 3):
	badge = [item for item in lines[index] if item in lines[index+1] and item in lines[index+2]][0]
	badgeSum += getPriority(badge)

print('Part 2:', badgeSum)