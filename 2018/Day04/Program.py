import operator
import re
from collections import Counter

typeGuard = 0
typeSleep = 1
typeWake = 2

times = []
guards = {}

with open('Input') as inFile:
	records = inFile.readlines()
	guardTimes = [r for r in records if '#' in r]
	sleepTimes = [r for r in records if '#' not in r and 'falls asleep' in r]
	wakeTimes = [r for r in records if '#' not in r and 'wakes up' in r]

	for (year, month, day, hour, minute, Id) in map(lambda s: map(int, re.findall(r'-?\d+', s)), guardTimes):
		times.append([typeGuard, year, -month, -day, hour, minute, Id])

	for (year, month, day, hour, minute) in map(lambda s: map(int, re.findall(r'-?\d+', s)), sleepTimes):
		times.append([typeSleep, year, -month, -day, hour, minute])

	for (year, month, day, hour, minute) in map(lambda s: map(int, re.findall(r'-?\d+', s)), wakeTimes):
		times.append([typeWake, year, -month, -day, hour, minute])

	times = sorted(times, key=operator.itemgetter(1, 2, 3, 4, 5))

	for time in times:
		if time[0] == typeGuard:
			currentGuard = time[6]
			if time[6] not in guards:
				guards[currentGuard] = []				
		if time[0] == typeSleep:
			currentBedTime = time[5]
		if time[0] == typeWake:
			for t in range(currentBedTime, time[5]):
				guards[currentGuard].append(t)

	guardId = max(guards, key=lambda x:len(guards[x]))
	minute, timesAsleep = Counter(guards[guardId]).most_common(1)[0]

	print('Part 1:', guardId * minute)

	(guardId, minute, timesAsleep) = max([(guard, minute, guards[guard].count(minute)) 
		for guard in guards 
		for minute in guards[guard]], 
		key=lambda x:x[2])

	print('Part 2:', guardId * minute)