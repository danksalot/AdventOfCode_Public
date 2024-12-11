from PacketDecoder import PacketDecoder

with open('Input') as inFile:
	hexInput = inFile.read()

decoder = PacketDecoder(hexInput)
evaluationResult = decoder.readNextPacket()

print('Part 1:', decoder.versionSum)
print('Part 2:', evaluationResult)