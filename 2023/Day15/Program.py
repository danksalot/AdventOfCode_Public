import re

with open('Input') as inFile:
	sequence = inFile.read().strip()

boxes = [[i, []] for i in range(256)]

def calculateFocus(boxes):
	focus = 0
	for box in boxes:
		for idx, lens in enumerate(box[1]):
			focus += (1 + box[0]) * (1 + idx) * lens[1]
	return focus

def processStep(step):
	label = re.search(r'([a-z]+)', step).group(1)
	boxNum = int(hash(label))
	op = re.search(r'(=|-)', step).group(1)
	if op == '-':
		boxes[boxNum][1] = [x for x in boxes[boxNum][1] if x[0] != label]
	else:
		focalLength = int(re.search(r'([0-9]+)', step).group(1))
		set = False
		for lens in boxes[boxNum][1]:
			if lens[0] == label:
				lens[1] = focalLength
				set = True
				break
		if not set:
			boxes[boxNum][1].append([label, focalLength])

def hash(line):
	value = 0
	for char in line:
		value += ord(char)
		value *= 17
		value %= 256
	return value

print('Part 1:', sum([hash(step) for step in sequence.split(',')]))

for step in sequence.split(','):
	processStep(step)

print('Part 2:', calculateFocus(boxes))