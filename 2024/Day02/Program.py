
def isSafe(levels):
	diffs = [int(levels[i]) - int(levels[i + 1]) for i in range(len(levels) - 1)]
	allAscending = all(diff > 0 for diff in diffs)
	allDescending = all(diff < 0 for diff in diffs)
	allWithinRange = all(abs(diff) > 0 and abs(diff) < 4 for diff in diffs)
	return (allAscending or allDescending) and allWithinRange

with open('Input') as inFile:
	reports = [line.rstrip() for line in inFile.readlines()]

print("Part 1:", sum(1 for report in reports if isSafe(report.split(' '))))

safeCount = 0
for report in reports:
	levels = report.split(' ')
	if (isSafe(levels)):
		safeCount += 1
	else:
		for i in range(len(levels)):
			if (isSafe(levels[0:i] + levels[i+1:])):
				safeCount += 1
				break

print("Part 2:", safeCount)
