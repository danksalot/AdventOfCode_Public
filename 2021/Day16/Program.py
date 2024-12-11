import binascii
from math import prod
import operator

with open('Input') as inFile:
	hexInput = inFile.read()

TypeIds = { 0:operator.add }
LITERAL_TYPE_ID = 4
versionSum = 0

def readLiteral(binInput, index):
	binaryNumber = ""
	while 1 == 1:
		positionBit = binInput[index]
		binaryNumber += binInput[index+1:index+5]
		index += 5		
		if positionBit == '0':
			break		

	literal = int(binaryNumber, 2)
	return literal, index

def readOperator(packetType, binInput, index):
	lengthType = int(binInput[index], 2)
	subPackets = []
	if lengthType == 0:
		bitLength = int(binInput[index+1:index+16], 2)
		index += 16
		targetBit = index + bitLength
		while index < targetBit:
			value, index = readPacketAtIndex(binInput, index)
			subPackets.append(value)
	else:
		numSubPackets = int(binInput[index+1:index+12], 2)
		index += 12
		for i in range(numSubPackets):
			value, index = readPacketAtIndex(binInput, index)
			subPackets.append(value)

	if packetType == 0:
		returnValue = sum(subPackets)
	elif packetType == 1:
		returnValue = prod(subPackets)
	elif packetType == 2:
		returnValue = min(subPackets)
	elif packetType == 3:
		returnValue = max(subPackets)
	elif packetType == 5:
		returnValue = int(subPackets[0] > subPackets[1])
	elif packetType == 6:
		returnValue = int(subPackets[0] < subPackets[1])
	elif packetType == 7:
		returnValue = int(subPackets[0] == subPackets[1])
	return returnValue, index

def readPacketAtIndex(binInput, index):
	global versionSum
	version = int(binInput[index:index + 3], 2)
	versionSum += version
	packetType = int(binInput[index+3:index+6], 2)
	if packetType == LITERAL_TYPE_ID:
		value, index = readLiteral(binInput, index+6)
	else:
		value, index = readOperator(packetType, binInput, index+6)
	return value, index

# hexInput = '9C0141080250320F1802104A08'
binaryInput = bin(int(hexInput, 16))[2:].zfill(len(hexInput) * 4)


index = 0
# Keep going until we've reached the end, or all remaining characters are zeroes
while index < len(binaryInput) and set(binaryInput[index:]) != set('0'):
	value, index = readPacketAtIndex(binaryInput, index)

print('Part 1:', versionSum)
print('Part 2:', value)