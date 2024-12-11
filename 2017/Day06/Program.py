import numpy as np

def increment(index):
	return (index + 1) % len(banks)

states = {}
banks = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
redistributions = 0

states[str(banks)] = 1

while True:
	redistributions += 1
	maxIndex = np.argmax(banks)
	redist = banks[maxIndex]
	banks[maxIndex] = 0
	currentIndex = increment(maxIndex)

	while (redist > 0):
		banks[currentIndex] += 1
		redist -= 1
		currentIndex = increment(currentIndex)

	if str(banks) in states:
		print "Redistributed", redistributions, "times"
		print "Loop length", redistributions - states[str(banks)]
		break
	else:
		states[str(banks)] = redistributions
