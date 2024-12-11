programs = {}
notRoot = []
root = ''

def getTotalWeight(progName):
	return programs[progName][0] + sum(map(lambda x: getTotalWeight(x), programs[progName][1]))

with open('Input') as inFile:
	lines = inFile.readlines()

for line in lines:
	parts = line.split()
	progName = parts[0]
	weight = int(parts[1].lstrip('(').rstrip(')'))

	if (progName not in programs):
		programs[progName] = [weight, []]
	
	if (len(parts) > 2):
		heldUp = parts[3:]
		for program in heldUp:
			program = program.rstrip(',')
			programs[progName][1].append(program)
			if program not in notRoot:
				notRoot.append(program)

for program in programs:
	if (program not in notRoot):
		root = program

print "Base program is:", root

foundWrongWeight = False
currentProg = root
wrongWeight = 0
rightWeight = 0

while not foundWrongWeight:
	onDisk = programs[currentProg][1]
	weights = map(lambda x: getTotalWeight(x), onDisk)
	foundWrongWeight = len(set(weights)) == 1
	if not foundWrongWeight:
		for i, w in enumerate(weights):
			if weights.count(w) == 1:
				currentProg = onDisk[i]
				wrongWeight = w
			else:
				rightWeight = w
	else:
		print "Wrong weight:", currentProg, "weighs", programs[currentProg][0], "but should weigh", programs[currentProg][0] - (wrongWeight - rightWeight)