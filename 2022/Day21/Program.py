with open('Input') as inFile:
	lines = inFile.read().splitlines()

monkeys = {}
yelled = {}

for line in lines:
	name, job = line.split(': ')
	if ' ' not in job:
		yelled[name] = int(job)
	else:
		monkeys[name] = job.split(' ')

def tryDoingJob(name, curMonkeys, curYelled):
	A = curMonkeys[name][0]
	Op = curMonkeys[name][1]
	B = curMonkeys[name][2]
	if A in curYelled and B in curYelled:
		if Op == '+':
			curYelled[name] = curYelled[A] + curYelled[B]
		elif Op == '-':
			curYelled[name] = curYelled[A] - curYelled[B]
		elif Op == '*':
			curYelled[name] = curYelled[A] * curYelled[B]
		elif Op == '/':
			curYelled[name] = curYelled[A] // curYelled[B]
		elif Op == '=':
			curYelled[name] = curYelled[A] == curYelled[B]
		return True
	return False

# Preprocessing
print('Preprocessing starting', len(monkeys))
while monkeys:
	didJob = []
	for name in monkeys:
		if name in ['root', 'humn']:
			success = False
		else:
			success = tryDoingJob(name, monkeys, yelled)
		if success:
			didJob.append(name)
	for name in didJob:
		del monkeys[name]
	if len(didJob) == 0:
		break

pt1monkeys = dict(monkeys)
pt1yelled = dict(yelled)
while pt1monkeys:
	didJob = []
	for name in pt1monkeys:
		success = tryDoingJob(name, pt1monkeys, pt1yelled)
		if success:
			didJob.append(name)
	for name in didJob:
		del pt1monkeys[name]

print('Part 1:', pt1yelled['root'])

print(monkeys)
print(yelled)
