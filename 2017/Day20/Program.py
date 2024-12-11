import re
import copy

POSITION = 1
VELOCITY = 2
ACCEL = 3
X = 0
Y = 1
Z = 2

particles = []

def update(particle):
	particle[VELOCITY][X] += particle[ACCEL][X]
	particle[VELOCITY][Y] += particle[ACCEL][Y]
	particle[VELOCITY][Z] += particle[ACCEL][Z]
	particle[POSITION][X] += particle[VELOCITY][X]
	particle[POSITION][Y] += particle[VELOCITY][Y]
	particle[POSITION][Z] += particle[VELOCITY][Z]
	return particle

def removeDuplicates(particles):
	dupes = [x[POSITION] for n, x in enumerate(particles) if x[POSITION] in [y[POSITION] for y in particles[:n]]]
	#print len(dupes), 'dupes found.'
	particles = [x for x in particles if x[POSITION] not in dupes]
	#print len(particles), 'particles left.'
	return particles

with open('Input') as inFile:
	lines = inFile.readlines()

for i, line in enumerate(lines):
	coords = re.findall(r'<[^>]*>', line)
	particles.append([i])
	particles[i].append(map(int, coords[0].lstrip('<').rstrip('>').split(',')))
	particles[i].append(map(int, coords[1].lstrip('<').rstrip('>').split(',')))
	particles[i].append(map(int, coords[2].lstrip('<').rstrip('>').split(',')))

part1Particles = copy.deepcopy(particles)

for i in range(1000):
	for particle in part1Particles:
		particle = update(particle)

print min(part1Particles, key=lambda x: abs(x[POSITION][X]) + abs(x[POSITION][Y]) + abs(x[POSITION][Z]))[0], 'was the best out of', len(part1Particles), 'particles'

for i in range(1000):
	for particle in particles:
		particle = update(particle)
	particles = removeDuplicates(particles)

print len(particles), 'particles left after duplicates were removed'