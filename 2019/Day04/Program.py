from collections import Counter

with open('Input') as inFile:
	minimum, maximum = map(int, inFile.read().split('-'))

total = 0
for i in range(minimum, maximum + 1):
	num = str(i)

	if list(num) == sorted(num):
		if max(Counter(num).values()) >= 2:
			total += 1

print("Part 1:", total)

total = 0
for i in range(minimum, maximum + 1):
	num = str(i)

	if list(num) == sorted(num):
		if 2 in Counter(num).values():
			total += 1

print("Part 2:", total)
