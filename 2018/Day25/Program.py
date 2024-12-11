import re

constelations = []

with open('Input') as inFile:
	lines = inFile.read().splitlines()

fitsInExisting = False
for (x, y, z, t) in map(lambda s: map(int, re.findall(r'-?\d+', s)), lines):
	fitsInExisting = False
	fitsInto = []
	for constIndex, constelation in enumerate(constelations):
		for point in constelation:
			distanceToCurrent = abs(point[0] - x) + abs(point[1] - y) + abs(point[2] - z) + abs(point[3] - t)
			if distanceToCurrent <= 3:
				fitsInExisting = True
				fitsInto.append(constIndex)
				#print('adding to a current constelation')
				constelation.append([x, y, z, t])
				#for constelation in constelations:
				#	print(constelation)
				break
	
	if len(fitsInto) > 1:
		first = fitsInto.pop(0)
		for other in fitsInto[::-1]:
			constelations[first] = constelations[first] + constelations[other]
			del constelations[other]

	if not fitsInExisting:
		#print('adding new constelation')
		constelations.append([[x, y, z, t]])
		#print('We now have', len(constelations), 'constelations')
		#for constelation in constelations:
			#print(constelation)

print('Part 1:', len(constelations))
	