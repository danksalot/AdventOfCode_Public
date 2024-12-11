import re
from functools import reduce

with open('Input') as inFile:
	lines = inFile.readlines()

raceLengths = [int(x) for x in re.findall(r'\d+', lines[0])]
raceRecords = [int(x) for x in re.findall(r'\d+', lines[1])]
ways2Win = [0] * len(raceLengths)

for race in range(0, len(raceLengths)):
	for t in range(0, raceLengths[race]):
		distance = (raceLengths[race] - t) * t
		if distance > raceRecords[race]:
			ways2Win[race] += 1

print('Part 1:', reduce(lambda x, y: x * y, ways2Win))

raceLength = int(''.join([str(x) for x in raceLengths]))
raceRecord = int(''.join([str(x) for x in raceRecords]))

min = 0
for t in range(0, raceLength):
	distance = (raceLength - t) * t
	if (raceLength - t) * t > raceRecord:		
		min = t
		break

max = 0
for t in range(raceLength, 0, -1):
	distance = (raceLength - t) * t
	if distance > raceRecord:		
		max = t
		break

print('Part 2:', max - min + 1)