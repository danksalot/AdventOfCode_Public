scanners = {}

with open('Input') as inFile:
	for line in inFile:
		parts = line.split(': ')
		scanners[int(parts[0])] = int(parts[1].rstrip())

def calculateSeverity(delay):
	severity = 0
	cought = False
	for i in scanners:
		if ((i + delay) % ((scanners[i] * 2) - 2)) == 0:
			cought = True
			severity += i * scanners[i]
	return severity, cought

print 'Severity of starting at 0:', calculateSeverity(0)[0]

delay = 1
while True:
	severity, cought = calculateSeverity(delay)
	if cought:
		delay += 1
	else:
		print 'Coast is clear after delaying', delay, 'picoseconds.'
		break