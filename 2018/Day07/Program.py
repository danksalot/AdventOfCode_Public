from collections import defaultdict

prereqs1 = {}
prereqs2 = {}
instructions = []
order = ""
ordinalOffset = 64
stepOffset = 60
numberOfWorkers = 5
workerPlace = 0
assignedStep = 1
timeFinished = 2

with open('Input') as inFile:
	lines = inFile.read().splitlines()

	for line in lines:
		parts = line.split()
		instructions.append([parts[1], parts[7]])

for step in set([x[0] for x in instructions]):
	prereqs1[step] = []
	prereqs2[step] = []

for step in set([x[1] for x in instructions]):
	prereqs1[step] = []
	prereqs2[step] = []

for instruction in instructions:
	prereqs1[instruction[1]].append(instruction[0])
	prereqs2[instruction[1]].append(instruction[0])

# PART 1
while len(prereqs1) > 0:
	nxt = [key for key in prereqs1 if prereqs1[key] == []]
	nextStep = sorted(nxt)[0]
	order += nextStep
	for key in prereqs1:
		prereqs1[key] = [x for x in prereqs1[key] if x != nextStep]
	del prereqs1[nextStep]

print('Part 1:', order)

# PART 2
second = 0
workers = [[x, '', 0] for x in range(numberOfWorkers)]
while len(prereqs2) > 0:
#	print('Starting second', second)

	# First take care of any completed steps
	for worker in workers:
		if worker[timeFinished] == second and worker[assignedStep] != '':
#			print('Worker finished a step', worker)
			finishedStep = worker[assignedStep]
			worker[assignedStep] = ''
			for key in prereqs2:
				prereqs2[key] = [x for x in prereqs2[key] if x != finishedStep]
			workers[worker[workerPlace]] = worker
#			print('New worker status', worker)

	# Now see who is available and assign steps that are ready
	nxt = [key for key in prereqs2 if prereqs2[key] == []]
	nextSteps = sorted(nxt)[:5]
	availableWorkers = [w for w in workers if w[timeFinished] <= second]
#	print('Available workers at second', second, 'are', availableWorkers)
	for worker in availableWorkers:		
#		print('Looking for a step to assign worker', worker)
		if len(nextSteps) > 0:
			workersStep = nextSteps.pop(0)
#			print('Assigning step', workersStep, 'to worker', worker[workerPlace])
			finished = second + stepOffset + ord(workersStep) - ordinalOffset
			workers[worker[workerPlace]] = [worker[workerPlace], workersStep, finished]
			del prereqs2[workersStep]
			

#	print('Workers at second', second, ':', workers)
#	print('Steps to go', prereqs2)
	second += 1

print('Part 2:', max(workers, key=lambda x:x[timeFinished])[timeFinished])