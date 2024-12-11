import string

# Caesar function adapted from http://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
# answer by amillerrhodes
def Shift(text, distance):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[distance:] + alphabet[:distance]
    table = string.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def IsValidRoom(names, checksum):
	allNames = names.replace(" ", "")
	count = lambda s : list([char, s.count(char)] for char in set(s))
	counts = count(allNames)
	counts.sort(key = lambda x: x[0])
	counts.sort(key = lambda x: x[1], reverse=True)
	value = counts[0][0] + counts[1][0] + counts[2][0] + counts[3][0] + counts[4][0]
	return value == checksum

def GetParts(line):
	parts = line.strip().split("-")
	nonName = parts[len(parts)-1]
	sectorID = nonName[:nonName.find("[")]
	names = line[:line.find(sectorID)].replace("-", " ")
	checksum = nonName[-6:-1]
	return names, checksum, int(sectorID)

SectorSum = 0

with open("Input") as inputFile:
	lines = inputFile.readlines()
    
for line in lines:
	names, checksum, sectorID = GetParts(line)
	if IsValidRoom(names, checksum):
		SectorSum += sectorID
		shiftedRoomName = Shift(names, sectorID % 26).strip()
		print "SectorID:", sectorID, "Room Name:", shiftedRoomName
		if (shiftedRoomName == "northpole object storage"):
			targetSectorID = sectorID
		
print "\nSectorID of NorthPole Object Storage:", targetSectorID
print "Sum of valid SectorIDs:", SectorSum
