with open('Input') as inFile:
	lines = inFile.read().splitlines()

def snafuToDecimal(numString):
	decimal = 0
	for i in range(len(numString)):
		char = numString[-(i+1)]
		if char == '-':
			decimal += -1 * (5**i)
		elif char == '=':
			decimal += -2 * (5**i)
		else:
			decimal += int(char) * (5**i)
	return decimal

fuelSum = sum([snafuToDecimal(x) for x in lines])
print('In decimal', fuelSum)

# 30535047052797

# for i in range(25):
# 	print(i, 1 * (5**i))

# Part 1 converted to SNAFU: 2=001=-2=--0212-22-2