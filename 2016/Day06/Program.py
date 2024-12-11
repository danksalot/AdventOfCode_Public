import operator

chars = [[],[],[],[],[],[],[],[]]

with open("Input") as inputFile:
	lines = inputFile.readlines()
    
for line in lines:
	for position, char in enumerate(line[:8]):
		chars[position].append(char)

message = ""
for i in range(8):
	stats = dict((letter,chars[i].count(letter)) for letter in set(chars[i]))
	message += max(stats.iteritems(), key=operator.itemgetter(1))[0]

print "Message using Max repitition code:", message

message = ""
for i in range(8):
	stats = dict((letter,chars[i].count(letter)) for letter in set(chars[i]))
	message += min(stats.iteritems(), key=operator.itemgetter(1))[0]

print "Message using Min repitition code:", message