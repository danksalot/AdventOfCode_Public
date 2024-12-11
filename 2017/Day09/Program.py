score = 0
level = 0
garbageCount = 0

with open('Input') as inFile:
	data = inFile.read()

i = 0
while i < len(data):
	if data[i] == '{':
		level += 1
		score += level
	elif data[i] == '}':
		level -= 1
	elif data[i] == '<':
		i += 1
		while data[i] != '>':
			if data[i] == '!':
				i += 1
			else:
				garbageCount += 1
			i += 1
	i += 1

print "Final Score:", score
print "Garbage Count:", garbageCount