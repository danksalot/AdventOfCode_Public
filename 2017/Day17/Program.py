buff = [0]
current = 0
step = 345

for i in range(1, 2018):
	current = ((current + step) % i)
	buff.insert(current + 1, i)
	current += 1

print 'Part1:', buff[current + 1]

current = 0
zeroIndex = 0
afterZero = None

for i in range(1, 50000001):
	current = ((current + step) % i)
	if current == zeroIndex:
		afterZero = i
	if (current + 1) == zeroIndex:
		zeroIndex += 1
	current += 1	

print 'Part2:', afterZero