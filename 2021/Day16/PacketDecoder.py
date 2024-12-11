from math import prod

class PacketDecoder:
	hexInput = ''
	binInput = ''
	index = 0
	versionSum = 0
	LITERAL_TYPE_ID = 4

	def __init__(self, hexInput):
		self.hexInput = hexInput
		self.binInput = bin(int(hexInput, 16))[2:].zfill(len(hexInput) * 4)

	def readLiteral(self):
		binaryNumber = ""
		while 1 == 1:
			positionBit = self.binInput[self.index]
			binaryNumber += self.binInput[self.index+1:self.index+5]
			self.index += 5		
			if positionBit == '0':
				break		

		return int(binaryNumber, 2)

	def readOperator(self, packetType):
		lengthType = int(self.binInput[self.index], 2)
		subPackets = []
		if lengthType == 0:
			bitLength = int(self.binInput[self.index+1:self.index+16], 2)
			self.index += 16
			targetBit = self.index + bitLength
			while self.index < targetBit:
				value = self.readNextPacket()
				subPackets.append(value)
		else:
			numSubPackets = int(self.binInput[self.index+1:self.index+12], 2)
			self.index += 12
			for i in range(numSubPackets):
				value = self.readNextPacket()
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
		return returnValue

	def readNextPacket(self):
		version = int(self.binInput[self.index:self.index + 3], 2)
		self.versionSum += version
		packetType = int(self.binInput[self.index+3:self.index+6], 2)
		self.index += 6
		if packetType == self.LITERAL_TYPE_ID:
			value = self.readLiteral()
		else:
			value = self.readOperator(packetType)
		return value