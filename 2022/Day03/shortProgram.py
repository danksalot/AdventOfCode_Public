with open('Input') as inFile:
	lines = inFile.read().splitlines()

def getPriority(item):
	return ord(item) - (38 if item.isupper() else 96)

print('Part 1:', sum([getPriority([item for item in line[0:int(len(line)/2)] if item in line[int(len(line)/2):]][0]) for line in lines]))
print('Part 2:', sum([getPriority([item for item in lines[i] if item in lines[i+1] and item in lines[i+2]][0]) for i in range(0, len(lines), 3)]))
