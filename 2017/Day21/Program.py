import numpy as np
from math import sqrt

def splitArray(array, numRows, numCols):
	height, width = array.shape
	return (array.reshape(height // numRows, numRows, -1, numCols).swapaxes(1, 2).reshape(-1, numRows, numCols))

def combineArray(array, height, width):
	n, numRows, numCols = array.shape
	return (array.reshape(height // numRows, -1, numRows, numCols).swapaxes(1, 2).reshape(height, width))

def enhance(pic, rules, passes):
	for i in range(passes):
		newArray = []
		currentWidth = len(pic[0])
		arrayParts = []
		if (currentWidth % 2 == 0):
			arrayParts = splitArray(pic, 2, 2)
		else:
			arrayParts = splitArray(pic, 3, 3)
		newWidth = int(currentWidth + sqrt(len(arrayParts)))
		for part in arrayParts:
			newArray.append(processUsingRules(part, rules))
			for rule in rules:
				if '/'.join([''.join(x) for x in part]) in rule[:-1]:
					newArray.append(rule[-1])
		pic = combineArray(np.array(newArray), newWidth, newWidth)

	return pic

rules = []
picture = np.array([['.','#','.'],['.','.','#'],['#','#','#']])

with open('Input') as inFile:
	lines = map(str.rstrip, inFile.readlines())

for line in lines:
	parts = line.split(' => ')
	
	before = [list(x) for x in parts[0].split('/')]
	beforeHFlip = before[::-1]
	beforeVFlip = [x[::-1] for x in before]
	beforeR1 = list(list(x) for x in zip(*before[::-1]))
	beforeR1HFlip = beforeR1[::-1]
	beforeR1VFlip = [x[::-1] for x in beforeR1]
	beforeR2 = list(list(x) for x in zip(*beforeR1[::-1]))
	beforeR3 = list(list(x) for x in zip(*beforeR2[::-1]))
	after = [list(x) for x in parts[1].split('/')]

	b1 = '/'.join([''.join(x) for x in before])
	b2 = '/'.join([''.join(x) for x in beforeHFlip])
	b3 = '/'.join([''.join(x) for x in beforeVFlip])
	b4 = '/'.join([''.join(x) for x in beforeR1])
	b5 = '/'.join([''.join(x) for x in beforeR1HFlip])
	b6 = '/'.join([''.join(x) for x in beforeR1VFlip])
	b7 = '/'.join([''.join(x) for x in beforeR2])
	b8 = '/'.join([''.join(x) for x in beforeR3])

	rules.append([b1, b2, b3, b4, b5, b6, b7, b8, after])

print('Pixels on after 5 iterations:', (enhance(picture, rules, 5) == '#').sum())
#print('Pixels on after 18 iterations:', (enhance(picture, rules, 18) == '#').sum())
