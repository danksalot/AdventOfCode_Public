class Item:
	Value = None
	RefIdx = None

	def __init__(self, value, refIdx):
		self.Value = value
		self.RefIdx = refIdx

with open('Input') as inFile:
	nums = list(map(int, inFile.read().split('\n')))

groveCoords = []
itemCount = len(nums)

for i, num in enumerate(nums):
	groveCoords.append(Item(num, i))

def moveItem(refIdx):
	for i, item in enumerate(groveCoords):
		if item.RefIdx == refIdx:
			oldIdx = i
			break
	newIndex = (oldIdx + item.Value) % (itemCount - 1)
	groveCoords.insert(newIndex, groveCoords.pop(oldIdx))

for i in range(itemCount):
	moveItem(i)	

decrypted = [x.Value for x in groveCoords]
startIndex = decrypted.index(0)
coord1 = decrypted[(startIndex + 1000) % itemCount]
coord2 = decrypted[(startIndex + 2000) % itemCount]
coord3 = decrypted[(startIndex + 3000) % itemCount]
print('Part 1:', coord1 + coord2 + coord3)


groveCoords = []
decryptionKey = 811589153

for i, num in enumerate(nums):
	groveCoords.append(Item(num * decryptionKey, i))

for iteration in range(10):
	for i in range(itemCount):
		moveItem(i)

decrypted = [x.Value for x in groveCoords]
startIndex = decrypted.index(0)
coord1 = decrypted[(startIndex + 1000) % itemCount]
coord2 = decrypted[(startIndex + 2000) % itemCount]
coord3 = decrypted[(startIndex + 3000) % itemCount]
print('Part 2:', coord1 + coord2 + coord3)