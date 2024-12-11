import re

with open('Input') as inFile:
	lines = [l.strip() for l in inFile.readlines()]

total = 0
for line in lines:
	level = 0
	history = [[int(x) for x in line.split(' ')]]
	while not all(x == 0 for x in history[level]):
		temp = []
		for i in range(len(history[level]) - 1):
			temp.append(history[level][i+1] - history[level][i])
		history.append(temp)
		level += 1
	
	while level > 0:
		history[level-1].append(history[level-1][-1] + history[level][-1])
		level -= 1

	total += history[0][-1]
					 
print('Part 1:', total)


total = 0
for line in lines:
	level = 0
	history = [[int(x) for x in line.split(' ')]]
	while not all(x == 0 for x in history[level]):
		temp = []
		for i in range(len(history[level]) - 1):
			temp.append(history[level][i+1] - history[level][i])
		history.append(temp)
		level += 1
	
	while level > 0:
		history[level-1].insert(0, history[level-1][0] - history[level][0])
		level -= 1

	total += history[0][0]
					 
print('Part 2:', total)