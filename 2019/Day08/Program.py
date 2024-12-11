from collections import Counter

WIDTH = 25
HEIGHT = 6

layers = []

with open('Input') as inFile:
	line = inFile.read()

position = 0
while position < len(line):
	for row in range(WIDTH):
		layers.append([])
		for column in range(HEIGHT):
			layers[-1].append([int(x) for x in line[position:position+WIDTH]])
			position += WIDTH

fewestZeros = WIDTH * HEIGHT
bestLayer = None
bestLayerHash = None

for i in range(len(layers)):
	zeroCount = 0
	oneCount = 0
	twoCount = 0
	for row in layers[i]:
		counter = Counter(row)
		zeroCount += counter[0]
		oneCount += counter[1]
		twoCount += counter[2]

	if zeroCount < fewestZeros:
		fewestZeros = zeroCount
		bestLayer = i
		bestLayerHash = oneCount * twoCount

print("Part 1:", bestLayerHash)

finalImage = [ ["-"]*WIDTH for _ in range(HEIGHT) ]

for layer in layers:
	for rowIndex in range(HEIGHT):
		for columnIndex in range(WIDTH):
			if finalImage[rowIndex][columnIndex] == "-":
				if layer[rowIndex][columnIndex] == 0:
					finalImage[rowIndex][columnIndex] = " "
				elif layer[rowIndex][columnIndex] == 1:
					finalImage[rowIndex][columnIndex] = "*"

print("Part 2:")
for row in finalImage:
	print(''.join(row))
print('\n')