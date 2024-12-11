with open('Input') as inFile:
	input = inFile.read()

def findUniqueChars(text, size):
	for i in range(size, len(text)+1):
		block = text[i-size:i]
		if len(set(block)) == size:
			return i

print("Part 1:", findUniqueChars(input, 4))
print("Part 2:", findUniqueChars(input, 14))