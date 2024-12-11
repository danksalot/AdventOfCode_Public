def expandData(data, length):
	while len(data) < length:
		data += "0" + ''.join("0" if n == "1" else "1" for n in data[::-1])
	return data[:length]

def contractChecksum(checksum):
	while not len(checksum) & 1:
		checksum = ''.join("1" if x == y else "0" for x, y in zip(checksum[0::2], checksum[1::2]))
	return checksum

print contractChecksum(expandData("11101000110010100", 272))
print contractChecksum(expandData("11101000110010100", 35651584))