with open('Input') as inFile:
	lines = inFile.read()

def findReflectionScore(field, exclude = -1):
	for x in range(1, len(field[0])):
		found = True
		for y in range(len(field)):
			left = field[y][x-1::-1]
			right = field[y][x:]
			length = min(len(left), len(right))
			if left[:length] != right[:length]:
				found = False
		if found and x != exclude:
			return x
	
	for y in range(1, len(field)):
		found = True
		for x in range(len(field[0])):
			left = ''.join([field[i][x] for i in range(y-1, -1, -1)])
			right = ''.join([field[i][x] for i in range(y, len(field))])
			length = min(len(left), len(right))
			if left[:length] != right[:length]:
				found = False
		if found and (100 * y) != exclude:
			return 100 * y

	return None


total = 0
for field in lines.split('\n\n'):
	field = field.split('\n')
	total += findReflectionScore(field)

print('Part 1:', total)

def fixSmudge(field, exclude):
	for y in range(len(field)):
		for x in range(len(field[y])):
			original = field[y][x]
			sub = '.' if original == '#' else '#'
			field[y] = field[y][:x] + sub + field[y][x+1:]
			score = findReflectionScore(field, exclude)
			if score is None:
				field[y] = field[y][:x] + original + field[y][x+1:]
			else:
				return score

total = 0		
for field in lines.split('\n\n'):
	field = field.split('\n')

	originalScore = findReflectionScore(field)
	total += fixSmudge(field, exclude = originalScore)

print('Part 2:', total)
			