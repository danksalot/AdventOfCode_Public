with open('Input') as inFile:
	lineGroups = inFile.read().split('\n\n')

locks = []
keys = []

def readSchematic(lineGroup):
    part = [-1,-1,-1,-1,-1]
    for line in lineGroup.split('\n'):
        for i in range(5):
            if line[i] == '#':
                part[i] += 1
    return part

for lineGroup in lineGroups:
    if lineGroup[0][0] == '.':
        keys.append(readSchematic(lineGroup))
    else:
        locks.append(readSchematic(lineGroup))

matches = 0
for lock in locks:
    for key in keys:
        if all(lock[i] + key[i] <= 5 for i in range(5)):
            matches += 1

print('Part 1:', matches)
