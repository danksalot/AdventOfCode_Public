def spin(dancers, num):
	return dancers[-num:] + dancers[:-num]

def exchange(dancers, first, second):
	dancers[first], dancers[second] = dancers[second], dancers[first]
	return dancers

def partner(dancers, first, second):
	return exchange(dancers, dancers.index(first), dancers.index(second))

def dance(troop, steps, passes):
	repeats = []

	for i in range(passes):
		troopString = ''.join(troop)
		if troopString in repeats:
			return repeats[passes % i]
		repeats.append(troopString)
		for step in steps:
			if step[0] == 's':
				troop = spin(troop, int(step[1:]))
			elif step[0] == 'x':
				first, second = step[1:].split('/')
				troop = exchange(troop, int(first), int(second))
			elif step[0] == 'p':
				first, second = step[1:].split('/')
				troop = partner(troop, first, second)
	return troop

programs = list('abcdefghijklmnop')
instructions = open('Input').read().split(',')

print 'Part1:', ''.join(dance(programs[:], instructions, 1))
print 'Part2:', ''.join(dance(programs[:], instructions, 1000000))
