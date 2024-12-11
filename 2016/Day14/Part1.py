import md5
import re

size = 30000
currentKey = 0
tripple = re.compile(r'(.)\1\1')

hashes = [0 for x in range(size)]
keys = [0 for x in range(64)]

starter = "ahsbgdzn"

for i in range(size):
    m = md5.new(starter)
    m.update("%d" % (i))
    hashes[i] = m.hexdigest()
    
for i in range(size - 1000):
	match = tripple.search(hashes[i])
	char = ' '
	if currentKey < 64 and match != None:
		char = match.groups()[0]
		for j in range(i+1, i+1000):
			if str(char + char + char + char + char) in hashes[j]:
				print "Index:", i, "Key Index:", currentKey
				print "Hashes[i]:", hashes[i]
				print "Hashes[j]:", hashes[j], "\n"
				keys[currentKey] = i
				currentKey += 1
				continue

print keys
