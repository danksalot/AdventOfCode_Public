from itertools import permutations

count = 0

with open("Input") as inputFile:
	lines = inputFile.readlines()

del lines[0]
del lines[0]

for idx, line in enumerate(lines):
	line = line.split()
	line[1] = int(line[1].replace('T', ''))
	line[2] = int(line[2].replace('T', ''))
	line[3] = int(line[3].replace('T', ''))
	line[4] = int(line[4].replace('%', ''))
	lines[idx] = line

for idx, line in enumerate(lines):
	for i in range(len(lines)):
		if i != idx and lines[idx][2] > 0 and lines[idx][2] <= lines[i][3]:
			print lines[idx]
			print lines[i]
			print count
			count += 1

print count